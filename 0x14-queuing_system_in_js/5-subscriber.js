/*
create a redis client:

  - On connect, it should log the message Redis client connected to the server
  - On error, it should log the message Redis client not connected to the server: ERROR MESSAGE
  - It should subscribe to the channel holberton school channel
  - When it receives message on the channel holberton school channel, it should log the message to the console
  - When the message is KILL_SERVER, it should unsubscribe and quit

In a file named 5-publisher.js, create a redis client:

  - On connect, it should log the message Redis client connected to the server
  - On error, it should log the message Redis client not connected to the server: ERROR MESSAGE
  - Write a function named publishMessage:
    - It will take two arguments: message (string), and time (integer - in ms)
    - After time millisecond:
      - The function should log to the console About to send MESSAGE
      - The function should publish to the channel holberton school channel, the message passed in argument after the time passed in arguments
  - At the end of the file, call:

publishMessage("Holberton Student #1 starts course", 100);
publishMessage("Holberton Student #2 starts course", 200);
publishMessage("KILL_SERVER", 300);
publishMessage("Holberton Student #3 starts course", 400);
*/

import redis from 'redis';

const client = redis.createClient();

client.on('connect', () => {
  console.log('Redis client connected to the server');
});

client.on('error', (error) => {
  console.log(`Redis client not connected to the server: ${error}`);
});

client.subscribe('holberton school channel');

const channel = 'holberton school channel';

client.on('message', (channel, message) => {
  if (message === 'KILL_SERVER') {
    client.unsubscribe(channel);
    client.quit();
  } else {
    console.log(message);
  }
});

const publishMessage = (message, time) => {
  setTimeout(() => {
    console.log(`About to send ${message}`);
    client.publish('holberton school channel', message);
  }, time);
};

publishMessage('Holberton Student #1 starts course', 100);
publishMessage('Holberton Student #2 starts course', 200);
publishMessage('KILL_SERVER', 300);
publishMessage('Holberton Student #3 starts course', 400);
