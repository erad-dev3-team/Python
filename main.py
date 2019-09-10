from flask import Flask
app = Flask(__name__)

app.config['DEBUG'] = True


@app.route('/')
def hello_world():
    return 'Hello, World!22233444'

if __name__ == '__main__':
    app.run() 