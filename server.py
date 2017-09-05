"""Greeting Flask app."""

from random import choice

from flask import Flask, request

# "__name__" is a special Python variable for the name of the current module
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza',
    'oh-so-not-meh', 'brilliant', 'ducky', 'coolio', 'incredible',
    'wonderful', 'smashing', 'lovely']

MEANNESS = ['scum', 'a scoundrel', 'a fleabag', 'a bronicorn', 'smelly']


@app.route('/')
def start_here():
    """Home page."""

    return "<!doctype html><html>Hi! This is the home page.<br><a href=/hello>Click Here</a></html>"


@app.route('/hello')
def say_hello():
    """Say hello and prompt for user's name."""

    return """
    <!doctype html>
    <html>
      <head>
        <title>Hi There!</title>
      </head>
      <body>
        <h1>Hi There!</h1>
        <form action="/greet">
          What's your name? <input type="text" name="person"><br>
          What compliment would make you happy? <br>
          <input type="radio" name="compliment" value="awesome">awesome
          <input type="radio" name="compliment" value="ridiculous">ridiculous
          <input type="radio" name="compliment" value="squishy">squishy<br>
          <input type="submit" value="Make me feel better about myself"><br><br>
        </form>
        <form action= "/diss">
               Do you instead feel the need to be insulted today?<br>
        Waz ur name? <input type="text" name="person"><br>
        <input type="submit" value="Insult Me Pls">
        </form>
      </body>
    </html>
    """


@app.route('/greet')
def greet_person():
    """Get user by name."""

    player = request.args.get("person")

    #compliment = choice(AWESOMENESS)
    compliment = request.args.get("compliment")

    return """
    <!doctype html>
    <html>
      <head>
        <title>A Compliment</title>
      </head>
      <body>
        Hi, {player}! I think you're {compliment}!
      </body>
    </html>
    """.format(player=player, compliment=compliment)

@app.route('/diss')
def diss_person():
  """Greets person rudely"""

  player = request.args.get("person")

  meanthing = choice(MEANNESS)

  return """
  <!doctype html>
  <html>
    <head>
      <title>A RUDE GREETING!!!!!</title>
    </head>
    <body>
      HAI {player}! You're {meanthing}!
    </body>
  </html>
  """.format(player=player, meanthing=meanthing)


if __name__ == '__main__':
    # debug=True gives us error messages in the browser and also "reloads"
    # our web app if we change the code.
    app.run(debug=True)
