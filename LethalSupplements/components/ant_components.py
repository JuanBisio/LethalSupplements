import reflex as rx 

class Carrousel(rx.Component):
    library = 'antd'
    tag = 'Carousel'
    height = '160px'
    color = '#fff'
    lineHeight = '160px'
    textAlign = 'center'
    background = '#364d79'
carrousel_antd = Carrousel.create

class FloatButton(rx.Component):
    library = 'antd'
    tag = 'FloatButton'
    
float_button= FloatButton.create
