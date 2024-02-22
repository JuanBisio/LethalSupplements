import reflex as rx
from LethalSupplements.styles.styles import Color, Size, Font
import LethalSupplements.styles.styles as styles

def image_galery(image:str) -> rx.Component:
    return rx.image(
            src=image,
            width='25em',
            height='30em',
            #padding_x=Size.BIG.value,
        )