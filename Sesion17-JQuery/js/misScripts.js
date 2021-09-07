$(document).ready(function(){
    $("a").click(function(evento){
        alert("Has pulsado el enlace. Ahora seras enviado a la pagina de la USAT")
    });
});

//Ocultar o mostrar bloque
$("#c1b").click(function(){
    $("#cont1").toggle(1500);
},function(){
    $("#cont1").toggle(1500);
})