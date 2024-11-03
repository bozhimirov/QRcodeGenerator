import os
from PIL import Image
from PIL.Image import Resampling
import qrcode
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.colormasks import RadialGradiantColorMask, SolidFillColorMask, QRColorMask
from qrcode.main import GenericImage

from constants import STYLES, SIZES, HEX_COLORS, LOGO_PATHS
from helpers import hex_to_rgb, convert_logo, calculate_logo_position
from validators import validate_hex, validate_style, validate_size


class QRCodeGenerator:
    """
    A class representing a qr code generator.

    Attributes:
        logo (str): The logo shown at the center of the QR code image.
        style (StyledPilQRModuleDrawer): The type of style used when creating QR code image.
        size (str): The size of the logo at the center of the QR code image.
        link (str): The incorporated data/link into the QR code image.
        cc (str): The central color used for making gradient color of the QR code image.
        ec (str): The edge color used for making gradient color of the QR code image.
        bc (str): The back color used for making gradient color of the QR code image.
        qr (QRCode): Created QR code object.
        color_mask (QRColorMask): The color mask of the QR code image.
        qr_image (GenericImage): The final QR code image.
    """

    def __init__(self, style: str, link: str, size: str, cc: str, ec: str, bc: str, logo=None) -> None:
        """Initialize the QR code generator.

        Parameters:
            logo (str): The logo shown at the center of the QR code image.
            style (StyledPilQRModuleDrawer): The type of style used when creating QR code image.
            size (str): The size of the logo at the center of the QR code image.
            link (str): The incorporated data/link into the QR code image.
            cc (str): The central color used for making gradient color of the QR code image.
            ec (str): The edge color used for making gradient color of the QR code image.
            bc (str): The back color used for making gradient color of the QR code image.
        Return:
        None
        """
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

    def _make_color_mask(self) -> QRColorMask:
        """
        This internal function generates the color mask needed for QR code generator.

        Return:
        QRColorMask: Return the generated color mask using central, edge and back colors.
        """
        if self.cc == self.ec:
            return SolidFillColorMask(front_color=self.cc, back_color=self.bc)
        return RadialGradiantColorMask(back_color=self.bc, center_color=self.cc, edge_color=self.ec)

    def _resize_image(self, new_size=(440, 440)) -> GenericImage:
        """
        This internal function changes the size of the generated QR code image with fixed size(440px, 440px).

        Return:
        GenericImage: Returns QR code image with predefined width and height.
        """
        return self.qr_image.resize(new_size)

    def _logo_resize(self, logo_image: Image) -> Image:
        """
        This internal function resize the logo based on the size of the QR code image.

        Return:
        Image: Returns the resized logo.
        """
        if logo_image:
            base_width = self.size
            while logo_image.size[0] > base_width or logo_image.size[1] > base_width:
                logo_image = logo_image.resize((int(logo_image.size[0]*0.9), int(logo_image.size[1]*0.9)), Resampling.LANCZOS)
            if logo_image.size[0] >= logo_image.size[1]:
                width_percent = (base_width / float(logo_image.size[0]))
                h_size = int((float(logo_image.size[1]) * float(width_percent)))
                return logo_image.resize((base_width, h_size), Resampling.LANCZOS)
            height_percent = (base_width / float(logo_image.size[1]))
            w_size = int((float(logo_image.size[0]) * float(height_percent)))
            return logo_image.resize((w_size, base_width), Resampling.LANCZOS)
        return None

    def _get_logo(self) -> Image:
        """
        This internal function get the logo if any or uses predefined logos.
        Converts logo image into RGBA mode if needed.

        Return:
        Image: Image of the logo provided.
        """
        if self.logo in LOGO_PATHS.keys():
            logo_path = os.path.join(os.getcwd(), self.logo)
            if os.path.exists(logo_path):
                logo_image = Image.open(logo_path)
                return convert_logo(logo_image)
            else:
                return None
        else:
            logo_path = self.logo
            try:
                logo_image = Image.open(logo_path)
                return convert_logo(logo_image)
            except FileNotFoundError:
                return None

    def add_data(self) -> None:
        """
        This function adds data/link to the generated QR code object.

        Return:
        The function directly modify one of the class attributes - QR code object.
        """
        self.qr.add_data(self.link)
        self.qr.make(fit=True)

    def make_image(self) -> None:
        """
        This function creates a styled QR code image from the given QR code object using the generated color mask and
        provided style. The image is resized to predefined values.

        Return:
        The function directly modify the class attributes - QR code image.
        """
        self.qr_image = self.qr.make_image(
            color_mask=self.color_mask,
            image_factory=StyledPilImage,
            module_drawer=self.style,
        )
        self.qr_image = self._resize_image()

    def add_logo(self) -> None:
        """
        This function load and embed a logo into the QR code image if available

        Return:
        The function directly modify one of the class attributes - QR code image.
        """
        logo_image = self._logo_resize(self._get_logo() if self._get_logo() else None)
        if logo_image:
            logo_position = calculate_logo_position(self.qr_image, logo_image)
            mask = logo_image.split()[3] if logo_image.mode == 'RGBA' else None
            self.qr_image.paste(im=logo_image, box=logo_position, mask=mask)
