import unittest

from constants import STYLES, SIZES
from validators import validate_hex, validate_style, validate_size


class TestValidators(unittest.TestCase):

    def test_validate_hex_valid(self):
        # Valid 3- and 6-digit hex codes
        valid_hex_colors = ['#fff', '#FFFFFF', 'fff', 'ffffff', '#123abc', '123ABC']
        for color in valid_hex_colors:
            with self.subTest(color=color):
                self.assertTrue(validate_hex(color), f"Expected {color} to be valid.")

    def test_validate_hex_invalid(self):
        # Invalid hex formats and other types
        invalid_hex_colors = [
            '#ff', '#fffg', 'g12345', '(123, 123, 123)', '12345', 'rd', '', '#12345aa', None, '#fff1az'
        ]
        for color in invalid_hex_colors:
            with self.subTest(color=color):
                self.assertFalse(validate_hex(color), f"Expected {color} to be invalid.")

    def test_validate_style_valid(self):
        # Valid style keys from constants
        valid_styles = list(STYLES.keys())
        for style in valid_styles:
            with self.subTest(style=style):
                self.assertTrue(validate_style(style, STYLES), f"Expected {style} to be valid.")

    def test_validate_style_invalid(self):
        # Styles not in STYLES dictionary
        invalid_styles = ['unknown', '', None, 'roundedSquare', 'none']
        for style in invalid_styles:
            with self.subTest(style=style):
                self.assertFalse(validate_style(style, STYLES), f"Expected {style} to be invalid.")

    def test_validate_size_valid(self):
        # Valid sizes from constants
        valid_sizes = list(SIZES.keys())
        for size in valid_sizes:
            with self.subTest(size=size):
                self.assertTrue(validate_size(size, SIZES), f"Expected {size} to be valid.")

    def test_validate_size_invalid(self):
        # Sizes not in SIZES dictionary
        invalid_sizes = ['extra-large', '', None, 'huge', 'none', 'media']
        for size in invalid_sizes:
            with self.subTest(size=size):
                self.assertFalse(validate_size(size, SIZES), f"Expected {size} to be invalid.")


if __name__ == '__main__':
    unittest.main()
