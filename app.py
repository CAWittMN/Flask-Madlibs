from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension
from stories import stories

app = Flask(__name__)
app.config["SECRET_KEY"] = "porkfloople"

debug = DebugToolbarExtension(app)

@app.route('/')
def story_select():
    """Select which story to add words to"""
    return render_template('story_select.html', stories=stories.values())

@app.route('/words')
def choose_words():
    """Choose the words to add to the story"""
    story_id = request.args['story_id']
    story = stories[story_id]
    prompts = story.prompts
    return render_template('words.html',
                           story_id=story_id,
                           title=story.title,
                           prompts=prompts)


