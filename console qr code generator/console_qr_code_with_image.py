import os

import qrcode
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.moduledrawers.pil import RoundedModuleDrawer, CircleModuleDrawer, GappedSquareModuleDrawer, \
    SquareModuleDrawer, VerticalBarsDrawer, HorizontalBarsDrawer
from qrcode.image.styles.colormasks import RadialGradiantColorMask
from pathlib import Path
from matplotlib import colors as clrs


def make_name(u_choice: str, u_name: str, u_style: str) -> str:
    if not u_style:
        u_style = 'd'
    if u_name:
        file_name = f'{u_choice}-{u_name}-{u_style}'
    else:
        file_name = f'{u_choice}-{u_style}'
    return file_name


def save_image(file_name: str, u_img: StyledPilImage) -> None:
    file_ext = '.png'
    uniq = 1
    Path("./generated_qrcodes").mkdir(exist_ok=True)
    path = './generated_qrcodes/%s%s' % (file_name, file_ext)
    while os.path.exists(path):
        path = './generated_qrcodes/%s_%d%s' % (file_name, uniq, file_ext)
        uniq += 1
    u_img.save(path)


def make_image(image_factory, module_drawer, color_mask, embeded_image_path):
    return qr.make_image(image_factory=image_factory,
                         module_drawer=module_drawer,
                         color_mask=color_mask,
                         embeded_image_path=embeded_image_path
                         ).convert('RGB')


def validate_rgb(rgb_color):
    condition = True
    for _ in [int(x) for x in rgb_color]:
        if not 0 <= _ <= 255:
            condition = False
    if condition:
        return True
    return False


def make_color(clr):
    user_input = input(f'Write the {clr} in RBG format separated with commas, or HEX format, or name of the color: ')
    try:
        r_g_b = tuple([int(x * 255) for x in clrs.to_rgb(clrs.cnames[user_input])])
        if not validate_rgb(r_g_b):
            return make_color(clr)
        return r_g_b

    except (KeyError, ValueError):
        try:
            user_input = user_input.replace('#', '', -1)
            r_g_b = tuple(int(user_input[i:i + 2], 16) for i in (0, 2, 4))
            if not validate_rgb(r_g_b):
                return make_color(clr)
            return r_g_b
        except ValueError:
            try:
                user_input = user_input.replace(' ', '')
                r_g_b = tuple([int(x) for x in user_input.split(',')])
                if not validate_rgb(r_g_b):
                    return make_color(clr)
                return r_g_b
            except ValueError:
                return make_color(clr)


def make_file_name():
    f_name = input("Enter file name: ")
    while not f_name:
        f_name = input('Enter file name: ')
    return f_name

user_continuation = True
while user_continuation:

    choice = input('Choose which logo you want to generate: fb(facebook) or ig(instagram) or n(none)?'
                   ' \nEnter your choice here: ') \
        .lower()
    while choice not in ['fb', 'ig', 'n', '']:
        choice = input('Choose which logo you want to generate: fb(facebook) or ig(instagram) or n(none)?'
                       '\nType fb or ig or n here: ') \
            .lower()
    color = input('Choose colors: cc(custom_colored) or nc(non_colored) or dc(default_colored)?'
                  ' \nEnter your choice here: ') \
        .lower()
    while color not in ['cc', 'nc', 'dc', '']:
        color = input('Choose colors: cc(custom_colored) or nc(non_colored) or dc(default_colored)?'
                      '\nType cc or nc or dc here: ') \
            .lower()

    data = input('Enter anything to generate QR code: ')
    name = None
    styles = {
        'd': RoundedModuleDrawer(),
        '': RoundedModuleDrawer(),
        'c': CircleModuleDrawer(),
        'g': GappedSquareModuleDrawer(),
        's': SquareModuleDrawer(),
        'v': VerticalBarsDrawer(),
        'h': HorizontalBarsDrawer(),
        'a': None

    }

    datas = {
        'fb': 'www.facebook.com/profile.php?id=100087327551813',
        'ig': 'www.instagram.com/scouts.kreslivorel',

    }

    logos = {
        'fb': "./logos/fblogo.png",
        'ig': "./logos/iglogo.png",
        'n': None,
        '': None
    }

    rgb = {
        'fb': {
            'center color': (0, 0, 0),
            'edge color': (0, 0, 255),
            'back color': (255, 255, 255)
        },
        'ig': {
            'center color': (255, 220, 128),
            'edge color': (184, 76, 245),
            'back color': (255, 255, 255)
        },
        'n': {
            'center color': '',
            'edge color': '',
            'back color': ''
        },
        '': {
            'center color': '',
            'edge color': '',
            'back color': ''
        }

    }

    colors = {
        'cc': RadialGradiantColorMask(back_color=rgb['n']['back color'],
                                      center_color=rgb['n']['center color'],
                                      edge_color=rgb['n']['edge color']),
        'nc': RadialGradiantColorMask(back_color=(255, 255, 255),
                                      center_color=(0, 0, 0),
                                      edge_color=(0, 0, 0)),
        'dc': RadialGradiantColorMask(back_color=rgb[choice]['back color'],
                                      center_color=rgb[choice]['center color'],
                                      edge_color=rgb[choice]['edge color']),
        '': RadialGradiantColorMask(back_color=rgb[choice]['back color'],
                                    center_color=rgb[choice]['center color'],
                                    edge_color=rgb[choice]['edge color']),
    }
    if choice == 'n' or choice == '' or color == 'cc':
        while rgb['n']['center color'] in ['', None]:
            rgb['n']['center color'] = make_color('center color')
        while rgb['n']['edge color'] in ['', None]:
            rgb['n']['edge color'] = make_color('edge color')
        while rgb['n']['back color'] in ['', None]:
            rgb['n']['back color'] = make_color('back color')
        colors[color] = RadialGradiantColorMask(
            back_color=rgb['n']['back color'],
            center_color=rgb['n']['center color'],
            edge_color=rgb['n']['edge color']
        )

    style = input('Enter style for the QR code. Choose between "d"(default), "c"(circled), "g"(gapped), "s"(squared),'
                  ' "v"(vertical), "h"(horizontal), "a"(all): ').lower()
    while style not in list(styles.keys()):
        style = input(
            'Enter style for the QR code. Choose between "d"(default), "c"(circled), "g"(gapped), "s"(squared),'
            ' "v"(vertical), "h"(horizontal), "a"(all): ').lower()
    if data:
        name = make_file_name()
    else:
        while not data:
            try:
                data = datas[choice]
            except KeyError:
                data = input('Enter anything to generate QR code: ')
                while not name:
                    name = make_file_name()

    qr = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_H, version=2, box_size=30, border=1)
    qr.add_data(data)
    qr.make(fit=True)
    if style != 'a':
        img = make_image(StyledPilImage, styles[style], colors[color], logos[choice])
        save_image(make_name(choice, name, style), img)
    else:
        for k, _ in styles.items():
            if k and styles[k]:
                img = make_image(StyledPilImage, styles[k], colors[color], logos[choice])
                save_image(make_name(choice, name, k), img)

    user_choice = input('Do you want to continue? Type "y" or "n": ')
    while user_choice not in ['y', 'n']:
        user_choice = input('Do you want to continue? Type "y" or "n": ')
    if user_choice == 'n':
        user_continuation = False
