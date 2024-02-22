import reflex as rx

from LethalSupplements.components.button import buttonPrimary
from LethalSupplements.styles.styles import Color, Size, Font
from LethalSupplements.styles.buttonStyle import svgIcon


class ModalStates(rx.State):
    show: bool = False

    def change(self):
        print('Hello s')


def header(color_bg) -> rx.Component:
    return rx.hstack(
            rx.vstack(
                rx.text(
                    'LETHAL',
                    font_size= Size.VERY_BIG.value,
                    text_aling='center',
                    margin_bottom='0px',
                    padding_bottom='0px',
                ),
                rx.text(
                    'SUPPLEMENTS',
                    font_size= Size.VERY_BIG.value,
                    text_aling='center',
                ),
                #buttonPrimary(rx.icon(tag='arrow_down',width=Size.BIG.value,height=Size.BIG.value, ), '50px',ModalStates.change,Size.VERY_BIG.value,Size.VERY_BIG.value),
            ),
            rx.vstack(
            ),
        display='flex',
        justify_content='center',
        align_items='center',
        bg=color_bg,
        width='100%',
        height='89vh',
        margin='0px !important',
        font_family=Font.TITLE.value
    )