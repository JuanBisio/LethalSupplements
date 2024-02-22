import reflex as rx
from LethalSupplements.styles.styles import Color, Size, Font
import LethalSupplements.styles.styles as styles

def about_us() -> rx.Component:
    return rx.center(
        rx.vstack(
            rx.heading(
                'Sobre nosotros', 
                size='2xl', 
                #font_family=Font.DEFAULT.value,
                margin=Size.SMALL.value,
                font_family=Font.SUBTITLE.value,
            ),
            rx.hstack(
                rx.text('Lethal Supplements es un proveedor líder de suplementos deportivos de alta calidad con sede en Cordoba, Argentina. Nuestros productos están diseñados para mejorar el rendimiento deportivo y apoyar el bienestar general. Con un compromiso con la excelencia y la satisfacción del cliente, Lethal Supplements es la opción preferida para los atletas y entusiastas del fitness que buscan llevar su entrenamiento al siguiente nivel. Elija Lethal Supplements para obtener productos de primera categoría que brinden resultados reales.'),
                rx.image(
                    src='/certificadoCut.webp',
                    alt='',
                    width='25em',
                    padding_y=Size.BIG.value
                ),
                display='flex',
                flex_direction = ["column", "column", "column", "row", "row"],
                
            ),
            font_family=Font.DEFAULT.value,
            max_width='800px',
            margin_x=Size.BIG.value,  
        ),
        bg='#212529',
        padding_top=Size.BIG.value,
    )