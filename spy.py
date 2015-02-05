from nic import NicChile
from flask import Flask
app = Flask(__name__)

b = NicChile()
print b.trabajar()

@app.route('/')
def hello_world():

    return 'Hello World!'

if __name__ == '__main__':
    app.run()


