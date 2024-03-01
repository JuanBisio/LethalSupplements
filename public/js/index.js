document.addEventListener("scroll", function() {

    var scrollPosition = window.scrollY;
    var content = document.querySelector(".blink");
  
    // Cambia el fondo dependiendo de la posición de desplazamiento
    if (scrollPosition > 70) { // Ejemplo: cambia el fondo cuando se haya desplazado 100px
      content.style.backgroundColor = "#212121"; // Cambia el color de fondo 
    } else {
      content.style.backgroundColor = "#212121CC"; // Vuelve al color de fondo predeterminado
    }
  });