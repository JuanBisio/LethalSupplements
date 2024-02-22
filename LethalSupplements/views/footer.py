import reflex as rx
from LethalSupplements.styles.styles import Color, Size, Font
from LethalSupplements.components.link_navbar import link_navbar

def footer(bg) -> rx.Component:
    return rx.center(
            rx.vstack(
                rx.heading('Lethal Supplements', size='xl', font_family=Font.TITLE.value),
                rx.heading('Copyright © 2024 Juan Cruz Celli.', size='xs', color='#fefefe'),
                rx.hstack(
                    link_navbar(
                        rx.image(src='icons/instagram.svg',width=Size.DEFAULT.value,height=Size.DEFAULT.value),
                        'https://www.instagram.com/lethal_supplements/?hl=es-la'
                    ),
                    link_navbar(
                        rx.image(src='icons/whatsapp.svg',width=Size.DEFAULT.value,height=Size.DEFAULT.value),
                        """https://api.whatsapp.com/send?phone=+543584014857&text=Quiero%20mas%20informacion%20sobre:%20"""
                    ),
                ),
                
                max_width='1200px',
                margin=Size.BIG.value,
                
            ),
            bg=Color.PRIMARY.value,
            
        )