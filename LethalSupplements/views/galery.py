import reflex as rx
import LethalSupplements.styles.styles as styles

from LethalSupplements.components.cards import cards
from LethalSupplements.components.image_galery import image_galery
from LethalSupplements.styles.styles import Color, Size, Font





def galery() -> rx.Component:
    return rx.center(
        rx.vstack(
            rx.chakra.text(
                'Servicios',
                font_size=Size.SUBTITLE.value,
                margin_top=Size.SMALL.value,
                font_family=Font.SUBTITLE.value,
                text_transform='uppercase',
                font_weight='600',
                color='linear-gradient(315deg, #5F2C23 10%, #ba0210 75%)'
            ),
            rx.box(
                cards('Asesoria en el uso de quimica','/IA/IAImage7.jpeg'),
                rx.spacer(),
                cards('Composición Corporal','/IA/IAImage9.jpeg'),
                rx.spacer(),
                cards('Planificación alimenticia','/service/servicio2.webp'),
                max_width='1000px',
                display='flex',
                flex_direction = ["column", "column", "column", "row", "row"],
            ),
        ),  
        bg=Color.PRIMARY.value,     
        id='servicios'   
    )
