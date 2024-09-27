// Pilih semua elemen imput dengan querySelectorAll
document.querySelectorAll("input").forEach(function (inputField) {
  inputField.addEventListener("input", function (event) {
    let input = event.target;
    let value = input.value;

    // Hapus semua karakter kecuali angka dan titik desimal
    let numericValue = value.replace(/[^0-9.]/g, "");

    // Jika input kosong atau tidak valid, tampilkan "0"
    if (isNaN(numericValue) || numericValue === "") {
      numericValue = "0";
    }

    // Dapatkan lokal pengguna
    let userLocale = navigator.language || "en-US";
    let userCurrency = userLocale === "en-US" ? "USD" : "IDR";

    // Format angka sesuai dengan lokal pengguna tanpa menentukan simbol mata uang
    let formattedValue = parseFloat(numericValue).toLocaleString(userLocale, {
      style: "currency", // "IDR" bisa diubah dengan mata uang sesuai lokal pengguna
      currency: userCurrency,
      currencyDisplay: "symbol",
      minimumFractionDigits: 2,
      maximumFractionDigits: 20,
    });

    // Tampilkan nilai yang diformat dalam elemen <span> yang sesuai
    let outputId = input.getAttribute("data-output-id"); // Mengambil ID elemen <span> dari atribut data
    let amount = document.getElementById(outputId);
    amount.textContent = formattedValue;

    // Jika nilai kosong, setel menjadi "0"
    if (isNaN(value) || value === "") {
      amount.textContent = "0"; // Atur sesuai dengan format yang diinginkan
    }
  });
});
