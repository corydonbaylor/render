from flask import Flask, send_from_directory, jsonify

app = Flask(__name__, static_folder='../frontend/public')

@app.route('/api/hello')
def hello():
    return "Hello from Flask!"

@app.route('/api/about')
def about():
    return jsonify({
        "frontend": "Svelte",
        "backend": "Flask"
    })

@app.route('/')
@app.route('/<path:path>')
def serve(path='index.html'):
    return send_from_directory(app.static_folder, path)

if __name__ == '__main__':
    app.run(debug=True)
