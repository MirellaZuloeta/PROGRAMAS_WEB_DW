//CLASE: Default Params y Concatenación
function newFunction(name, age, country) {
  var name = name || "oscar";
  var age = age || 32;
  var country = country || "MX";
  console.log(name, age, country);
}

// es6
function newFunction2(name = "oscar", age = 32, country = "MX") {
  console.log(name, age, country);
}

newFunction2();
newFunction2("Ricardo", "23", "CO");

let hello = "Hello";
let world = "World";
let epicPhrase = hello + " " + world;
console.log(epicPhrase);

//es6
let epicPhrase2 = `${hello} ${world}`;
console.log(epicPhrase2);



//CLASE: LET y CONST, Multilínea, Spread Operator y Desestructuración

let lorem =
  "Qui consequatur. Commodi. Ipsum vel duis yet minima \n" +
  "otra frase epica que necesitamos.";

// es6: multilinea
let lorem2 = `otra frase epica que necesitamos
ahora es otra frase epica
`;

console.log(lorem);
console.log(lorem2);

let person = {
  name: "oscar",
  age: 32,
  country: "MX",
};

console.log(person.name, person.age);

//es6: desestructuracion
let { name } = person;
console.log(name);

//es6: unir arreglos, estructurar
let team1 = ["Oscar", "Julian", "Ricardo"];
let team2 = ["Valeria", "Yesica", "Camila"];

let education = ["David", ...team1, ...team2];

console.log(education);

{
  var globalVar = "Global Var";
}

{
  let globalLet = "Global Let";
  console.log(globalLet); //let es de scope interno
}

console.log(globalVar);

const a = "b";
a = "a"; //una constante no se le puede reasignar otro valor
console.log(a);




//CLASE: Arrow Functions, Promesas y Parámetros en objetos
let name = 'oscar';
let age = 32;

//es5
obj = { name: name, age: age };
//es6
obj2 = { name, age };
console.log(obj2);

const names = [
  { name: 'Oscar', age: 32 },
  { name: 'Yesica', age: 27 }
]

let listOfNames = names.map(function (item) {
  console.log(item.name);
})

let listOfNames2 = names.map(item => console.log(item.name));

const listOfNames3 = (name, age, country) => {
  ... 
}

const listOfNames4 = name => {
  ...
}

const square = num => num * num;

const helloPromise = () => {
  return new Promise((resolve, reject) => {
    if (false) {
      resolve('Hey!');
    } else {
      reject('Ups!!');
    }
  });
}

helloPromise()
  .then(response => console.log(response))
  .catch(error => console.log(error));




  
  //Clases, Módulos y Generadores

  class calculator {
  constructor() {
    this.valueA = 0;
    this.valueB = 0;
  }
  sum(valueA, valueB) {
    this.valueA = valueA;
    this.valueB = valueB;
    return this.valueA + this.valueB;
  }
}

const calc = new calculator();
console.log(calc.sum(2, 2));

import { hello } from './module';

hello();

function* helloWorld() {
  if (true) {
    yield 'Hello, ';
  }
  if (true) {
    yield 'World';
  }
};

const generatorHello = helloWorld();
console.log(generatorHello.next().value);
console.log(generatorHello.next().value);
console.log(generatorHello.next().value);



/**
 * Importaciones nombradas

Puedes importar uno o más objetos o valores utilizando el nombre que se le definió en el módulo y que se 
haya declarado con la palabra clave export. Ejemplo:
 */

// module.js
export const myExport = "hola"

// index.js
import { myExport } from "module.js"




/**Importación predeterminada (default)

Cuando el módulo tiene una exportación predeterminada (default) omitimos el uso 
de llaves al momento de importar. Ejemplo: */
// module.js
function myFunction() {...}

export default myFunction

// index.js
import myFunction from "module.js"

/**Para importar los dos tipos de exportaciones podemos separarlos por comas. Ejemplo: */
// module.js
export const myExport = "hola"
function myFunction() {}

export default myFunction

// index.js
import myFunction, { myExport }