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