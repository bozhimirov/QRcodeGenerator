from flask import Flask, jsonify, request, render_template
from io import BytesIO
import base64
import logging
from class_qr_code_with_image import QRCodeGenerator
from constants import LOGO_PATHS
from helpers import shorten_link


def create_app():
    app = Flask(__name__)

    # Define your logo upload folder here
    app.config['LOGOS'] = 'static/logos'  # Ensure this directory exists

    # Define index page
    INDEX = "index.html"

    # Configure logging
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(levelname)s - %(message)s')

    @app.route('/', methods=['POST', 'GET'])
    def manage():
        if request.method == 'POST':
            try:
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
                logging.info(f"Generating QR code with data:"
                             f" logo: {logo}, "
                             f" link: {link}, "
                             f" style: {style}, "
                             f" size: {size}, "
                             f" cc: {cc}, "
                             f" ec: {ec}, "
                             f" bc: {bc}, "
                             f" logo_path: {logo_path} ")
                # Initialize the QR code generator
                logging.info(f"Generating QR code.")
                qr_generator = QRCodeGenerator(
                    logo=logo_path,
                    style=style,
                    size=size,
                    link=link,
                    cc=cc,
                    ec=ec,
                    bc=bc
                )

                logging.info(f"QR code generated successfully.")
                # Generate QR code image
                if link:
                    logging.info(f"Adding data to QR code.")
                    qr_generator.add_data()
                    logging.info(f"Data added successfully.")

                logging.info(f"Making image for QR code.")
                qr_generator.make_image()
                logging.info(f"Image made successfully.")

                if logo != 'none':
                    logging.info(f"Adding logo to QR code image.")
                    qr_generator.add_logo()
                    logging.info(f"Logo added successfully.")

                # Convert image to base64 for embedding in HTML

                logging.info(f"Converting QR code image to base64.")
                img_io = BytesIO()
                qr_generator.qr_image.save(img_io, 'PNG')
                img_io.seek(0)
                img_base64 = base64.b64encode(img_io.getvalue()).decode('utf-8')
                logging.info(f"Image successfully converted to base64.")

                return jsonify({'qr_code_image': img_base64})
            except Exception as e:
                logging.error(f"Error generating QR code: {e}")
                return "An error occurred while generating the QR code. Please try again.", 500
        return render_template(INDEX)

    return app


if __name__ == '__main__':
    app = create_app()
    app.run()
