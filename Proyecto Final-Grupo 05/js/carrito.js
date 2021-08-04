let productos = new Map();
productos.set(
    '1', ["Reloj Análogo Unisex", "169"]
);
productos.set(
    '2', ["Reloj Dual Multifunción Iluminación Cobra", "74.90"]
);
productos.set(
    '3', ["Smart Band M5 Reloj Deportivo Bluetooth Rojo", "39"]
);
productos.set(
    '4', ["Chompa Hombre Negra", "64.99"]
);
productos.set(
    '5', ["Chompa Hombre con cierre", "49.99"]
);
productos.set(
    '6', ["Chompa Hombre Blanca", "77.94"]
);
productos.set(
    '7', ["Pantalón Cargo Hombre", "59.90"]
);
productos.set(
    '8', ["Pantalón Hombre", "88"]
);
productos.set(
    '9', ["Pantalón Hombre Negro", "59.94"]
);
productos.set(
    '10', ["Polo Manga Corta Hombre", "17.94"]
);
productos.set(
    '11', ["Polo Manga Corta Hombre", "35.99"]
);
productos.set(
    '12', ["Polo Manga Corta Hombre", "25.99"]
);
productos.set(
    '13', ["Chompa Hombre Negra", "64.99"]
);
productos.set(
    '14', ["Chompa Hombre con cierre", "49.99"]
);
productos.set(
    '15', ["Chompa Hombre Blanca", "77.94"]
);
productos.set(
    '16', ["Pantalón Cargo Hombre", "59.90"]
);
productos.set(
    '17', ["Pantalón Hombre", "88"]
);
productos.set(
    '18', ["Pantalón Hombre Negro", "59.94"]
);
productos.set(
    '19', ["Polo Corto Tie Dye Mujer", "24.95",]
);
productos.set(
    '20', ["Polo Manga Corta Mujer Sybilla", "49.90"]
);
productos.set(
    '21', ["Polo Manga Larga Mujer University Club", "23.99"]
);
productos.set(
    '22', ["Sweater Mujer Sybilla", "34.99"]
);
productos.set(
    '23', ["Chompa Mujer Basement", "39.96"]
);
productos.set(
    '24', ["Sweater Mujer", "29.99"]
);
productos.set(
    '25', ["Jean Skinny Mujer Sybilla", "49.90"]
);
productos.set(
    '26', ["Jean High Mujer Sybilla", "49.90"]
);
productos.set(
    '27', ["Pantalón Mujer Stefano Cocci", "49.90"]
);
productos.set(
    '28', ["Polo Algodón Niña Yamp", "17.94"]
);
productos.set(
    '29', ["Polo Algodón Niña Yamp", "8.94"]
);
productos.set(
    '30', ["Polo Algodón Niña Frozen", "23.99"]
);
productos.set(
    '31', ["Polerón Sherpa Eleven", "75.90"]
);
productos.set(
    '32', ["Cardigan Miley", "55.93"]
);
productos.set(
    '33', ["Chompa Night Niña", "51.96"]
);
productos.set(
    '34', ["Pantalón Algodón Orgánico Niña", "64.95"]
);
productos.set(
    '35', ["Jean Skinny Algodón Niña", "49.95"]
);
productos.set(
    '36', ["Legging Polly Algodón Niña", "49.95"]
);
productos.set(
    '37', ["Reloj ROYAL LONDON", "209.80"]
);
productos.set(
    '38', ["Reloj digitales SkECHERS", "119"]
);
productos.set(
    '39', ["Reloj ROYAL LONDON", "209.80"]
);
productos.set(
    '40', ["Top Básico Mujer Sybilla", "9.03"]
);
productos.set(
    '41', ["Polerón Crop Mujer Sybilla", "29.94"]
);
productos.set(
    '42', ["Sweater Mujer Sybilla", "19.90"]
);
productos.set(
    '43', ["Polo Manga Corta Hombre", "17.90"]
);
productos.set(
    '44', ["Polo Manga Corta Hombre Bearcliff", "17.94"]
);
productos.set(
    '45', ["Polo Manga Larga Hombre Doo Australia", "34.93"]
);
productos.set(
    '46', ["Chompa Niña Eleven", "31.96"]
);
productos.set(
    '47', ["Polera Niña Eleven", "35.94"]
);
productos.set(
    '48', ["Chompa Viscosa Niña", "31.96"]
);
function agregarCarrito(id) {
    var nombreProducto = productos.get(id)[0];
    var precioProducto = productos.get(id)[1];
    var cantidadActual = 1;
    if (localStorage.length > 0) {
        if (localStorage.getItem(id) != null) {
            cantidadActual += parseInt(localStorage.getItem(id).split(',')[2], 10);
        }
    }
    localStorage.setItem(id, [nombreProducto, precioProducto, cantidadActual]);
    llenarHTMLCarrito();
}
function removerCarrito(id) {
    localStorage.removeItem(id);
    llenarHTMLCarrito();
}
function disminuirCantidad(id) {
    var nombreProducto = productos.get(id)[0];
    var precioProducto = productos.get(id)[1];
    var cantidad = localStorage.getItem(id).split(',')[2];
    if (cantidad > 1) {
        cantidad -= 1;
        localStorage.setItem(id, [nombreProducto, precioProducto, cantidad]);
        llenarHTMLCarrito();
    }else{
        removerCarrito(id);
    }
}
function llenarHTMLCarrito() {
    var bodyCarrito = document.getElementById('bodyCarrito');
    var html = "";
    for (let i = 0; i < localStorage.length; i++) {
        const id = localStorage.key(i);
        const nombreProducto = localStorage.getItem(id).split(',')[0]
        const precioProducto = localStorage.getItem(id).split(',')[1]
        const cantidad = localStorage.getItem(id).split(',')[2];
        html += '<tr><td>' + nombreProducto + '</td><td>S/' +
            precioProducto + '.00</td><td>' + cantidad + '</td><td>' +
            '<div class="btn-group" role="group" aria-label="Basic mixed styles example">' +
            '<button type="button" class="btn btn-success" onclick="agregarCarrito(\'' + id + '\')">' +
            '<i class="fas fa-plus"></i></button>' +
            '<button type="button" class="btn btn-warning" onclick="disminuirCantidad(\'' + id + '\')">' +
            '<i class="fas fa-minus"></i></button>' +
            '<button ' +
            'class="btn btn-danger dflex-inline" onclick="removerCarrito(\'' + id + '\')">' +
            '<i class="fas fa-times"></i>' +
            '</button>' +
            '</div></td><tr>';
    }
    bodyCarrito.innerHTML = html;
    var suma = calcularTotal();
    const costoTotalCarrito = document.getElementById('costoTotalCarrito');
    costoTotalCarrito.innerText = 'Total: S/' + suma;
}
function calcularTotal() {
    var suma = 0;
    for (let i = 0; i < localStorage.length; i++) {
        const id = localStorage.key(i);
        const precioProducto = localStorage.getItem(id).split(',')[1]
        const precioFloat = parseFloat(precioProducto);
        const cantidad = localStorage.getItem(id).split(',')[2]
        suma += precioFloat * cantidad;
    }
    return suma;
}
function calcularCantidadTotal() {
    var total = 0;
    for (let i = 0; i < localStorage.length; i++) {
        const id = localStorage.key(i);
        const cantidad = localStorage.getItem(id).split(',')[2]
        total += parseInt(cantidad);
    }
    return total;
}
function nuevaCompra() {
    localStorage.clear();
    document.getElementById('nombresApellidos').value = "";
    document.getElementById('email').value = "";
    llenarHTMLCarrito();
}

function llenarModalCompraFinal() {
    const nombreApellidoModal = document.getElementById('nombreApellidoModal')
    const emailModal = document.getElementById('emailModal');
    const nombresApellidos = document.getElementById('nombresApellidos').value;
    const email = document.getElementById('email').value;
    nombreApellidoModal.innerText = 'Nombres y apellidos: ' + nombresApellidos;
    emailModal.innerText = 'Email: ' + email;
    var suma = calcularTotal();
    const costoTotalModalFinal = document.getElementById('costoTotalModalFinal');
    costoTotalModalFinal.innerText = 'Total compra: S/' + suma;
}

function llenarModalCarrito() {
    var suma = calcularTotal();
    var total = calcularCantidadTotal();
    const costoTotal = document.getElementById('costoTotalModal');
    const cantidadTotalModal = document.getElementById('cantidadTotalModal');
    costoTotal.innerText = 'Costo total: S/' + suma ;
    cantidadTotalModal.innerText = 'Cantidad de productos: ' + total;
}