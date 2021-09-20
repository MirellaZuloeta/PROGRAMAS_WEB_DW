let productos = new Map();
productos.set(
    '1', ["Pinturas CPP", "100"]
);
productos.set(
    '2', ["Luminarias", "50"]
);
productos.set(
    '3', ["Tubos PAVCO", "30"]
);
productos.set(
    '4', ["Candado SUPER", "40"]
);
productos.set(
    '5', ["Taladros DWalt", "300"]
);
productos.set(
    '6', ["Destornillador", "20"]
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
    costoTotalCarrito.innerText = 'Total: S/' + suma + '.00';
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
    costoTotalModalFinal.innerText = 'Total compra: S/' + suma + '.00';
}

function llenarModalCarrito() {
    var suma = calcularTotal();
    var total = calcularCantidadTotal();
    const costoTotal = document.getElementById('costoTotalModal');
    const cantidadTotalModal = document.getElementById('cantidadTotalModal');
    costoTotal.innerText = 'Costo total: S/' + suma + '.00';
    cantidadTotalModal.innerText = 'Cantidad de productos: ' + total;
}