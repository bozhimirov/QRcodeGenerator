import re
from typing import Dict


# -- validate if the color is in hex format (regex is used ) --
def validate_hex(hex_color: str) -> bool:
    """
    This function validate if the provided color is in hex format.

    Parameters:
        hex_color (str): the color to check.

    Return:
        bool: True if the color is a valid hex format, False otherwise.
    """
    if not hex_color:
        return False  # Handle None or empty string case

    # Compile the regex once for performance
    _hex_string = re.compile(r'^#?([a-fA-F0-9]{3}|[a-fA-F0-9]{6})$')
    return bool(_hex_string.match(hex_color))


# -- validate if the style is in predefined values --
def validate_style(style: str, styles: Dict[str, any]) -> bool:
    """
    This function validates if the style one of the predefined styles.

    Parameters:
        style (str): The style to check.
        styles (Dict[str, any]): A dictionary of valid styles.

    Return:
        bool: Return True if the style is valid, False otherwise.
    """
    return style in styles


# -- validate if the size is in predefined values --
def validate_size(size: str, sizes: Dict[str, any]) -> bool:
    """
    This function validates if the size is one of the predefined sizes.

    Parameters:
        size (str): The size to check.
        sizes (Dict[str, any]): A dictionary of valid sizes.

    Return:
        bool: Return True if the size is valid, False otherwise.
    """
    return size in sizes

