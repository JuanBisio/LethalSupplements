import reflex as rx 

def about_function() -> rx.Component:
    return rx.vstack(
        rx.text('Hola mundo About'),
    )
