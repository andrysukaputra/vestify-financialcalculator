// ROI Pie & Bar Charts Data
const ROIFinalValueOfInvestmentPie = document
  .getElementById("final-value-of-investment-pie")
  .getAttribute("data-value");

const ROIInitialValueOfInvestmentPie = document
  .getElementById("initial-value-of-investment-pie")
  .getAttribute("data-value");

const ROICostOfInvestmentPie = document
  .getElementById("cost-of-investment-pie")
  .getAttribute("data-value");

const ROIResult = document
  .getElementById("roi-result")
  .getAttribute("data-value");

const ROIpiechartcontainer = document.getElementById("roi-pie-chart-container");

if (ROIResult !== "") ROIpiechartcontainer.style.display = "block";

const roipie = document.getElementById("roi-pie-chart").getContext("2d");
const roipiechart = new Chart(roipie, {
  type: "pie",
  data: {
    labels: [
      "%Final Value of Investment",
      "%Initial Value of Investment",
      "%Cost of Investment",
    ],
    datasets: [
      {
        data: [
          ROIFinalValueOfInvestmentPie,
          ROIInitialValueOfInvestmentPie,
          ROICostOfInvestmentPie,
        ],
        backgroundColor: ["#007bff", "#dc3545", "#ffc107"],
      },
    ],
  },
  option: {
    responsive: true,
  },
});

const roibar = document.getElementById("roi-bar-chart").getContext("2d");
const roibarchart = new Chart(roibar, {
  type: "bar",
  data: {
    labels: ["Your ROI", "Strong if > 10%", "Minimum ROI Limit"], // Label pada sumbu Y
    datasets: [
      {
        label: ["%ROI Comparison"],
        data: [ROIResult, 10.0, 5.0], // Nilai untuk sumbu X
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
