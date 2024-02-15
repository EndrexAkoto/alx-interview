#!/usr/bin/node

const request = require('request');

const movieID = process.argv[2];
const options = { json: true };
const url = `https://swapi-api.alx-tools.com/api/films/${movieID}`;

request(url, options, async (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }

  for (const character of body.characters) {
    await new Promise((resolve) => {
      request(character, options, (error, response, body) => {
        if (error) {
          console.error(error);
          resolve();
        }

        console.log(body.name);
        resolve();
      });
    });
  }
});
