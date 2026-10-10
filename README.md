# ⚡ OmniTrack — Multimodal 3D Telemetry & Safety Cockpit

**OmniTrack** is an offline-first PWA and 3D Blackbox safety system for modern transit, aviation, and rider safety. It leverages smartphone IMU sensors (accelerometer & gyroscope) combined with high-accuracy GPS telemetry to provide real-time 3D motion tracking, G-force vector analytics, and emergency crash detection.

---

## 🌟 Key Features

1. **3D Artificial Horizon & Attitude Indicator:**
   - Real-time Pitch & Roll ladder display powered by phone gyroscope.
   - Zero-Gyro baseline calibration for custom mounting angles.

2. **3-Axis Vector G-Force Analytics:**
   - Multi-axis telemetry breakdown ($G_x$ Lateral cornering, $G_y$ Longitudinal acceleration/braking, $G_z$ Vertical bumps/gravity).
   - Dynamic smoothness index calculation and turbulence tracking.

3. **Multimodal Transit Profiles:**
   - **Aviation:** Turbulence severity & altitude vector tracking.
   - **Transit / Rail:** Cornering force & transit efficiency monitor.
   - **Bike / Ride:** Lean angle, apex monitor, and road hazard detector.

4. **Autonomous Crash Safety & Dead-Man Switch:**
   - Automatic detection of high-impact deceleration spikes ($>3.2\text{G}$).
   - 10-second countdown alert modal with audio siren trigger.
   - Instant emergency contact SOS payload dispatch with live GPS coordinates.

5. **Road Hazard & Pothole Tagging:**
   - One-tap geolocation tagging of road anomalies.
   - Offline storage in `localStorage` & IndexedDB for background sync.

6. **Interactive Tactical Map:**
   - Leaflet map integration with dark mode map tile rendering.
   - Real-time path trail plotting and location re-centering.
   - Dual tracking modes: **Real Live GPS** & **Dynamic 3D Simulator**.

---

## 🚀 Getting Started

Simply open `hi.html` in any modern mobile or desktop web browser (HTTPS or localhost required for hardware sensor permissions).

```bash
# Python HTTPS server (for local testing with sensor access)
python server_https.py
```

---

## 📁 Repository Structure

```
Layover/
├── hi.html            # Main PWA application & 3D Safety Cockpit
├── README.md          # Project documentation
├── server_https.py    # Local HTTPS development server
└── tunnel.txt         # Dev tunnel configuration reference
```

---

## 🔒 Tech Stack & APIs

- **UI & Styling:** Vanilla HTML5, CSS3 Glassmorphism, Space Grotesk & Orbitron Google Fonts.
- **Mapping:** Leaflet.js with CartoDB Dark Matter tiles.
- **Sensors:** Generic Sensor API, `DeviceMotionEvent`, `DeviceOrientationEvent`, HTML5 Geolocation API.
- **Offline & PWA:** Service Worker caching with Web Manifest.
