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
    replaced = re.sub(r"(?:https?:\/\/)?(?:www\.|mobile\.|touch\.|mbasic\.)", '', data, flags=re.IGNORECASE)
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
