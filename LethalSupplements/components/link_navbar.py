import reflex as rx
from LethalSupplements.styles.styles import Color, Size, Font


def link_navbar(text: str, href: str,on_click, is_external=False) -> rx.Component:
    return rx.link(
        rx.button(
            rx.box(
                rx.span(
                    text,
                    class_name='actual-text'
                ),
                rx.span(
                    text,
                    class_name='hover-text',
                    aria_hidden='true'
                ),
                class_name='button',
                data_text="Awesome",
                bg='none',
                # font_size='1.05em',
                font_family=Font.SUBTITLE.value,
                font_weight='500',

            ),
            bg='none',
            _hover={
            },
            on_click=on_click

        ),
        href=href,
        is_external=is_external,
        padding_x='.2em',
        text_decoration='none',
    )
