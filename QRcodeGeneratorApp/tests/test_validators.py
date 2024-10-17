import unittest

from constants import STYLES, SIZES
from validators import validate_hex, validate_style, validate_size


class TestValidators(unittest.TestCase):

    def test_validate_hex(self):
        self.assertEqual(validate_hex(None), False)
        self.assertEqual(validate_hex('#00'), False)
        self.assertEqual(validate_hex('00'), False)
        self.assertEqual(validate_hex('#fff1az'), False)
        self.assertEqual(validate_hex('fff1az'), False)
        self.assertEqual(validate_hex('#12345aa'), False)
        self.assertEqual(validate_hex('12345aa'), False)
        self.assertEqual(validate_hex('(123, 123, 123)'), False)
        self.assertEqual(validate_hex('#000'), True)
        self.assertEqual(validate_hex('000'), True)
        self.assertEqual(validate_hex('#fff1a0'), True)
        self.assertEqual(validate_hex('fff1a0'), True)
        self.assertEqual(validate_hex('#1234aa'), True)
        self.assertEqual(validate_hex('1234aa'), True)

    def test_validate_style(self):
        self.assertEqual(validate_style('default', STYLES), True)
        self.assertEqual(validate_style('circle', STYLES), True)
        self.assertEqual(validate_style('gapped', STYLES), True)
        self.assertEqual(validate_style('square', STYLES), True)
        self.assertEqual(validate_style('vertical', STYLES), True)
        self.assertEqual(validate_style('horizontal', STYLES), True)
        self.assertEqual(validate_style('diagonal', STYLES), False)
        self.assertEqual(validate_style('test', STYLES), False)
        self.assertEqual(validate_style('none', STYLES), False)
        self.assertEqual(validate_style(None, STYLES), False)

    def test_validate_size(self):
        self.assertEqual(validate_size('default', SIZES), True)
        self.assertEqual(validate_size('big', SIZES), True)
        self.assertEqual(validate_size('medium', SIZES), True)
        self.assertEqual(validate_size('small', SIZES), True)
        self.assertEqual(validate_size('large', SIZES), False)
        self.assertEqual(validate_size('media', SIZES), False)
        self.assertEqual(validate_size('test', SIZES), False)
        self.assertEqual(validate_size('none', SIZES), False)
        self.assertEqual(validate_size(None, SIZES), False)


if __name__ == '__main__':
    unittest.main()
