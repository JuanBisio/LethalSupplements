import reflex as rx
import LethalSupplements.styles.styles as styles

from LethalSupplements.styles.styles import Color, Size, Font
from LethalSupplements.views.navbar import navbar
from LethalSupplements.views.new_navbar import new_navbar
from LethalSupplements.views.header import header
from LethalSupplements.views.about_us import about_us
from LethalSupplements.views.galery import galery
from LethalSupplements.views.cards import cards
from LethalSupplements.views.parrax import parrax
from LethalSupplements.views.branding import branding
from LethalSupplements.views.branding_slide import branding_slide
from LethalSupplements.views.registration_form import registration_form
from LethalSupplements.views.grid_galery import grid_galery
from LethalSupplements.views.footer import footer
from LethalSupplements.components.spacer import spacer







def index_function() -> rx.Component:
    return rx.box(
        navbar('#212121CC'),
        header('#212121CC'),
        spacer('about_us'),
        about_us(),
        spacer(),
        galery(),
        spacer(),
        registration_form(),
        spacer(),
        branding_slide(),
        spacer(),
        footer('#212121CC'),


        bg=Color.PRIMARY.value,
        #background_image='/protein1.webp',
        background_image='/IA/IAImage1.jpeg',
        background_attachment='fixed',
        background_size='cover',
        background_position='center',
        background_repeat='no-repeat',
        style=styles.BASE_STYLE,
    )
