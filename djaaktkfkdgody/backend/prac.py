from flask import Flask
app = Flask(__name__)

@app.route('/helloo')
def helloo():
    return 'helloo'

@app.route('/helloo/<name>')
def helloo_name(name):
    return f'helloo {name}'

app.run(host='0.0.0.0', port=5000, debug=True)
