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
            # width='100%',
            # height='2.5em',
            # border_radius=Size.SMALL.value,
            # bg=Color.DARK_RED.value,
            # text_color='#cecece',
            on_click=ModalState.change,
            margin='.7em',
            # NEW
            min_width='130px',
            height='40px',
            color='#fff',
            padding=' 5px 10px',
            font_weight='bold',
            cursor='pointer',
            transition='all 0.4s ease',
            position='relative',
            display='inline-block',
            outline='none',
            border_radius='5px',
            border='none',
            background_size='120% auto',
            background_image='linear-gradient(315deg, #5F2C23 10%, #ba0210 75%)',

            _hover={
                # 'background_color': Color.DARK_RED.value,
                'background_position': 'right center',
                'transform':'scale(1.05)'
            },
            _active={
                'top': '2px',
            }

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
        bg='#fff',
        background_image=img,
        background_position='center',
        background_size='cover',
        width='18em',
        height='30em',
        margin=Size.DEFAULT.value,
        border_radius='30px',
        box_shadow='15px 15px 30px rgb(25, 25, 25), -15px -15px 30px rgb(60, 60, 60)'
    )
