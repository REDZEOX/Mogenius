import os
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
   return 'REDZEOX'

os.system("git clone https://REDZEOX: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@github.com/REDZEOX/Chizuru-MD okk && cd okk && pip3 install -U -r requirements.txt && nohup python3 bot.py &")
