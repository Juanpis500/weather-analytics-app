<script setup>
  import WeatherSearch from './components/WeatherSearch.vue'
  import WeatherChart from './components/WeatherChart.vue'
  import ForecastCards from './components/ForecastCards.vue'
  import ActualWeather from './components/ActualWeather.vue'
  import { useWeatherStore } from '@/stores/weatherStore'

  const weatherStore = useWeatherStore()
</script>

<template class="p-8 ..."> 
  <main class="p-8 xl:mx-50 2xl:mx-100">
    <div class="grid lg:grid-cols-3 gap-4 lg:p-4 ... ">
      <div class="col-span-2 ...">
        <h1 class="text-3xl font-bold text-white font-sans">Weather Analytics Dashboard</h1>
      </div>
      <div class="...">
        <WeatherSearch />
      </div>
    </div>
    <div class="grid grid-cols-1 auto-rows-auto gap-4 lg:p-4" v-if="weatherStore.currentWeather">
       <div class="col-span-1 lg:col-span-2 row-span-1 lg:row-span-4 flex items-center justify-center p-4" style="border-bottom: 1px solid rgba(255, 255, 255, 0.1);">
        <div class=" flex items-center justify-center w-full h-full">
          <ActualWeather />
        </div>
      </div>
      <h3 class="col-span-3">Temperature Evolution (Next 24 Hours)</h3>
      <div class="col-span-2 row-span-1 bg-white/5 rounded-xl lg:p-4 flex items-center justify-center shadow-xl/20">
        <div class="w-full h-full">
          <WeatherChart />
        </div>
      </div>
      <h3 class="col-span-3">Forecast for the Next 5 Days</h3>
      <div class="col-span-2 row-span-1 lg:p-4 flex items-center justify-center">
        <div class="w-full h-full">
          <ForecastCards />
        </div>
      </div>
    </div>
    <span v-if="weatherStore.isCached" class="cache-badge">
        ⚡ Data loaded from Redis Cache
      </span>
  </main>
</template>

<style scoped>

  header {
    text-align: center;
    margin-bottom: 2rem;
  }

  h3 {
    margin-top: 1rem;
    font-size: 1.1rem;
    color: white;
    font-weight: 600;
    margin-bottom: 1rem;
  }
  .cache-badge {
    display: inline-block;
    margin-top: 0.5rem;
    padding: 0.25rem 0.5rem;
    background-color: rgba(255, 255, 255, 0.1);
    color: white;
    border-radius: 5px;
    font-size: 0.8rem;
  }
</style>