import reflex as rx
from LethalSupplements.styles.styles import Color, Size, Font
import LethalSupplements.styles.styles as styles


def about_us() -> rx.Component:
    return rx.center(
        rx.vstack(
            rx.chakra.text(
                'Sobre nosotros',
                font_size=Size.SUBTITLE.value,
                # font_family=Font.DEFAULT.value,
                margin_top=Size.SMALL.value,
                font_family=Font.SUBTITLE.value,
                text_transform='uppercase',
                font_weight='600',
                text_color='#cecece',
            ),
            rx.hstack(
                rx.text(
                    'En Lethal Supplements nos dedicamos desde 2018 a los estudios de ciencias de la salud y del deporte, con sede en Córdoba, Argentina. Nuestros servicios se centran en la educación y acompañamiento en el entrenamiento y uso de suplementación deportiva, los productos con los que trabajamos están diseñados para mejorar el rendimiento deportivo y apoyar el bienestar general. Con un compromiso con la excelencia y la satisfacción del cliente, Lethal Supplements se centra en acompañar desde el primer hasta el último paso al deportista, por eso somos la opción preferida para los atletas y entusiastas del fitness que buscan llevar su entrenamiento al siguiente nivel. Contamos con estudios en kinesiología y fisioterapia UNC y certificaciones en alimentación, suplementacion y farmacologia orientada al deporte.',
                    font_weight='200',
                    padding_y=Size.DEFAULT.value,

                ),
                rx.image(
                    src='/certificadoCut.webp',
                    alt='Certificacion Farmacologica deportia y fitness de Juan Cruz Celli',
                    width='25em',
                    padding=Size.DEFAULT.value,
                ),
                display='flex',
                flex_direction=["column", "column", "column", "row", "row"],

            ),
            font_family=Font.DEFAULT.value,
            max_width='900px',
            margin_x=Size.BIG.value,
        ),
        # bg='#212529',
        bg='#212121',
    )
