import os
import textwrap

def create_file(path, content):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w') as f:
        f.write(textwrap.dedent(content).strip())

# 1. UI Components (Simplified shadcn-like)
create_file("components/ui/button.tsx", """
import * as React from "react"
import { Slot } from "@radix-ui/react-slot"
import { cva, type VariantProps } from "class-variance-authority"
import { cn } from "@/lib/utils"

const buttonVariants = cva(
  "inline-flex items-center justify-center whitespace-nowrap rounded-md text-sm font-medium ring-offset-background transition-colors focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2 disabled:pointer-events-none disabled:opacity-50",
  {
    variants: {
      variant: {
        default: "bg-primary text-primary-foreground hover:bg-primary/90",
        destructive: "bg-destructive text-destructive-foreground hover:bg-destructive/90",
        outline: "border border-input bg-background hover:bg-accent hover:text-accent-foreground",
        secondary: "bg-secondary text-secondary-foreground hover:bg-secondary/80",
        ghost: "hover:bg-accent hover:text-accent-foreground",
        link: "text-primary underline-offset-4 hover:underline",
      },
      size: {
        default: "h-10 px-4 py-2",
        sm: "h-9 rounded-md px-3",
        lg: "h-11 rounded-md px-8",
        icon: "h-10 w-10",
      },
    },
    defaultVariants: {
      variant: "default",
      size: "default",
    },
  }
)

export interface ButtonProps
  extends React.ButtonHTMLAttributes<HTMLButtonElement>,
    VariantProps<typeof buttonVariants> {
  asChild?: boolean
}

const Button = React.forwardRef<HTMLButtonElement, ButtonProps>(
  ({ className, variant, size, asChild = false, ...props }, ref) => {
    const Comp = asChild ? Slot : "button"
    return (
      <Comp
        className={cn(buttonVariants({ variant, size, className }))}
        ref={ref}
        {...props}
      />
    )
  }
)
Button.displayName = "Button"

export { Button, buttonVariants }
""")

create_file("components/ui/card.tsx", """
import * as React from "react"
import { cn } from "@/lib/utils"

const Card = React.forwardRef<HTMLDivElement, React.HTMLAttributes<HTMLDivElement>>(({ className, ...props }, ref) => (
  <div ref={ref} className={cn("rounded-lg border bg-card text-card-foreground shadow-sm", className)} {...props} />
))
Card.displayName = "Card"

const CardHeader = React.forwardRef<HTMLDivElement, React.HTMLAttributes<HTMLDivElement>>(({ className, ...props }, ref) => (
  <div ref={ref} className={cn("flex flex-col space-y-1.5 p-6", className)} {...props} />
))
CardHeader.displayName = "CardHeader"

const CardTitle = React.forwardRef<HTMLParagraphElement, React.HTMLAttributes<HTMLHeadingElement>>(({ className, ...props }, ref) => (
  <h3 ref={ref} className={cn("text-2xl font-semibold leading-none tracking-tight", className)} {...props} />
))
CardTitle.displayName = "CardTitle"

const CardDescription = React.forwardRef<HTMLParagraphElement, React.HTMLAttributes<HTMLParagraphElement>>(({ className, ...props }, ref) => (
  <p ref={ref} className={cn("text-sm text-muted-foreground", className)} {...props} />
))
CardDescription.displayName = "CardDescription"

const CardContent = React.forwardRef<HTMLDivElement, React.HTMLAttributes<HTMLDivElement>>(({ className, ...props }, ref) => (
  <div ref={ref} className={cn("p-6 pt-0", className)} {...props} />
))
CardContent.displayName = "CardContent"

const CardFooter = React.forwardRef<HTMLDivElement, React.HTMLAttributes<HTMLDivElement>>(({ className, ...props }, ref) => (
  <div ref={ref} className={cn("flex items-center p-6 pt-0", className)} {...props} />
))
CardFooter.displayName = "CardFooter"

export { Card, CardHeader, CardFooter, CardTitle, CardDescription, CardContent }
""")

