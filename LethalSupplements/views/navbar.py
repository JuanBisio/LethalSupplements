
import reflex as rx
import LethalSupplements.constants as constants

from LethalSupplements.styles.styles import Size, Color, TextColor, Font
from LethalSupplements.components.link_icon import link_icon
from LethalSupplements.components.drawer import drawer
from LethalSupplements.components.link_navbar import link_navbar


def navbar(scroll) -> rx.Component:
    return rx.vstack(
        rx.hstack(
            # LOGO
            rx.image(
                src='/LogoNegro.webp',
                alt='Logo de Lethal Supplements',
                width=Size.VERY_BIG.value,
                height=Size.VERY_BIG.value,
                border_radius=Size.BIG.value
            ),
            rx.spacer(),
            # Celular y Tablets

            # Escritorio
            rx.desktop_only(
                rx.hstack(
                    link_navbar('Planificaciones', '/planificaciones'),
                    link_navbar('Farmacologia', '/farmacologia'),
                    link_navbar('Alimentación', '/alimentacion'),
                    link_navbar('Suplementación', '/suplementos'),
                ),
            ),

            rx.spacer(),
            rx.mobile_and_tablet(
                drawer()
            ),
            rx.desktop_only(
                rx.hstack(
                    link_navbar(
                        rx.image(src='icons/instagram.svg',
                                 width=Size.DEFAULT.value, height=Size.DEFAULT.value),
                        'https://www.instagram.com/lethal_supplements/?hl=es-la'
                    ),
                    link_navbar(
                        rx.image(
                            src='icons/whatsapp.svg', width=Size.DEFAULT.value, height=Size.DEFAULT.value),
                        """https://api.whatsapp.com/send?phone=+543584014857&text=Quiero%20mas%20informacion%20sobre:%20"""
                    ),
                ),
            ),
            width='100%',

        ),
        bg=scroll,
        position='sticky',
        padding_x=Size.BIG.value,
        padding_y=Size.SMALL.value,
        z_index='999',
        top='0',
        width='100%',
        font_family=Font.DEFAULT.value
    )
