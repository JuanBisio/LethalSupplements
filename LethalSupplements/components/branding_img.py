import reflex as rx
from LethalSupplements.styles.styles import Color, Size, Font

def branding_img(src) -> rx.Component:
    return rx.box(
        rx.image(
            src=src,
            width='14.06em',
            heigth='14.06em',
            border_radius=Size.LARGE.value,
            box_shadow='0 2px 5px 0 rgba(255,255,255,0.4)',

        ),
        flex='1 0 auto',
        margin_y='2em',
        margin_x='1em',

        
    )