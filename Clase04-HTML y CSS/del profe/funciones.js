function alerta(){
	window.alert("Probando JavaScript");
}

function saludar(){
	var nombre = document.getElementById("txt1").value;
	alert("Buenos dias " + nombre);
}

function saludo(){
	var nombre = document.getElementById("txt1").value;
	var saludo = "Buenos d&iacute;as " + nombre;
	var contenedor = document.getElementById("divsaludo");
	contenedor.innerHTML = saludo;
}