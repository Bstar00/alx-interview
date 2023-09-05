#!/usr/bin/node

const request = require('request');

function fetchCharacterNames(characterUrls, index) {
  if (index === characterUrls.length) {
    return;
  }

  request(characterUrls[index], (error, response, body) => {
    if (error) {
      console.error(`Error fetching character: ${error}`);
    } else {
      try {
        const character = JSON.parse(body);
        console.log(`Character Name: ${character.name}`);
      } catch (parseError) {
        console.error(`Error parsing character data: ${parseError}`);
      }
    }

    fetchCharacterNames(characterUrls, index + 1);
  });
}

const filmId = process.argv[2];

if (!filmId) {
  console.error('Usage: node script.js <filmId>');
  process.exit(1);
}

const filmUrl = `https://swapi-api.hbtn.io/api/films/${filmId}`;

request(filmUrl, (error, response, body) => {
  if (error) {
    console.error(`Error fetching film: ${error}`);
  } else {
    try {
      const film = JSON.parse(body);
      const characterUrls = film.characters;
      fetchCharacterNames(characterUrls, 0);
    } catch (parseError) {
      console.error(`Error parsing film data: ${parseError}`);
    }
  }
});
