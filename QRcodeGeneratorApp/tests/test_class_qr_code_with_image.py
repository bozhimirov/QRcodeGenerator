import unittest
from PIL import Image

from qrcode.image.styles.colormasks import SolidFillColorMask, RadialGradiantColorMask

from QRcodeGenerator.QRcodeGeneratorApp.class_qr_code_with_image import QRCodeGenerator
from QRcodeGenerator.QRcodeGeneratorApp.constants import STYLES, SIZES, HEX_COLORS
from QRcodeGenerator.QRcodeGeneratorApp.helpers import hex_to_rgb


class TestQRCodeGenerator(unittest.TestCase):
    """Unit tests for the QRCodeGenerator class."""

    CONSTANTS = {
        'style': STYLES['circle'],
        'link': 'some data',
        'size': SIZES['default'],
        'cc': HEX_COLORS['instagram']['cc'],
        'ec': HEX_COLORS['instagram']['ec'],
        'bc': HEX_COLORS['instagram']['bc'],
        'logo': 'pomarina',
    }

    DEFAULT_LOGO_SIZE = 160

    def setUp(self):
        """Set up test fixtures for each test."""
        self.qr_code = QRCodeGenerator(
            style='circle',
            link=self.CONSTANTS['link'],
            size='default',
            cc=self.CONSTANTS['cc'],
            ec=self.CONSTANTS['ec'],
            bc=self.CONSTANTS['bc'],
            logo='pomarina'
        )
        self.qr_code_default = QRCodeGenerator(style='', link='', size='', cc='', ec='', bc='', logo='')
        self.qr_code_with_logo = QRCodeGenerator(style='', link=self.CONSTANTS['link'], size='', cc='', ec='', bc='',
                                                 logo='logo.png')
        self.image = Image.new('RGBA', size=(40, 40))
        self.logo_small = Image.new('RGBA', size=(40, 40))
        self.logo_wide = Image.new('RGBA', size=(140, 40))
        self.logo_tall = Image.new('RGBA', size=(40, 140))

    def test_initialization(self):
        """Test the initialization of the QRCodeGenerator."""
        self.assertEqual(type(self.qr_code.style), type(self.CONSTANTS['style']))
        self.assertIsInstance(self.qr_code.style, type(self.CONSTANTS['style']))

        self.assertNotEqual(self.qr_code.style, self.qr_code_default.style)
        self.assertEqual(self.qr_code.link, self.CONSTANTS['link'])
        self.assertNotEqual(self.qr_code.link, self.qr_code_default.link)
        self.assertEqual(self.qr_code.size, self.CONSTANTS['size'])
        self.assertNotEqual(self.qr_code.size, self.qr_code_default.size)
        self.assertEqual(self.qr_code.cc, hex_to_rgb(self.CONSTANTS['cc']))
        self.assertNotEqual(self.qr_code.cc, self.qr_code_default.cc)
        self.assertEqual(self.qr_code.ec, hex_to_rgb(self.CONSTANTS['ec']))
        self.assertNotEqual(self.qr_code.ec, self.qr_code_default.ec)
        self.assertEqual(self.qr_code.bc, hex_to_rgb(self.CONSTANTS['bc']))
        self.assertEqual(self.qr_code.logo, self.CONSTANTS['logo'])
        self.assertNotEqual(self.qr_code.logo, self.qr_code_default.logo)

    def test_make_color_mask(self):
        """Test the color mask creation."""

        # Test default instance for SolidFillColorMask
        default_mask = self.qr_code_default._make_color_mask()
        self.assertIsInstance(default_mask, SolidFillColorMask)
        self.assertEqual(default_mask.back_color, hex_to_rgb(self.CONSTANTS['bc']))
        self.assertEqual(default_mask.front_color, hex_to_rgb(HEX_COLORS['none']['cc']))
        self.assertEqual(default_mask.front_color, hex_to_rgb(HEX_COLORS['none']['ec']))
        self.assertNotEqual(type(self.qr_code_default._make_color_mask()), type(self.qr_code.color_mask))

        # Test styled instance for RadialGradiantColorMask
        styled_mask = self.qr_code._make_color_mask()
        self.assertIsInstance(styled_mask, RadialGradiantColorMask)
        self.assertEqual(type(styled_mask), type(self.qr_code.color_mask))
        self.assertNotEqual(type(styled_mask), type(self.qr_code_default.color_mask))
        self.assertEqual(styled_mask.back_color, hex_to_rgb(self.CONSTANTS['bc']))
        self.assertEqual(styled_mask.center_color, hex_to_rgb(self.CONSTANTS['cc']))
        self.assertEqual(styled_mask.edge_color, hex_to_rgb(self.CONSTANTS['ec']))

    def test_resize_image(self):
        """Test the image resizing functionality."""
        self.qr_code_default.qr_image = self.image
        resized_image = self.qr_code_default._resize_image()
        self.assertEqual(resized_image.size, (440, 440))
        self.assertNotEqual(resized_image.size, self.image.size)

    def test_logo_resize(self):
        """Test the logo resizing functionality."""

        resized_small_logo = self.qr_code_default._logo_resize(self.logo_small)
        self.assertEqual(resized_small_logo.size, (self.DEFAULT_LOGO_SIZE, self.DEFAULT_LOGO_SIZE))
        self.assertNotEqual(resized_small_logo.size, self.logo_small.size)

        resized_wide_logo = self.qr_code_default._logo_resize(self.logo_wide)
        self.assertEqual(resized_wide_logo.size, (self.DEFAULT_LOGO_SIZE, 45))
        self.assertNotEqual(resized_wide_logo.size, self.logo_wide.size)

        resized_tall_logo = self.qr_code_default._logo_resize(self.logo_tall)
        self.assertEqual(resized_tall_logo.size, (45, self.DEFAULT_LOGO_SIZE))
        self.assertNotEqual(resized_tall_logo.size, self.logo_tall.size)

    def test_add_data(self):
        """Test adding data to the QR code."""
        self.qr_code.add_data()
        self.qr_code_with_logo.add_data()
        self.qr_code_default.add_data()
        self.assertEqual(self.qr_code_with_logo.qr.data_cache, self.qr_code.qr.data_cache)
        self.assertNotEqual(self.qr_code_default.qr.data_cache, self.qr_code.qr.data_cache)
        self.assertNotEqual(self.qr_code_default.qr.data_cache, self.qr_code_with_logo.qr.data_cache)

    def test_make_image(self):
        """Test image generation for the QR code."""
        self.qr_code.make_image()
        self.qr_code_with_logo.make_image()
        self.qr_code_default.make_image()
        self.assertEqual(self.qr_code_with_logo.qr_image, self.qr_code_default.qr_image)
        self.assertNotEqual(self.qr_code_default.qr_image, self.qr_code.qr_image)
        self.assertNotEqual(self.qr_code.qr_image, self.qr_code_with_logo.qr_image)

    def test_get_logo(self):
        """Test handling of invalid logo paths."""
        invalid_qr_code = QRCodeGenerator(style='circle',
                                          link='some data',
                                          size='default',
                                          cc=self.CONSTANTS['cc'],
                                          ec=self.CONSTANTS['ec'],
                                          bc=self.CONSTANTS['bc'],
                                          logo='invalid_logo.png')
        logo_image = invalid_qr_code._get_logo()
        self.assertIsNone(logo_image)

    def test_color_validation(self):
        """Test that invalid colors are handled properly."""
        invalid_cc = 'invalid_color'
        qr_image = QRCodeGenerator(style='circle',
                                   link='some data',
                                   size='default',
                                   cc=invalid_cc,
                                   ec=self.CONSTANTS['ec'],
                                   bc=self.CONSTANTS['bc']
                                   )
        self.assertEqual(qr_image.cc, hex_to_rgb(HEX_COLORS['none']['cc']))

    def test_edge_case_empty_link(self):
        """Test behavior when an empty link is provided."""
        qr_code_empty_link = QRCodeGenerator(style='circle',
                                             link='',
                                             size='default',
                                             cc=self.CONSTANTS['cc'],
                                             ec=self.CONSTANTS['ec'],
                                             bc=self.CONSTANTS['bc']
                                             )

        qr_code_not_empty_link = QRCodeGenerator(style='circle',
                                                 link='non empty link',
                                                 size='default',
                                                 cc=self.CONSTANTS['cc'],
                                                 ec=self.CONSTANTS['ec'],
                                                 bc=self.CONSTANTS['bc']
                                                 )
        qr_code_empty_link.add_data()
        qr_code_not_empty_link.add_data()
        self.assertEqual(qr_code_empty_link.qr.data_list, [])
        self.assertNotEqual(qr_code_empty_link.qr.data_list, qr_code_not_empty_link.qr.data_list)

    def test_edge_case_large_logo(self):
        """Test behavior with a logo that is too large."""
        large_logo = Image.new('RGBA', size=(600, 600))
        resized_large_logo = self.qr_code._logo_resize(large_logo)
        self.assertEqual(resized_large_logo.size, (140, 140))


if __name__ == '__main__':
    unittest.main()
