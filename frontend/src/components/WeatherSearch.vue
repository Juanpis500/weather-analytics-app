<script setup>
    import { ref } from 'vue'
    import { useWeatherStore } from '@/stores/weatherStore'

    const weatherStore = useWeatherStore()
    const searchCity = ref('')

    const handleSearch = () => {
        if (searchCity.value) {
            weatherStore.fetchWeatherData(searchCity.value)
        }
    }
</script>

<template>
  <div class="weather-dashboard">
    <!-- Searcher -->
    <form @submit.prevent="handleSearch" class="search-form">
      <input
        v-model="searchCity"
        type="text"
        placeholder="Enter a city (e.g., Tokyo)..."
        :disabled="weatherStore.isLoading"
        class="search-input"
      />
      <button type="submit" :disabled="weatherStore.isLoading" class="search-button">
        {{ weatherStore.isLoading ? 'Loading...' : 'Search' }}
      </button>
    </form>

    <!-- Error Indicator -->
    <div v-if="weatherStore.error" class="error-badge">
      {{ weatherStore.error }}
    </div>
  </div>
</template>

<style scoped> 
  .search-form {
    display: flex;
    gap: 10px;
    margin-bottom: 1rem;
  }
  .search-button {
    background-color: none;
    color: rgba(255, 255, 255, 0.6) ;
    border: 2px solid rgba(255, 255, 255, 0.4); 
    padding: 0.5rem 1rem;
    cursor: pointer;
    border-radius: 5px;
  }
  .search-button:disabled {
    background-color: #ccc;
    cursor: not-allowed;
  }
  .search-input {
    padding: 0.5rem;
    border-radius: 5px;
    border: 2px solid rgba(255, 255, 255, 0.4); 
    color: rgba(255, 255, 255, 0.6);
    width: 100%;
  }
  .error-badge {
    display: inline-block;
    margin-top: 0.5rem;
    padding: 0.25rem 0.5rem;
    background-color: rgba(255, 0, 0, 0.2);
    color: red;
    border-radius: 5px;
  }
</style>