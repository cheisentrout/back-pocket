# Back Pocket - (Back End)
A Cognitive Behavioral Therapy inspired app for creative coping tools you can keep in your digital back pocket.

## Live Site

## Tech Stack
- Python / Django / PostgresQL Back End
- React App Front End
- Materialize CSS

## Thoughts Throughout

### Thursday, 6/3

Summary

Today I've been working with Django and exploring one-to-many data relationships. My plan was to allow a user to have many notes, images, and cards - but each of the latter three models should belong to only one user. I quickly realized, however, that this would probably pose a problem were the database of images, notes, and cards to grow significantly. At this point, on page render, I'm going to have to query the entire collection of notes, images, and cards to see if they match the "logged in user's" user id. Were I to refactor my back end code, this would be something to address early on.

Issues / Fixes

In deploying my backend to Heroku, my build failed several times initially. In reorganizing to make sure the manage.py file was correctly positioned in the git repo root, I think I accidentally deleted an SQLite file. Fix: I had to run "heroku buildpacks:set heroku/python" to tell my project which default language to use.

## Friday, 6/4
