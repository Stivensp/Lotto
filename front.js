const form_login = document.querySelector(".form_login");
const form_register = document.querySelector(".form_register");

const cont_login = document.querySelector(".container_login");
const cont_register = document.querySelector(".container_register");

const button_login = document.querySelector(".change_login");
const button_register = document.querySelector(".change_register");

let menu = 0;
register();

function register() {
  form_login.classList.add("open");
  cont_login.classList.add("open");
  cont_register.classList.remove("open");
  form_register.classList.remove("open");
  console.log("si");
}
function login() {
  form_register.classList.add("open");
  cont_register.classList.add("open");

  cont_login.classList.remove("open");
  form_login.classList.remove("open");
}

button_register.addEventListener("click", function () {
  register();
});

button_login.addEventListener("click", function () {
  login();
});

const back = document.querySelector(".back");
back.addEventListener("click", function () {
  window.location.href = "menuprincipal.html";
});
