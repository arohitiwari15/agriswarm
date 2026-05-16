'use client';
import { useSimulation, Detection } from "@/lib/simulation";
import { Badge } from "@/components/ui/badge";
import { formatDistanceToNow } from "date-fns";
import { AlertTriangle, CheckCircle, MapPin } from "lucide-react";
import { Card, CardContent } from "@/components/ui/card";
import { motion } from "framer-motion";

export default function DetectionFeed() {
  const { detections } = useSimulation();

  return (
    <div className="container py-12 relative z-10">
      <div className="mb-12">
        <h1 className="text-4xl font-bold mb-3 tracking-tight">AI Detection Feed</h1>
        <p className="text-text-secondary text-lg">Live YOLOv8 feed streamed from the drone swarm.</p>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-2 xl:grid-cols-3 gap-8">
        {detections.map((det: Detection, i) => (
          <motion.div 
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ duration: 0.4, delay: i * 0.1 }}
            key={det.id}
          >
            <Card className="overflow-hidden border-border bg-card/60 backdrop-blur-md shadow-lg hover:shadow-2xl transition-all duration-300 hover:-translate-y-1 group">
              <div className="h-56 bg-elevated relative flex items-center justify-center p-4 overflow-hidden">
                <div 
                  className="absolute inset-0 bg-cover bg-center transition-transform duration-700 group-hover:scale-105"
                  style={{ backgroundImage: `url(${det.imageUrl})` }}
                ></div>
                <div className="absolute inset-0 bg-gradient-to-t from-black/80 via-black/20 to-transparent"></div>

                {/* Bounding box mock */}
                {det.disease !== 'Healthy' && (
                  <div className="absolute w-32 h-32 border-2 border-alert-red rounded bg-alert-red/10 flex items-end shadow-[0_0_15px_rgba(230,57,70,0.5)] animate-pulse-slow">
                    <span className="bg-alert-red text-white text-[10px] px-1.5 py-0.5 font-mono shadow-md backdrop-blur-md">{det.disease} {Math.round(det.confidence*100)}%</span>
                  </div>
                )}

                <div className="absolute bottom-3 left-3 flex items-center text-white text-xs font-mono bg-black/50 px-2 py-1 rounded backdrop-blur-sm">
                  <MapPin className="w-3 h-3 mr-1" /> {det.position[0].toFixed(4)}, {det.position[1].toFixed(4)}
                </div>
              </div>
              <CardContent className="p-6">
                <div className="flex justify-between items-start mb-5">
                  <div>
                    <h3 className="font-bold text-xl text-foreground mb-1 flex items-center gap-2">
                      {det.disease === 'Healthy' ? <CheckCircle className="w-5 h-5 text-accent-green" /> : <AlertTriangle className="w-5 h-5 text-alert-red" />}
                      {det.disease}
                    </h3>
                    <p className="text-xs text-text-secondary">{formatDistanceToNow(new Date(det.timestamp), { addSuffix: true })}</p>
                  </div>
                  <Badge variant={det.disease === 'Healthy' ? 'secondary' : 'destructive'} className="shadow-sm">
                    {det.severity}
                  </Badge>
                </div>

                <div className="space-y-2 mb-4">
                  <div className="flex justify-between text-sm">
                    <span className="text-text-muted">Confidence Level</span>
                    <span className="font-medium text-foreground">{(det.confidence * 100).toFixed(1)}%</span>
                  </div>
                  <div className="w-full bg-border rounded-full h-2 overflow-hidden">
                    <motion.div 
                      initial={{ width: 0 }}
                      animate={{ width: `${det.confidence * 100}%` }}
                      transition={{ duration: 1, ease: "easeOut" }}
                      className={`h-full rounded-full ${det.confidence > 0.9 ? 'bg-accent-green' : 'bg-alert-amber'}`} 
                    />
                  </div>
                </div>

                <div className="flex justify-between text-sm text-text-secondary bg-background/50 border border-border p-3 rounded-lg mt-4">
                  <span className="font-medium">Zone: <span className="text-foreground">{det.zone}</span></span>
                  <span className="font-mono text-xs">ID: {det.id.split('-')[1]}</span>
                </div>
              </CardContent>
            </Card>
          </motion.div>
        ))}
      </div>
    </div>
  );
}