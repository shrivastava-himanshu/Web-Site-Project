from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template("index.html")

@app.route('/demo.html')
def demo():
    return render_template("demo.html")

@app.route('/single.html')
def singleblog():
    return render_template("single.html")

@app.route('/commontest')
def common():
    return render_template("common.html")

@app.route('/test')
def index_common():
    return render_template("index - Copy.html")

if __name__ == '__main__':
    app.run()
