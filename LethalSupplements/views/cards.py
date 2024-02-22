import reflex as rx
from LethalSupplements.styles.styles import Color, Size, Font
from LethalSupplements.components.iconCards import iconCard

def cards() -> rx.Component:
    return rx.center(
            rx.hstack(
                iconCard('/pilds.ico', 'title 1', 'Lorem ipsum es el texto que se usa habitualmente '),
                rx.spacer(),
                iconCard('/mancuerna.ico', 'title 2', 'Lorem ipsum es el texto que se usa habitualmente '),
                rx.spacer(),
                iconCard('/proteina.ico', 'title 3  ', 'Lorem ipsum es el texto que se usa habitualmente '),
                max_width='1000px',
                display='flex',
                flex_direction = ["column", "column", "column", "row", "row"],
                margin_top=Size.BIG.value 
            ),
            bg=Color.PRIMARY.value,
        )