create_file("components/ui/badge.tsx", """
import * as React from "react"
import { cva, type VariantProps } from "class-variance-authority"
import { cn } from "@/lib/utils"

const badgeVariants = cva(
  "inline-flex items-center rounded-full border px-2.5 py-0.5 text-xs font-semibold transition-colors focus:outline-none focus:ring-2 focus:ring-ring focus:ring-offset-2",
  {
    variants: {
      variant: {
        default: "border-transparent bg-primary text-primary-foreground hover:bg-primary/80",
        secondary: "border-transparent bg-secondary text-secondary-foreground hover:bg-secondary/80",
        destructive: "border-transparent bg-destructive text-destructive-foreground hover:bg-destructive/80",
        outline: "text-foreground",
      },
    },
    defaultVariants: {
      variant: "default",
    },
  }
)

export interface BadgeProps extends React.HTMLAttributes<HTMLDivElement>, VariantProps<typeof badgeVariants> {}

function Badge({ className, variant, ...props }: BadgeProps) {
  return (<div className={cn(badgeVariants({ variant }), className)} {...props} />)
}

export { Badge, badgeVariants }
""")

create_file("components/ui/tabs.tsx", """
import * as React from "react"
import * as TabsPrimitive from "@radix-ui/react-tabs"
import { cn } from "@/lib/utils"

const Tabs = TabsPrimitive.Root

const TabsList = React.forwardRef<
  React.ElementRef<typeof TabsPrimitive.List>,
  React.ComponentPropsWithoutRef<typeof TabsPrimitive.List>
>(({ className, ...props }, ref) => (
  <TabsPrimitive.List
    ref={ref}
    className={cn(
      "inline-flex h-10 items-center justify-center rounded-md bg-muted p-1 text-muted-foreground",
      className
    )}
    {...props}
  />
))
TabsList.displayName = TabsPrimitive.List.displayName

const TabsTrigger = React.forwardRef<
  React.ElementRef<typeof TabsPrimitive.Trigger>,
  React.ComponentPropsWithoutRef<typeof TabsPrimitive.Trigger>
>(({ className, ...props }, ref) => (
  <TabsPrimitive.Trigger
    ref={ref}
    className={cn(
      "inline-flex items-center justify-center whitespace-nowrap rounded-sm px-3 py-1.5 text-sm font-medium ring-offset-background transition-all focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2 disabled:pointer-events-none disabled:opacity-50 data-[state=active]:bg-background data-[state=active]:text-foreground data-[state=active]:shadow-sm",
      className
    )}
    {...props}
  />
))
TabsTrigger.displayName = TabsPrimitive.Trigger.displayName

const TabsContent = React.forwardRef<
  React.ElementRef<typeof TabsPrimitive.Content>,
  React.ComponentPropsWithoutRef<typeof TabsPrimitive.Content>
>(({ className, ...props }, ref) => (
  <TabsPrimitive.Content
    ref={ref}
    className={cn(
      "mt-2 ring-offset-background focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2",
      className
    )}
    {...props}
  />
))
TabsContent.displayName = TabsPrimitive.Content.displayName

export { Tabs, TabsList, TabsTrigger, TabsContent }
""")

