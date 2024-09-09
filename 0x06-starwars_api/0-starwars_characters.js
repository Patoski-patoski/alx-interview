#!/usr/bin/node
/**
 * Write a script that prints all characters of a Star Wars movie:
 * - The first positional argument passed is the Movie ID - example: 3 = “Return of the Jedi”
 * - Display one character name per line in the same order as the “characters” list in the /films/ endpoint
 * - You must use the Star wars API
 * - You must use the request module
 */

const request = require('request');

const getRequest = (url) => {
  return new Promise((resolve, reject) => {
    request(url, (error, response, body) => {
      if (error) {
        reject(error);
      } else {
        resolve(JSON.parse(body));
      }
    });
  });
};

const movieId = process.argv[2];
if (!movieId) {
  console.error('Usage: 0-starwars_characters.js <movie_id>');
  process.exit(1);
}
const url = `https://swapi.dev/api/films/${movieId}/`;

getRequest(url)
  .then((film) => Promise.all(film.characters.map(getRequest)))
  .then((characters) => {
    characters.forEach((character) => {
      console.log(character.name);
    });
  })
  .catch((error) => {
    console.error(error);
  });
