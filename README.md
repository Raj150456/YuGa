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
