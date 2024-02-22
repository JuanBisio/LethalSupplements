import reflex as rx
from .fonts import Font 
from .colors import TextColor, Color
from enum import Enum

class Size(Enum):
    SMALL = '0.5em'
    DEFAULT = "1em"
    MEDIUM = '1.25em'
    LARGE = '1.5em'
    BIG = '2em'
    MEDIUM_BIG = '3em'
    VERY_BIG = '4em'
    MEGA_BIG = '6em'

STYLESHEETS = [
    "https://fonts.googleapis.com/css2?family=Oswald&display=swap",
    "https://fonts.googleapis.com/css2?family=Protest+Guerrilla&display=swap",
    "https://db.onlinewebfonts.com/c/ecd9c1fa8dbb2338b017932c61344252?family=Heretic+W00+Black&display=swap",
    "https://fonts.googleapis.com/css2?family=Open+Sans&display=swap"
]

BASE_STYLE = {
    'font_family': Font.DEFAULT.value,
    'color': TextColor.PRIMARY.value,
    'background': Color.PRIMARY.value,
    'scroll_behavior': 'smooth',
}