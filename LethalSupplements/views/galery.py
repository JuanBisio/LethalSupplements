import reflex as rx
import LethalSupplements.styles.styles as styles

from LethalSupplements.components.cards import cards
from LethalSupplements.components.image_galery import image_galery
from LethalSupplements.styles.styles import Color, Size, Font





def galery() -> rx.Component:
    return rx.center(
        rx.vstack(
            rx.heading(
                    'Servicios', 
                    size='2xl', 
                    font_family=Font.SUBTITLE.value,
                    margin=Size.SMALL.value,  
            ),
            rx.box(
                cards('Asesoria en el uso de quimica','/service/servicio1.webp'),
                rx.spacer(),
                cards('Planificación alimenticia','/service/servicio2.webp'),
                rx.spacer(),
                cards('Composición Corporal','/service/servicio3.webp'),
                max_width='1000px',
                display='flex',
                flex_direction = ["column", "column", "column", "row", "row"],
            ),
        ),  
        bg=Color.PRIMARY.value,
    )
