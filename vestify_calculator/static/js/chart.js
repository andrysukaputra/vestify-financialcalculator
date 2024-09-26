let ctx = document.getElementById("myChart").getContext("2d");

let data = {
  labels: [
    "Final Value of Investment",
    "Initial Value of Investment",
    "Cost of Investment",
  ],
  datasets: [
    {
      label: "Distribusi",
      data: [0, 0, 0], // Data awal
      backgroundColor: [
        "rgba(255, 99, 132, 0.2)",
        "rgba(54, 162, 235, 0.2)",
        "rgba(75, 192, 192, 0.2)",
      ],
      borderColor: [
        "rgba(255, 99, 132, 1)",
        "rgba(54, 162, 235, 1)",
        "rgba(75, 192, 192, 1)",
      ],
      borderWidth: 1,
    },
  ],
};

let config = {
  type: "pie",
  data: data,
  options: {
    responsive: true,
    maintainAspectRatio: true,
    plugins: {
      legend: {
        position: "top",
      },
      tooltip: {
        enabled: true,
      },
    },
  },
};

let myChart = new Chart(ctx, config);

function updateChart() {
  const FinalValueOfInvestment =
    document.getElementById("final_value_of_investment").value || 0;
  const InitialValueOfInvestment =
    document.getElementById("initial_value_of_investment").value || 0;
  const CostOfInvestment =
    document.getElementById("cost_of_investment").value || 0;

  // Update data chart
  myChart.data.datasets[0].data = [
    FinalValueOfInvestment,
    InitialValueOfInvestment,
    CostOfInvestment,
  ];
  myChart.update(); // Refresh chart
}

window.onload = function () {
  const roiResult = document.getElementById("roi-result");
  const chartContainer = document.getElementById("chart-container");

  if (roiResult.innerText !== "") {
    chartContainer.style.display = "block";
    updateChart();
  }
};
