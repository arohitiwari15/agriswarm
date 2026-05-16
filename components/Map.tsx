'use client';

import { MapContainer, TileLayer, Marker, Popup, Circle } from 'react-leaflet';
import 'leaflet/dist/leaflet.css';
import { useSimulation } from '@/lib/simulation';
import L from 'leaflet';

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