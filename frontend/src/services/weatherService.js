import apiClient from '@/api/axios'

export const weatherService = {
  // Get the current weather for a city
  getCurrentWeather(city) {
    return apiClient.get(`/weather/current/${encodeURIComponent(city)}`)
  },

  // Get the 5-day forecast for a city
  getForecast(city) {
    return apiClient.get(`/weather/forecast/${encodeURIComponent(city)}`)
  },
}