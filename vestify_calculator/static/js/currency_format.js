document.querySelector("input").addEventListener("input", function (event) {
  let input = event.target;
  let value = input.value;

  // Hapus semua karakter kecuali angka
  //let numericValue = value.replace(/[^0-9]/g, "");

  // Dapatkan lokal pengguna
  let userLocale = navigator.language || "en-US";

  // Format angka sesuai dengan lokal pengguna tanpa menentukan simbol mata uang
  let formattedValue = parseFloat(value).toLocaleString(userLocale, {
    //new Intl.NumberFormat(userLocale, {
    style: "currency",
    currency: "IDR",
    currencyDisplay: "symbol",
    minimumFractionDigits: 2,
    maximumFractionDigits: 20,
  }); //.format(numericValue);

  // Tampilkan nilai yang diformat di dalam kotak input
  let amount = document.getElementById("currency-output");
  amount.textContent = formattedValue;
  //input.value = formattedValue;
  if (isNaN(amount.textContent)) {
    amount.textContent = 0;
  }
});
