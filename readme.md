# Flask Request-Response Application

This project is a simple Flask web application demonstrating various routes that respond to user inputs. The application features routes for greetings, favorite animals, desserts, mad libs, multiplication, repeating words, and a dice game.

## Features
- Homepage with a greeting.
- Favorite animal and dessert responses.
- Mad Libs functionality.
- Simple multiplication operation.
- Word repetition based on user input.
- Dice game with random outcomes.

## Setup Instructions

1. **Clone the repository**:
   ```bash
   git clone https://github.com/mrochelle23/Flask-Request-Response.git
   cd Flask-Request-Response
   ```

2. **Install Flask**:
   ```bash
   pip install Flask
   ```

3. **Run the application**:
   ```bash
   python app.py
   ```

4. **Run tests**:
   Make sure you have `pytest` installed:
   ```bash
   pip install pytest
   ```
   Then run:
   ```bash
   pytest
   ```

## Endpoints
- `GET /`: Homepage greeting
- `GET /Hello`: "Hello World!"
- `GET /animal/<users_animal>`: Responds with a message about the user's favorite animal.
- `GET /dessert/<users_dessert>`: Responds with a message about the user's favorite dessert.
- `GET /madlibs/<adjective>/<noun>`: Displays a mad lib story.
- `GET /multiply/<number1>/<number2>`: Multiplies two numbers.
- `GET /sayntimes/<word>/<n>`: Repeats a word `n` times.
- `GET /dicegame`: Simulates rolling a dice.

## Credits
This project is created by Mikhai Rochelle as part of a Flask exercise.
