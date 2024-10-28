
from flask import Flask, jsonify, request, render_template
from io import BytesIO
import base64
from class_qr_code_with_image import QRCodeGenerator
from constants import LOGO_PATHS
from helpers import shorten_link

app = Flask(__name__)

# Define your logo upload folder here
app.config['LOGOS'] = 'static/logos'  # Ensure this directory exists

# Define index page
INDEX = "index.html"


@app.route('/', methods=['POST', 'GET'])
def manage():
    if request.method == 'POST':
        logo_path = None

        # Retrieve form data
        logo = request.form.get('logo', 'pomarina')  # Default to 'pomarina'
        link = request.form.get('link')
        style = request.form.get('style')
        size = request.form.get('size')
        cc = request.form.get('cc')
        ec = request.form.get('ec')
        bc = request.form.get('bc')

        link = shorten_link(link)

        # Handle custom logo upload
        if logo == 'custom' and 'logoFile' in request.files:
            logo_file = request.files['logoFile']
            if logo_file and logo_file.filename:
                logo_path = logo_file
        else:
            logo_path = LOGO_PATHS.get(logo, LOGO_PATHS['pomarina'])

        # Initialize the QR code generator
        qr_generator = QRCodeGenerator(
            logo=logo_path,
            style=style,
            size=size,
            link=link,
            cc=cc,
            ec=ec,
            bc=bc
        )

        # Generate QR code image
        if link:
            qr_generator.add_data()
        qr_generator.make_image()

        if logo != 'none':
            qr_generator.add_logo()

        # Convert image to base64 for embedding in HTML
        img_io = BytesIO()
        qr_generator.qr_image.save(img_io, 'PNG')
        img_io.seek(0)
        img_base64 = base64.b64encode(img_io.getvalue()).decode('utf-8')

        return jsonify({'qr_code_image': img_base64})
    return render_template(INDEX)


if __name__ == '__main__':
    app.run()
