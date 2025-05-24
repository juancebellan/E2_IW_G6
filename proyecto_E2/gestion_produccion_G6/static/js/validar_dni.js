document.addEventListener("DOMContentLoaded", function () {
  let form = document.querySelector("form");
  let dniInput = document.getElementById("dni");

  form.addEventListener("submit", function (e) {
    let dniValue = dniInput.value.trim().toUpperCase();
    let dniRegex = /^[0-9]{8}[A-Z]$/;

    if (!dniRegex.test(dniValue)) {
      e.preventDefault();
      alert("El DNI no tiene un formato válido. Debe tener 8 números y una letra mayúscula (ej: 12345678Z)");
    }
  });
});
