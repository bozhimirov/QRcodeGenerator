import unittest
from PIL import Image

from qrcode.image.styles.colormasks import SolidFillColorMask, RadialGradiantColorMask

from QRcodeGenerator.QRcodeGeneratorApp.class_qr_code_with_image import QRCodeGenerator
from QRcodeGenerator.QRcodeGeneratorApp.constants import STYLES, SIZES, HEX_COLORS
from QRcodeGenerator.QRcodeGeneratorApp.helpers import hex_to_rgb


class TestQRCodeGenerator(unittest.TestCase):
    CONSTANTS = {
        'style': STYLES['circle'],
        'link': 'some data',
        'size': SIZES['default'],
        'cc': HEX_COLORS['instagram']['cc'],
        'ec': HEX_COLORS['instagram']['ec'],
        'bc': HEX_COLORS['instagram']['bc'],
        'logo': 'pomarina',
    }

    def setUp(self):
        self.qr_code = QRCodeGenerator(style='circle', link=self.CONSTANTS['link'],
                                       size='default', cc=self.CONSTANTS['cc'], ec=self.CONSTANTS['ec'],
                                       bc=self.CONSTANTS['bc'], logo='pomarina')
        self.qr_code_def = QRCodeGenerator(style='', link='', size='', cc='', ec='', bc='', logo='')
        self.qr_code_1 = QRCodeGenerator(style='', link=self.CONSTANTS['link'], size='', cc='', ec='', bc='',
                                         logo='logo.png')
        self.image = Image.new('RGBA', size=(40, 40))
        self.logo = Image.new('RGBA', size=(40, 40))
        self.logo1 = Image.new('RGBA', size=(140, 40))
        self.logo2 = Image.new('RGBA', size=(40, 140))

    def test_init(self):
        self.assertEqual(type(self.qr_code.style), type(self.CONSTANTS['style']))

        self.assertNotEqual(self.qr_code.style, self.qr_code_def.style)
        self.assertEqual(self.qr_code.link, self.CONSTANTS['link'])
        self.assertNotEqual(self.qr_code.link, self.qr_code_def.link)
        self.assertEqual(self.qr_code.size, self.CONSTANTS['size'])
        self.assertNotEqual(self.qr_code.size, self.qr_code_def.size)
        self.assertEqual(self.qr_code.cc, hex_to_rgb(self.CONSTANTS['cc']))
        self.assertNotEqual(self.qr_code.cc, self.qr_code_def.cc)
        self.assertEqual(self.qr_code.ec, hex_to_rgb(self.CONSTANTS['ec']))
        self.assertNotEqual(self.qr_code.ec, self.qr_code_def.ec)
        self.assertEqual(self.qr_code.bc, hex_to_rgb(self.CONSTANTS['bc']))
        self.assertEqual(self.qr_code.logo, self.CONSTANTS['logo'])
        self.assertNotEqual(self.qr_code.logo, self.qr_code_def.logo)

    def test_make_color_mask(self):
        self.assertEqual(type(self.qr_code_def._make_color_mask()), SolidFillColorMask)
        self.assertEqual(type(self.qr_code_def._make_color_mask()), type(self.qr_code_def.color_mask))
        self.assertNotEqual(type(self.qr_code_def._make_color_mask()), type(self.qr_code.color_mask))
        self.assertEqual(self.qr_code_def._make_color_mask().back_color, hex_to_rgb(self.CONSTANTS['bc']))
        self.assertEqual(self.qr_code_def._make_color_mask().front_color, hex_to_rgb(HEX_COLORS['none']['cc']))
        self.assertEqual(self.qr_code_def._make_color_mask().front_color, hex_to_rgb(HEX_COLORS['none']['ec']))
        self.assertEqual(type(self.qr_code._make_color_mask()), RadialGradiantColorMask)
        self.assertEqual(type(self.qr_code._make_color_mask()), type(self.qr_code.color_mask))
        self.assertNotEqual(type(self.qr_code._make_color_mask()), type(self.qr_code_def.color_mask))
        self.assertEqual(self.qr_code._make_color_mask().back_color, hex_to_rgb(self.CONSTANTS['bc']))
        self.assertEqual(self.qr_code._make_color_mask().center_color, hex_to_rgb(self.CONSTANTS['cc']))
        self.assertEqual(self.qr_code._make_color_mask().edge_color, hex_to_rgb(self.CONSTANTS['ec']))

    def test_resize_image(self):
        self.qr_code_def.qr_image = self.image
        self.assertEqual(self.qr_code_def._resize_image().size, (440, 440))
        self.assertNotEqual(self.qr_code_def.size, self.image.size)

    def test_logo_resize(self):
        self.assertEqual(self.qr_code_def._logo_resize(self.logo).size, (160, 160))
        self.assertNotEqual(self.qr_code_def._logo_resize(self.logo).size, self.logo.size)
        self.assertEqual(self.qr_code_def._logo_resize(self.logo1).size, (160, 45))
        self.assertNotEqual(self.qr_code_def._logo_resize(self.logo1).size, self.logo1.size)
        self.assertEqual(self.qr_code_def._logo_resize(self.logo2).size, (45, 160))
        self.assertNotEqual(self.qr_code_def._logo_resize(self.logo2).size, self.logo2.size)


    def test_add_data(self):
        self.qr_code.add_data()
        self.qr_code_1.add_data()
        self.qr_code_def.add_data()
        self.assertEqual(self.qr_code_1.qr.data_cache, self.qr_code.qr.data_cache)
        self.assertNotEqual(self.qr_code_def.qr.data_cache, self.qr_code.qr.data_cache)
        self.assertNotEqual(self.qr_code_def.qr.data_cache, self.qr_code_1.qr.data_cache)

    def test_make_image(self):
        self.qr_code.make_image()
        self.qr_code_1.make_image()
        self.qr_code_def.make_image()
        self.assertEqual(self.qr_code_1.qr_image, self.qr_code_def.qr_image)
        self.assertNotEqual(self.qr_code_def.qr_image, self.qr_code.qr_image)
        self.assertNotEqual(self.qr_code.qr_image, self.qr_code_1.qr_image)

