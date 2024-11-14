#!/usr/bin/node
const request = require('request');
const API_URL = 'https://swapi-api.hbtn.io/api';

function fetch (url) {
  return new Promise((resolve, reject) => {
    request(url, (err, _, body) => {
      if (err) {
        return reject(err);
      }
      resolve(JSON.parse(body));
    });
  });
}

async function getFilmCharacters (filmId) {
  try {
    const film = await fetch(`${API_URL}/films/${filmId}/`);
    const characterPromises = film.characters.map(url => fetch(url));
    const characters = await Promise.all(characterPromises);
    characters.forEach(character => console.log(character.name));
  } catch (error) {
    console.error('Error:', error.message);
  }
}

// Run if film ID is provided as a command line argument
if (process.argv.length > 2) {
  const filmId = process.argv[2];
  getFilmCharacters(filmId);
}
