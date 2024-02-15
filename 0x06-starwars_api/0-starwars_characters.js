#!/usr/bin/node
import request from "request";
import { promisify } from "util";
const movieId = process.argv[2];
if (!movieId || isNaN(movieId)) {
  console.error("Usage: ./0-starwars_characters.js <movie_id>");
  process.exit(1);
}
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;
const asyncRequest = promisify(request);

async function print_characters(urls) {
  for (const urlt of urls) {
    const val = await asyncRequest({ url: urlt, json: true });

    console.log(val.body.name);
  }
}

async function get_stuff() {
  const val = await asyncRequest({ url: url, json: true });
  if (val.statusCode === 200) {
    await print_characters(val.body.characters);
  }

  console.error("Invalid response:", val.statusCode);
  process.exit(1);
}
get_stuff();
