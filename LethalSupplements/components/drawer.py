import reflex as rx 
from LethalSupplements.styles.styles import Size, Color, TextColor
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
            rx.icon(
                tag='hamburger',
                width=Size.MEDIUM.value,
                height=Size.MEDIUM.value,
            ),
            on_click=DrawerState.right,
            bg='none',
            _hover={
                'background_color':Color.DARK_RED.value 
            }
             
        ),
        rx.drawer(
            rx.drawer_overlay(
                rx.drawer_content(
                    rx.drawer_header(
                        "Lethal Supplements",
                        display='flex',
                        justify_content='center',
                        font_size=Size.LARGE.value
                        ),
                    rx.drawer_body(
                        rx.vstack(
                            link_navbar('About Us', '/aboutus'),
                            link_navbar('Proteina', '/proteina'),
                            link_navbar('Creatina', '/creatina'),
                            link_navbar('Pre entreno', '/preentreno'),
                        ),
                        font_size=Size.MEDIUM.value,
                        display='flex',
                        justify_content='center',

                        
                    ),
                    rx.drawer_footer(
                        rx.button(
                            "Cerrar", 
                            on_click=DrawerState.right,
                            bg=Color.DARK_RED.value,
                        )
                    ),
                    bg="#212529CC",
                )
            ),
            is_open=DrawerState.show_right,
        ),
    )
