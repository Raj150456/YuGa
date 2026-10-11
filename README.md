<div align="center">

<img src="https://readme-typing-svg.demolab.com?font=DM+Serif+Display&size=42&duration=3000&pause=800&color=F06526&center=true&vCenter=true&multiline=false&width=600&height=80&lines=✦+Yugago;Your+Ride.+Your+Data.;Your+Safety." alt="Yugago" />

### 🛰️ 3D Telemetry & Safety Cockpit — _in a browser tab_

<br/>

[![PWA Ready](https://img.shields.io/badge/PWA-Offline--First-F06526?style=for-the-badge&logo=pwa&logoColor=white)](https://yugago.vercel.app)
[![Leaflet](https://img.shields.io/badge/Maps-Leaflet.js-199900?style=for-the-badge&logo=leaflet&logoColor=white)](https://leafletjs.com)
[![Vercel](https://img.shields.io/badge/Deployed-Vercel-000000?style=for-the-badge&logo=vercel&logoColor=white)](https://yugago.vercel.app)
[![Built at Hackathon](https://img.shields.io/badge/Built%20in-12%20Hours-FFBA00?style=for-the-badge&logoColor=black)](#)
[![No Backend](https://img.shields.io/badge/Backend-None%20🎉-29B2FE?style=for-the-badge)](#)
[![No Build Step](https://img.shields.io/badge/Build%20Step-Also%20None-2DB87A?style=for-the-badge)](#)

<br/>

> **Built in 12 hours at [Layover 2026](https://tinkerspace.in) · TinkerSpace Hackathon · Kozhikode**
> *Team YuGa · October 2026*

</div>

---

```
 __   ___   _  ___  _   ___  ___
 \ \ / / | | |/ __|| | / _ \| __|
  \ V /| |_| | (_ || || (_) | _|
   |_|  \___/ \___||_| \___/|___|

  Your ride. Your data. Your safety.
  — all in a single browser tab.
```

---

## 🤔 What even is this?

Yugago turns your **boring smartphone** into a legit **flight-grade motion blackbox** — G-force analytics, crash detection, live GPS trail, and an artificial horizon — the works. No app store. No backend. No special hardware.

Just open a browser, tap **Get Started**, and watch your phone go from _"thing I doom-scroll on"_ to _"aircraft-grade telemetry system"_.

> One HTML file. ~1800 lines. 12 hours. Hackathon yolo. 🚀

---

## ⚡ Features

<details>
<summary><b>🛩️ 3D Artificial Horizon</b></summary>
<br/>

Real-time **pitch & roll** attitude display, just like what pilots see — except it's your phone, and you might be in a rickshaw.

- Live gyroscope data rendered as a smooth horizon animation
- **Zero-Gyro calibration** — mount the phone anywhere, reset the reference with one tap
- Handles screen orientation math (portrait, landscape, flipped) automatically

</details>

<details>
<summary><b>📡 3-Axis G-Force Analytics</b></summary>
<br/>

Your phone's accelerometer reports force in three axes. We show all three at once, with live bars and a smoothness score:

| Axis | What it feels like |
|------|-------------------|
| **Gx** Lateral | That sideways push when cornering hard 🏎️ |
| **Gy** Longitudinal | The chest-punch when you brake or floor it 💨 |
| **Gz** Vertical | Potholes, speed bumps, turbulence 💀 |

The **smoothness score** (0–100%) tells you how bumpy your ride is — great for road quality data collection.

</details>

<details>
<summary><b>🚨 Crash Detection & SOS Dead-Man Switch</b></summary>
<br/>

When G-total spikes above **3.2G**:

1. 🔊 Audio siren fires immediately
2. ⏱️ A **10-second countdown** modal appears
3. 📍 If uncancelled → SOS broadcast with live GPS coordinates
4. 📦 Black box log auto-saved with impact telemetry

Designed so that if you *actually* crash, help gets called **without you needing to do anything**.

</details>

<details>
<summary><b>🗺️ Tactical Live Map</b></summary>
<br/>

- Live GPS path drawn in real time as you move
- **Orange trail** = your exact route history
- **🚩 Hazard pins** = potholes / road anomalies tagged with one tap
- All hazard data saved offline, reloads next session
- Toggle: **Street View ↔ Satellite** with the 🗺️ FAB button

</details>

<details>
<summary><b>🌀 3D Physics Simulator</b></summary>
<br/>

No vehicle? No problem. Switch to **3D Simulator mode**:

- Simulated GPS vehicle with real physics — speed, heading, pitch, roll
- Crash alerts trigger at realistic G-spikes
- Hazard tagging & logs still work
- Perfect for **demoing at the hackathon booth** without running outside 😅

</details>

<details>
<summary><b>🚗 Transit Mode Profiles</b></summary>
<br/>

| Mode | Vibe | Tuning |
|------|------|--------|
| ✈️ **Aviation** | You're on a flight | Turbulence severity, altitude vectors, high-G alerts |
| 🚆 **Transit / Rail** | Train / bus / metro | Cornering force, efficiency index |
| 🏍️ **Bike / Ride** | Two-wheeler / cab | Lean angle, apex monitor, hazard mode |

</details>

---

## 🎮 Quick Start

```bash
# ✅ Already live — just open this on your phone:
# https://yugago.vercel.app

# 💻 Or run locally:
npx serve .
# Open http://localhost:3000 on your phone (same WiFi)
```

> [!IMPORTANT]
> **HTTPS is required on mobile** for sensors (`DeviceMotion`, `Geolocation`) to work.
> Vercel gives you this for free. For local testing, use `ngrok` or your phone on same WiFi.

---

## 📁 Project Structure

```
LAYOVER/
│
├── 📄 index.html     ← The ENTIRE app. One file. ~1800 lines.
│                        HTML + CSS + JS + Service Worker. All of it.
│
├── ⚙️  vercel.json    ← 8 lines. Tells Vercel "serve index.html".
│
└── 📖 README.md      ← You are here 👋
```

> Yes, it's one HTML file. Yes, it installs as a PWA. Yes, we're proud of it.

---

## 🔧 Tech Stack

| Layer | Tech | Why |
|-------|------|-----|
| 🖼️ **UI** | Vanilla HTML5 + CSS3 | Zero framework overhead, instant load |
| 🎨 **Styling** | Glassmorphism + CSS Grid + animations | Looks premium, zero dependencies |
| 🗺️ **Maps** | Leaflet.js + Esri ArcGIS tiles | Free, no API key, reliable |
| 📐 **Fonts** | DM Serif Display + DM Sans | Classy + readable |
| 📱 **Sensors** | `DeviceMotionEvent` + `DeviceOrientationEvent` + Geolocation | Native browser APIs, no SDK needed |
| 📦 **Offline** | Service Worker + Web App Manifest | Installable PWA, works without internet |
| 🚀 **Deploy** | Vercel | Push → live in 30 seconds |

---

## 📊 Real Stats

```
Lines of code   ~1,800
Files           1  (yes, one HTML file)
npm packages    0  (just CDN links)
Build step      none
Backend         none
Time to build   12 hours
Sleep           0 hours
Coffee          ∞
```

---

## 👥 Team YuGa

Built in one night at **Layover 2026** — TinkerSpace Hackathon, Kozhikode.

We had 12 hours, one laptop, and a dangerous idea. This is what came out.

---

<div align="center">

### 💥 One file. One night. Real sensors. Real impact.

[![Try it Live](https://img.shields.io/badge/🚀%20Try%20it%20Live-yugago.vercel.app-F06526?style=for-the-badge)](https://yugago.vercel.app)

<br/>

*Made with ☕ + zero sleep + a lot of G-force*
*— Layover 2026, TinkerSpace Kozhikode* ✦

</div>




---

## ✦ Features

### 🛩️ 3D Artificial Horizon
Real-time pitch & roll attitude display, just like an aircraft's attitude indicator. Zero-Gyro baseline calibration lets you mount the phone at any angle and reset the reference on the fly.

### 📡 3-Axis G-Force Analytics

Breaks down forces across all three axes simultaneously:

| Axis | Meaning |
|------|---------|
| **Gx** (Lateral) | Cornering force — how hard you're turning |
| **Gy** (Longitudinal) | Acceleration & braking force |
| **Gz** (Vertical) | Bumps, potholes, turbulence |

Live **smoothness score** calculated from vector magnitude deviation.

### 🚨 Autonomous Crash Detection
- Monitors combined G-vector for spikes **> 3.2G**
- Triggers a **10-second countdown** with audio siren
- Automatically dispatches SOS with live GPS coordinates if not cancelled
- Dead-man switch design — cancel it yourself, or help is on the way

### 🗺️ Tactical Live Map
- Live GPS trail plotted in real time on an interactive map
- One-tap **hazard tagging** drops a geofenced pin at your current location
- Hazard data is saved offline in `localStorage` and persists across sessions
- Toggle between **Street View** and **Satellite** map styles

### 🌀 3D Physics Simulator
Can't test on the road? Flip to **3D Simulator mode**:
- Fully simulated GPS path with realistic physics — speed, heading, pitch, roll
- Crash alerts and hazard tagging work in sim mode too
- Great for demo + testing without needing to be in a vehicle

### 🚗 Transit Mode Profiles

Switch context based on how you're travelling:

| Mode | Tuning |
|------|--------|
| ✈️ **Aviation** | Turbulence severity, altitude vector, high-G thresholds |
| 🚆 **Transit / Rail** | Cornering force, transit efficiency index |
| 🏍️ **Bike / Ride** | Lean angle, apex detection, road hazard tagging |

---

## 🚀 Run It

No setup needed — just open in a browser with HTTPS (required for sensor access):

```bash
# Option 1: Already live on Vercel
# https://yugago.vercel.app

# Option 2: Local with any static server
npx serve .

# Option 3: Open index.html directly
# (sensors may be limited without HTTPS on mobile)
```

> **Note:** Sensor APIs (`DeviceMotion`, `DeviceOrientation`, `Geolocation`) require HTTPS on iOS/Chrome. Vercel handles this automatically.

---

## 📁 Project Structure

```
LAYOVER/
├── index.html        ← Entire app — single-file PWA (HTML + CSS + JS)
├── vercel.json       ← Vercel routing config
└── README.md         ← You're here
```

Everything lives in `index.html` — CSS, JS, HTML, Service Worker — all self-contained and deployable instantly.

---

## 🔧 Tech Stack

| Layer | Technology |
|-------|-----------|
| **UI** | Vanilla HTML5 + CSS3 (glassmorphism, CSS Grid, animations) |
| **Fonts** | DM Serif Display + DM Sans (Google Fonts) |
| **Map** | Leaflet.js + Esri ArcGIS tiles (no API key needed) |
| **Sensors** | `DeviceMotionEvent`, `DeviceOrientationEvent`, HTML5 Geolocation API |
| **Offline** | Service Worker + Web App Manifest (installable PWA) |
| **Deployment** | Vercel Static Hosting |

---

## 👥 Team

**Team YuGa** — built over 12 hours at **Layover 2026**, TinkerSpace Hackathon, Kozhikode.

---

<div align="center">

*Made with ☕, zero sleep, and a lot of G-force — Layover 2026*

</div>

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
