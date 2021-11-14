from flask import Flask
from threading import Thread

app = Flask('')

@app.route('/')
def home():
    return "<p>I did your mom in reeno just to watch you cry I did oyur m,om in xbox live!</p><p> I thlammed my penith in the car door, you slammed your penis in the car door, EeeEeeEeeEeee</p>"

def run():
  app.run(host='0.0.0.0',port=8080)

def keep_alive():
  t = Thread(target=run)
  t.start()