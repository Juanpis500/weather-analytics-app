<script setup>
import { computed } from 'vue'
import { useWeatherStore } from '@/stores/weatherStore'

const weatherStore = useWeatherStore()

// We filter the list to obtain a representative reading for each day (around 12:00 PM).
const dailyForecast = computed(() => {
  if (!weatherStore.forecast.length) return []

  return weatherStore.forecast.filter(item => item.dt_txt.includes('12:00:00'))
})

// Function to format dates into translated day numbers
const formatDate = (dateStr) => {
  const date = new Date(dateStr)
  return new Intl.DateTimeFormat('en-EN', { weekday: 'short', day: 'numeric', month: 'short' }).format(date)
}
</script>

<template>
  <div v-if="dailyForecast.length" class="forecast-section">
    
    <div class="cards-grid">
      <div 
        v-for="item in dailyForecast" 
        :key="item.dt_txt" 
        class="forecast-card shadow-xl/20 bg-white/5"
      >
        <p class="day-name">{{ formatDate(item.dt_txt) }}</p>
        
        <img 
          :src="`https://openweathermap.org/img/wn/${item.weather.icon}@2x.png`" 
          :alt="item.weather.description"
          class="weather-icon"
        />
        
        <p class="temp-main">{{ Math.round(item.metrics.temp) }}°C</p>
        <p class="weather-desc">{{ item.weather.description }}</p>
        
        <div class="card-details">
          <span>💧 {{ item.metrics.humidity }}%</span>
          <span>💨 {{ item.wind.speed }} m/s</span>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>

.cards-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(140px, 1fr));
  gap: 1rem;
}

.forecast-card {
  border-radius: 10px;
  padding: 1rem;
  text-align: center;
  transition: transform 0.2s ease, box-shadow 0.2s ease;
}

.forecast-card:hover {
  transform: translateY(-3px);
  box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
}

.day-name {
  font-weight: 600;
  color: #EAECEE;
  text-transform: capitalize;
  font-size: 0.9rem;
  margin: 0;
}

.weather-icon {
  width: 60px;
  height: 60px;
}

.temp-main {
  font-size: 1.4rem;
  font-weight: 700;
  color: #D6EAF8;
  margin: 0.2rem 0;
}

.weather-desc {
  font-size: 0.8rem;
  color: #D4E6F1;
  text-transform: capitalize;
  margin-bottom: 0.8rem;
  min-height: 2.4em;
  display: flex;
  align-items: center;
  justify-content: center;
}

.card-details {
  display: flex;
  justify-content: space-between;
  font-size: 0.75rem;
  color: #D6DBDF;
  border-top: 1px solid #f1f5f9;
  padding-top: 0.5rem;
}
</style>