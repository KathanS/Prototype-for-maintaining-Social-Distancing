from flask import Flask, render_template
from datetime import datetime

now = datetime.now()
current_time = now.strftime("%H:%M:%S")

app = Flask(__name__)

imgs = ["https://images.unsplash.com/photo-1604580824859-20d9665f58b5?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto"
          "=format&fit=crop&w=500&q=60",
          "https://images.unsplash.com/photo-1603999870974-2cd2258dac8a?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9"
          "&auto=format&fit=crop&w=500&q=60",
          "https://images.unsplash.com/photo-1604502130010-22a9eb4c77a8?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9"
          "&auto=format&fit=crop&w=500&q=60",
          "https://images.unsplash.com/photo-1604180540768-78abbc4ab189?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9"
          "&auto=format&fit=crop&w=500&q=60",
          "https://dochub.com/ybt2027/pqb0g5YRq7PyOj1VJ2nx67/bingimageoftheday-jpg?dt=szGjTQWxG5gJ-AU6mfRM","sample2.jpg"]
people = 10


@app.route('/')
def index():
    return render_template('index.html', people=people, imgs=imgs, current_time=current_time)


if __name__ == '__main__':

    app.run()