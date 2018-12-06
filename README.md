# Auto timeline from twitter

A barebones Django app, which can easily be deployed to Heroku.

This app gives the past 3 days data of unitedAIRLINES. The data is  collected from twitter using tweepy. the sentences containing dates are extracted from all data this extracted sentences are stored in a ua.csv file.  

## Deploying to Heroku

```sh
$ heroku create
$ git push heroku master

$ heroku run python manage.py migrate
$ heroku open
```
or

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://fast-mountain-77770.herokuapp.com/)
