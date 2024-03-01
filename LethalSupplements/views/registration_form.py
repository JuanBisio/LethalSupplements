import reflex as rx
from LethalSupplements.styles.styles import Color, Size, Font


class SpecialEventsState(rx.State):
    def alert(self):
        return rx.red("Hello World!")


class RegistrationFormState(rx.State):
    form_data: dict = {}

    def handle_submit(self, form_data: dict):
        self.form_data = form_data
        # print(form_data)
        actividades = []
        for clave, valor in form_data.items():
            if (clave != "Nombre: ") and (clave != "Apellido: ") and (clave != "Mensaje: "):
                actividades.append(clave)
            elif clave == "Nombre: ":
                nombre = valor
            elif clave == "Apellido: ":
                apellido = valor
            elif clave == "Mensaje: ":
                mensaje = valor

        string = f"Nombre: {nombre} -- Apellido: {apellido} -- Mensaje: {mensaje}"

        link = f'https://api.whatsapp.com/send?phone=+5493584299645&text={string}'
        return rx.redirect(link, external=True)


class RegistrationTextareaState(rx.State):
    text: str = "Consulta o Duda"


class RegistrationFormErrorState(rx.State):
    name: str

    @rx.var
    def is_error(self) -> bool:
        return len(self.name) <= 3


def registration_form() -> rx.Component:
    return rx.chakra.center(
        rx.chakra.vstack(
            rx.chakra.text(
                'contáctanos',
                font_size=Size.SUBTITLE.value,
                # font_family=Font.DEFAULT.value,
                margin_top=Size.SMALL.value,
                font_family=Font.SUBTITLE.value,
                text_transform='uppercase',
                font_weight='600',
                text_color='#cecece',
                id='about_us',
            ),
            rx.chakra.vstack(
                rx.chakra.form(
                    rx.chakra.input(
                        placeholder='Nombre',
                        on_blur=RegistrationFormErrorState.set_name,
                        name='Nombre: ',
                        type_='text',
                        focus_border_color=Color.DARK_RED.value,
                        error_border_color='#777771',
                        border=f"1px dotted #777771",
                        _hover={
                            'border': f'1px dotted {Color.DARK_RED.value}'
                        },
                    ),
                    rx.chakra.input(
                        placeholder='Apellido',
                        on_blur=RegistrationFormErrorState.set_name,
                        name='Apellido: ',
                        type_='text',
                        focus_border_color=Color.DARK_RED.value,
                        error_border_color='#777771',
                        border=f"1px dotted #777771",
                        _hover={
                            'border': f'1px dotted {Color.DARK_RED.value}'
                        },
                    ),

                    rx.chakra.text_area(
                        value=RegistrationTextareaState.text,
                        on_change=RegistrationTextareaState.set_text,
                        border=f"1px dotted #777771",
                        name='Mensaje: ',
                        focus_border_color=Color.DARK_RED.value,
                        _hover={
                            'border': f'1px dotted {Color.DARK_RED.value}'
                        },
                        margin_y=Size.DEFAULT.value,
                    ),
                    rx.hstack(
                        rx.button(
                            'Enviar a Whatsapp',
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
                            type_='submit',
                            _hover={
                                'background_position': 'right center',
                                'transform': 'scale(1.05)'
                            },
                            _active={
                                'top': '2px',
                            },
                        ),
                    ),
                    on_submit=RegistrationFormState.handle_submit,
                    reset_on_submit=False,
                    width=['20em', '15em', '15em', '20em', '30em']
                ),
            ),
            max_width='1200px',
        ),
        id='contacto',
        bg=Color.PRIMARY.value,
        overflow='overview'
    )
