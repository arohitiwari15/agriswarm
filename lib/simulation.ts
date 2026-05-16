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