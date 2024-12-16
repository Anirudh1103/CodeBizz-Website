from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/members')
def members():
    return render_template('members.html')

@app.route('/events')
def events():
    return render_template('events.html')

@app.route('/blogs')
def blogs():
    return render_template('blogs.html')
if __name__ == "__main__":
    app.run(debug=True)