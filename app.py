from flask import Flask, render_template

app = Flask(__name__)


@app.route('/test')
def test():
    return render_template('test.html')


@app.route('/passing')
@app.route('/passing/<name>')
def passing(name="frank"):
    name = name.capitalize()
    return render_template('passing.html', given_name=name)


@app.route('/test-fail')
def test_fail():
    return render_template('index-fail.html')


@app.route('/')
def index():  # put application's code here
    # return 'Hello World!'
    return render_template('index.html')


if __name__ == '__main__':
    app.run()
