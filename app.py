from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension
from stories import Story

app = Flask(__name__)
app.config["SECRET_KEY"] = "porkfloople"

debug = DebugToolbarExtension(app)

@app.route('/')
def story_select():
    """Select which story to add words to"""
    return render_template('story_select.html', stories=stories.values())

@app.route('/words')
def add_words():
    """Choose the words to add to the story"""
    return render_template('words.html')

