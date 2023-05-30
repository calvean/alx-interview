#!/usr/bin/node

const request = require('request');
const filmId = process.argv[2];
const url = `https://swapi-api.hbtn.io/api/films/${filmId}`;

request(url, async (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }

  const characters = JSON.parse(body).characters;
  const characterSet = new Set();

  for (const characterUrl of characters) {
    try {
      const characterData = await fetchCharacterData(characterUrl);
      const characterName = characterData.name;

      if (!characterSet.has(characterName)) {
        console.log(characterName);
        characterSet.add(characterName);
      }
    } catch (error) {
      console.error(error);
    }
  }
});

function fetchCharacterData (url) {
  return new Promise((resolve, reject) => {
    request(url, (error, response, body) => {
      if (error) {
        reject(error);
      } else if (response.statusCode !== 200) {
        reject(new Error(`Request failed with status code ${response.statusCode}`));
      } else {
        resolve(JSON.parse(body));
      }
    });
  });
}
