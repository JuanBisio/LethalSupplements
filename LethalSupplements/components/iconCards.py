import reflex as rx
from LethalSupplements.styles.styles import Color, Size, Font
from LethalSupplements.styles.cardsStyles import *

def iconCard(icon, title:str,text:str) -> rx.Component:
    return rx.box(
        rx.center(
            rx.vstack(
                rx.image(
                    src=icon,
                    style=iconStyle
                ),
                rx.heading(title, size='xl', style=titleStyle),
                rx.text(text, style=textStyle)
            ),
            bg=Color.PRIMARY.value, 
            height='18em',
            #width=Size.LARGE.value,
        )   
    )