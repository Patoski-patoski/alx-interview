#!/usr/bin/node
/**
 * Write a script that prints all characters of a Star Wars movie:
 * - The first positional argument passed is the Movie ID - example: 3 = “Return of the Jedi”
 * - Display one character name per line in the same order as the “characters” list in the /films/ endpoint
 * - You must use the Star wars API
 * - You must use the request module
 */

const request = require('request');

const movieId = process.argv[2];
const api = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

function getCharacterName (url) {
  return new Promise((resolve, reject) => {
    request(url, (error, response, body) => {
      if (error) {
        reject(error);
      }
      if (response.statusCode === 200) {
        const characterData = JSON.parse(body);
        const characterNames = characterData.name;
        resolve(characterNames);
      } else {
        reject(error);
      }
    });
  });
}

request(api, (error, response, body) => {
  if (error) {
    console.error('Error', error);
  }
  if (response.statusCode === 200) {
    const movieData = JSON.parse(body);
    const characters = movieData.characters;

    const characterPromises = characters.map(characterUrl => getCharacterName(characterUrl));

    Promise.all(characterPromises)
      .then((characterNames) => {
        characterNames.forEach((character) => {
          console.log(character);
        });
      })
      .catch(error => {
        console.error(`Failed to fetch character data: ${error}`);
      });
  } else {
    console.error('Failed to fetch movie data. Status code:', response.statusCode);
  }
});
