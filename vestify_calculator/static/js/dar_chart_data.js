// SR Pie & Bar Charts Data
const DARTotalDebtDist = document
  .getElementById("total_debt_dist")
  .getAttribute("data-value");

const DARTotalAssetsDist = document
  .getElementById("total_assets_dist")
  .getAttribute("data-value");

const DARResult = document
  .getElementById("dar-result")
  .getAttribute("data-value");

console.log(DARResult, DARTotalDebtDist, DARTotalAssetsDist);

const DARpiechartcontainer = document.getElementById("dar-pie-chart-container");

if (DARResult !== "") DARpiechartcontainer.style.display = "block";

const darpie = document.getElementById("dar-pie-chart").getContext("2d");
const darpiechart = new Chart(darpie, {
  type: "pie",
  data: {
    labels: ["%Total Debt", "%Total Assets"],
    datasets: [
      {
        data: [DARTotalDebtDist, DARTotalAssetsDist],
        backgroundColor: ["#007bff", "#dc3545", "#ffc107"],
      },
    ],
  },
  option: {
    responsive: true,
  },
});

const darbar = document.getElementById("dar-bar-chart").getContext("2d");
const darbarchart = new Chart(darbar, {
  type: "bar",
  data: {
    labels: [
      "Your Debt to Assets Ratio",
      "It's good if it gets closer or equal to 0%",
    ], // Label pada sumbu Y
    datasets: [
      {
        label: ["%Debt to Assets Ratio Comparison"],
        data: [DARResult, 0.0], // Nilai untuk sumbu X
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
