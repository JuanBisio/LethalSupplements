import reflex as rx
from LethalSupplements.styles.styles import Size, Color, Font
from LethalSupplements.components.link_navbar import link_navbar


class DrawerState(rx.State):
    show_right: bool = False
    show_top: bool = False

    def top(self):
        self.show_top = not (self.show_top)

    def right(self):
        self.show_right = not (self.show_right)


def drawer() -> rx.Component:
    return rx.box(
        rx.button(
            rx.box(
                rx.span(
                    rx.icon(
                        tag='hamburger',
                        width=Size.MEDIUM.value,
                        height=Size.MEDIUM.value,
                    ),
                    class_name='icon'
                ),
                rx.span(
                    'MENU',
                    class_name='text',
                ),
                class_name='btn',
                font_size='1.07em',
                font_family=Font.SUBTITLE.value,
                font_weight='500',
                width=['7em','7em','7em','9em','9em',],
                height='3em',

            ),
            bg='none',
            margin='0 !important',
            padding='0 !important',
            _hover={
                'background': 'transparent'
            },
            active={
                'background': 'transparent'
            },
            on_click=DrawerState.right,
        ),
        rx.drawer(
            rx.drawer_overlay(
                rx.drawer_content(
                    rx.drawer_header(
                        rx.text(
                            'MENU'
                        ),
                        font_size=Size.LARGE.value,
                        display='flex',
                        justify_content='center',
                        margin_top=Size.DEFAULT.value,
                    ),
                    rx.drawer_body(
                        rx.vstack(
                            link_navbar('Sobre Nosotros', '#about_us',DrawerState.right,),
                            link_navbar('Servicios', '#servicios',DrawerState.right,),
                            link_navbar('Contacto', '#contacto',DrawerState.right,),
                            link_navbar('Quimicos', '#quimicos',DrawerState.right,),
                            link_navbar('Quimicos', '#quimicos',DrawerState.right,),
                        ),
                        font_size=Size.LARGE.value,
                        display='flex',
                        margin_top=Size.SMALL.value,
                        justify_content='center',
                    ),
                    rx.drawer_footer(
                        rx.box(
                            link_navbar(
                                rx.image(src='icons/instagram.svg',
                                             width=Size.DEFAULT.value, height=Size.DEFAULT.value),
                                'https://www.instagram.com/lethal_supplements/?hl=es-la',
                                DrawerState.right,
                            ),
                            link_navbar(
                                rx.image(
                                    src='icons/whatsapp.svg', width=Size.DEFAULT.value, height=Size.DEFAULT.value),
                                """https://api.whatsapp.com/send?phone=+543584014857&text=Quiero%20mas%20informacion%20sobre:%20""",DrawerState.right,
                            ),
                        ),
                        rx.box(
                            rx.button(
                                "Cerrar",
                                on_click=DrawerState.right,
                                bg='linear-gradient(315deg, #5F2C23 10%, #ba0210 75%)',
                                _hover={
                                    'background-color': 'transparent',
                                    'transform': 'scale(1.1)',
                                },
                                active={
                                    'background': 'transparent',
                                    'top': '2px'
                                },
                            ),
                        ),
                        display='flex',
                        flex_direction='row',
                        justify_content='space-between'
                    ),

                    bg="#212121",
                )
            ),
            is_open=DrawerState.show_right,
        ),
    )
