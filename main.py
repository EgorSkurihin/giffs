from flask import Flask, request, render_template

from giphy import get_gif_url

app = Flask(__name__)

@app.route("/")
def index():
    tag = request.args.get('tag', '')
    gif_url = get_gif_url(tag)
    return render_template('index.html', gif_url=gif_url)

#if __name__ == '__main__':
#    app.run(debuf=False, host='0.0.0.0')
