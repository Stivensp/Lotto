///////////////////////////////////////////////////////////////////////////////////////////
const numerosGenerados = [];

function generarNumeros() {
    for (let i = 1; i <= 6; i++) {
        const numero = Math.floor(Math.random() * 10);
        document.getElementById(`ale${i}`).innerText = numero;
        numerosGenerados.push(numero);
    }
    const numeroJoin=numerosGenerados.join('')
    const resulti =document.getElementById("result").innerText=numeroJoin
}

document.addEventListener('DOMContentLoaded', generarNumeros);

///////////////////////////////////////////////////////////////////////////////////////////
let visible = true;

function desaparecerHaciaArriba() {
  const panel = document.getElementById("Tienda");

  if (visible) {
    panel.style.animation = "desaparecerHaciaArriba 2s ease forwards";
  } else {

    panel.style.animation = "aparecerDesdeArriba 2s ease forwards";
  }

  visible = !visible;
}

let pausado = true; 
///////////////////////////////////////////////////////////////////////////////////////////
function jugar() {
    const numeros = document.querySelectorAll('.ContenedorLuck div p');
    const celda1 = document.querySelector('.Celda1');

    if (pausado) {
        numeros.forEach(n => {
            n.style.animationPlayState = 'running';
        });
        if (celda1) {
            celda1.style.zIndex = '2';
        }
        setTimeout(() => {

            pausado = true;

            numeros.forEach(n => {
                n.style.animationPlayState = 'paused';
                n.style.top = '0px';  
            });

            if (celda1) {
                celda1.style.zIndex = '1';
            }
        }, 3000);
        pausado = false;
    }
}
///////////////////////////////////////////////////////////////////////////////////////////

// LO BORRE PORQUE DABA ERROR
///////////////////////////////////////////////////////////////////////////////////////////
const boletas = [456412,456412,456412,456412];

function getlist() {
  window.pywebview.api.Comprar(value).then((response) => {
      if (value == "ok") {
        window.pywebview.api.getList().then((response) => {
          boletas = response;
        });
      }
  });
}





function renderBoletas() {
    const contenedor = document.getElementById('contenedor-boletas');
    contenedor.innerHTML = '';

    boletas.forEach(numero => {
        const div = document.createElement('div');
        div.classList.add('t1');
        div.innerHTML = `
            <img style="width:40px;" src="icons/ticket.png" alt="">
            <p>${numero}</p>
            <div class="Basura">
                <img class="borrar" style="width:30px;" src="icons/basuri.png" alt="">
            </div>
        `;
        contenedor.appendChild(div);
    });

    document.querySelector('.TotalTicket p').textContent = `${boletas.length} BOLETAS REGISTRADAS`;
}

renderBoletas();
document.addEventListener('click', function(e) {
    if (e.target.classList.contains('borrar')) {
        const numero = parseInt(e.target.closest('.t1').querySelector('p').textContent);
        const index = boletas.indexOf(numero);
        if (index !== -1) {
            boletas.splice(index, 1);
            renderBoletas();
        }
    }
});
