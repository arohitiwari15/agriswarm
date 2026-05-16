'use client';
import { Button } from "@/components/ui/button";
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { Badge } from "@/components/ui/badge";

import { motion } from "framer-motion";
import { ArrowRight, Droplet, Wind, Crosshair, PlayCircle, Cpu, Radar, Shield } from "lucide-react";
import Link from "next/link";
import dynamic from 'next/dynamic';

const MapPreview = dynamic(() => import('@/components/Map'), { ssr: false, loading: () => <div className="h-full w-full bg-card rounded-lg flex items-center justify-center animate-pulse">Loading map...</div> });

export default function Home() {
  return (
    <div className="flex flex-col">
      {/* HERO SECTION */}
      <section className="relative h-[90vh] flex items-center overflow-hidden border-b border-border">
        <div className="absolute inset-0 bg-grid-pattern opacity-30 pointer-events-none" />
        <div className="container relative z-10 grid grid-cols-1 lg:grid-cols-2 gap-12 items-center">
          <motion.div 
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ duration: 0.6 }}
            className="flex flex-col space-y-8"
          >
            <div>
              <Badge variant="outline" className="border-accent-green text-accent-green mb-6 px-3 py-1">
                <span className="h-2 w-2 rounded-full bg-accent-green mr-2 animate-pulse-dot"></span> 
                Live System Active
              </Badge>
              <h1 className="text-5xl md:text-7xl font-bold tracking-tight text-white mb-4 leading-tight">
                Protect Farmers.<br/>
                <span className="text-transparent bg-clip-text bg-gradient-to-r from-accent-green to-emerald-400">
                  Nourish Crops.
                </span>
              </h1>
              <p className="text-xl text-text-secondary max-w-lg leading-relaxed">
                A closed-loop drone + rover ecosystem with AI crop disease detection, laser pest control & precision irrigation.
              </p>
            </div>
            <div className="flex flex-col sm:flex-row gap-4">
              <Link href="/dashboard">
                <Button size="lg" className="w-full sm:w-auto bg-accent-green text-bg-primary hover:bg-emerald-400 font-bold text-md px-8 py-6 h-auto">
                  View Live Demo <ArrowRight className="ml-2 h-5 w-5" />
                </Button>
              </Link>
              <Button size="lg" variant="outline" className="w-full sm:w-auto border-border text-white hover:bg-accent-dark/30 px-8 py-6 h-auto">
                <PlayCircle className="mr-2 h-5 w-5" /> Watch How It Works
              </Button>
            </div>
            <div className="pt-8 border-t border-border/50">
              <p className="text-sm text-text-muted font-medium flex flex-wrap gap-x-6 gap-y-2">
                <span>50%+ Water Saved</span>
                <span>₹100-150/Acre</span>
                <span>Zero Chemicals</span>
                <span>94% AI Accuracy</span>
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
              <div className="w-48 h-16 bg-card border border-border rounded-full flex items-center justify-center shadow-[0_0_30px_rgba(82,183,136,0.2)] animate-float mb-32 z-20">
                <Radar className="text-accent-green mr-2" /> <span className="font-bold">Drone D1</span>
              </div>

              {/* Animated scan beam */}
              <div className="absolute top-[200px] w-0 h-0 border-l-[100px] border-l-transparent border-r-[100px] border-r-transparent border-b-[200px] border-b-accent-green/20 animate-pulse-slow blur-sm z-10" />

              <div className="w-56 h-20 bg-elevated border border-border rounded-lg flex items-center justify-center shadow-lg z-20 mt-16">
                <Cpu className="text-alert-red mr-2" /> <span className="font-bold">Rover Active</span>
              </div>
            </div>

            {/* Floating cards */}
            <motion.div className="absolute top-10 right-0 bg-card border-l-4 border-l-alert-red p-4 rounded shadow-xl w-64"
               initial={{ opacity: 0, x: 20 }} animate={{ opacity: 1, x: 0 }} transition={{ delay: 0.8 }}>
              <p className="text-xs text-text-secondary">YOLOv8 Detection</p>
              <p className="font-bold text-white text-sm">Early Blight — 94% conf.</p>
            </motion.div>

            <motion.div className="absolute bottom-20 left-0 bg-card border-l-4 border-l-accent-green p-4 rounded shadow-xl w-64"
               initial={{ opacity: 0, x: -20 }} animate={{ opacity: 1, x: 0 }} transition={{ delay: 1.2 }}>
              <p className="text-xs text-text-secondary">Action Layer</p>
              <p className="font-bold text-white text-sm">Sprinkler ON — Zone 4A</p>
            </motion.div>
          </motion.div>
        </div>
      </section>

      {/* PROBLEM STATEMENT */}
      <section className="py-24 bg-background border-b border-border relative">
        <div className="container">
          <div className="text-center mb-16">
            <h2 className="text-3xl md:text-4xl font-bold mb-4">Current agriculture fails at the extremes</h2>
            <p className="text-text-secondary max-w-2xl mx-auto">The industry is stuck between extreme waste and physical impossibility.</p>
          </div>

          <div className="grid grid-cols-1 md:grid-cols-2 gap-8 items-stretch relative max-w-4xl mx-auto">
            <Card className="bg-card border-alert-red/20 shadow-[0_0_15px_rgba(230,57,70,0.05)]">
              <CardHeader>
                <div className="w-12 h-12 rounded-full bg-alert-red/10 flex items-center justify-center mb-4 text-alert-red">
                  <Droplet size={24} />
                </div>
                <CardTitle>Flood / Manual Irrigation</CardTitle>
              </CardHeader>
              <CardContent className="space-y-4">
                <p className="text-text-secondary">Wastes enormous amounts of water, increases root rot risk, and relies on manual labor.</p>
                <ul className="text-sm font-medium space-y-2 text-alert-red/80">
                  <li>• 50%+ water waste</li>
                  <li>• Root rot risk high</li>
                  <li>• ₹300-500/acre operating cost</li>
                </ul>
              </CardContent>
            </Card>

            <div className="hidden md:flex absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-12 h-12 bg-background border border-border rounded-full items-center justify-center font-bold text-lg z-10 text-white shadow-xl">
              VS
            </div>

            <Card className="bg-card border-alert-amber/20 shadow-[0_0_15px_rgba(244,162,97,0.05)]">
              <CardHeader>
                <div className="w-12 h-12 rounded-full bg-alert-amber/10 flex items-center justify-center mb-4 text-alert-amber">
                  <Wind size={24} />
                </div>
                <CardTitle>Aerial Drone Spraying</CardTitle>
              </CardHeader>
              <CardContent className="space-y-4">
                <p className="text-text-secondary">Highly affected by wind drift, cannot carry sufficient payload, and wastes chemical via evaporation.</p>
                <ul className="text-sm font-medium space-y-2 text-alert-amber/80">
                  <li>• High wind drift issues</li>
                  <li>• Cannot carry water weight</li>
                  <li>• Evaporation loss before hitting roots</li>
                </ul>
              </CardContent>
            </Card>
          </div>
        </div>
      </section>

      {/* SOLUTION */}
      <section className="py-24 bg-card border-b border-border">
        <div className="container">
          <div className="text-center mb-16">
            <h2 className="text-3xl md:text-4xl font-bold mb-4">We separate intelligence from payload</h2>
            <p className="text-text-secondary max-w-2xl mx-auto">A multi-agent approach to precision farming.</p>
          </div>

          <div className="grid grid-cols-1 md:grid-cols-3 gap-8 mb-16">
            <div className="p-6 bg-background rounded-xl border border-border hover:border-accent-green transition-colors group">
              <Radar className="w-10 h-10 text-accent-green mb-4 group-hover:scale-110 transition-transform" />
              <h3 className="text-xl font-bold mb-2 text-white">1. Drones — Intelligence</h3>
              <p className="text-text-secondary text-sm">Fly at 120m, scan 80m width, stream real-time YOLOv8 detections. Eyes in the sky.</p>
            </div>
            <div className="p-6 bg-background rounded-xl border border-border hover:border-accent-green transition-colors group">
              <Crosshair className="w-10 h-10 text-accent-green mb-4 group-hover:scale-110 transition-transform" />
              <h3 className="text-xl font-bold mb-2 text-white">2. Rover — Action</h3>
              <p className="text-text-secondary text-sm">Carries 8L hot-swap tanks, 300W motors, executes AI-directed precision watering and laser targeting.</p>
            </div>
            <div className="p-6 bg-background rounded-xl border border-border hover:border-accent-green transition-colors group">
              <Shield className="w-10 h-10 text-accent-green mb-4 group-hover:scale-110 transition-transform" />
              <h3 className="text-xl font-bold mb-2 text-white">3. Farmer — Control</h3>
              <p className="text-text-secondary text-sm">Approves tasks from anywhere. One tap = rover dispatched. Full audit trail.</p>
            </div>
          </div>
        </div>
      </section>

      {/* COMPARISON TABLE */}
      <section className="py-24 bg-background border-b border-border">
        <div className="container max-w-5xl">
          <h2 className="text-3xl md:text-4xl font-bold mb-12 text-center">Optimizing cost, precision, and crop health</h2>

          <div className="overflow-x-auto">
            <table className="w-full text-left border-collapse">
              <thead>
                <tr className="border-b border-border text-text-muted text-sm uppercase tracking-wider">
                  <th className="py-4 px-6 font-medium">Method</th>
                  <th className="py-4 px-6 font-medium">Water Use</th>
                  <th className="py-4 px-6 font-medium">Precision</th>
                  <th className="py-4 px-6 font-medium">Labor</th>
                  <th className="py-4 px-6 font-medium text-right">Cost/Acre</th>
                </tr>
              </thead>
              <tbody className="text-sm">
                <tr className="border-b border-border/50 bg-card/30">
                  <td className="py-5 px-6 font-medium">Flood/Manual</td>
                  <td className="py-5 px-6 text-alert-red">High</td>
                  <td className="py-5 px-6 text-text-secondary">Low</td>
                  <td className="py-5 px-6 text-alert-red">High</td>
                  <td className="py-5 px-6 text-right font-medium">₹300-500</td>
                </tr>
                <tr className="border-b border-border/50 bg-card/30">
                  <td className="py-5 px-6 font-medium">Drone Spraying</td>
                  <td className="py-5 px-6 text-alert-amber">Medium (drift)</td>
                  <td className="py-5 px-6 text-alert-amber">Medium</td>
                  <td className="py-5 px-6 text-accent-green">Low</td>
                  <td className="py-5 px-6 text-right font-medium">₹200-350</td>
                </tr>
                <tr className="border-2 border-accent-green bg-accent-dark/20 relative">
                  <td className="py-5 px-6 font-bold text-accent-green flex items-center">
                    Agri-Swarm <span className="ml-2 text-lg">✓</span>
                  </td>
                  <td className="py-5 px-6 font-medium text-white">Low (targeted)</td>
                  <td className="py-5 px-6 font-medium text-white">High (zone-spec)</td>
                  <td className="py-5 px-6 font-medium text-white">Zero</td>
                  <td className="py-5 px-6 text-right font-bold text-accent-green">₹100-150</td>
                </tr>
              </tbody>
            </table>
          </div>
        </div>
      </section>

      {/* LIVE DEMO PREVIEW */}
      <section className="py-24 bg-card relative overflow-hidden">
        <div className="absolute inset-0 bg-gradient-to-t from-background to-transparent z-0" />
        <div className="container relative z-10">
          <div className="text-center mb-12">
            <h2 className="text-3xl md:text-4xl font-bold mb-4">See the system working — live</h2>
            <p className="text-text-secondary">Simulated field data updates every 3 seconds.</p>
          </div>

          <div className="max-w-6xl mx-auto bg-background border border-border rounded-xl shadow-2xl overflow-hidden flex flex-col md:flex-row h-[500px]">
            <div className="w-full md:w-2/3 h-[300px] md:h-full relative">
              <MapPreview />
            </div>
            <div className="w-full md:w-1/3 p-6 flex flex-col bg-card border-l border-border">
              <h3 className="font-bold text-lg mb-6 flex items-center">
                <span className="h-2 w-2 rounded-full bg-accent-green mr-2 animate-pulse-dot"></span> 
                Live Telemetry
              </h3>

              <div className="space-y-4 mb-auto">
                <div className="bg-background p-3 rounded border border-border text-sm flex justify-between">
                  <span className="text-text-secondary">Drone D1 Status</span>
                  <span className="text-accent-green font-medium">Scanning (82%)</span>
                </div>
                <div className="bg-background p-3 rounded border border-border text-sm flex justify-between">
                  <span className="text-text-secondary">Rover R1 Status</span>
                  <span className="text-white font-medium">Moving to Zone 4A</span>
                </div>
                <div className="bg-alert-red/10 border border-alert-red/30 p-3 rounded text-sm flex flex-col gap-1">
                  <span className="text-alert-red text-xs font-bold uppercase tracking-wider">Latest Detection</span>
                  <span className="text-white">Early Blight — 94% conf.</span>
                </div>
              </div>

              <div className="mt-8 text-center">
                <Link href="/dashboard">
                  <Button className="w-full bg-accent-green text-bg-primary hover:bg-emerald-400">
                    Open Full Dashboard <ArrowRight className="ml-2 h-4 w-4" />
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