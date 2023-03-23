import Currency from "./3-currency.js";

const dollar = new Currency('$', 'Dollars');
console.log(dollar.displayFullCurrency());

const pesos = new Currency('$$', 'Pesos');
console.log(pesos.displayFullCurrency());
