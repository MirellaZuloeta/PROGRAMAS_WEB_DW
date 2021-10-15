/*         console.log(window)
        console.log(document)


        let texto = "mirellafdghfdh"

        const hablar = (texto) => speechSynthesis.speak(new SpeechSynthesisUtterance(texto));

        hablar(texto) */

console.log(window.document);
console.log(document);
console.log(document.head);
console.log(document.body);
console.log(document.documentElement);
console.log(document.doctype);
console.log(document.characterSet);
console.log(document.title);
console.log(document.links);
console.log(document.images);
console.log(document.forms);
console.log(document.styleSheets);
console.log(document.scripts);

setTimeout(() => {
  console.log(document.getSelection().toString());
}, 3000);
