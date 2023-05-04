import requests
import json
import datetime
import random
import os
from app import db
from app.main import bp
from app.models import Poem, Poet

from flask import render_template

OPEN_AI_TOKEN = os.getenv("OPEN_AI_TOKEN")

@bp.route("/")
def get_poem():
    poet = get_random_poet()

    ###Get poem from ChatGPT
    content = write_poem(poet)
    poem = content['choices'][0]['message']['content']
    date = datetime.datetime.now()
    ###Add poem to database
    poem_entry = Poem(
        created=date.timestamp(),
        poet=poet,
        poem=poem,
        total_tokens=content['usage']['total_tokens']
    )
    db.session.add(poem_entry)
    db.session.commit()

    poem_lines = [l.strip() for l in poem.split("\n") if l]

    return render_template("index.html", poem_lines=poem_lines, poet=poet, date=date)


def write_poem(poet):
    poem_prompt = f"Write a haiku about a beautiful neighborhood called Oak Terrace Preserve in the style of {poet}"

    url = 'https://api.openai.com/v1/chat/completions'
    headers = {"Content-Type": "application/json",
               "Authorization": f"Bearer {OPEN_AI_TOKEN}"}
    data = {"model": "gpt-3.5-turbo",
            "messages": [{"role": "system", "content": "You are a creative poet"},
                         {"role": "user", "content": poem_prompt}],
            "temperature": 1.3,
            'max_tokens': 60}

    r = requests.post(url=url,
                      data=json.dumps(data),
                      headers=headers)

    return r.json()

def get_random_poet():
    poet_entries = db.session.execute(db.select(Poet.poet)).scalars()
    poets = [p for p in poet_entries]
    return random.choice(poets)
