import reflex as rx
from LethalSupplements.styles.styles import Color, Size, Font
from LethalSupplements.styles.buttonStyle import button

class PreventDefault():
    
    def default():
        return print('hola')
    


def buttonPrimary(text,Width, Height, onclick=rx.redirect('', external=False)) -> rx.Component:
    return rx.button(
        text,
        margin='.7em',
        # NEW
        min_width='130px',
        height=Height,
        width=Width,
        color=Color.WHITE.value,
        padding=' 5px 10px',
        font_weight='bold',
        cursor='pointer',
        transition='all 0.4s ease',
        position='relative',
        display='inline-block',
        outline='none',
        border_radius='5px',
        border='none',
        background_size='120% auto',
        background_image='linear-gradient(315deg, #5F2C23 10%, #ba0210 75%)',
        on_click=onclick,
        _hover={
            'background_position': 'right center',
            'transform': 'scale(1.05)'
        },
        _active={
            'top': '2px',
        },
    )
