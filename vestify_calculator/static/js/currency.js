function formatCurrency() {
  let final_value_of_investment = document.getElementById(
    "final_value_of_investment"
  ).value;

  let formattedCurrency = parseFloat(
    final_value_of_investment
  ).toLocaleString();

  document.getElementById("currency-output").textContent = formattedCurrency;
}
