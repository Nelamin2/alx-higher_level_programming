#!/usr/bin/node
const request = require('request');

const actorId = '18';
const url = process.argv[2];

request.get(url, (error, response, body) => {
  if (error) {
    console.log(error);
    return;
  }

  let totalMovies = 0;
  const movieData = JSON.parse(body);
  if (response.statusCode === 200) {
    movieData.results.forEach(film => {
      if (film.characters.includes(`https://swapi-api.alx-tools.com/api/people/${actorId}/`)) {
        totalMovies++;
      }
    });
  }
  console.log(totalMovies);
});
