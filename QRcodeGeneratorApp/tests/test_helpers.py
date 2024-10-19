import unittest

import PIL

from helpers import shorten_link, reformat_facebook_link, convert_logo, calculate_logo_position
from test_qr_code_generator.validators import hex_to_rgb


class TestHelpers(unittest.TestCase):

    def setUp(self):
        self.image = PIL.Image.new('RGBA', size=(440, 440))
        self.image1 = PIL.Image.new('RGB', size=(50, 50))
        self.image2 = PIL.Image.new('CMYK', size=(150, 150))
        self.image3 = PIL.Image.new('LAB', size=(250, 250))

    def test_hex_to_rgb(self):
        with self.assertRaises(Exception):
            hex_to_rgb('#00')
        with self.assertRaises(Exception):
            hex_to_rgb('#fff1az')
        with self.assertRaises(Exception):
            hex_to_rgb('fff1az')
        with self.assertRaises(Exception):
            hex_to_rgb('#12345aa')
        self.assertEqual(hex_to_rgb('#12345a'), (18, 52, 90))
        with self.assertRaises(Exception):
            hex_to_rgb('12345aa')
        self.assertEqual(hex_to_rgb('12345a'), (18, 52, 90))
        with self.assertRaises(Exception):
            hex_to_rgb('(123, 123, 123)')
        self.assertEqual(hex_to_rgb('#000'), (0, 0, 0))
        self.assertEqual(hex_to_rgb('f00'), (15, 0, 0))
        self.assertEqual(hex_to_rgb('#fff1a0'), (255, 241, 160))
        self.assertEqual(hex_to_rgb('fff1a0'), (255, 241, 160))
        self.assertEqual(hex_to_rgb('#1234aa'), (18, 52, 170))
        self.assertEqual(hex_to_rgb('1234aa'), (18, 52, 170))

    def test_shorten_link(self):
        self.assertEqual(shorten_link('http://127.0.0.1:5000/'), '127.0.0.1:5000')
        self.assertEqual(shorten_link('https://127.0.0.1:5000/'), '127.0.0.1:5000')
        self.assertEqual(shorten_link('www.mobile.instagram.com/scouts.kreslivorel/'),
                         'instagram.com/scouts.kreslivorel')
        self.assertEqual(shorten_link('www.instagram.com/scouts.kreslivorel'),
                         'instagram.com/scouts.kreslivorel')
        self.assertEqual(shorten_link('touch.mobile.instagram.com/scouts.kreslivorel'),
                         'instagram.com/scouts.kreslivorel')
        self.assertEqual(shorten_link('mobile.instagram.com/scouts.kreslivorel/'),
                         'instagram.com/scouts.kreslivorel')
        self.assertEqual(shorten_link('mbasic.instagram.com/scouts.kreslivorel/'),
                         'instagram.com/scouts.kreslivorel')
        self.assertEqual(shorten_link('https://www.mobile.touch.mbasic.instagram.com/scouts.kreslivorel'),
                         'instagram.com/scouts.kreslivorel')

    def test_reformat_facebook_link(self):
        self.assertEqual(reformat_facebook_link(
            'facebook.com/people/%D0%A1%D0%BA%D0%B0%D1%83%D1%82%D1%81%D0%BA%D0%B8-%D0%BA%D0%BB%D1%83%D0%B1-'
            '%D0%9A%D1%80%D0%B5%D1%81%D0%BB%D0%B8%D0%B2-%D0%BE%D1%80%D0%B5%D0%BB-%D0%A8%D1%83%D0%BC%D0%B5%D0%BD/'
            '100087327551813'),
            'fb.com/100087327551813')
        self.assertEqual(reformat_facebook_link('facebook.com/Скаутски-клуб-Креслив-орел-Шумен/100087327551813'),
                         'fb.com/100087327551813')
        self.assertEqual(reformat_facebook_link('fb.com/Скаутски-клуб-Креслив-орел-Шумен/100087327551813'),
                         'fb.com/100087327551813')
        self.assertEqual(reformat_facebook_link('fb.com/Scout-club-Kresliv-orel/100087327551813'),
                         'fb.com/100087327551813')
        self.assertEqual(reformat_facebook_link('facebook.com/100087327551813'),
                         'fb.com/100087327551813')
        self.assertEqual(reformat_facebook_link('facebook.com/people/other-data/100087327551813'),
                         'fb.com/100087327551813')
        self.assertNotEqual(reformat_facebook_link('link/some-data/1234566786534'),
                            'fb.com/1234566786534')
        self.assertNotEqual(reformat_facebook_link('none'),
                            'fb.com/none')
        self.assertNotEqual(reformat_facebook_link('127.0.0.1:5000'),
                            'fb.com/127.0.0.1:5000')

    def test_convert_logo(self):
        self.assertEqual(convert_logo(self.image).mode, 'RGBA')
        self.assertEqual(convert_logo(self.image1).mode, 'RGBA')
        self.assertEqual(convert_logo(self.image2).mode, 'RGBA')
        self.assertNotEqual(convert_logo(self.image2).mode, 'CMYK')
        self.assertEqual(convert_logo(self.image3).mode, 'RGBA')

    def test_calculate_logo_position(self):
        self.assertEqual(calculate_logo_position(self.image, self.image1), (195, 195))
        self.assertNotEqual(calculate_logo_position(self.image, self.image1), 195)
        self.assertEqual(calculate_logo_position(self.image, self.image2), (145, 145))
        self.assertEqual(calculate_logo_position(self.image, self.image3), (95, 95))
        self.assertNotEqual(calculate_logo_position(self.image, self.image3), (195, 195))


if __name__ == '__main__':
    unittest.main()