create_file("components/ui/dialog.tsx", """
import * as React from "react"
import * as DialogPrimitive from "@radix-ui/react-dialog"
import { X } from "lucide-react"

import { cn } from "@/lib/utils"

const Dialog = DialogPrimitive.Root
const DialogTrigger = DialogPrimitive.Trigger
const DialogPortal = DialogPrimitive.Portal
const DialogClose = DialogPrimitive.Close

const DialogOverlay = React.forwardRef<
  React.ElementRef<typeof DialogPrimitive.Overlay>,
  React.ComponentPropsWithoutRef<typeof DialogPrimitive.Overlay>
>(({ className, ...props }, ref) => (
  <DialogPrimitive.Overlay
    ref={ref}
    className={cn(
      "fixed inset-0 z-50 bg-black/80  data-[state=open]:animate-in data-[state=closed]:animate-out data-[state=closed]:fade-out-0 data-[state=open]:fade-in-0",
      className
    )}
    {...props}
  />
))
DialogOverlay.displayName = DialogPrimitive.Overlay.displayName

const DialogContent = React.forwardRef<
  React.ElementRef<typeof DialogPrimitive.Content>,
  React.ComponentPropsWithoutRef<typeof DialogPrimitive.Content>
>(({ className, children, ...props }, ref) => (
  <DialogPortal>
    <DialogOverlay />
    <DialogPrimitive.Content
      ref={ref}
      className={cn(
        "fixed left-[50%] top-[50%] z-50 grid w-full max-w-lg translate-x-[-50%] translate-y-[-50%] gap-4 border bg-background p-6 shadow-lg duration-200 data-[state=open]:animate-in data-[state=closed]:animate-out data-[state=closed]:fade-out-0 data-[state=open]:fade-in-0 data-[state=closed]:zoom-out-95 data-[state=open]:zoom-in-95 data-[state=closed]:slide-out-to-left-1/2 data-[state=closed]:slide-out-to-top-[48%] data-[state=open]:slide-in-from-left-1/2 data-[state=open]:slide-in-from-top-[48%] sm:rounded-lg",
        className
      )}
      {...props}
    >
      {children}
      <DialogPrimitive.Close className="absolute right-4 top-4 rounded-sm opacity-70 ring-offset-background transition-opacity hover:opacity-100 focus:outline-none focus:ring-2 focus:ring-ring focus:ring-offset-2 disabled:pointer-events-none data-[state=open]:bg-accent data-[state=open]:text-muted-foreground">
        <X className="h-4 w-4" />
        <span className="sr-only">Close</span>
      </DialogPrimitive.Close>
    </DialogPrimitive.Content>
  </DialogPortal>
))
DialogContent.displayName = DialogPrimitive.Content.displayName

const DialogHeader = ({
  className,
  ...props
}: React.HTMLAttributes<HTMLDivElement>) => (
  <div
    className={cn(
      "flex flex-col space-y-1.5 text-center sm:text-left",
      className
    )}
    {...props}
  />
)
DialogHeader.displayName = "DialogHeader"

const DialogFooter = ({
  className,
  ...props
}: React.HTMLAttributes<HTMLDivElement>) => (
  <div
    className={cn(
      "flex flex-col-reverse sm:flex-row sm:justify-end sm:space-x-2",
      className
    )}
    {...props}
  />
)
DialogFooter.displayName = "DialogFooter"

const DialogTitle = React.forwardRef<
  React.ElementRef<typeof DialogPrimitive.Title>,
  React.ComponentPropsWithoutRef<typeof DialogPrimitive.Title>
>(({ className, ...props }, ref) => (
  <DialogPrimitive.Title
    ref={ref}
    className={cn(
      "text-lg font-semibold leading-none tracking-tight",
      className
    )}
    {...props}
  />
))
DialogTitle.displayName = DialogPrimitive.Title.displayName

const DialogDescription = React.forwardRef<
  React.ElementRef<typeof DialogPrimitive.Description>,
  React.ComponentPropsWithoutRef<typeof DialogPrimitive.Description>
>(({ className, ...props }, ref) => (
  <DialogPrimitive.Description
    ref={ref}
    className={cn("text-sm text-muted-foreground", className)}
    {...props}
  />
))
DialogDescription.displayName = DialogPrimitive.Description.displayName

export {
  Dialog,
  DialogPortal,
  DialogOverlay,
  DialogClose,
  DialogTrigger,
  DialogContent,
  DialogHeader,
  DialogFooter,
  DialogTitle,
  DialogDescription,
}
""")


# 2. Simulation State (Zustand)
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
const ZONES = ['4A', '2B', '6B', '1C', '3A'];
const DISEASES = [
  "Early Blight", "Late Blight", "Leaf Mold", "Spider Mites",
  "Bacterial Spot", "Powdery Mildew", "Aphid Cluster",
  "Leaf Miner", "Septoria Leaf Spot", "Healthy"
];

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
    { id: 'det-1', disease: 'Early Blight', confidence: 0.94, zone: '4A', timestamp: new Date(Date.now() - 60000), position: generateRandomCoord(INITIAL_CENTER, 0.008), severity: 'HIGH' },
    { id: 'det-2', disease: 'Healthy', confidence: 0.98, zone: '4A', timestamp: new Date(Date.now() - 120000), position: generateRandomCoord(INITIAL_CENTER, 0.008), severity: 'LOW' }
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

