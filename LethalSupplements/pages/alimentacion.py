import reflex as rx 
import LethalSupplements.styles.styles as styles

from LethalSupplements.views.header import header
from LethalSupplements.views.navbar import navbar 


def alimentacion_function() -> rx.Component:
   return rx.box(
        navbar('#212529CC'),
        header('#212529CC'),
        background_image='/protein1.jpeg',    

        style=styles.BASE_STYLE,
    )