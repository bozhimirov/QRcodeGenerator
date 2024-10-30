from PIL.Image import Image
import re


# -- convert hex color to rgb color --
def hex_to_rgb(color: str) -> tuple[int, int, int]:
    """
    This function convert a hex color string to an RGB tuple.

    Parameters:
        color (str): The hex color string (e.g., '#FFFFFF' or '#FFF').

    Return:
        tuple[int, int, int]: A tuple containing the RGB values.

    Raises:
        ValueError: If the color format is invalid.
    """

    if not isinstance(color, str):
        raise ValueError("Color must be a string.")

    value = color.lstrip('#')
    if len(value) == 3:
        value = ''.join([(x+x) for x in value])
    if len(value) == 6:
        return tuple(int(value[i:i + 2], 16) for i in range(0, 6, 2))
    raise ValueError("Invalid hex color format.")


# -- if the data provided is recognized as website link, it is formatted to be shorter--
def shorten_link(data: str) -> str:
    """
    This function make the length of the data shorter, if is recognized as a website link.
    If facebook link is recognized, it is shortened additionally

    Parameters:
        data (str): The data provided.

    Return:
        str: Return the data with the same or shorter length.
    """
    replaced = re.sub(r"(?:https?://)?(?:www\.|mobile\.|touch\.|mbasic\.)?(/$)?", '', data, flags=re.IGNORECASE)
    return reformat_facebook_link(replaced)


# -- if the provided data is recognized as facebook link, it is formatted to be shorter, using only the id of the page--
def reformat_facebook_link(data: str) -> str:
    """
    This function shorten facebook link for optimization, if it is recognizes as facebook link.

    Parameters:
        data (str): The data provided.

    Return:
        str: Return the data with the same or shorter length.
    """
    fb = re.search(r"^facebook|fb\.com", data, re.IGNORECASE)
    if fb:
        id_search = re.compile(r"\d{5,}")
        match_result = id_search.search(data)
        if match_result:
            return f'fb.com/{match_result.group()}'
    return data


# -- convert logo image into RGBA mode if needed--
def convert_logo(logo_image: Image) -> Image:
    """
    This function converts logo image into RGBA mode if needed.

    Parameters:
        logo_image (Image): The logo image.

    Return:
        Image: Return the logo image in RGBA mode.
    """
    return logo_image.convert('RGBA') if logo_image.mode != 'RGBA' else logo_image


# -- calculate logo position according to image size--
def calculate_logo_position(image: Image, logo: Image) -> tuple[int, int]:
    """
    This function calculate the position to center the logo on the QR code image.

    Parameters:
        image (Image): The QR code image.
        logo (Image): The logo image to be positioned.

    Return:
        tuple[int, int]: The (x, y) coordinates for placing the logo.
    """
    qr_width, qr_height = image.size
    logo_width, logo_height = logo.size
    return (
        (qr_width - logo_width) // 2,
        (qr_height - logo_height) // 2
    )