create_file("components/SimulationProvider.tsx", """
'use client';
import { useEffect } from 'react';
import { useSimulation } from '@/lib/simulation';

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
      const diseases = ["Early Blight", "Late Blight", "Powdery Mildew", "Aphid Cluster"];
      const randomDisease = diseases[Math.floor(Math.random() * diseases.length)];
      addDetection({
        id: `det-${Date.now()}`,
        disease: randomDisease,
        confidence: 0.85 + Math.random() * 0.14,
        zone: ['4A', '2B', '6B', '1C', '3A'][Math.floor(Math.random() * 5)],
        timestamp: new Date(),
        position: [17.3850 + (Math.random() - 0.5) * 0.01, 78.4867 + (Math.random() - 0.5) * 0.01],
        severity: Math.random() > 0.5 ? 'HIGH' : 'MEDIUM'
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

# 3. Map Component (React-Leaflet)
create_file("components/Map.tsx", """
'use client';

import { MapContainer, TileLayer, Marker, Popup, Circle } from 'react-leaflet';
import 'leaflet/dist/leaflet.css';
import { useSimulation } from '@/lib/simulation';
import L from 'leaflet';
import { useEffect } from 'react';

// Fix for default leaflet icons in Next.js
const droneIcon = new L.Icon({
  iconUrl: 'https://cdn-icons-png.flaticon.com/512/3256/3256083.png',
  iconSize: [32, 32],
  iconAnchor: [16, 16],
});

const roverIcon = new L.Icon({
  iconUrl: 'https://cdn-icons-png.flaticon.com/512/2822/2822081.png',
  iconSize: [32, 32],
  iconAnchor: [16, 16],
});

const detectionIcon = new L.Icon({
  iconUrl: 'https://cdn-icons-png.flaticon.com/512/1201/1201138.png',
  iconSize: [24, 24],
  iconAnchor: [12, 12],
});

export default function FieldMap() {
  const { drones, rover, detections } = useSimulation();
  
  return (
    <div className="h-full w-full rounded-lg overflow-hidden border border-border shadow-sm">
      <MapContainer 
        center={[17.3850, 78.4867]} 
        zoom={15} 
        style={{ height: '100%', width: '100%', background: '#0D1B2A' }}
        zoomControl={false}
      >
        <TileLayer
          url="https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}"
          attribution="&copy; Esri"
          className="map-tiles grayscale opacity-60"
        />
        
        {/* Draw a subtle scan grid area */}
        <Circle center={[17.3850, 78.4867]} radius={600} pathOptions={{ color: '#52B788', weight: 1, fillOpacity: 0.1 }} />

        {/* Drones */}
        {drones.map(d => (
          <Marker key={d.id} position={d.position} icon={droneIcon}>
            <Popup>
              <div className="text-black p-1">
                <strong>Drone {d.id}</strong><br/>
                Battery: {Math.round(d.battery)}%<br/>
                Status: {d.status}
              </div>
            </Popup>
          </Marker>
        ))}

        {/* Rover */}
        <Marker position={rover.position} icon={roverIcon}>
          <Popup>
            <div className="text-black p-1">
              <strong>Rover {rover.id}</strong><br/>
              Battery: {Math.round(rover.battery)}%<br/>
              Status: {rover.status}
            </div>
          </Popup>
        </Marker>

        {/* Detections */}
        {detections.map(det => (
          <Marker key={det.id} position={det.position} icon={detectionIcon}>
            <Popup>
              <div className="text-black p-1">
                <strong>{det.disease}</strong><br/>
                Confidence: {(det.confidence * 100).toFixed(1)}%<br/>
                Zone: {det.zone}
              </div>
            </Popup>
          </Marker>
        ))}
      </MapContainer>
      <style jsx global>{`
        .leaflet-container { background: #0D1B2A !important; }
        .leaflet-popup-content-wrapper { background: rgba(255, 255, 255, 0.9); border-radius: 8px; }
      `}</style>
    </div>
  );
}
""")

# 4. Layout & Global Navigation
create_file("app/layout.tsx", """
import type { Metadata } from "next";
import { Inter } from "next/font/google";
import "./globals.css";
import Link from "next/link";
import { Badge } from "@/components/ui/badge";
import { SimulationProvider } from "@/components/SimulationProvider";

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
    <html lang="en" className="dark">
      <body className={inter.className}>
        <SimulationProvider>
          <div className="flex flex-col min-h-screen bg-background text-foreground">
            <header className="sticky top-0 z-50 w-full border-b border-border/40 bg-background/95 backdrop-blur supports-[backdrop-filter]:bg-background/60">
              <div className="container flex h-16 items-center">
                <div className="mr-8 flex items-center space-x-2">
                  <Link href="/" className="flex items-center space-x-2">
                    <span className="font-bold text-xl tracking-tight text-white">Agri-Swarm</span>
                    <Badge variant="outline" className="border-accent-green text-accent-green ml-2 hidden sm:inline-flex">
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
                </div>
              </div>
            </header>
            <main className="flex-1">{children}</main>
            <footer className="border-t border-border py-6 md:py-0">
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
      </body>
    </html>
  );
}
""")

# 5. Homepage
create_file("app/page.tsx", """
'use client';
import { Button } from "@/components/ui/button";
import { Card, CardContent, CardHeader, CardTitle, CardDescription } from "@/components/ui/card";
import { Badge } from "@/components/ui/badge";
import { Tabs, TabsContent, TabsList, TabsTrigger } from "@/components/ui/tabs";
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
""")

# 6. Dashboard
create_file("app/dashboard/page.tsx", """
'use client';

