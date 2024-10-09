from PIL.Image import Image


# -- convert hex color to rgb color --
def hex_to_rgb(color: str) -> tuple:
    """
    This function convert hex color to rgb color.

    Parameters:
        color (str): the color that have to be converted.

    Return:
        tuple: Return tuple with rgb color data.
    """
    value = color.lstrip('#')
    len_value = len(value)
    return tuple(int(value[i:i + len_value // 3], 16) for i in range(0, len_value, len_value // 3))


# -- if the data provided is recognized as website link, it is formatted to be shorter--
def shorten_link(data: str) -> str:
    """
    This function make the length of the data shorter, if is recognized as a website link.
    If facebook link is recognized, it is shortened additionally

    Parameters:
        data (str): the data provided.

    Return:
        str: Return the data with the same or shorter length.
    """
    import re
    replaced = re.sub(r"(?:https?://)?(?:www\.|mobile\.|touch\.|mbasic\.)", '', data, flags=re.IGNORECASE)
    shorten = reformat_facebook_link(replaced)
    return shorten


# -- if the provided data is recognized as facebook link, it is formatted to be shorter, using only the id of the page--
def reformat_facebook_link(data: str) -> str:
    """
    This function shorten facebook link for optimization, if it is recognizes as facebook link.

    Parameters:
        data (str): the data provided.

    Return:
        str: Return the data with the same or shorter length.
    """
    import re
    fb = re.search(r"^facebook|fb\.com", data, re.IGNORECASE)
    if fb:
        id_search = re.compile(r"\d{5,}")
        matchResult = id_search.search(data)
        if matchResult:
            return f'fb.com/{matchResult.group()}'
    return data


# -- convert logo image into RGBA mode if needed--
def convert_logo(logo_image: Image) -> Image:
    """
    This function converts logo image into RGBA mode if needed.

    Parameters:
        logo_image (Image): logo image that may need to be converted

    Return:
        Image: Return the logo image in RGBA mode
    """
    if logo_image.mode != 'RGBA':
        return logo_image.convert('RGBA')
    return logo_image.convert('RGBA')


# -- calculate logo position according to image size--
def calculate_logo_position(image: Image, logo: Image) -> tuple:
    """
    This function calculate logo position according to image size.

    Parameters:
        image (Image): image where the logo will be centered
        logo (Image): logo image used for calculation

    Return:
        tuple: Return the position for the logo according to the size of the image as a tuple
    """
    qr_width, qr_height = image.size
    logo_width, logo_height = logo.size
    return (
        (qr_width - logo_width) // 2,
        (qr_height - logo_height) // 2
    )
