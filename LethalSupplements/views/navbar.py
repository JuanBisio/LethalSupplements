
import reflex as rx
import LethalSupplements.constants as constants


from LethalSupplements.styles.styles import Size, Color, TextColor, Font
from LethalSupplements.components.link_icon import link_icon
from LethalSupplements.components.drawer import drawer
from LethalSupplements.components.link_navbar import link_navbar


def navbar(bg) -> rx.Component:
    return rx.vstack(
        rx.script(src='/js/index.js'),
        rx.hstack(
            # LOGO
            rx.link(
                rx.image(
                    src='/LogoNegro.webp',
                    alt='Logo de Lethal Supplements',
                    width=Size.VERY_BIG.value,
                    height=Size.VERY_BIG.value,
                    border_radius=Size.BIG.value,
                    _hover={
                        'transform': 'scale(1.2)'
                    }
                ),
                href='/',
                cursor='pointer',
            ),
            rx.spacer(),

            drawer(),
            width='100%',
        ),
        position='sticky',
        padding_x=Size.BIG.value,
        padding_y=Size.SMALL.value,
        z_index='999',
        top='0',
        width='100%',
        font_family=Font.DEFAULT.value,
        class_name='blink'
    )