import { useSimulation } from "@/lib/simulation";
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { Badge } from "@/components/ui/badge";
import { Button } from "@/components/ui/button";
import { Tabs, TabsList, TabsTrigger, TabsContent } from "@/components/ui/tabs";
import { AlertCircle, Battery, BatteryCharging, Crosshair, Map as MapIcon, CheckCircle2, AlertTriangle, ShieldAlert } from "lucide-react";
import dynamic from 'next/dynamic';
import { formatDistanceToNow } from 'date-fns';

const FieldMap = dynamic(() => import('@/components/Map'), { ssr: false });

export default function DashboardPage() {
  const { drones, rover, detections, tasks, stats, approveTask } = useSimulation();

  return (
    <div className="container py-8 h-[calc(100vh-4rem)] flex flex-col gap-6">
      <div className="flex items-center justify-between">
        <div>
          <h1 className="text-2xl font-bold tracking-tight">Reddy Farms — Hyderabad, Telangana</h1>
          <p className="text-text-secondary">Farmer Command Center</p>
        </div>
        <Badge variant="outline" className="border-accent-green text-accent-green px-4 py-1 text-sm bg-accent-green/10">
          <span className="h-2 w-2 rounded-full bg-accent-green mr-2 animate-pulse-dot"></span> System Active
        </Badge>
      </div>

      {/* STATS ROW */}
      <div className="grid grid-cols-2 lg:grid-cols-4 gap-4">
        <Card>
          <CardHeader className="flex flex-row items-center justify-between space-y-0 pb-2">
            <CardTitle className="text-sm font-medium text-text-muted">Acres Scanned</CardTitle>
            <MapIcon className="h-4 w-4 text-text-secondary" />
          </CardHeader>
          <CardContent>
            <div className="text-2xl font-bold">{stats.acresScanned}</div>
            <p className="text-xs text-accent-green">↑ +2.1 this hour</p>
          </CardContent>
        </Card>
        <Card>
          <CardHeader className="flex flex-row items-center justify-between space-y-0 pb-2">
            <CardTitle className="text-sm font-medium text-text-muted">Active Detections</CardTitle>
            <AlertCircle className="h-4 w-4 text-alert-red" />
          </CardHeader>
          <CardContent>
            <div className="text-2xl font-bold text-alert-red">{detections.filter(d => d.disease !== 'Healthy').length}</div>
            <p className="text-xs text-text-secondary">Needs review</p>
          </CardContent>
        </Card>
        <Card>
          <CardHeader className="flex flex-row items-center justify-between space-y-0 pb-2">
            <CardTitle className="text-sm font-medium text-text-muted">Active Fleet</CardTitle>
            <Crosshair className="h-4 w-4 text-accent-green" />
          </CardHeader>
          <CardContent>
            <div className="text-2xl font-bold">{drones.length}/3 Drones</div>
            <p className="text-xs text-text-secondary">1 Rover active</p>
          </CardContent>
        </Card>
        <Card>
          <CardHeader className="flex flex-row items-center justify-between space-y-0 pb-2">
            <CardTitle className="text-sm font-medium text-text-muted">Water Saved</CardTitle>
            <CheckCircle2 className="h-4 w-4 text-blue-400" />
          </CardHeader>
          <CardContent>
            <div className="text-2xl font-bold">{stats.waterSaved}L</div>
            <p className="text-xs text-text-secondary">Today vs Flood</p>
          </CardContent>
        </Card>
      </div>

      <div className="grid grid-cols-1 lg:grid-cols-3 gap-6 flex-1 min-h-[400px]">
        {/* MAP */}
        <div className="lg:col-span-2 h-full flex flex-col">
          <div className="flex-1 rounded-xl overflow-hidden border border-border shadow-md">
            <FieldMap />
          </div>
        </div>

        {/* SIDEBAR */}
        <div className="flex flex-col gap-6 overflow-hidden">
          
          {/* FLEET STATUS */}
          <Card className="flex-shrink-0">
            <CardHeader className="py-4">
              <CardTitle className="text-base font-semibold">Fleet Status</CardTitle>
            </CardHeader>
            <CardContent className="space-y-4">
              {drones.map(d => (
                <div key={d.id} className="flex items-center justify-between text-sm">
                  <div className="flex items-center gap-2">
                    <span className="font-medium w-8 text-text-secondary">{d.id}</span>
                    <Battery className="w-4 h-4 text-accent-green" />
                    <span className="w-8">{Math.round(d.battery)}%</span>
                  </div>
                  <Badge variant={d.status === 'Returning' ? 'secondary' : 'default'} className="w-24 justify-center text-xs">
                    {d.status}
                  </Badge>
                </div>
              ))}
              <div className="h-px bg-border my-2"></div>
              <div className="flex items-center justify-between text-sm">
                <div className="flex items-center gap-2">
                  <span className="font-medium w-8 text-text-secondary">{rover.id}</span>
                  <BatteryCharging className="w-4 h-4 text-white" />
                  <span className="w-8">{Math.round(rover.battery)}%</span>
                </div>
                <Badge variant={rover.status === 'Idle' ? 'secondary' : 'default'} className="w-24 justify-center bg-blue-600 text-white text-xs">
                  {rover.status}
                </Badge>
              </div>
            </CardContent>
          </Card>

          {/* TASKS */}
          <Card className="flex-1 flex flex-col overflow-hidden">
            <CardHeader className="py-4 border-b border-border bg-background/50">
              <CardTitle className="text-base font-semibold">Task Console</CardTitle>
            </CardHeader>
            <CardContent className="p-0 flex-1 overflow-auto">
              <Tabs defaultValue="pending" className="w-full h-full flex flex-col">
                <div className="px-4 py-2 bg-background border-b border-border">
                  <TabsList className="grid w-full grid-cols-2">
                    <TabsTrigger value="pending">Pending ({tasks.filter(t => t.status === 'Pending').length})</TabsTrigger>
                    <TabsTrigger value="active">Active ({tasks.filter(t => t.status === 'In Progress').length})</TabsTrigger>
                  </TabsList>
                </div>
                <TabsContent value="pending" className="p-4 m-0 flex-1 overflow-auto space-y-4">
                  {tasks.filter(t => t.status === 'Pending').map(t => (
                    <div key={t.id} className="p-4 rounded-lg bg-card border border-border shadow-sm">
                      <div className="flex justify-between items-start mb-2">
                        <h4 className="font-medium text-sm text-white">{t.title}</h4>
                        <Badge variant="destructive" className="bg-alert-red/20 text-alert-red border-alert-red/50 text-[10px]">
                          {t.priority}
                        </Badge>
                      </div>
                      <p className="text-xs text-text-secondary mb-4 flex items-center gap-1">
                        <MapIcon className="w-3 h-3" /> Zone {t.zone}
                      </p>
                      <div className="flex gap-2">
                        <Button size="sm" className="w-full bg-accent-green text-bg-primary hover:bg-emerald-400 h-8 text-xs" onClick={() => approveTask(t.id)}>
                          Dispatch Rover
                        </Button>
                      </div>
                    </div>
                  ))}
                  {tasks.filter(t => t.status === 'Pending').length === 0 && (
                    <div className="text-center text-text-muted text-sm py-8">No pending tasks</div>
                  )}
                </TabsContent>
                <TabsContent value="active" className="p-4 m-0">
                  {tasks.filter(t => t.status === 'In Progress').map(t => (
                    <div key={t.id} className="p-4 rounded-lg bg-card border border-border shadow-sm border-l-4 border-l-blue-500">
                      <h4 className="font-medium text-sm text-white mb-1">{t.title}</h4>
                      <p className="text-xs text-text-secondary">Executing in Zone {t.zone}</p>
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

# 7. Detection Feed
create_file("app/detection/page.tsx", """
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
""")

# 8. Technology Page
create_file("app/technology/page.tsx", """
export default function Technology() {
  return (
    <div className="container py-12 max-w-4xl">
      <h1 className="text-4xl font-bold mb-8">System Architecture</h1>
      
      <div className="space-y-12 text-text-secondary leading-relaxed">
        <section className="bg-card p-8 rounded-xl border border-border">
          <h2 className="text-2xl font-semibold text-white mb-4">1. YOLOv8 Edge Detection</h2>
          <p className="mb-4">
            The aerial layer is powered by the YOLOv8n object detection model, heavily fine-tuned on the <strong>PlantVillage dataset</strong>. 
            The model achieves a 94.2% mAP on testing splits across 10 classes including Early Blight, Late Blight, and Spider Mites.
          </p>
          <p>
            Inference runs locally on the drone payload using embedded edge hardware (Nvidia Jetson / Coral TPU), ensuring zero latency and functioning without internet connectivity in remote fields.
          </p>
        </section>

        <section className="bg-card p-8 rounded-xl border border-border border-l-4 border-l-accent-green">
          <h2 className="text-2xl font-semibold text-white mb-4">2. Swarm Coordination</h2>
          <p>
            Multiple drones use a decentralized Voronoi-based path planning algorithm to partition the field dynamically. 
            If a drone runs low on battery, the remaining swarm instantly recalculates boundaries to maintain 100% coverage without human intervention.
          </p>
        </section>

        <section className="bg-card p-8 rounded-xl border border-border">
          <h2 className="text-2xl font-semibold text-white mb-4">3. Laser Pest Control & Precision Irrigation</h2>
          <ul className="list-disc pl-5 space-y-4">
            <li><strong>Laser Targeting:</strong> The ground rover is equipped with a galvanometer-steered class 4 laser system. Using secondary camera tracking, it vaporizes small pests (aphids, mites) mid-air or on leaves, completely eliminating chemical pesticide usage.</li>
            <li><strong>Precision Injection:</strong> Instead of flood irrigation, the rover uses a high-pressure precision nozzle to inject a micro-dose of water and nutrients directly into the soil at the base of the stem, drastically reducing evaporation and weed growth.</li>
          </ul>
        </section>
      </div>
    </div>
  );
}
""")

print("All files generated successfully.")
