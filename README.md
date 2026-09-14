# Weather Analytics Dashboard 🌦️

Full-stack weather analytics application built with FastAPI, Redis, Vue 3, Pinia, and Tailwind CSS v4.

Demo version online
https://weather-analytics-app-green.vercel.app/

## Features
- **Real-time Weather & 5-Day Forecast**: OpenWeatherMap API integration.
- **High-Performance Caching**: Redis Cache-Aside pattern (10-minute TTL).
- **Interactive Visualizations**: Chart.js for temperature trends over time.
- **Modern UI/UX**: Custom responsive dashboard styled with Tailwind CSS v4.

## Tech Stack
- **Backend**: Python 3.11+, FastAPI, Pydantic v2, Redis (async), HTTPX.
- **Frontend**: Vue 3 (Composition API), Pinia, Axios, Chart.js, Tailwind CSS.

# 🌤️ Weather Analytics Dashboard

[![FastAPI](https://img.shields.io/badge/FastAPI-0.110+-009688?style=for-the-badge&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![Vue.js](https://img.shields.io/badge/Vue.js-3.x-4FC08D?style=for-the-badge&logo=vuedotjs&logoColor=white)](https://vuejs.org/)
[![Tailwind CSS](https://img.shields.io/badge/Tailwind_CSS-v4.0-06B6D4?style=for-the-badge&logo=tailwindcss&logoColor=white)](https://tailwindcss.com/)
[![Redis](https://img.shields.io/badge/Redis-Upstash-DC382D?style=for-the-badge&logo=redis&logoColor=white)](https://upstash.com/)
[![Render](https://img.shields.io/badge/Render-Backend-46E3B7?style=for-the-badge&logo=render&logoColor=white)](https://render.com/)
[![Vercel](https://img.shields.io/badge/Vercel-Frontend-000000?style=for-the-badge&logo=vercel&logoColor=white)](https://vercel.com/)

A high-performance weather analytics dashboard built with a **FastAPI** asynchronous backend using a **Cache-Aside pattern with Redis**, paired with a reactive **Vue 3** frontend styled with Tailwind CSS.

---

## 🏗️ System Architecture

The project implements a decoupled REST API architecture designed to minimize latency and optimize third-party API rate limits through intelligent caching.

```text
[ Web Client (Vue 3 / Vite) ]
             │
             ▼ (HTTP / JSON via Axios)
  [ Backend (FastAPI / Render) ]
             │
      ┌──────┴──────┐
      │             │
  (Hit)           (Miss)
      ▼             ▼
[ Redis Cache ]  [ OpenWeatherMap API ]
 (Upstash TLS)      (Write to Redis)
```

## Getting Started

### Prerequisites
- Python 3.11+
- Node.js 18+
- Docker (for Redis)

### Backend Setup
```bash
cd backend
python -m venv venv
# On Windows:
.\venv\Scripts\activate
pip install -r requirements.txt
# Copy .env.example to .env and insert your OpenWeatherMap API Key
python -m uvicorn app.main:app --reload
```

### Frontend Setup
```bash
cd frontend
npm install
npm run dev
```

### Run Redis via Docker
```bash
docker run -d --name weather-redis -p 6379:6379 redis:alpine
```
