document.getElementById("toggleNavbar").addEventListener("click", function () {
  this.classList.toggle("collapsed");
  var sidebar = document.getElementById("sidebar");
  if (sidebar.style.display === "none" || sidebar.style.display === "") {
    sidebar.style.display = "block";
  } else {
    sidebar.style.display = "none";
  }
});
