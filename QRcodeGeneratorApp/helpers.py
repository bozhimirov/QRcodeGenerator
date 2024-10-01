# helpers.py


def resize_logo(image_path, max_size=(60, 60)):
    from PIL import Image
    """Resize the logo to fit within the QR code."""
    logo = Image.open(image_path)
    logo.thumbnail(max_size)  # Resize the logo to fit within the specified max_size
    return logo


def shorten_link(link):
    import re
    shorten = link.replace('https://www.', '').replace('https://', '').replace('http://', '').replace('www.', '')
    if 'facebook.com' in link:
        ll = re.compile(r"\d{5,}")
        matchResult = ll.search(link)
        if matchResult:
            print(matchResult)
            print(matchResult.group())
            return f'facebook.com/{matchResult.group()}'
    return shorten
