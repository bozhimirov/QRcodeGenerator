# validators.py

import re


def validate_hex(hex_color):
    import re
    if hex_color is None:
        return False  # or raise an error

    _hex_string = re.compile(r'^#?([a-fA-F0-9]{3}|[a-fA-F0-9]{6})$')
    return bool(_hex_string.match(hex_color))


def hex_to_rgb(color):
    value = color.lstrip('#')
    lv = len(value)
    return tuple(int(value[i:i + lv // 3], 16) for i in range(0, lv, lv // 3))


def validate_rgb(rgb_color: str) -> bool:
    """Check if the RGB values are in the correct range."""
    return all(0 <= int(x) <= 255 for x in rgb_color.split(','))


def validate_style(style: str, styles: dict) -> bool:
    return style in styles.keys()


def validate_size(size: str, sizes: dict) -> bool:
    return size in sizes.keys()


def validate_name(name: str) -> str:
    if 0 < len(name) < 100:
        return name.replace(' ', '', -1).replace('.', '', -1)
    return ''


# def validate_url(string: str) -> bool:
#     import re
#     _url_string = re.compile(
#         r'(^https?://)?'  # http:// or https://
#         r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.+)'
#         r'([A-Z]{2,6}\.?|)'  # domain...
#         r'localhost|'  # localhost...
#         r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'  # ...or ip
#         r'(?::\d+)?'  # optional port
#         r'(?:/?|[/?]\S+)$', re.IGNORECASE)
#     # return url is not None and regex.search(url)
#     # _url_string = re.compile(r'^#?([a-fA-F0-9]{3}|[a-fA-F0-9]{6})$')
#     return bool(_url_string.match(string))
