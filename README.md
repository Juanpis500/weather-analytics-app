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
