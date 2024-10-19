// SR Pie & Bar Charts Data
const BHRHousingCostsDist = document
  .getElementById("housing_costs_dist")
  .getAttribute("data-value");

const BHRGrossIncomeDist = document
  .getElementById("gross_income_dist")
  .getAttribute("data-value");

const BHRResult = document
  .getElementById("bhr-result")
  .getAttribute("data-value");

console.log(BHRResult, BHRHousingCostsDist, BHRGrossIncomeDist);

const BHRpiechartcontainer = document.getElementById("bhr-pie-chart-container");

if (BHRResult !== "") BHRpiechartcontainer.style.display = "block";

const bhrpie = document.getElementById("bhr-pie-chart").getContext("2d");
const bhrpiechart = new Chart(bhrpie, {
  type: "pie",
  data: {
    labels: ["%Housing Costs", "%Gross Income"],
    datasets: [
      {
        data: [BHRHousingCostsDist, BHRGrossIncomeDist],
        backgroundColor: ["#007bff", "#dc3545"],
      },
    ],
  },
  option: {
    responsive: true,
  },
});

const bhrbar = document.getElementById("bhr-bar-chart").getContext("2d");
const bhrbarchart = new Chart(bhrbar, {
  type: "bar",
  data: {
    labels: [
      "Your Basic Housing Ratio",
      "Strong if > 15%",
      "Recommended Starting",
    ], // Label pada sumbu Y
    datasets: [
      {
        label: ["%Basic Housing Ratio Comparison"],
        data: [BHRResult, 15.0, 5.0], // Nilai untuk sumbu X
        backgroundColor: ["blue", "red"],
      },
    ],
  },
  options: {
    indexAxis: "y", // Menampilkan chart secara horizontal
    responsive: true,
    scales: {
      x: {
        beginAtZero: true, // Menyesuaikan sumbu X
      },
    },
  },
});
