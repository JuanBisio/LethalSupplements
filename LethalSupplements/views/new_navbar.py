
import reflex as rx
import LethalSupplements.constants as constants

from LethalSupplements.styles.styles import Size, Color, TextColor, Font
from LethalSupplements.components.link_icon import link_icon
from LethalSupplements.components.drawer import drawer
from LethalSupplements.components.new_drawer import new_drawer
from LethalSupplements.components.link_navbar import link_navbar


def new_navbar(scroll) -> rx.Component:
    return rx.vstack(
        rx.hstack(
            drawer(),
            rx.spacer(),
            rx.text(
                'LETHAL SUPPLEMENTS',
                font_size= '2.3em',
                text_aling='center',
                margin_bottom='0px',
                font_family=Font.TITLE.value,
                padding_bottom='0px',
            ),
            rx.spacer(),
            new_drawer(),
            width='100%',
        ),
        bg=scroll,
        position='sticky',
        padding_x=Size.BIG.value,
        padding_y=Size.SMALL.value,
        z_index='999',
        top='0',
        width='100%',
    )
