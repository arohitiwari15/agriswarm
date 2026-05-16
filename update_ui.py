import os
import textwrap

def create_file(path, content):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w') as f:
        f.write(textwrap.dedent(content).strip())

# 1. Update globals.css for light theme
create_file("app/globals.css", """
@tailwind base;
@tailwind components;
@tailwind utilities;

@layer base {
  :root {
    /* LIGHT THEME VARIABLES */
    --bg-primary: 0 0% 100%;       /* #FFFFFF */
    --bg-card: 210 40% 96%;        /* #F1F5F9 */
    --bg-elevated: 0 0% 100%;      /* #FFFFFF */
    
    --accent-green: 152 42% 40%;   /* Darker mint for contrast */
    --accent-dark: 155 42% 18%;    /* Forest green */
    
    --alert-red: 355 78% 56%;      
    --alert-amber: 26 89% 50%;     
    
    --text-primary: 216 53% 11%;   /* Dark navy */
    --text-secondary: 215 16% 47%; /* Slate */
    --text-muted: 215 20% 65%;     
    
    --border: 214 32% 91%;         /* Light gray border */

    --background: var(--bg-primary);
    --foreground: var(--text-primary);
    
    --card: var(--bg-card);
    --card-foreground: var(--text-primary);
    
    --popover: var(--bg-elevated);
    --popover-foreground: var(--text-primary);
    
    --primary: var(--accent-green);
    --primary-foreground: 0 0% 100%;
    
    --secondary: 214 32% 91%;
    --secondary-foreground: 222.2 47.4% 11.2%;
    
    --muted: 210 40% 96.1%;
    --muted-foreground: 215.4 16.3% 46.9%;
    
    --accent: 210 40% 96.1%;
    --accent-foreground: 222.2 47.4% 11.2%;
    
    --destructive: var(--alert-red);
    --destructive-foreground: 0 0% 100%;

    --border-color: var(--border);
    --input: var(--border);
    --ring: var(--accent-green);

    --radius: 0.5rem;
  }

  .dark {
    /* DARK THEME VARIABLES */
    --bg-primary: 216 53% 11%;     /* #0D1B2A */
    --bg-card: 216 42% 18%;        /* #1A2940 */
    --bg-elevated: 211 41% 20%;    /* #1E3448 */
    
    --accent-green: 152 42% 52%;   /* #52B788 */
    --accent-dark: 155 42% 18%;    /* #1B4332 */
    
    --text-primary: 0 0% 100%;     /* #FFFFFF */
    --text-secondary: 216 15% 71%; /* #A8B2C1 */
    --text-muted: 218 17% 35%;     /* #4A5568 */
    
    --border: 216 38% 27%;         /* #2A3F5F */

    --background: var(--bg-primary);
    --foreground: var(--text-primary);
    
    --card: var(--bg-card);
    --card-foreground: var(--text-primary);
    
    --popover: var(--bg-elevated);
    --popover-foreground: var(--text-primary);
    
    --primary: var(--accent-green);
    --primary-foreground: var(--bg-primary);
    
    --secondary: var(--accent-dark);
    --secondary-foreground: var(--text-primary);
    
    --muted: var(--bg-elevated);
    --muted-foreground: var(--text-muted);
    
    --accent: var(--accent-green);
    --accent-foreground: var(--bg-primary);
    
    --border-color: var(--border);
    --input: var(--border);
    --ring: var(--accent-green);
  }
}

@layer base {
  * {
    @apply border-border;
  }
  body {
    @apply bg-background text-foreground antialiased transition-colors duration-300;
    font-family: 'Inter', sans-serif;
  }
}

@layer utilities {
  .animate-float {
    animation: float 3s ease-in-out infinite;
  }
  .animate-pulse-slow {
    animation: pulse 2s cubic-bezier(0.4, 0, 0.6, 1) infinite;
  }
  .animate-pulse-dot {
    animation: pulse-dot 1.5s ease-in-out infinite;
  }
  .bg-grid-pattern {
    background-size: 40px 40px;
    background-image: linear-gradient(to right, rgba(82, 183, 136, 0.05) 1px, transparent 1px),
                      linear-gradient(to bottom, rgba(82, 183, 136, 0.05) 1px, transparent 1px);
  }
  .glass-card {
    @apply bg-card/70 backdrop-blur-md border border-white/10 shadow-xl;
  }
}

@keyframes float {
  0% { transform: translateY(0px); }
  50% { transform: translateY(-8px); }
  100% { transform: translateY(0px); }
}

@keyframes pulse-dot {
  0% { transform: scale(0.95); box-shadow: 0 0 0 0 rgba(82, 183, 136, 0.7); }
  70% { transform: scale(1); box-shadow: 0 0 0 6px rgba(82, 183, 136, 0); }
  100% { transform: scale(0.95); box-shadow: 0 0 0 0 rgba(82, 183, 136, 0); }
}
""")

