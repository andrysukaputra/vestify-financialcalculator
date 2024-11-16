// SR Pie & Bar Charts Data
const SRAnnualSavingsDist = document
  .getElementById("annual_savings_dist")
  .getAttribute("data-value");

const SREmployerMatchDist = document
  .getElementById("employer_match_dist")
  .getAttribute("data-value");

const SRAnnualGrossIncomeDist = document
  .getElementById("annual_gross_income_dist")
  .getAttribute("data-value");

const SRResult = document
  .getElementById("sr-result")
  .getAttribute("data-value");

console.log(
  SRResult,
  SRAnnualSavingsDist,
  SREmployerMatchDist,
  SRAnnualGrossIncomeDist
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
          SRAnnualSavingsDist,
          SREmployerMatchDist,
          SRAnnualGrossIncomeDist,
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
    maintainAspectRatio: true,
    scales: {
      x: {
        beginAtZero: true, // Menyesuaikan sumbu X
      },
    },
  },
});
