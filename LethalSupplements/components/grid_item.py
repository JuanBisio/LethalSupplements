import reflex as rx
from LethalSupplements.styles.styles import Color, Size, Font


def grid_item(row, col, img, top, txt, href) -> rx.Component:
    return rx.grid_item(
        rx.vstack(
            rx.image(
                src=img,
                width='100%',
                height='100%',
                fit='contain',
                transition='0.5s',
                _hover={
                    'transform': 'scale(1.2)'
                }
            ),
            rx.box(
                rx.link(
                    rx.button(
                        txt,
                        bg='#5F2C23DD',
                        border_radius='0px',
                        width='100%',
                        height='100%',
                        _hover={
                            'background': '#212529DD'
                        }
                    ),
                    href=href,
                    is_external=True,


                ),
                position='absolute',
                top=top,
                width='9.5em',
                height='2.7em',
            ),
            position='relative',

        ),
        overflow='hidden',
        row_span=row,
        col_span=col,
        bg='#212529CC',

    )
