import reflex as rx
import LethalSupplements.styles.styles as styles
from LethalSupplements.pages.index import index_function

#Import pages LethalSupplements
from LethalSupplements.pages.planificaciones import planificaciones_function
from LethalSupplements.pages.alimentacion import alimentacion_function
from LethalSupplements.pages.suplementos import suplementos_function
from LethalSupplements.pages.farmacologia import farmacologia_function


def index() -> rx.Component:
    return index_function() 


def alimentacion() -> rx.Component:
    return alimentacion_function() 


def planificaciones() -> rx.Component:
    return planificaciones_function() 


def suplementos() -> rx.Component:
    return suplementos_function() 


def farmacologia() -> rx.Component:
    return farmacologia_function() 


app = rx.App(
    stylesheets=styles.STYLESHEETS,
    style=styles.BASE_STYLE,
)

app.add_page(index, route="/", title='Lethal Supplements')
app.add_page(planificaciones, route="/planificaciones", title='Planificaciones of Lethal Supplements')
app.add_page(alimentacion, route="/alimentacion", title='Alimentacion of Lethal Supplements')
app.add_page(suplementos, route="/suplementos", title='Suplementos of Lethal Supplements')
app.add_page(farmacologia, route="/farmacologia", title='Farmacologia of Lethal Supplements')






