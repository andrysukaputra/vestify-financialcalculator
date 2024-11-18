// SR Pie & Bar Charts Data
const IAGPRInvestmentAssetsDist = document
  .getElementById("investment_assets_dist")
  .getAttribute("data-value");

const IAGPRCashDist = document
  .getElementById("cash_dist")
  .getAttribute("data-value");

const IAGPRAnnualGrossIncomeDist = document
  .getElementById("annual_gross_income_dist")
  .getAttribute("data-value");

const IAGPRResult = document
  .getElementById("iagpr-result")
  .getAttribute("data-value");

console.log(
  IAGPRResult,
  IAGPRInvestmentAssetsDist,
  IAGPRCashDist,
  IAGPRAnnualGrossIncomeDist
);

const IAGPRpiechartcontainer = document.getElementById(
  "iagpr-pie-chart-container"
);

if (IAGPRResult !== "") IAGPRpiechartcontainer.style.display = "block";

const iagprpie = document.getElementById("iagpr-pie-chart").getContext("2d");
const iagprpiechart = new Chart(iagprpie, {
  type: "pie",
  data: {
    labels: ["%Investment Assets", "%Cash", "%Annual Gross Income"],
    datasets: [
      {
        data: [
          IAGPRInvestmentAssetsDist,
          IAGPRCashDist,
          IAGPRAnnualGrossIncomeDist,
        ],
        backgroundColor: ["#007bff", "#dc3545", "#ffc107"],
      },
    ],
  },
  option: {
    responsive: true,
    maintainAspectRatio: true,
  },
});

const iagprbar = document.getElementById("iagpr-bar-chart").getContext("2d");
const iagprbarchart = new Chart(iagprbar, {
  type: "bar",
  data: {
    labels: [
      "Your Investment Assets to Gross Pay Ratio",
      "Starting at around 0.2% for those in their 20's.",
      "Starting at 20% as one approaches retirement.",
    ], // Label pada sumbu Y
    datasets: [
      {
        label: ["%Investment Assets to Gross Pay Ratio Comparison"],
        data: [IAGPRResult, 0.2, 20.0], // Nilai untuk sumbu X
        backgroundColor: ["blue", "red"],
      },
    ],
  },
  options: {
    indexAxis: "y", // Menampilkan chart secara horizontal
    responsive: true,
    maintainAspectRatio: true,
    scales: {
      x: {
        beginAtZero: true, // Menyesuaikan sumbu X
      },
    },
  },
});
