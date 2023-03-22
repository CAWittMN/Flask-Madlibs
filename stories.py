"""Madlibs Stories."""


class Story:
    """Madlibs story.

    To  make a story, pass a list of prompts, and the text
    of the template.

        >>> s = Story(["noun", "verb"],
        ...     "I love to {verb} a good {noun}.")

    To generate text from a story, pass in a dictionary-like thing
    of {prompt: answer, promp:answer):

        >>> ans = {"verb": "eat", "noun": "mango"}
        >>> s.generate(ans)
        'I love to eat a good mango.'
    """

    def __init__(self, id, title, words, text):
        """Create story with words and template text."""
        self.id = id
        self.title = title
        self.prompts = words
        self.template = text
        self.add_to_stories()

    def generate(self, answers):
        """Substitute answers into text."""

        text = self.template

        for (key, val) in answers.items():
            text = text.replace("{" + key + "}", val)

        return text
    def add_to_stories(self):
        stories.append(self)


# Here's a story to get you started
stories = []


story1 = Story("large", "The Large Thing",
    ["place", "noun", "verb", "adjective", "plural_noun"],
    """Once upon a time in a long-ago {place}, there lived a
       large {adjective} {noun}. It loved to {verb} {plural_noun}."""
)

story2 = Story("delivery", "The Delivery",
    ["noun", "verb", "adjective", "verb", "adjective", "adjective"], 
    """I ordered some {noun}, and it arrived before I could {verb}. 
       I was so {adjective} with the delivery, I {verb} a {adjective} review. 
       The delivery guy was also super {adjective}."""
)

story3 = Story('nonsense', "All Words",
    ['verb', 'adjective', 'noun', 'verb', 'plural_noun', 'adjective', 'noun'],
    """Yesterday I {verb} a {adjective} {noun}. 
       Then I {verb} lots of {plural_noun} like a {adjective} {noun}."""
)

story_ids = {s.id: s for s in stories}
