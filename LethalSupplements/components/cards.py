import reflex as rx
from LethalSupplements.styles.styles import Color, Size, Font
from LethalSupplements.components.button import buttonPrimary


class ModalState(rx.State):
    show: bool = False

    def change(self):
        self.show = not (self.show)


def cards(text_button, img) -> rx.Component:
    return rx.box(
        rx.button(
            text_button,
            width='100%',
            height='2.5em',
            border_radius=Size.SMALL.value,
            bg=Color.PRIMARY.value,
            _hover={
                'background_color': Color.DARK_RED.value,
            },
            on_click=ModalState.change,
            margin='.7em'
        ),
        rx.modal(
            rx.modal_overlay(
                rx.modal_content(
                    rx.modal_header("Titulo"),
                    rx.modal_body(
                        "Lorem ipsum es el texto que se usa habitualmente en diseño gráfico en demostraciones de tipografías o de borradores de diseño para probar el diseño visual antes de insertar el texto final."
                    ),
                    rx.modal_footer(
                        rx.button(
                            "Cerrar",
                            on_click=ModalState.change,
                            bg=Color.DARK_RED.value,
                            _hover={
                                'background_color': '#5F2C23DD'  
                            },

                        )
                    ),
                    bg=Color.PRIMARY.value
                ),
            ),
            is_open=ModalState.show,
        ),
        display='flex',
        justify_content='center',
        align_items='end',
        background_image=img,
        background_position='center',
        background_size='contain',
        width='20em',
        height='30em',
        border=Color.DARK_RED.value,
        border_radius=Size.DEFAULT.value,
        margin=Size.DEFAULT.value
    )
