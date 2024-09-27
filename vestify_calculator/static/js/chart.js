const FinalValueOfInvestment = document
  .getElementById("Final-Value-of-Investment")
  .getAttribute("data-value");

const InitialValueOfInvestment = document
  .getElementById("Initial-Value-of-Investment")
  .getAttribute("data-value");

const CostOfInvestment = document
  .getElementById("Cost-of-Investment")
  .getAttribute("data-value");

const ROIResult = document
  .getElementById("roi-result")
  .getAttribute("data-value");

const chartContainer = document.getElementById("chart-container");

let userLocale = navigator.language || "en-US";
let numberFormat = new Intl.NumberFormat(userLocale);
let parts = numberFormat.formatToParts(1234567.89);

let decimalSeparator = parts.find((part) => part.type === "decimal").value;
let groupSeparator = parts.find((part) => part.type === "group").value;

let cleanedvaluefinal = FinalValueOfInvestment.replace(
  new RegExp("\\" + groupSeparator, "g"),
  ""
)
  .replace(new RegExp("\\" + decimalSeparator), ".")
  .replace(/[^\d.-]/g, "");

let cleanedvalueinitial = InitialValueOfInvestment.replace(
  new RegExp("\\" + groupSeparator, "g"),
  ""
)
  .replace(new RegExp("\\" + decimalSeparator), ".")
  .replace(/[^\d.-]/g, "");

let cleanedvaluecost = CostOfInvestment.replace(
  new RegExp("\\" + groupSeparator, "g"),
  ""
)
  .replace(new RegExp("\\" + decimalSeparator), ".")
  .replace(/[^\d.-]/g, "");

let decimalfinalvalue = parseFloat(cleanedvaluefinal);
let decimalinitialvalue = parseFloat(cleanedvalueinitial);
let decimalcost = parseFloat(cleanedvaluecost);

console.log(decimalfinalvalue, decimalinitialvalue, decimalcost);

if (ROIResult !== "") chartContainer.style.display = "block";

const ctx = document.getElementById("ROIChart").getContext("2d");

const ROIChart = new Chart(ctx, {
  type: "pie",
  data: {
    labels: [
      "Final Value of Investment",
      "Initial Value of Investment",
      "Cost of Investment",
    ],
    datasets: [
      {
        data: [decimalfinalvalue, decimalinitialvalue, decimalcost],
        backgroundColor: ["#007bff", "#dc3545", "#ffc107"],
      },
    ],
  },
  option: {
    responsive: true,
  },
});
