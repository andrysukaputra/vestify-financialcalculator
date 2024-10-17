// SR Pie & Bar Charts Data
const SRTotalAnnualSavingsPie = document
  .getElementById("total-annual-savings-pie")
  .getAttribute("data-value");

const SREmployerMatchPie = document
  .getElementById("employer-match-pie")
  .getAttribute("data-value");

const SRAnnualGrossIncomePie = document
  .getElementById("annual-gross-income-pie")
  .getAttribute("data-value");

const SRResult = document
  .getElementById("sr-result")
  .getAttribute("data-value");

console.log(
  SRResult,
  SRTotalAnnualSavingsPie,
  SREmployerMatchPie,
  SRAnnualGrossIncomePie
);

const SRpiechartcontainer = document.getElementById("sr-pie-chart-container");

if (SRResult !== "") SRpiechartcontainer.style.display = "block";

const srpie = document.getElementById("sr-pie-chart").getContext("2d");
const srpiechart = new Chart(srpie, {
  type: "pie",
  data: {
    labels: [
      "%Total Annual Savings",
      "%Employer Match",
      "%Annual Gross Income",
    ],
    datasets: [
      {
        data: [
          SRTotalAnnualSavingsPie,
          SREmployerMatchPie,
          SRAnnualGrossIncomePie,
        ],
        backgroundColor: ["#007bff", "#dc3545", "#ffc107"],
      },
    ],
  },
  option: {
    responsive: true,
  },
});

const srbar = document.getElementById("sr-bar-chart").getContext("2d");
const srbarchart = new Chart(srbar, {
  type: "bar",
  data: {
    labels: ["Your Savings Rate", "Strong if > 15%", "Recommended Starting"], // Label pada sumbu Y
    datasets: [
      {
        label: ["%Savings Rate Comparison"],
        data: [SRResult, 15.0, 5.0], // Nilai untuk sumbu X
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
