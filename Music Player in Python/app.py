from flask import Flask, render_template, request, url_for
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/uploads/'

# Ensure the upload folder exists
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/Dashboard', methods=["POST", "GET"])
def dashboard():
    if request.method == "POST":
        if 'path' in request.files:
            files = request.files.getlist('path')
            saved_files = []
            for file in files:
                if file.filename.endswith(".mp3"):
                    file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
                    os.makedirs(os.path.dirname(file_path), exist_ok=True)
                    file.save(file_path)
                    saved_files.append(file.filename)
            return render_template('Dashboard.html', files=saved_files)

if __name__ == '__main__':
    app.run(debug=True)
