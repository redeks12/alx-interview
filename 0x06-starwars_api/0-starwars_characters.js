#!/usr/bin/node
import fetch from "node-fetch";
const url = `https://swapi-api.alx-tools.com/api/films/${process.argv[2]}`;

async function print_characters(urls) {
  for (const urlt of urls) {
    const val = await fetch(urlt);
    const data = await val.json();
    console.log(data.name);
  }
}

async function get_stuff() {
  const val = await fetch(url);
  const data = await val.json();
  await print_characters(data.characters);
}
get_stuff();
