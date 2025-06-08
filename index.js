
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
let visible = true; // estado inicial, visible

function desaparecerHaciaArriba() {
  const panel = document.getElementById("Tienda");

  if (visible) {
    // Si está visible, desaparecer hacia arriba
    panel.style.animation = "desaparecerHaciaArriba 2s ease forwards";
  } else {
    // Si está invisible, aparecer desde arriba
    panel.style.animation = "aparecerDesdeArriba 2s ease forwards";
  }

  // Alternar estado para el próximo click
  visible = !visible;
}

let pausado = true; // Empieza en pausa

function jugar() {
    const numeros = document.querySelectorAll('.ContenedorLuck div p');
    const celda1 = document.querySelector('.Celda1');

    if (pausado) {
        // 1. Reanudar animaciones
        numeros.forEach(n => {
            n.style.animationPlayState = 'running';
        });

        // 2. Cambiar z-index a 2 inmediatamente
        if (celda1) {
            celda1.style.zIndex = '2';
        }

        // 3. Establecer pausa después de 3 segundos
        setTimeout(() => {
            // 4. Cambiar estado a pausado
            pausado = true;

            // 5. Pausar animaciones y resetear posición
            numeros.forEach(n => {
                n.style.animationPlayState = 'paused';
                n.style.top = '0px';  // <-- Aquí la clave
            });

            // 6. Bajar z-index
            if (celda1) {
                celda1.style.zIndex = '1';
            }

        }, 3000);

        // Mientras tanto, se considera que está "corriendo"
        pausado = false;
    }
}


    async function loadNombre() {
      try {
        const respuesta = await window.pywebview.api.get_nombre();
        document.getElementById('nombre').innerText = respuesta.nombre;
      } catch (error) {
        document.getElementById('nombre').innerText = 'Error al cargar nombre';
        console.error(error);
      }
    }

    window.addEventListener('pywebviewready', () => {
        loadNombre();
    });
    //Funciones conectadas al python


