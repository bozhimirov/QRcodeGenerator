# -- validate if the color is in hex format (regex is used ) --
def validate_hex(hex_color: str) -> bool:
    """
    This function validates if the color is in hex format.

    Parameters:
        hex_color (str): the color that have to be checked.

    Return:
        bool: Return if the color is in hex format.
    """
    import re
    if hex_color is None:
        return False  # or raise an error

    _hex_string = re.compile(r'^#?([a-fA-F0-9]{3}|[a-fA-F0-9]{6})$')
    return bool(_hex_string.match(hex_color))


# -- validate if the style is in predefined values --
def validate_style(style: str, styles: dict) -> bool:
    """
    This function validates if the style is in the predefined values of a provided dictionary.

    Parameters:
        style (str): the style that have to be checked.
        styles (dict): the dictionary used for checking.

    Return:
        bool: Return if the style is in the predefined values of a provided dictionary.
    """
    return style in styles.keys()


# -- validate if the size is in predefined values --
def validate_size(size: str, sizes: dict) -> bool:
    """
    This function validates if the size is in the predefined values of a provided dictionary.

    Parameters:
        size (str): the size that have to be checked.
        sizes (dict): the dictionary used for checking.

    Return:
        bool: Return if the size is in the predefined values of a provided dictionary.
    """
    return size in sizes.keys()

