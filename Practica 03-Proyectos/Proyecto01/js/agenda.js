function guardarDato(){
    //capturando variables
    const nombre = document.getElementById("nombre").value;
    const movil = document.getElementById("movil").value;
    const email = document.getElementById("email").value;
    
    const datos = {
        'movil': movil,
        'email': email,
    };
    //Almacenando datos
    localStorage.setItem(nombre, JSON.stringify(datos));
    //Borrando datos
    document.getElementById("nombre").value = "";
    document.getElementById("movil").value = "";
    document.getElementById("email").value = "";
    //actualizando lista
    actualizarDatos();
}

function recuperarDato(){
    var nombre = document.getElementById("nombre").value;
    localStorage.getItem(nombre);
    document.getElementById("movil").value = JSON.parse(localStorage.getItem(nombre)).movil;
    document.getElementById("email").value = JSON.parse(localStorage.getItem(nombre)).email;
}

function eliminarDato(){
    var nombre = document.getElementById("nombre").value;
    localStorage.removeItem(nombre);
    actualizarDatos();
}

function eliminarTodo(){
    localStorage.clear();
    actualizarDatos();
}

function actualizarDatos(){
    var registro = "";
    if (localStorage.length === 0){
        registro += '<li>Vacío</li>';
    } else{
        for (var i = 0; i<=localStorage.length-1; i++ ){
            var key = localStorage.key(i);
            registro += '<li>' + '<span class="nom">' + key + '</span>'
            + '<span class="nom">' + JSON.parse(localStorage.getItem(key)).movil + '</span>' 
            + '<span class="nom">' + JSON.parse(localStorage.getItem(key)).email + '</span>' + '</li><br>';
        }
    }
    document.getElementById('contactos').innerHTML=registro;
}


     /*  // Example starter JavaScript for disabling form submissions if there are invalid fields
      (function() {
        'use strict';
        window.addEventListener('load', function() {
          // Fetch all the forms we want to apply custom Bootstrap validation styles to
          var forms = document.getElementsByClassName('needs-validation');
          // Loop over them and prevent submission
          var validation = Array.prototype.filter.call(forms, function(form) {
            form.addEventListener('submit', function(event) {
              if (form.checkValidity() === false) {
                event.preventDefault();
                event.stopPropagation();
              }
              form.classList.add('was-validated');
            }, false);
          });
        }, false);
      })(); */
     