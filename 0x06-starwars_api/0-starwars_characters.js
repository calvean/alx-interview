#!/usr/bin/node

const request = require('request');

function getCharacters (movieId) {
  const url = `https://swapi.dev/api/films/${movieId}/`;

  request(url, (error, response, body) => {
    if (error) {
      console.error('Error:', error);
    } else if (response.statusCode !== 200) {
      console.error('Status:', response.statusCode);
    } else {
      const film = JSON.parse(body);
      console.log(`Characters in "${film.title}":`);

      film.characters.forEach((characterUrl) => {
        request(characterUrl, (error, response, body) => {
          if (error) {
            console.error('Error:', error);
          } else if (response.statusCode !== 200) {
            console.error('Status:', response.statusCode);
          } else {
            const character = JSON.parse(body);
            console.log(character.name);
          }
        });
      });
    }
  });
}

// Usage example: Get characters from "Return of the Jedi" (Movie ID: 3)
getCharacters(3);
