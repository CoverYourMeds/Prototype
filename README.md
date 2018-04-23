# CoverYourMeds
Medication Management

View a hosted version at http://coveryourmeds-coveryourmeds.a.csh.rit.edu/

## Features

A medication tracker and reminder. This is primarily a UI mockup and does not have every feature fully functional. The appearance of them is shown and is able to to interact with.

## Usage

Account | Password
--------|---------
`user@gmail.com` | `password`
`caretaker@gmail.com` | `password`

## Development

### Grab development dependencies
```
pip3 install -r requirements.txt
```

Assets require [yarn](https://yarnpkg.com/lang/en/docs/install/)

### Grab UI dependencies
```
yarn install
npm install -g gulp
gulp
```

### Used Packages
ORM: [flask_sqlalchemy](http://flask-sqlalchemy.pocoo.org)
