import reflex as rx
import LethalSupplements.styles.styles as styles

from LethalSupplements.views.navbar import navbar 
#from LethalSupplements.views.new_navbar import new_navbar
 
from LethalSupplements.views.header import header
from LethalSupplements.views.about_us import about_us
from LethalSupplements.views.galery import galery
from LethalSupplements.views.cards import cards
from LethalSupplements.views.parrax import parrax
from LethalSupplements.views.branding import branding
from LethalSupplements.views.grid_galery import grid_galery
from LethalSupplements.views.footer import footer

from LethalSupplements.components.spacer import spacer



def index_function() -> rx.Component:
    return rx.box(
        #new_navbar('#212529CC'),
        navbar('#212529CC'),
        header('#212529CC'),
        about_us(),
        spacer(),
        galery(),
        spacer(),
        grid_galery(),
        spacer(),
        branding(),
        spacer(),
        # carrousel_antd(),
        #parrax(), 
        footer('#212529CC'),
        
        #cards(),
        
        background_image='protein1.webp',  
        background_attachment='fixed',  
        style=styles.BASE_STYLE,
        
    )
