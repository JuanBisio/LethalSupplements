import reflex as rx
from LethalSupplements.styles.styles import Color, Size, Font

def link_navbar(text:str, href:str,) -> rx.Component:
    return rx.link(
                rx.button(
                    text,
                    bg='none',
                    _hover= {
                        "background_color": Color.DARK_RED.value,
                    },
                    font_size='1.05em',
                    font_family=Font.SUBTITLE.value


                ),
                href= href,
                is_external=True,
                padding_x='.2em',
                text_decoration='none',
                
            )