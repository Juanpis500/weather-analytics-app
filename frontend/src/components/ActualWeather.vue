<script setup>
    import { useWeatherStore } from '@/stores/weatherStore'
    const weatherStore = useWeatherStore()
</script>

<template>
  <div class="weather-dashboard">
    <!-- Current Weather Results -->
    <div v-if="weatherStore.currentWeather" class="weather-card">
      <div class="grid auto-rows-auto items-center h-full divide-dashed w-full gap-4 grid-cols-3">
        <div class=" col-span-1 row-span-2 sm:col-span-1 sm:row-span-1">
          <img 
            :src="`https://openweathermap.org/img/wn/${weatherStore.currentWeather.weather.icon}@2x.png`" 
            :alt="weatherStore.currentWeather.weather.description"
            class="weather-icon"
          />
        </div>
        <div class="col-span-2 row-span-1 sm:col-span-1">
          <p class="temp">{{ weatherStore.currentWeather.metrics.temp }} °C</p>
          
        </div>
        <div class="col-span-2 row-span-1 sm:col-span-1">
          <h2 class="text-xl font-semibold text-white">
            {{ weatherStore.currentWeather.name }}, {{ weatherStore.currentWeather.country }}
          </h2>
          <p class="desc">{{ weatherStore.currentWeather.weather.description }}</p>
        </div>
        
      </div>
    </div>
  </div>
</template>

<style scoped>

  .temp {
    font-size: 2rem;
    font-weight: bold;
    color: white;
  }

  .desc {
    font-size: 1rem;
    color: rgb(230, 230, 230);
  }

  .weather-icon {
      border-right: 1px solid rgba(255, 255, 255, 0.1);
    }

</style>