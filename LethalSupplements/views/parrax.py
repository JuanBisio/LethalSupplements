import reflex as rx

def parrax() -> rx.Component:
    return rx.vstack(
        rx.box(
            rx.text('Hola'),
            #bg='#212529CC',
            width='20em',
            #class_name="boxParrax",
            #stylesheets=["/css/parrax.css"]

        ),
        display='flex',
        justify_content='center',
        aling_items='center',
        background_image='/protein1.webp',
        background_attachment='fixed',
        height='400px',
        width='100%',
        
    )