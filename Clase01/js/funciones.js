function alerta(){
    window.alert("Probando JS")
}

function saludar(){
    var nombre=document.getElementById("txt1").value;
    alert("BUEN DIA " +nombre)
}
function saludo(){
    var nombre=document.getElementById("txt1").value;
    var saludo="BUENOS DIAS "+nombre;
    var contenedor= document.getElementById("divsaludo");
    contenedor.innerHTML= saludo;
}