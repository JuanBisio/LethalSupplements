import reflex as rx
from LethalSupplements.styles.styles import Color, Size, Font
from LethalSupplements.components.branding_img import branding_img
from LethalSupplements.styles.sliderSyles import *


def bg_function(self,tipe):
    if tipe == 'default':
        self.bgC1 = Color.DARK_RED.value
        self.bgC2 = self.bgC3 = self.bgC4 = '#ffffff'
    elif tipe == 'medium':
        self.bgC2 = Color.DARK_RED.value
        self.bgC1 = self.bgC3 = self.bgC4 = '#ffffff'
    elif tipe == 'big':
        self.bgC3 = Color.DARK_RED.value
        self.bgC2 = self.bgC1 = self.bgC4 = '#ffffff'
    else:
        self.bgC4 = Color.DARK_RED.value
        self.bgC2 = self.bgC3 = self.bgC1 = '#ffffff'

        
class State(rx.State):
    translateX = '0em'
    bgC1 = Color.DARK_RED.value
    bgC2 = bgC3 = bgC4 = '#ffffff'
    
    def default(self):
        self.translateX = "0em"
        bg_function(self,'default')

    def medium(self):
        self.translateX = "-38em"
        bg_function(self,'medium')
        
    def big(self):
        self.translateX = "-75em"
        bg_function(self,'big')
        
    def large(self):
        self.translateX = "-86em"
        bg_function(self,'large')
    
    

        
def branding() -> rx.Component:
    return rx.center(
        rx.vstack(
            rx.heading(
                    'Marcas asociadas', 
                    font_family=Font.SUBTITLE.value,
                    size='2xl', 
                    margin=Size.SMALL.value,  
            ),
            rx.hstack(
                
                rx.box(
                    branding_img('sponsors/recize/webp/1.webp'),
                    branding_img('sponsors/recize/6.png'),
                    branding_img('sponsors/recize/8.png'),
                    branding_img('sponsors/recize/webp/5.webp'),
                    branding_img('sponsors/recize/webp/2.webp'),
                    branding_img('sponsors/recize/webp/3.webp'),
                    branding_img('sponsors/recize/4.png'),
                    branding_img('sponsors/recize/7.png'),
                    branding_img('sponsors/recize/webp/9.webp'),
                    branding_img('sponsors/recize/10.png'),
                    display='flex',
                    width='100%',
                    flex_wrap='nowrap',
                    transition='all 0.5s ease',
                    transform=f'translateX({State.translateX})',
                    #margin_left='-20em'
                    
                ),
                
                max_width='1200px',
                overflow='hidden',
                width='100%',                    

            ),
            rx.hstack(
                rx.button(
                    bg=State.bgC1,
                    on_click=State.default,
                ),
                rx.button(
                    bg=State.bgC2,
                    on_click=State.medium,
                ),
                rx.button(
                    bg=State.bgC3,
                    on_click=State.big,
                ),
                rx.button(
                    bg=State.bgC4,
                    on_click=State.large,
                ),
            ),
            
            
        ),  
        bg=Color.PRIMARY.value,
        
    )