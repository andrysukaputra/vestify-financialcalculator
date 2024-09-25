// Fungsi untuk memperbarui chart dengan nilai input baru
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

// Tambahkan event listener ke btn
document.querySelectorAll("btn btn-primary").forEach((button) => {
  button.addEventListener("submit", updateChart);
});
