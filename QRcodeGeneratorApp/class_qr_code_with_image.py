import os

from PIL import Image
from PIL.Image import Resampling
import qrcode
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.colormasks import RadialGradiantColorMask
from constants import STYLES, HEX_COLORS, LOGO_PATHS, SIZES
from helpers import hex_to_rgb, convert_logo, calculate_logo_position
from validators import validate_hex, validate_style, validate_size


class QRCodeGenerator:
    def __init__(self, style: str, link: str, size: str, cc: str, ec: str, bc: str, logo=None):
        """Initialize the QR code generator."""
        self.logo = logo
        self.style = STYLES[style] if validate_style(style, STYLES) else STYLES['default']
        self.size = SIZES[size] if validate_size(size, SIZES) else SIZES['big']
        self.link = link if link else ''
        self.cc = hex_to_rgb(cc) if validate_hex(cc) else hex_to_rgb(HEX_COLORS['none']['cc'])
        self.ec = hex_to_rgb(ec) if validate_hex(ec) else hex_to_rgb(HEX_COLORS['none']['ec'])
        self.bc = hex_to_rgb(bc) if validate_hex(bc) else hex_to_rgb(HEX_COLORS['none']['bc'])
        # Generate the base QR code image
        self.qr = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_Q, box_size=6, border=1, version=3)
        self.color_mask = self._make_color_mask()
        self.qr_image = None

    def _make_color_mask(self):
        return RadialGradiantColorMask(back_color=self.bc, center_color=self.cc, edge_color=self.ec)

    def _resize_image(self, new_size=(440, 440)):
        return self.qr_image.resize(new_size)

    def add_data(self):
        """Add data to QR code image."""
        self.qr.add_data(self.link)
        self.qr.make(fit=True)

    def make_image(self):
        """Create a styled QR code image."""
        self.qr_image = self.qr.make_image(
            color_mask=self.color_mask,
            image_factory=StyledPilImage,
            module_drawer=self.style,
        )
        self.qr_image = self._resize_image()

    def _logo_resize(self, logo_image: Image) -> Image:
        """Resize the logo"""
        # TODO diff logo ratio w vs h
        base_width = self.size
        width_percent = (base_width / float(logo_image.size[0]))
        hsize = int((float(logo_image.size[1]) * float(width_percent)))
        return logo_image.resize((base_width, hsize), Resampling.LANCZOS)

    def _get_logo(self) -> Image:
        """Get the logo if any"""
        if self.logo in LOGO_PATHS.keys():
            logo_path = os.path.join(os.getcwd(), self.logo)
            if os.path.exists(logo_path):
                logo_image = Image.open(logo_path)
                return convert_logo(logo_image)

        else:
            logo_path = self.logo
            logo_image = Image.open(logo_path)
            return convert_logo(logo_image)

    def add_logo(self):
        """Load and embed a logo if available"""
        logo_image = self._logo_resize(self._get_logo() if self._get_logo() else None)
        if logo_image:
            logo_position = calculate_logo_position(self.qr_image, logo_image)
            mask = logo_image.split()[3] if logo_image.mode == 'RGBA' else None
            self.qr_image.paste(im=logo_image, box=logo_position, mask=mask)


