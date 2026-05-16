import os
import textwrap

def create_file(path, content):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w') as f:
        f.write(textwrap.dedent(content).strip())

create_file("app/page.tsx", """
'use client';
import { Button } from "@/components/ui/button";
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { Badge } from "@/components/ui/badge";

import { motion } from "framer-motion";
import { ArrowRight, Droplet, Wind, Crosshair, PlayCircle, Cpu, Radar, Shield } from "lucide-react";
import Link from "next/link";
import dynamic from 'next/dynamic';

const MapPreview = dynamic(() => import('@/components/Map'), { ssr: false, loading: () => <div className="h-full w-full bg-muted rounded-lg flex items-center justify-center animate-pulse">Loading map...</div> });

export default function Home() {
  return (
    <div className="flex flex-col relative z-10">
      {/* HERO SECTION */}
      <section className="relative min-h-[90vh] flex items-center overflow-hidden border-b border-border/50">
        <div className="absolute inset-0 bg-grid-pattern opacity-30 pointer-events-none" />
        <div className="container relative z-10 grid grid-cols-1 lg:grid-cols-2 gap-12 items-center py-20">
          <motion.div 
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ duration: 0.6 }}
            className="flex flex-col space-y-8"
          >
            <div>
              <Badge variant="outline" className="bg-background/80 backdrop-blur border-accent-green text-accent-green mb-6 px-3 py-1 shadow-lg">
                <span className="h-2 w-2 rounded-full bg-accent-green mr-2 animate-pulse-dot"></span> 
                Live System Active
              </Badge>
              <h1 className="text-5xl md:text-7xl font-bold tracking-tight text-foreground mb-4 leading-tight">
                Protect Farmers.<br/>
                <span className="text-transparent bg-clip-text bg-gradient-to-r from-accent-green to-blue-500">
                  Nourish Crops.
                </span>
              </h1>
              <p className="text-xl text-text-secondary max-w-lg leading-relaxed">
                A closed-loop drone + rover ecosystem with AI crop disease detection, laser pest control & precision irrigation.
              </p>
            </div>
            <div className="flex flex-col sm:flex-row gap-4">
              <Link href="/dashboard">
                <Button size="lg" className="w-full sm:w-auto bg-accent-green text-white hover:bg-emerald-600 shadow-xl shadow-accent-green/20 font-bold text-md px-8 py-6 h-auto transition-transform hover:-translate-y-1">
                  View Live Demo <ArrowRight className="ml-2 h-5 w-5" />
                </Button>
              </Link>
              <Button size="lg" variant="outline" className="w-full sm:w-auto border-border text-foreground bg-background/50 backdrop-blur-md hover:bg-accent/50 px-8 py-6 h-auto transition-transform hover:-translate-y-1">
                <PlayCircle className="mr-2 h-5 w-5" /> Watch How It Works
              </Button>
            </div>
            <div className="pt-8 border-t border-border/50">
              <p className="text-sm text-text-muted font-medium flex flex-wrap gap-x-6 gap-y-2">
                <span className="flex items-center"><Droplet className="w-4 h-4 mr-1 text-blue-400" /> 50%+ Water Saved</span>
                <span className="flex items-center"><span className="text-accent-green font-bold mr-1">₹</span> 100-150/Acre</span>
                <span className="flex items-center"><Shield className="w-4 h-4 mr-1 text-emerald-400" /> Zero Chemicals</span>
                <span className="flex items-center"><Cpu className="w-4 h-4 mr-1 text-purple-400" /> 94% AI Accuracy</span>
              </p>
            </div>
          </motion.div>

          {/* Right side mock schematic */}
          <motion.div 
            initial={{ opacity: 0, scale: 0.9 }}
            animate={{ opacity: 1, scale: 1 }}
            transition={{ duration: 0.8, delay: 0.2 }}
            className="relative h-[500px] hidden lg:block"
          >
            <div className="absolute inset-0 flex flex-col items-center justify-center">
              <div className="w-48 h-16 glass-card rounded-full flex items-center justify-center shadow-[0_0_30px_rgba(82,183,136,0.2)] animate-float mb-32 z-20">
                <Radar className="text-accent-green mr-2" /> <span className="font-bold text-foreground">Drone D1</span>
              </div>
              
              {/* Animated scan beam */}
              <div className="absolute top-[200px] w-0 h-0 border-l-[100px] border-l-transparent border-r-[100px] border-r-transparent border-b-[200px] border-b-accent-green/20 animate-pulse-slow blur-sm z-10" />
              
              <div className="w-56 h-20 glass-card rounded-lg flex items-center justify-center shadow-lg z-20 mt-16 border-blue-500/30">
                <Cpu className="text-blue-500 mr-2" /> <span className="font-bold text-foreground">Rover Active</span>
              </div>
            </div>

            {/* Floating cards */}
            <motion.div className="absolute top-10 right-0 glass-card border-l-4 border-l-alert-red p-4 rounded-xl shadow-xl w-64 backdrop-blur-md"
               initial={{ opacity: 0, x: 20 }} animate={{ opacity: 1, x: 0 }} transition={{ delay: 0.8 }}>
              <p className="text-xs text-text-secondary uppercase tracking-wider font-bold mb-1">YOLOv8 Detection</p>
              <p className="font-bold text-foreground text-sm flex items-center"><span className="w-2 h-2 rounded-full bg-alert-red mr-2"></span> Early Blight — 94% conf.</p>
            </motion.div>

            <motion.div className="absolute bottom-20 left-0 glass-card border-l-4 border-l-accent-green p-4 rounded-xl shadow-xl w-64 backdrop-blur-md"
               initial={{ opacity: 0, x: -20 }} animate={{ opacity: 1, x: 0 }} transition={{ delay: 1.2 }}>
              <p className="text-xs text-text-secondary uppercase tracking-wider font-bold mb-1">Action Layer</p>
              <p className="font-bold text-foreground text-sm flex items-center"><span className="w-2 h-2 rounded-full bg-accent-green mr-2"></span> Sprinkler ON — Zone 4A</p>
            </motion.div>
          </motion.div>
        </div>
      </section>

      {/* PROBLEM STATEMENT */}
      <section className="py-32 bg-background/50 border-b border-border/50 relative">
        <div className="container">
          <div className="text-center mb-20">
            <h2 className="text-4xl md:text-5xl font-bold mb-6 tracking-tight">Current agriculture fails at the extremes</h2>
            <p className="text-text-secondary text-lg max-w-2xl mx-auto">The industry is stuck between extreme waste and physical impossibility.</p>
          </div>

          <div className="grid grid-cols-1 md:grid-cols-2 gap-8 items-stretch relative max-w-5xl mx-auto">
            <Card className="glass-card border-alert-red/20 shadow-[0_0_30px_rgba(230,57,70,0.05)] transition-transform hover:-translate-y-2 duration-300">
              <CardHeader>
                <div className="w-14 h-14 rounded-full bg-alert-red/10 flex items-center justify-center mb-6 text-alert-red border border-alert-red/20 shadow-inner">
                  <Droplet size={28} />
                </div>
                <CardTitle className="text-2xl">Flood / Manual Irrigation</CardTitle>
              </CardHeader>
              <CardContent className="space-y-6">
                <p className="text-text-secondary leading-relaxed">Wastes enormous amounts of water, increases root rot risk, and relies heavily on unavailable manual labor.</p>
                <ul className="text-sm font-medium space-y-3 text-foreground/80 bg-background/50 p-4 rounded-lg border border-border">
                  <li className="flex items-center"><span className="text-alert-red mr-2">✕</span> 50%+ water waste</li>
                  <li className="flex items-center"><span className="text-alert-red mr-2">✕</span> Root rot risk high</li>
                  <li className="flex items-center"><span className="text-alert-red mr-2">✕</span> ₹300-500/acre operating cost</li>
                </ul>
              </CardContent>
            </Card>

            <div className="hidden md:flex absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-16 h-16 glass-card rounded-full items-center justify-center font-bold text-xl z-10 text-foreground shadow-2xl border-white/20">
              VS
            </div>

            <Card className="glass-card border-alert-amber/20 shadow-[0_0_30px_rgba(244,162,97,0.05)] transition-transform hover:-translate-y-2 duration-300">
              <CardHeader>
                <div className="w-14 h-14 rounded-full bg-alert-amber/10 flex items-center justify-center mb-6 text-alert-amber border border-alert-amber/20 shadow-inner">
                  <Wind size={28} />
                </div>
                <CardTitle className="text-2xl">Aerial Drone Spraying</CardTitle>
              </CardHeader>
              <CardContent className="space-y-6">
                <p className="text-text-secondary leading-relaxed">Highly affected by wind drift, cannot carry sufficient payload, and wastes chemical via evaporation before hitting roots.</p>
                <ul className="text-sm font-medium space-y-3 text-foreground/80 bg-background/50 p-4 rounded-lg border border-border">
                  <li className="flex items-center"><span className="text-alert-amber mr-2">⚠</span> High wind drift issues</li>
                  <li className="flex items-center"><span className="text-alert-amber mr-2">⚠</span> Cannot carry water weight</li>
                  <li className="flex items-center"><span className="text-alert-amber mr-2">⚠</span> Evaporation loss</li>
                </ul>
              </CardContent>
            </Card>
          </div>
        </div>
      </section>

      {/* SOLUTION */}
      <section className="py-32 bg-card/30 border-b border-border/50">
        <div className="container">
          <div className="text-center mb-20">
            <h2 className="text-4xl md:text-5xl font-bold mb-6 tracking-tight">We separate intelligence from payload</h2>
            <p className="text-text-secondary text-lg max-w-2xl mx-auto">A multi-agent approach to precision farming.</p>
          </div>

          <div className="grid grid-cols-1 md:grid-cols-3 gap-8">
            <div className="p-8 glass-card rounded-2xl hover:border-accent-green hover:shadow-[0_0_30px_rgba(82,183,136,0.15)] transition-all duration-300 group hover:-translate-y-2">
              <div className="w-16 h-16 bg-background rounded-full flex items-center justify-center mb-6 border border-border shadow-sm group-hover:scale-110 transition-transform">
                <Radar className="w-8 h-8 text-accent-green" />
              </div>
              <h3 className="text-2xl font-bold mb-4 text-foreground">1. Intelligence Layer</h3>
              <p className="text-text-secondary leading-relaxed">Fly at 120m, scan 80m width, stream real-time YOLOv8 detections. The unblinking eyes in the sky.</p>
            </div>
            <div className="p-8 glass-card rounded-2xl hover:border-blue-500 hover:shadow-[0_0_30px_rgba(59,130,246,0.15)] transition-all duration-300 group hover:-translate-y-2">
              <div className="w-16 h-16 bg-background rounded-full flex items-center justify-center mb-6 border border-border shadow-sm group-hover:scale-110 transition-transform">
                <Crosshair className="w-8 h-8 text-blue-500" />
              </div>
              <h3 className="text-2xl font-bold mb-4 text-foreground">2. Action Layer</h3>
              <p className="text-text-secondary leading-relaxed">Carries 8L hot-swap tanks, 300W motors, executes AI-directed precision watering and laser targeting on the ground.</p>
            </div>
            <div className="p-8 glass-card rounded-2xl hover:border-purple-500 hover:shadow-[0_0_30px_rgba(168,85,247,0.15)] transition-all duration-300 group hover:-translate-y-2">
              <div className="w-16 h-16 bg-background rounded-full flex items-center justify-center mb-6 border border-border shadow-sm group-hover:scale-110 transition-transform">
                <Shield className="w-8 h-8 text-purple-500" />
              </div>
              <h3 className="text-2xl font-bold mb-4 text-foreground">3. Control Layer</h3>
              <p className="text-text-secondary leading-relaxed">Approves tasks from anywhere. One tap = rover dispatched. Full audit trail and analytics dashboard.</p>
            </div>
          </div>
        </div>
      </section>

      {/* LIVE DEMO PREVIEW */}
      <section className="py-32 bg-background relative overflow-hidden">
        <div className="absolute inset-0 bg-gradient-to-t from-background via-transparent to-transparent z-0 pointer-events-none" />
        <div className="container relative z-10">
          <div className="text-center mb-16">
            <h2 className="text-4xl md:text-5xl font-bold mb-6 tracking-tight">See the system working — live</h2>
            <p className="text-text-secondary text-lg">Simulated field data updates every 3 seconds.</p>
          </div>
          
          <div className="max-w-6xl mx-auto glass-card rounded-2xl overflow-hidden flex flex-col md:flex-row h-[600px] shadow-2xl">
            <div className="w-full md:w-2/3 h-[300px] md:h-full relative">
              <MapPreview />
            </div>
            <div className="w-full md:w-1/3 p-8 flex flex-col bg-background/50 backdrop-blur-md border-l border-border">
              <h3 className="font-bold text-xl mb-8 flex items-center text-foreground">
                <span className="h-2.5 w-2.5 rounded-full bg-accent-green mr-3 animate-pulse-dot shadow-[0_0_10px_rgba(82,183,136,0.8)]"></span> 
                Live Telemetry
              </h3>
              
              <div className="space-y-5 mb-auto">
                <div className="bg-card p-4 rounded-xl border border-border/50 text-sm flex justify-between items-center shadow-sm hover:shadow-md transition-shadow">
                  <span className="text-text-secondary font-medium">Drone D1 Status</span>
                  <Badge variant="outline" className="text-accent-green border-accent-green/30 bg-accent-green/10">Scanning (82%)</Badge>
                </div>
                <div className="bg-card p-4 rounded-xl border border-border/50 text-sm flex justify-between items-center shadow-sm hover:shadow-md transition-shadow">
                  <span className="text-text-secondary font-medium">Rover R1 Status</span>
                  <Badge className="bg-blue-500 hover:bg-blue-600">Moving to 4A</Badge>
                </div>
                <div className="bg-alert-red/5 border border-alert-red/20 p-5 rounded-xl flex flex-col gap-2 shadow-sm relative overflow-hidden">
                  <div className="absolute right-0 top-0 w-16 h-16 bg-alert-red/10 rounded-bl-full"></div>
                  <span className="text-alert-red text-[10px] font-bold uppercase tracking-widest flex items-center">
                    <span className="w-1.5 h-1.5 rounded-full bg-alert-red mr-2"></span> Latest Detection
                  </span>
                  <span className="text-foreground font-semibold text-base">Early Blight — 94% conf.</span>
                </div>
              </div>
              
              <div className="mt-8">
                <Link href="/dashboard" className="block w-full">
                  <Button className="w-full bg-accent-green text-white hover:bg-emerald-600 shadow-lg font-bold py-6">
                    Open Full Dashboard <ArrowRight className="ml-2 h-5 w-5" />
                  </Button>
                </Link>
              </div>
            </div>
          </div>
        </div>
      </section>
    </div>
  );
}
""")

print("Home page updated successfully.")
