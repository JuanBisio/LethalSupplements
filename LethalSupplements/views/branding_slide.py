import reflex as rx
from LethalSupplements.styles.styles import Color, Size, Font
from LethalSupplements.components.branding_img import branding_img
from LethalSupplements.styles.sliderSyles import *


def branding_slide() -> rx.Component:
    return rx.center(
        rx.vstack(
            rx.chakra.text(
                'marcas asociadas',
                font_size=Size.SUBTITLE.value,
                # font_family=Font.DEFAULT.value,
                margin_top=Size.SMALL.value,
                font_family=Font.SUBTITLE.value,
                text_transform='uppercase',
                font_weight='600',
                text_color='#cecece',
                id='about_us',
            ),
            rx.hstack(
                rx.box(
                    rx.box(
                        rx.box(
                            rx.image(src='sponsors/recize/webp/1.webp'),
                            class_name='slide',
                        ),
                        rx.box(
                            rx.image(src='sponsors/recize/webp/2.webp'),
                            class_name='slide',
                        ),
                        rx.box(
                            rx.image(src='sponsors/recize/webp/3.webp'),
                            class_name='slide',
                        ),
                        rx.box(
                            rx.image(src='sponsors/recize/webp/4.webp'),
                            class_name='slide',
                        ),
                        rx.box(
                            rx.image(src='sponsors/recize/webp/5.webp'),
                            class_name='slide',
                        ),
                        rx.box(
                            rx.image(src='sponsors/recize/webp/6.webp'),
                            class_name='slide',
                        ),
                        rx.box(
                            rx.image(src='sponsors/recize/webp/7.webp'),
                            class_name='slide',
                        ),
                        rx.box(
                            rx.image(src='sponsors/recize/webp/8.webp'),
                            class_name='slide',
                        ),
                        rx.box(
                            rx.image(src='sponsors/recize/webp/9.webp'),
                            class_name='slide',
                        ),
                        class_name='slide-track'
                    ),
                    class_name='slider'
                )
            ),
            # max_width='1200px',
        ),
        bg=Color.PRIMARY.value,
    )
