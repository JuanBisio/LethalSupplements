import reflex as rx
from LethalSupplements.styles.styles import Color, Size, Font
from LethalSupplements.components.grid_item import grid_item


def grid_galery() -> rx.Component:
    return rx.center(
        rx.vstack(
            rx.heading(
                'Secciones',
                size='2xl',
                font_family=Font.SUBTITLE.value,
                margin=Size.SMALL.value,
            ),
            rx.mobile_and_tablet(
                rx.center(
                    rx.grid(
                        grid_item(1, 2, '/galery/resize/mujerSaker.webp', '41%', 'Planificación', '/planificaciones'),
                        grid_item(3, 2, '/galery/resize/mujerEntrenando.webp','85%', 'Farmacologia', '/farmacologia'),
                        grid_item(1, 2, '/galery/resize/mujerSakerCocina.webp','65%', 'Suplemetación', '/suplementos'),
                        grid_item(3, 2, '/galery/resize/mujerTomandoShaker.webp', '85%', 'Alimentación', '/alimentacion'),
                        template_rows="repeat(4, 0.6fr)",
                        template_columns="repeat(2, 0.6fr)",
                        width='70%',
                        gap=3,
                    ),
                ),
            ),
            rx.desktop_only(
                rx.center(
                    rx.grid(
                        grid_item(1, 2, '/galery/resize/mujerSaker.webp', '51%', 'Planificación', '/planificaciones'),
                        grid_item(3, 2, '/galery/resize/mujerEntrenando.webp','90%', 'Farmacologia', '/farmacologia'),
                        grid_item(3, 2, '/galery/resize/mujerTomandoShaker.webp', '90%', 'Alimentación', '/alimentacion'),
                        grid_item(1, 2, '/galery/resize/mujerSakerCocina.webp','51%', 'Suplemetación', '/suplementos'),
                        template_rows="repeat(4, 0.6fr)",
                        template_columns="repeat(4, 0.6fr)",
                        width='70%',
                        gap=3,
                    ),
                ),
            ),

            max_width='1200px',
        ),
        bg=Color.PRIMARY.value,
    )