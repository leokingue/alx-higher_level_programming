#!/usr/bin/node
const language = ['C', 'Python', 'Javascript'];
for (let i = 0; i < language.length; ++i) {
  switch (i) {
    case 0:
      console.log(language[0] + ' is fun');
      break;
    case 1:
      console.log(language[1] + ' is cool');
      break;
    case 2:
      console.log(language[2] + ' is amazing');
      break;
    default:
      break;
  }
}
