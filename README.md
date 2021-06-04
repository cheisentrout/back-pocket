# Back Pocket - (Back End)
A Cognitive Behavioral Therapy inspired app for creative coping tools you can keep in your digital back pocket.

## Live Site

## Tech Stack
- Python / Django / PostgresQL Back End
- React App Front End
- Materialize CSS

## Thoughts Throughout

- Thursday, 6/3
Today I've been working with Django and exploring one-to-many data relationships. My plan was to allow a User to have many notes, images, and cards - but each of the latter three models should belong to only one User. I quickly realized, however, that this will probably pose a theoretical problem were the database of images, notes, and cards to grow significantly. At this point, on page render, I'm going to have to query the entire collection of notes, images, and cards to see if they match the "logged in user's" user id.
