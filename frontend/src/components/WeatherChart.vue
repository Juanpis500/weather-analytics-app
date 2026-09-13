<script setup>
import { computed } from 'vue'
import {
  Chart as ChartJS,
  CategoryScale,
  LinearScale,
  PointElement,
  LineElement,
  Title,
  Tooltip,
  Legend,
  Filler
} from 'chart.js'
import { Line } from 'vue-chartjs'
import { useWeatherStore } from '@/stores/weatherStore'

// Register necessary Chart.js modules.
ChartJS.register(
  CategoryScale,
  LinearScale,
  PointElement,
  LineElement,
  Title,
  Tooltip,
  Legend,
  Filler
)

const weatherStore = useWeatherStore()

// Map the store data to the structure required by Chart.js.
const chartData = computed(() => {
  // We take the first 8 readings (~24-hour forecast).
  const items = weatherStore.forecast.slice(0, 8)

  const labels = items.map(item => {
    const date = new Date(item.dt_txt)
    return date.toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' })
  })

  const temperatures = items.map(item => item.metrics.temp)

  return {
    labels,
    datasets: [
      {
        label: 'Temperatura (°C)',
        data: temperatures,
        borderColor: '#3b82f6',
        backgroundColor: 'rgba(59, 130, 246, 0.15)',
        borderWidth: 3,
        fill: true,
        tension: 0.35, // Smooth curve for the line
        pointBackgroundColor: '#2563eb',
        pointRadius: 4
      }
    ]
  }
})

// Chart configuration options
const chartOptions = {
  responsive: true,
  maintainAspectRatio: false,
  plugins: {
    legend: {
      display: false,
      color: 'rgba(255, 255, 255, 0.7)'
    },
    tooltip: {
      callbacks: {
        label: (context) => ` ${context.parsed.y} °C`
      }
    }
  },
  scales: {
    y: {
      grid: {
        color: 'rgba(255, 255, 255, 0.1)'
      },
      ticks: {
        callback: (value) => `${value}°C`,
        color: 'rgba(255, 255, 255, 0.7)'
      }
    },
    x: {
      grid: {
        display: false
      },
      ticks: {
        color: 'rgba(255, 255, 255, 0.7)'
      }
    }
  }
}
</script>

<template>
  <div v-if="weatherStore.forecast.length" class="chart-card">
    <div class="chart-container">
      <Line :data="chartData" :options="chartOptions" />
    </div>
  </div>
</template>

<style scoped>
.chart-card {
  background: none;
  border-radius: 10px;
  padding: 1.25rem;
  margin-top: 1.5rem;
  width: 100%;
}

h3 {
  margin-top: 0;
  margin-bottom: 1rem;
  font-size: 1.1rem;
  color: white;
}
</style>