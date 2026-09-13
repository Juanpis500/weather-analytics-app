import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import { weatherService } from '@/services/weatherService'

export const useWeatherStore = defineStore('weather', () => {
  // Estado
  const currentWeather = ref(null)
  const forecast = ref([])
  const currentCity = ref('')
  const isLoading = ref(false)
  const error = ref(null)

  // Getters (Computed properties)
  const isCached = computed(() => currentWeather.value?.cached ?? false)

  // Actions
  async function fetchWeatherData(city) {
    if (!city.trim()) return

    isLoading.value = true
    error.value = null

    try {
      // We execute both requests in parallel to optimize loading.
      const [currentRes, forecastRes] = await Promise.all([
        weatherService.getCurrentWeather(city),
        weatherService.getForecast(city),
      ])

      currentWeather.value = currentRes.data
      forecast.value = forecastRes.data.list
      currentCity.value = currentRes.data.name
    } catch (err) {
      if (err.response?.status === 404) {
        error.value = `La ciudad "${city}" no fue encontrada.`
      } else {
        error.value = 'Ocurrió un error al consultar la información del clima.'
      }
      currentWeather.value = null
      forecast.value = []
    } finally {
      isLoading.value = false
    }
  }

  return {
    currentWeather,
    forecast,
    currentCity,
    isLoading,
    error,
    isCached,
    fetchWeatherData,
  }
})