# 2. Theme Provider
create_file("components/ThemeProvider.tsx", """
"use client"

import * as React from "react"
import { ThemeProvider as NextThemesProvider } from "next-themes"
import { type ThemeProviderProps } from "next-themes/dist/types"

export function ThemeProvider({ children, ...props }: ThemeProviderProps) {
  return <NextThemesProvider {...props}>{children}</NextThemesProvider>
}
""")

# 3. Theme Toggle
create_file("components/ThemeToggle.tsx", """
"use client"

import * as React from "react"
import { Moon, Sun } from "lucide-react"
import { useTheme } from "next-themes"

import { Button } from "@/components/ui/button"

export function ThemeToggle() {
  const { setTheme, theme } = useTheme()

  return (
    <Button
      variant="ghost"
      size="icon"
      onClick={() => setTheme(theme === "light" ? "dark" : "light")}
      className="rounded-full w-9 h-9"
    >
      <Sun className="h-[1.2rem] w-[1.2rem] rotate-0 scale-100 transition-all dark:-rotate-90 dark:scale-0" />
      <Moon className="absolute h-[1.2rem] w-[1.2rem] rotate-90 scale-0 transition-all dark:rotate-0 dark:scale-100 text-white" />
      <span className="sr-only">Toggle theme</span>
    </Button>
  )
}
""")

# 4. Layout
create_file("app/layout.tsx", """
import type { Metadata } from "next";
import { Inter } from "next/font/google";
import "./globals.css";
import Link from "next/link";
import { Badge } from "@/components/ui/badge";
import { SimulationProvider } from "@/components/SimulationProvider";
import { ThemeProvider } from "@/components/ThemeProvider";
import { ThemeToggle } from "@/components/ThemeToggle";

const inter = Inter({ subsets: ["latin"] });

export const metadata: Metadata = {
  title: "Agri-Swarm | Precision Farming AI",
  description: "AI-powered precision farming platform using drone swarms and rover.",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en" suppressHydrationWarning>
      <body className={inter.className}>
        <ThemeProvider
          attribute="class"
          defaultTheme="dark"
          enableSystem={false}
          disableTransitionOnChange
        >
          <SimulationProvider>
            <div className="flex flex-col min-h-screen bg-background text-foreground relative overflow-x-hidden">
              {/* Premium Background Blurs */}
              <div className="fixed top-0 left-[-10%] w-[40%] h-[400px] bg-accent-green/10 rounded-full blur-[120px] pointer-events-none z-0"></div>
              <div className="fixed bottom-[-10%] right-[-5%] w-[30%] h-[300px] bg-blue-500/10 rounded-full blur-[100px] pointer-events-none z-0"></div>
              
              <header className="sticky top-0 z-50 w-full border-b border-border/40 bg-background/80 backdrop-blur-md supports-[backdrop-filter]:bg-background/60">
                <div className="container flex h-16 items-center">
                  <div className="mr-8 flex items-center space-x-2">
                    <Link href="/" className="flex items-center space-x-2">
                      <span className="font-bold text-xl tracking-tight text-foreground">Agri-Swarm</span>
                      <Badge variant="outline" className="border-accent-green text-accent-green ml-2 hidden sm:inline-flex shadow-[0_0_10px_rgba(82,183,136,0.2)]">
                        <span className="h-1.5 w-1.5 rounded-full bg-accent-green mr-1.5 animate-pulse-dot"></span> System Active
                      </Badge>
                    </Link>
                  </div>
                  <div className="flex flex-1 items-center justify-between space-x-2 md:justify-end">
                    <nav className="flex items-center space-x-6 text-sm font-medium text-text-secondary">
                      <Link href="/dashboard" className="transition-colors hover:text-foreground">Dashboard</Link>
                      <Link href="/detection" className="transition-colors hover:text-foreground">Detection</Link>
                      <Link href="/technology" className="transition-colors hover:text-foreground">Technology</Link>
                    </nav>
                    <ThemeToggle />
                  </div>
                </div>
              </header>
              <main className="flex-1 relative z-10">{children}</main>
              <footer className="border-t border-border py-6 md:py-0 relative z-10 bg-background/50 backdrop-blur-sm">
                <div className="container flex flex-col items-center justify-between gap-4 md:h-24 md:flex-row text-text-muted">
                  <p className="text-center text-sm leading-loose md:text-left">
                    ©️ 2025 Agri-Swarm. Indigenous R&D, India.
                  </p>
                  <div className="flex space-x-4 text-sm">
                    <Link href="/dashboard" className="hover:text-foreground">Dashboard</Link>
                    <Link href="/technology" className="hover:text-foreground">Technology</Link>
                  </div>
                </div>
              </footer>
            </div>
          </SimulationProvider>
        </ThemeProvider>
      </body>
    </html>
  );
}
""")

