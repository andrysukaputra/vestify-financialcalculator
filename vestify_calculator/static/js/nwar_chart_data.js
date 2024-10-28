// SR Pie & Bar Charts Data
const NWARTotalAssetsDist = document
  .getElementById("total_assets_dist")
  .getAttribute("data-value");

const NWARLiabilitiesDist = document
  .getElementById("liabilities_dist")
  .getAttribute("data-value");

const NWARResult = document
  .getElementById("nwar-result")
  .getAttribute("data-value");

console.log(NWARResult, NWARTotalAssetsDist, NWARLiabilitiesDist);

const NWARpiechartcontainer = document.getElementById(
  "nwar-pie-chart-container"
);

if (NWARResult !== "") NWARpiechartcontainer.style.display = "block";

const nwarpie = document.getElementById("nwar-pie-chart").getContext("2d");
const nwarpiechart = new Chart(nwarpie, {
  type: "pie",
  data: {
    labels: ["%Total Assets", "%Liabilities"],
    datasets: [
      {
        data: [NWARTotalAssetsDist, NWARLiabilitiesDist],
        backgroundColor: ["#007bff", "#dc3545", "#ffc107"],
      },
    ],
  },
  option: {
    responsive: true,
  },
});

const nwarbar = document.getElementById("nwar-bar-chart").getContext("2d");
const nwarbarchart = new Chart(nwarbar, {
  type: "bar",
  data: {
    labels: [
      "Your Net Worth to Assets Ratio",
      "For retired individuals it is closer to 90% to 100%.",
      "For younger individuals it is generally 20%.",
    ], // Label pada sumbu Y
    datasets: [
      {
        label: ["%Net Worth to Assets Ratio Comparison"],
        data: [NWARResult, 90.0, 20.0], // Nilai untuk sumbu X
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
