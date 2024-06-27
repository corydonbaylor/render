from flask import Flask, send_from_directory

app = Flask(__name__, static_folder='../frontend/public')

@app.route('/api/hello')
def hello():
    return "Hello from Flask!"

@app.route('/')
def serve_frontend():
    return send_from_directory(app.static_folder, 'index.html')

@app.route('/<path:path>')
def serve_static(path):
    return send_from_directory(app.static_folder, path)

if __name__ == '__main__':
    app.run(debug=True)