# 5. Simulation Store Update
create_file("lib/simulation.ts", """
import { create } from 'zustand'

export type Coordinate = [number, number];

export interface Drone {
  id: string;
  battery: number;
  status: 'Scanning' | 'Returning' | 'Idle' | 'Charging';
  zone: string;
  position: Coordinate;
}

export interface Rover {
  id: string;
  battery: number;
  status: 'Idle' | 'Moving' | 'Spraying' | 'Charging';
  zone: string;
  position: Coordinate;
}

export interface Detection {
  id: string;
  disease: string;
  confidence: number;
  zone: string;
  timestamp: Date;
  position: Coordinate;
  severity: 'CRITICAL' | 'HIGH' | 'MEDIUM' | 'LOW';
  imageUrl: string;
}

export interface Task {
  id: string;
  title: string;
  status: 'Pending' | 'In Progress' | 'Completed';
  zone: string;
  priority: 'HIGH' | 'MEDIUM' | 'LOW';
}

interface SimulationState {
  drones: Drone[];
  rover: Rover;
  detections: Detection[];
  tasks: Task[];
  stats: {
    acresScanned: number;
    waterSaved: number;
  };
  addDetection: (d: Detection) => void;
  updateFleet: () => void;
  approveTask: (id: string) => void;
}

const INITIAL_CENTER: Coordinate = [17.3850, 78.4867]; // Hyderabad

// MAPPING DISEASES TO REAL IMAGES
export const DISEASE_IMAGES: Record<string, string> = {
  "Early Blight": "https://images.unsplash.com/photo-1599839619722-39751411ea63?q=80&w=600&auto=format&fit=crop",
  "Late Blight": "https://images.unsplash.com/photo-1622383563227-04401ab4e5ea?q=80&w=600&auto=format&fit=crop",
  "Leaf Mold": "https://images.unsplash.com/photo-1518531933037-91b2f5f229cc?q=80&w=600&auto=format&fit=crop",
  "Spider Mites": "https://images.unsplash.com/photo-1588602283944-18002df35222?q=80&w=600&auto=format&fit=crop",
  "Powdery Mildew": "https://images.unsplash.com/photo-1611078712760-4966606fbcf0?q=80&w=600&auto=format&fit=crop",
  "Aphid Cluster": "https://images.unsplash.com/photo-1621505353528-9842a24bc1ff?q=80&w=600&auto=format&fit=crop",
  "Healthy": "https://images.unsplash.com/photo-1550986518-e2168305eb41?q=80&w=600&auto=format&fit=crop"
};

const generateRandomCoord = (center: Coordinate, offset: number): Coordinate => {
  return [
    center[0] + (Math.random() - 0.5) * offset,
    center[1] + (Math.random() - 0.5) * offset
  ];
};

export const useSimulation = create<SimulationState>((set) => ({
  drones: [
    { id: 'D1', battery: 82, status: 'Scanning', zone: '4A', position: generateRandomCoord(INITIAL_CENTER, 0.01) },
    { id: 'D2', battery: 65, status: 'Returning', zone: 'Base', position: generateRandomCoord(INITIAL_CENTER, 0.01) },
    { id: 'D3', battery: 91, status: 'Scanning', zone: '6B', position: generateRandomCoord(INITIAL_CENTER, 0.01) },
  ],
  rover: {
    id: 'R1', battery: 90, status: 'Idle', zone: 'Base', position: generateRandomCoord(INITIAL_CENTER, 0.005)
  },
  detections: [
    { id: 'det-1', disease: 'Early Blight', confidence: 0.94, zone: '4A', timestamp: new Date(Date.now() - 60000), position: generateRandomCoord(INITIAL_CENTER, 0.008), severity: 'HIGH', imageUrl: DISEASE_IMAGES["Early Blight"] },
    { id: 'det-2', disease: 'Healthy', confidence: 0.98, zone: '4A', timestamp: new Date(Date.now() - 120000), position: generateRandomCoord(INITIAL_CENTER, 0.008), severity: 'LOW', imageUrl: DISEASE_IMAGES["Healthy"] }
  ],
  tasks: [
    { id: 'task-1', title: 'Spot Spray — Early Blight', status: 'Pending', zone: '4A', priority: 'HIGH' },
    { id: 'task-2', title: 'Laser Target — Aphid Cluster', status: 'In Progress', zone: '2B', priority: 'MEDIUM' },
  ],
  stats: {
    acresScanned: 24.5,
    waterSaved: 340
  },
  addDetection: (d) => set((state) => ({
    detections: [d, ...state.detections].slice(0, 50),
    stats: { ...state.stats, acresScanned: +(state.stats.acresScanned + 0.1).toFixed(1) }
  })),
  updateFleet: () => set((state) => ({
    drones: state.drones.map(d => ({
      ...d,
      battery: Math.max(0, d.battery - 0.1),
      position: d.status === 'Scanning' ? generateRandomCoord(d.position, 0.0005) : d.position
    })),
    rover: {
      ...state.rover,
      position: state.rover.status === 'Moving' ? generateRandomCoord(state.rover.position, 0.0005) : state.rover.position
    }
  })),
  approveTask: (id) => set((state) => ({
    tasks: state.tasks.map(t => t.id === id ? { ...t, status: 'In Progress' } : t),
    rover: { ...state.rover, status: 'Moving' }
  }))
}));
""")

