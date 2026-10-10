# Yugago — 3D Telemetry & Safety Cockpit

**Yugago** is an offline-first PWA and 3D Blackbox safety system for modern transit, aviation, and rider safety. It leverages smartphone IMU sensors (accelerometer & gyroscope) combined with high-accuracy GPS telemetry to provide real-time 3D motion tracking, G-force vector analytics, and emergency crash detection.

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

## 🚀 Live Deployment & Local Setup

Access the live web app deployed on Vercel (HTTPS is automatically enabled for device sensor access).

```bash
# Open index.html directly or serve locally with any HTTP/HTTPS server
npx serve .
```

---

## 📁 Repository Structure

```
Layover/
├── index.html         # Main PWA application & 3D Safety Cockpit (Vercel entry point)
├── hi.html            # Alternative standalone entry point
├── vercel.json        # Vercel deployment & routing configuration
└── README.md          # Project documentation
```

---

## 🔒 Tech Stack & APIs

- **UI & Styling:** Vanilla HTML5, CSS3 Glassmorphism, Space Grotesk & Orbitron Google Fonts.
- **Mapping:** Leaflet.js with CartoDB Dark Matter tiles.
- **Sensors:** Generic Sensor API, `DeviceMotionEvent`, `DeviceOrientationEvent`, HTML5 Geolocation API.
- **Offline & PWA:** Service Worker caching with Web Manifest.
- **Deployment:** Vercel Static Hosting.
