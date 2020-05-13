from flask import Flask, render_template, request,send_file
from werkzeug.utils import secure_filename
from services.segmentation import segment
import os

app = Flask(__name__, static_folder='templates')


@app.route('/')
def upload_files():
    return render_template('upload.html')


@app.route('/uploader', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['file']
        f.filename = '0.tif'
        filename = f.filename
        f.save(os.path.join('resources', secure_filename(filename)))
        try:
            output_path = segment()
        except Exception as e:
            return {'error':str(e)},400

        return send_file(output_path, mimetype='image/gif')

app.run(port=5000, debug=True)