# 6. SimulationProvider Update (to pass the image url)
create_file("components/SimulationProvider.tsx", """
'use client';
import { useEffect } from 'react';
import { useSimulation, DISEASE_IMAGES } from '@/lib/simulation';

export function SimulationProvider({ children }: { children: React.ReactNode }) {
  const updateFleet = useSimulation((state) => state.updateFleet);
  const addDetection = useSimulation((state) => state.addDetection);

  useEffect(() => {
    // Update fleet positions and battery every 3 seconds
    const fleetInterval = setInterval(() => {
      updateFleet();
    }, 3000);

    // Random new detection every 20 seconds
    const detectionInterval = setInterval(() => {
      const diseases = ["Early Blight", "Late Blight", "Powdery Mildew", "Aphid Cluster", "Healthy"];
      const randomDisease = diseases[Math.floor(Math.random() * diseases.length)];
      addDetection({
        id: `det-${Date.now()}`,
        disease: randomDisease,
        confidence: 0.85 + Math.random() * 0.14,
        zone: ['4A', '2B', '6B', '1C', '3A'][Math.floor(Math.random() * 5)],
        timestamp: new Date(),
        position: [17.3850 + (Math.random() - 0.5) * 0.01, 78.4867 + (Math.random() - 0.5) * 0.01],
        severity: randomDisease === "Healthy" ? 'LOW' : (Math.random() > 0.5 ? 'HIGH' : 'MEDIUM'),
        imageUrl: DISEASE_IMAGES[randomDisease] || DISEASE_IMAGES["Healthy"]
      });
    }, 20000);

    return () => {
      clearInterval(fleetInterval);
      clearInterval(detectionInterval);
    };
  }, [updateFleet, addDetection]);

  return <>{children}</>;
}
""")

