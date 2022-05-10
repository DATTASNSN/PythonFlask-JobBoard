# -*- coding: UTF-8 -*-
"""
hello_flask: First Python-Flask webapp
"""
from flask import Flask  # From module flask import class Flask
from flask import render_template
app = Flask(__name__)    # Construct an instance of Flask class for our webapp

@app.route('/')   # URL '/' to be handled by main() route handler
@app.route('/jobs')


def main():
  """Say hello"""
  return render_template('index.html')

def jobs():
  return render_template('index.html')


if __name__ == '__main__':  # Script executed directly?
  app.run(debug=True) #  # Launch built-in web server and run this Flask webapp