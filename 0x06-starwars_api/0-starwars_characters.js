#!/usr/bin/node

const request = require('request');

// Get the movie ID from command line arguments
const movieID = process.argv[2];

// Define the URL for the Star Wars API films endpoint
const apiUrl = `https://swapi.dev/api/films/${movieID}/`;

// Make a GET request to the API
request(apiUrl, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
  } else if (response.statusCode !== 200) {
    console.error('Unexpected status code:', response.statusCode);
  } else {
    // Parse the JSON response
    const filmData = JSON.parse(body);

    // Extract the characters array from the response
    const characters = filmData.characters;

    // Print each character name
    characters.forEach(characterUrl => {
      // Make a GET request to the character URL
      request(characterUrl, (error, response, body) => {
        if (error) {
          console.error('Error:', error);
        } else if (response.statusCode !== 200) {
          console.error('Unexpected status code:', response.statusCode);
        } else {
          // Parse the JSON response
          const characterData = JSON.parse(body);
          console.log(characterData.name);
        }
      });
    });
  }
});

