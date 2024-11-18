// BHODR Pie & Bar Charts Data
const BHODRHousingCostsDist = document
  .getElementById("broad_housing_costs_dist")
  .getAttribute("data-value");

const BHODROtherDebtPaymentsDist = document
  .getElementById("broad_other_debt_payments_dist")
  .getAttribute("data-value");

const BHODRGrossIncomeDist = document
  .getElementById("broad_gross_income_dist")
  .getAttribute("data-value");

const BHODRResult = document
  .getElementById("bhodr-result")
  .getAttribute("data-value");

console.log(
  BHODRResult,
  BHODRHousingCostsDist,
  BHODROtherDebtPaymentsDist,
  BHODRGrossIncomeDist
);

const BHODRpiechartcontainer = document.getElementById(
  "bhodr-pie-chart-container"
);

if (BHODRResult !== "") BHODRpiechartcontainer.style.display = "block";

const bhodrpie = document.getElementById("bhodr-pie-chart").getContext("2d");
const bhodrpiechart = new Chart(bhodrpie, {
  type: "pie",
  data: {
    labels: ["%Housing Costs", "%Other Debt Payments", "%Gross Income"],
    datasets: [
      {
        data: [
          BHODRHousingCostsDist,
          BHODROtherDebtPaymentsDist,
          BHODRGrossIncomeDist,
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

const bhodrbar = document.getElementById("bhodr-bar-chart").getContext("2d");
const bhodrbarchart = new Chart(bhodrbar, {
  type: "bar",
  data: {
    labels: [
      "Your Basic Housing and Other Debts Ratio",
      "The suggested limit is no more than 36%",
    ], // Label pada sumbu Y
    datasets: [
      {
        label: ["%Basic Housing and Other Debts Ratio Comparison"],
        data: [BHODRResult, 36.0], // Nilai untuk sumbu X
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
