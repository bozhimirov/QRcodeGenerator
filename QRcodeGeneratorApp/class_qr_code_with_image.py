# class_qr_code_with_image.py

import os
import time

from PIL import Image
from PIL.Image import Resampling
from io import BytesIO
import qrcode
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.colormasks import RadialGradiantColorMask, SolidFillColorMask
from pathlib import Path
from constants import STYLES, HEX_COLORS, LOGO_PATHS, SIZES
from helpers import resize_logo
from validators import validate_hex, validate_style, hex_to_rgb, validate_size


class QRCodeGenerator:
    def __init__(self, style: str, link: str, size: str, cc: str, ec: str, bc: str, logo=None):
        """Initialize the QR code generator."""
        Path("./generated_qrcodes").mkdir(exist_ok=True)
        self.logo = logo
        self.style = STYLES[style] if validate_style(style, STYLES) else STYLES['default']
        self.size = SIZES[size] if validate_size(size, SIZES) else SIZES['big']
        self.link = link if link else ''
        self.cc = hex_to_rgb(cc) if validate_hex(cc) else hex_to_rgb(HEX_COLORS['none']['cc'])
        self.ec = hex_to_rgb(ec) if validate_hex(ec) else hex_to_rgb(HEX_COLORS['none']['ec'])
        self.bc = hex_to_rgb(bc) if validate_hex(bc) else hex_to_rgb(HEX_COLORS['none']['bc'])
        self.start_time = time.time()
        self.qr = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_Q, box_size=6, border=1, version=3)
        self.end_time = time.time()
        self.qr_image = None
        print(f'self.qr {self.end_time - self.start_time}')

    def add_data(self):
        start_time = time.time()
        self.qr.add_data(self.link)
        self.qr.make(fit=True)
        end_time = time.time()
        print(f'add_data {end_time - start_time}')

    # def add_style(self):
    #     self.qr.make_image(module_drawer=self.style)

    def make_image(self):
        """Create a styled QR code image."""
        start_time = time.time()
        color_mask = RadialGradiantColorMask(back_color=self.bc, center_color=self.cc, edge_color=self.ec)
        # Generate the base QR code image
        self.qr_image = self.qr.make_image(
            color_mask=color_mask,
            image_factory=StyledPilImage,
            module_drawer=self.style,
        )
        end_time1 = time.time()
        print(type(self.qr_image))
        print(f'MAKE DATA {end_time1 - start_time}')
        self.qr_image = self.qr_image.resize((440, 440))
        end_time2 = time.time()
        print(f'resize img {end_time2 - end_time1}')

    # def add_color_mask(self):
    #     self.qr_image = self.qr.make_image(color_mask=RadialGradiantColorMask(back_color=self.bc,
    #                                                                           center_color=self.cc,
    #                                                                           edge_color=self.ec))

    # Load and embed the logo if available
    def add_logo(self):
        start_time = time.time()
        logo_image = None
        if self.logo in LOGO_PATHS.keys():
            logo_path = os.path.join(os.getcwd(), self.logo)  # Adjust path if necessary
            print(f"Resolved logo path: {logo_path}")
            if os.path.exists(logo_path):
                print("Logo file found, embedding in QR code.")
                logo_image = Image.open(logo_path)

                if logo_image.mode != 'RGBA':
                    logo_image = logo_image.convert('RGBA')
        else:
            logo_path = self.logo
            logo_image = Image.open(logo_path)

            if logo_image.mode != 'RGBA':
                logo_image = logo_image.convert('RGBA')

        # Resize the logo
        basewidth = self.size
        wpercent = (basewidth / float(logo_image.size[0]))
        # print(wpercent)
        hsize = int((float(logo_image.size[1]) * float(wpercent)))
        # print(hsize)
        logo_image = logo_image.resize((basewidth, hsize), Resampling.LANCZOS)

        qr_width, qr_height = self.qr_image.size
        logo_width, logo_height = logo_image.size
        logo_position = (
            (qr_width - logo_width) // 2,
            (qr_height - logo_height) // 2
        )

        mask = logo_image.split()[3] if logo_image.mode == 'RGBA' else None
        self.qr_image.paste(logo_image, logo_position, mask=mask)
        end_time2 = time.time()
        print(f'add logo {end_time2 - start_time}')
