// EFR Pie & Bar Charts Data
const EFREmergencyCashFundDist = document
  .getElementById("emergency_cash_fund_dist")
  .getAttribute("data-value");

const EFRMonthlyPrimaryExpensesDist = document
  .getElementById("monthly_primary_expenses_dist")
  .getAttribute("data-value");

const EFRResult = document
  .getElementById("efr-result")
  .getAttribute("data-value");

const EFRpiechartcontainer = document.getElementById("efr-pie-chart-container");

if (EFRResult !== "") EFRpiechartcontainer.style.display = "block";

const efrpie = document.getElementById("efr-pie-chart").getContext("2d");
const efrpiechart = new Chart(efrpie, {
  type: "pie",
  data: {
    labels: ["%Emergency Cash Fund", "%Monthly Primary Expenses"],
    datasets: [
      {
        data: [EFREmergencyCashFundDist, EFRMonthlyPrimaryExpensesDist],
        backgroundColor: ["#007bff", "#dc3545"],
      },
    ],
  },
  option: {
    responsive: true,
  },
});

const efrbar = document.getElementById("efr-bar-chart").getContext("2d");
const efrbarchart = new Chart(efrbar, {
  type: "bar",
  data: {
    labels: ["Your EFR", "Covering Max. 3 Months", "Covering Min. 6 Months"], // Label pada sumbu Y
    datasets: [
      {
        label: ["%EFR Comparison"],
        data: [EFRResult, 3.0, 6.0], // Nilai untuk sumbu X
        backgroundColor: ["blue", "red", "green"],
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
