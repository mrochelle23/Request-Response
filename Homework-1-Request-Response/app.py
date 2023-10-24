from flask import Flask

app = Flask(__name__)

@app.route('/')
def homepage():
    """Shows a greeting to the user."""
    return 'Are you there, world? It\'s me, Ducky!'

@app.route('/Hello')
def hellopage():
    """Shows a greeting to the user."""
    return 'Hello World!'

@app.route('/animal/<users_animal>')
def favorite_animal(users_animal):
    """Display a message to the user that changes based on their favorite animal."""
    return f'Wow, {users_animal} is my favorite animal, too!'

@app.route('/dessert/<users_dessert>')
def favorite_dessert(users_dessert):
    """Display a message to the user that changes based on their favorite dessert."""
    return f'How did you know I liked {users_dessert}?'

@app.route('/madlibs/<adjective>/<noun>')
def madlibs(adjective, noun):
    """Display a message to the user that changes based on their madlibs."""
    return f' Jacob started {noun} to the store and bought a {adjective} pair of pants'

@app.route('/multiply/<number1>/<number2>')
def multiply(number1, number2):
    """Display a message to the user that changes based on their numbers."""
    if number1.isdigit() and number2.isdigit():
        a = int(number1)
        b = int(number2)
        c = a * b
        return f'{number1} times {number2} is {c}'
    return f'Invalid inputs. Please try again by entering 2 numbers!'

@app.route('/sayntimes/<word>/<n>')
def sayntimes(word, n):
    """Display a message to the user that changes based on their word and number."""
    if n == "world":
        return f'Invalid input. Please try again by entering a word and a number!'
    return ('\n'.join([word] * int(n)))

@app.route('/dicegame')
def dicegame():
    """Display a message to the user that changes based on a random number and if it equals to 6."""
    import random
    number = random.randint(1, 6)
    if number == 6:
        return f'You rolled a 6. You won!'
    return f'You rolled a {number}. You lost!'
if __name__ == '__main__':
    app.run(debug=True)

# python3 -m pytest