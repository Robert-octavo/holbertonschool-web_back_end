/*
Create a function named getItemById:

    It will take id as argument
    It will return the item from listProducts with the same id


    Create an express server listening on the port 1245.

*/
const express = require('express');
const redis = require('redis');
const { promisify } = require('util');

const app = express();
const client = redis.createClient();

const listProducts = [
  { id: 1, name: 'Suitcase 250', price: 50, stock: 4 },
  { id: 2, name: 'Suitcase 450', price: 100, stock: 10 },
  { id: 3, name: 'Suitcase 650', price: 350, stock: 2 },
  { id: 4, name: 'Suitcase 1050', price: 550, stock: 5 },
];

function getItemById (id) {
  return listProducts.find((item) => item.id === id);
}

const setAsync = promisify(client.set).bind(client);
const getAsync = promisify(client.get).bind(client);

const reserveStockById = (itemId, stock) => setAsync(`item.${itemId}`, stock);
const getCurrentReservedStockById = async (itemId) => getAsync(`item.${itemId}`);


app.get('/list_products', (req, res) => {
  res.json(listProducts);
});

app.get('/list_products/:id', async (req, res) => {
  res.json(getItemById(req.params.id));
});


app.listen(1245);
