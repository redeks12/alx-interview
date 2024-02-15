#!/usr/bin/node
import request from "request";
import { promisify } from "util";
const url = `https://swapi-api.alx-tools.com/api/films/${process.argv[2]}`;
const asyncRequest = promisify(request);

async function print_characters(urls) {
  for (const urlt of urls) {
    const val = await asyncRequest({ url: urlt, json: true });
    console.log(val.body.name);
  }
}

async function get_stuff() {
  const val = await asyncRequest({ url: url, json: true });
  await print_characters(val.body.characters);
}
get_stuff();
