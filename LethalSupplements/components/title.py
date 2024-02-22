import reflex as rx
from LethalSupplements.styles.styles import Color, Size

def title(text, size, color) -> rx.Component:
    return rx.heading(
        text,
        size = size,
        color = color
    )