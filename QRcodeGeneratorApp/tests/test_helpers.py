import unittest
from PIL import Image
from helpers import (
    shorten_link,
    reformat_facebook_link,
    convert_logo,
    calculate_logo_position,
    hex_to_rgb,
)


class TestHelpers(unittest.TestCase):

    def setUp(self):
        # Test images in various modes for conversion and positioning tests
        self.image = Image.new('RGBA', (440, 440))
        self.logo_small = Image.new('RGB', (50, 50))
        self.logo_medium = Image.new('CMYK', (150, 150))
        self.logo_large = Image.new('LAB', (250, 250))

    def test_hex_to_rgb(self):
        # Valid cases
        self.assertEqual(hex_to_rgb('#12345a'), (18, 52, 90))
        self.assertEqual(hex_to_rgb('12345a'), (18, 52, 90))
        self.assertEqual(hex_to_rgb('#000'), (0, 0, 0))
        self.assertEqual(hex_to_rgb('f00'), (255, 0, 0))
        self.assertEqual(hex_to_rgb('fff1a0'), (255, 241, 160))
        self.assertEqual(hex_to_rgb('#fff1a0'), (255, 241, 160))
        self.assertEqual(hex_to_rgb('#1234aa'), (18, 52, 170))
        self.assertEqual(hex_to_rgb('1234aa'), (18, 52, 170))

        # Invalid cases
        invalid_hex_cases = ['#00', '#fff1az', 'fff1az', '#12345aa', '12345aa', '(123, 123, 123)']
        for case in invalid_hex_cases:
            with self.assertRaises(ValueError):
                hex_to_rgb(case)

    def test_shorten_link(self):
        # Testing with and without prefixes
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
        # Cases expected to be reformatted
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

        # Cases expected to remain unchanged
        self.assertNotEqual(reformat_facebook_link('link/some-data/1234566786534'),
                            'fb.com/1234566786534')
        self.assertNotEqual(reformat_facebook_link('none'),
                            'fb.com/none')
        self.assertNotEqual(reformat_facebook_link('127.0.0.1:5000'),
                            'fb.com/127.0.0.1:5000')

    def test_convert_logo(self):
        # Ensure images are converted to RGBA as expected
        for img in [self.image, self.logo_small, self.logo_medium, self.logo_large]:
            self.assertEqual(convert_logo(img).mode, 'RGBA')

        # Ensure images are not converted to CMYK as expected
        self.assertNotEqual(convert_logo(self.logo_small).mode, 'CMYK')

    def test_calculate_logo_position(self):
        # Test centered positioning
        self.assertEqual(calculate_logo_position(self.image, self.logo_small), (195, 195))
        self.assertEqual(calculate_logo_position(self.image, self.logo_medium), (145, 145))
        self.assertEqual(calculate_logo_position(self.image, self.logo_large), (95, 95))

        # Test with imaginary values

        self.assertNotEqual(calculate_logo_position(self.image, self.logo_small), 195)
        self.assertNotEqual(calculate_logo_position(self.image, self.logo_large), (195, 195))


if __name__ == '__main__':
    unittest.main()
