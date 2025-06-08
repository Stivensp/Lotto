const btn_register = document.querySelector(".button_register");
const btn_login = document.querySelector(".button_login");
const fm_login = document.querySelector(".form_login");
const fm_register = document.querySelector(".form_register");

btn_register.addEventListener("click", function () {
  sendRegister();
  printErrorRegister("Sin errores por ahora...");
});

btn_login.addEventListener("click", function () {
  sendLogin();
  printErrorLogin("Sin errores por ahora...");
});

function sendRegister() {
  const value = document.querySelector(".input_user_register").value;
  const password = document.querySelector(".input_password_register").value;
  window.pywebview.api.registrarse(value, password).then((response) => {
    printErrorRegister(response);
  });
  fm_register.reset();
}

function sendLogin() {
  const value = document.querySelector(".input_user_login").value;
  const password = document.querySelector(".input_password_login").value;
  window.pywebview.api.iniciarSesion(value, password).then((response) => {
    printErrorLogin(response);
  });
  fm_login.reset();
}

function printErrorLogin(value) {
  const printer = document.querySelector(".error_print_login");
  printer.textContent = value;
}

function printErrorRegister(value) {
  const printer = document.querySelector(".error_print_register");
  printer.textContent = value;
}
