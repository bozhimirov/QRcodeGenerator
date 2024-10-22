import os

from qrcode.image.styles.moduledrawers import RoundedModuleDrawer, CircleModuleDrawer, GappedSquareModuleDrawer, \
    SquareModuleDrawer, VerticalBarsDrawer, HorizontalBarsDrawer

# Constants for logo paths
LOGO_PATHS = {
    'facebook': os.path.join('static', 'logos', 'fblogo.png'),
    'instagram': os.path.join('static', 'logos', 'iglogo.png'),
    'none': None,
    'pomarina': os.path.join('static', 'logos', 'pomarina.png'),
}

# Hex color definitions
HEX_COLORS = {
    'facebook': {'cc': '#000000', 'ec': '#0000ff', 'bc': '#ffffff'},
    'instagram': {'cc': '#f9ce34', 'ec': '#840cf6', 'bc': '#ffffff'},
    'none': {'cc': '#000000', 'ec': '#000000', 'bc': '#ffffff'},
}

# Data for different logos
DATAS = {
    'facebook': 'fb.com/100087327551813',
    'instagram': 'instagram.com/scouts.kreslivorel',
    'custom': 'instagram.com/scouts.kreslivorel',
    'none': 'instagram.com/scouts.kreslivorel'
}

# Styles for QR codes
STYLES = {
    'default': RoundedModuleDrawer(),
    'circle': CircleModuleDrawer(),
    'gapped': GappedSquareModuleDrawer(),
    'square': SquareModuleDrawer(),
    'vertical': VerticalBarsDrawer(),
    'horizontal': HorizontalBarsDrawer(),
}

SIZES = {
    'default': 140,
    'big': 160,
    'medium': 120,
    'small': 100,
}