# 7. Detection Page Update
create_file("app/detection/page.tsx", """
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
""")

# 8. Dashboard Dashboard Updates (with recharts)
create_file("app/dashboard/page.tsx", """
'use client';

import { useSimulation } from "@/lib/simulation";
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { Badge } from "@/components/ui/badge";
import { Button } from "@/components/ui/button";
import { Tabs, TabsList, TabsTrigger, TabsContent } from "@/components/ui/tabs";
import { AlertCircle, Battery, BatteryCharging, Crosshair, Map as MapIcon, CheckCircle2 } from "lucide-react";
import dynamic from 'next/dynamic';
import { AreaChart, Area, XAxis, YAxis, CartesianGrid, Tooltip, ResponsiveContainer } from 'recharts';

const FieldMap = dynamic(() => import('@/components/Map'), { ssr: false, loading: () => <div className="h-full w-full bg-muted flex items-center justify-center animate-pulse rounded-xl">Loading Live Map...</div> });

const mockChartData = [
  { time: '08:00', water: 120 },
  { time: '09:00', water: 135 },
  { time: '10:00', water: 190 },
  { time: '11:00', water: 220 },
  { time: '12:00', water: 280 },
  { time: '13:00', water: 340 },
];

export default function DashboardPage() {
  const { drones, rover, detections, tasks, stats, approveTask } = useSimulation();

  return (
    <div className="container py-8 flex flex-col gap-8 relative z-10">
      <div className="flex flex-col md:flex-row items-start md:items-center justify-between gap-4">
        <div>
          <h1 className="text-3xl font-bold tracking-tight text-foreground">Reddy Farms — Hyderabad, Telangana</h1>
          <p className="text-text-secondary text-lg mt-1">Farmer Command Center</p>
        </div>
        <Badge variant="outline" className="border-accent-green text-accent-green px-4 py-1.5 text-sm bg-accent-green/5 shadow-sm">
          <span className="h-2 w-2 rounded-full bg-accent-green mr-2 animate-pulse-dot"></span> System Active
        </Badge>
      </div>

      {/* STATS ROW */}
      <div className="grid grid-cols-2 lg:grid-cols-4 gap-4 md:gap-6">
        <Card className="glass-card transition-all duration-300 hover:shadow-2xl hover:-translate-y-1">
          <CardHeader className="flex flex-row items-center justify-between space-y-0 pb-2">
            <CardTitle className="text-sm font-medium text-text-muted">Acres Scanned</CardTitle>
            <MapIcon className="h-5 w-5 text-text-secondary" />
          </CardHeader>
          <CardContent>
            <div className="text-3xl font-bold text-foreground">{stats.acresScanned}</div>
            <p className="text-sm text-accent-green mt-1 font-medium">↑ +2.1 this hour</p>
          </CardContent>
        </Card>
        <Card className="glass-card transition-all duration-300 hover:shadow-2xl hover:-translate-y-1">
          <CardHeader className="flex flex-row items-center justify-between space-y-0 pb-2">
            <CardTitle className="text-sm font-medium text-text-muted">Active Detections</CardTitle>
            <AlertCircle className="h-5 w-5 text-alert-red" />
          </CardHeader>
          <CardContent>
            <div className="text-3xl font-bold text-alert-red">{detections.filter(d => d.disease !== 'Healthy').length}</div>
            <p className="text-sm text-text-secondary mt-1">Needs review</p>
          </CardContent>
        </Card>
        <Card className="glass-card transition-all duration-300 hover:shadow-2xl hover:-translate-y-1">
          <CardHeader className="flex flex-row items-center justify-between space-y-0 pb-2">
            <CardTitle className="text-sm font-medium text-text-muted">Active Fleet</CardTitle>
            <Crosshair className="h-5 w-5 text-accent-green" />
          </CardHeader>
          <CardContent>
            <div className="text-3xl font-bold text-foreground">{drones.length}/3 Drones</div>
            <p className="text-sm text-text-secondary mt-1">1 Rover active</p>
          </CardContent>
        </Card>
        <Card className="glass-card transition-all duration-300 hover:shadow-2xl hover:-translate-y-1 border-b-4 border-b-blue-500">
          <CardHeader className="flex flex-row items-center justify-between space-y-0 pb-2">
            <CardTitle className="text-sm font-medium text-text-muted">Water Saved</CardTitle>
            <CheckCircle2 className="h-5 w-5 text-blue-500" />
          </CardHeader>
          <CardContent>
            <div className="text-3xl font-bold text-foreground">{stats.waterSaved}L</div>
            <p className="text-sm text-text-secondary mt-1">Today vs Flood Irrigation</p>
          </CardContent>
        </Card>
      </div>

      <div className="grid grid-cols-1 lg:grid-cols-3 gap-8">
        {/* MAP & CHART */}
        <div className="lg:col-span-2 flex flex-col gap-8">
          <div className="h-[450px] rounded-xl overflow-hidden border border-border shadow-xl glass-card">
            <FieldMap />
          </div>

          <Card className="glass-card">
            <CardHeader>
              <CardTitle>Water Savings Trend (Liters)</CardTitle>
            </CardHeader>
            <CardContent>
              <div className="h-[200px] w-full">
                <ResponsiveContainer width="100%" height="100%">
                  <AreaChart data={mockChartData}>
                    <defs>
                      <linearGradient id="colorWater" x1="0" y1="0" x2="0" y2="1">
                        <stop offset="5%" stopColor="#3b82f6" stopOpacity={0.3}/>
                        <stop offset="95%" stopColor="#3b82f6" stopOpacity={0}/>
                      </linearGradient>
                    </defs>
                    <CartesianGrid strokeDasharray="3 3" vertical={false} stroke="hsl(var(--border))" />
                    <XAxis dataKey="time" stroke="hsl(var(--text-muted))" fontSize={12} tickLine={false} axisLine={false} />
                    <YAxis stroke="hsl(var(--text-muted))" fontSize={12} tickLine={false} axisLine={false} />
                    <Tooltip contentStyle={{ backgroundColor: 'hsl(var(--card))', border: '1px solid hsl(var(--border))', borderRadius: '8px' }} />
                    <Area type="monotone" dataKey="water" stroke="#3b82f6" strokeWidth={3} fillOpacity={1} fill="url(#colorWater)" />
                  </AreaChart>
                </ResponsiveContainer>
              </div>
            </CardContent>
          </Card>
        </div>

        {/* SIDEBAR */}
        <div className="flex flex-col gap-8">
          
          {/* FLEET STATUS */}
          <Card className="glass-card">
            <CardHeader className="pb-4">
              <CardTitle className="text-lg">Fleet Telemetry</CardTitle>
            </CardHeader>
            <CardContent className="space-y-5">
              {drones.map(d => (
                <div key={d.id} className="flex items-center justify-between text-sm group">
                  <div className="flex items-center gap-3">
                    <span className="font-bold w-8 text-foreground">{d.id}</span>
                    <Battery className={`w-4 h-4 ${d.battery < 70 ? 'text-alert-amber' : 'text-accent-green'}`} />
                    <div className="w-24 h-2 bg-muted rounded-full overflow-hidden">
                      <div className={`h-full ${d.battery < 70 ? 'bg-alert-amber' : 'bg-accent-green'}`} style={{ width: `${d.battery}%` }}></div>
                    </div>
                  </div>
                  <Badge variant={d.status === 'Returning' ? 'secondary' : 'default'} className="w-24 justify-center text-[10px] uppercase font-bold tracking-wider">
                    {d.status}
                  </Badge>
                </div>
              ))}
              <div className="h-px bg-border my-4"></div>
              <div className="flex items-center justify-between text-sm">
                <div className="flex items-center gap-3">
                  <span className="font-bold w-8 text-foreground">{rover.id}</span>
                  <BatteryCharging className="w-4 h-4 text-blue-500" />
                  <div className="w-24 h-2 bg-muted rounded-full overflow-hidden">
                    <div className="h-full bg-blue-500" style={{ width: `${rover.battery}%` }}></div>
                  </div>
                </div>
                <Badge variant={rover.status === 'Idle' ? 'secondary' : 'default'} className="w-24 justify-center bg-blue-600 text-white hover:bg-blue-700 text-[10px] uppercase font-bold tracking-wider shadow-md">
                  {rover.status}
                </Badge>
              </div>
            </CardContent>
          </Card>

          {/* TASKS */}
          <Card className="flex-1 flex flex-col overflow-hidden glass-card">
            <CardHeader className="pb-4 border-b border-border bg-background/30">
              <CardTitle className="text-lg">Task Console</CardTitle>
            </CardHeader>
            <CardContent className="p-0 flex-1 overflow-auto">
              <Tabs defaultValue="pending" className="w-full h-full flex flex-col">
                <div className="px-4 py-3 bg-background/50 border-b border-border">
                  <TabsList className="grid w-full grid-cols-2">
                    <TabsTrigger value="pending">Pending ({tasks.filter(t => t.status === 'Pending').length})</TabsTrigger>
                    <TabsTrigger value="active">Active ({tasks.filter(t => t.status === 'In Progress').length})</TabsTrigger>
                  </TabsList>
                </div>
                <TabsContent value="pending" className="p-5 m-0 flex-1 overflow-auto space-y-4">
                  {tasks.filter(t => t.status === 'Pending').map(t => (
                    <div key={t.id} className="p-4 rounded-xl bg-background border border-border shadow-sm hover:shadow-md transition-shadow">
                      <div className="flex justify-between items-start mb-3">
                        <h4 className="font-semibold text-sm text-foreground">{t.title}</h4>
                        <Badge variant="destructive" className="bg-alert-red/10 text-alert-red border-alert-red/20 text-[10px] font-bold">
                          {t.priority}
                        </Badge>
                      </div>
                      <p className="text-xs text-text-secondary mb-4 flex items-center gap-1 font-medium">
                        <MapIcon className="w-3 h-3" /> Target Zone {t.zone}
                      </p>
                      <Button size="sm" className="w-full bg-accent-green text-white hover:bg-emerald-600 shadow-md font-semibold" onClick={() => approveTask(t.id)}>
                        Approve & Dispatch Rover
                      </Button>
                    </div>
                  ))}
                  {tasks.filter(t => t.status === 'Pending').length === 0 && (
                    <div className="text-center text-text-muted text-sm py-12 flex flex-col items-center">
                      <CheckCircle2 className="w-8 h-8 text-border mb-3" />
                      All clear! No pending tasks.
                    </div>
                  )}
                </TabsContent>
                <TabsContent value="active" className="p-5 m-0 space-y-4">
                  {tasks.filter(t => t.status === 'In Progress').map(t => (
                    <div key={t.id} className="p-4 rounded-xl bg-background border border-border shadow-sm border-l-4 border-l-blue-500 relative overflow-hidden">
                      <div className="absolute top-0 right-0 w-16 h-16 bg-blue-500/10 rounded-bl-full pointer-events-none"></div>
                      <h4 className="font-semibold text-sm text-foreground mb-1">{t.title}</h4>
                      <p className="text-xs text-text-secondary font-medium">Executing in Zone {t.zone}</p>
                    </div>
                  ))}
                </TabsContent>
              </Tabs>
            </CardContent>
          </Card>
        </div>
      </div>
    </div>
  );
}
""")

print("UI enhancements applied successfully.")
