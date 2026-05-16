'use client';
import { useSimulation, Detection } from "@/lib/simulation";
import { Badge } from "@/components/ui/badge";
import { formatDistanceToNow } from "date-fns";
import { AlertTriangle, CheckCircle } from "lucide-react";
import { Card, CardContent } from "@/components/ui/card";

export default function DetectionFeed() {
  const { detections } = useSimulation();

  return (
    <div className="container py-8">
      <div className="mb-8">
        <h1 className="text-3xl font-bold mb-2">AI Detection Feed</h1>
        <p className="text-text-secondary">Live YOLOv8 feed streamed from drones.</p>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
        {detections.map((det: Detection) => (
          <Card key={det.id} className="overflow-hidden border-border bg-card">
            <div className="h-48 bg-elevated relative flex items-center justify-center p-4">
              {/* Mock crop image placeholder */}
              <div className="absolute inset-0 opacity-20 bg-[url('https://images.unsplash.com/photo-1599839619722-39751411ea63?q=80&w=600&auto=format&fit=crop')] bg-cover bg-center mix-blend-overlay"></div>

              {/* Bounding box mock */}
              {det.disease !== 'Healthy' && (
                <div className="absolute w-32 h-32 border-2 border-alert-red rounded bg-alert-red/10 flex items-end">
                  <span className="bg-alert-red text-white text-[10px] px-1 py-0.5 font-mono">{det.disease} {Math.round(det.confidence*100)}%</span>
                </div>
              )}
            </div>
            <CardContent className="p-5">
              <div className="flex justify-between items-start mb-4">
                <div>
                  <h3 className="font-bold text-lg text-white mb-1 flex items-center gap-2">
                    {det.disease === 'Healthy' ? <CheckCircle className="w-5 h-5 text-accent-green" /> : <AlertTriangle className="w-5 h-5 text-alert-red" />}
                    {det.disease}
                  </h3>
                  <p className="text-xs text-text-secondary">{formatDistanceToNow(new Date(det.timestamp), { addSuffix: true })}</p>
                </div>
                <Badge variant={det.disease === 'Healthy' ? 'secondary' : 'destructive'} className="text-xs">
                  {det.severity}
                </Badge>
              </div>

              <div className="space-y-2 mb-4">
                <div className="flex justify-between text-sm">
                  <span className="text-text-muted">Confidence</span>
                  <span className="font-medium">{(det.confidence * 100).toFixed(1)}%</span>
                </div>
                <div className="w-full bg-background rounded-full h-1.5">
                  <div className={`h-1.5 rounded-full ${det.confidence > 0.9 ? 'bg-accent-green' : 'bg-alert-amber'}`} style={{ width: `${det.confidence * 100}%` }}></div>
                </div>
              </div>

              <div className="flex justify-between text-sm text-text-secondary bg-background p-2 rounded">
                <span>Zone: {det.zone}</span>
                <span>Coord: {det.position[0].toFixed(4)}, {det.position[1].toFixed(4)}</span>
              </div>
            </CardContent>
          </Card>
        ))}
      </div>
    </div>
  );
}