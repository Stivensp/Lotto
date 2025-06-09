const btn_buy = document.querySelector(".buttom_comprar");
const output = document.querySelector(".output_container");
const text_output = document.querySelector(".output_p");

btn_buy.addEventListener("click", function () {
  verificarTicket();
});

function verificarTicket() {
  const input = document.querySelector("#buscador");
  window.pywebview.api.Comprar(input.value).then((response) => {
    printReturnTicket(response);
  });
}

function printReturnTicket(value) {
  text_output.textContent = value;
  openOutput();
}

function openOutput() {
     output.classList.remove("open");
  output.classList.add("open");
  setTimeout(function () {
    closeOutput();
  }, 5000);
}

function closeOutput() {
  output.classList.remove("open");
}
