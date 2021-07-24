import base64

import zxing
from flask import request, jsonify

from app import app

ALLOWED_EXTENSIONS = {'jpg', 'png'}


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/process/license', methods=['POST'])
def process_license():
    headers = request.headers
    auth = headers.get('API-key')
    if auth == app.secret_key:
        # check if the post request has the file part
        if 'file' not in request.files:
            return jsonify({'message': 'No file part in the request', 'status': 400})

        file = request.files['file']
        if file.filename == '':
            return jsonify({'message': 'No file selected for uploading', 'status': 400})

        if file and allowed_file(file.filename):
            filepath = 'input.png'
            file.save(filepath)

            reader = zxing.BarCodeReader()
            barcode = reader.decode(filepath).raw
            barcode_byte = barcode.encode('ascii')
            b64_byte = base64.b64encode(barcode_byte)
            b64_msg = b64_byte.decode('ascii')

            return jsonify({'barcode': b64_msg, 'status': 200})
        else:
            return jsonify({'message': 'Allowed file types are jpg and png', 'status': 400})
    else:
        return jsonify({'message': 'ERROR: Unauthorized', 'status': 400})


if __name__ == "__main__":
    # app.run(host="0.0.0.0", port=80)

    from waitress import serve
    serve(app, host='0.0.0.0', port=4170)
