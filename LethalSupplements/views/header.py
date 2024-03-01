import reflex as rx

from LethalSupplements.components.button import buttonPrimary
from LethalSupplements.styles.styles import Color, Size, Font
from LethalSupplements.components.button import buttonPrimary


def header(color_bg) -> rx.Component:
    return rx.hstack(
        rx.vstack(
            rx.text(
                'LETHAL',
                font_size=Size.VERY_BIG.value,
                text_aling='center',
                margin_bottom='-10px',
                padding_bottom='0px',
                font_family=Font.TITLE.value,
            ),
            rx.text(
                'SUPPLEMENTS',
                font_size=Size.VERY_BIG.value,
                margin_top='-10px',
                text_aling='center',
                font_family=Font.TITLE.value,
            ),
            buttonPrimary('Ver más','130px', '40px', rx.redirect('#about_us')),
        ),
        display='flex',
        justify_content='center',
        align_items='center',
        bg=color_bg,
        width='100%',
        height='100vh',
        margin='0px !important',
    )
