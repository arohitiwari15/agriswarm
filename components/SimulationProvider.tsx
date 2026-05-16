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