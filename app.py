from flask import Flask, render_template, request,send_file, abort
from werkzeug.utils import secure_filename
from services.segmentation import segment
from jinja2 import TemplateNotFound
import os

app = Flask(__name__, template_folder='templates')


@app.route('/')
def upload_files():
    try:
        return render_template('index.html')
    except TemplateNotFound:
        abort(404)


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

app.run(host='0.0.0.0',port=8080, debug=False)