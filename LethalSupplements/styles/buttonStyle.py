import reflex as rx


svgIcon ={ 
    'width': '16px',
    'transition-duration': '0.25s',
    'fill': 'white',
    
    ':hover' : {
        'transition-duration': '0.4s',
        'transform': 'translateY(300%)',
    }
}

button = {
    'width': '50px',
    'height': '50px',
    'border-radius': '50%',
    'background-color': 'rgb(20, 20, 20)',
    'border': 'none',
    'font-weight': 400,
    'display': 'flex',
    'align-items': 'center',
    'justify-content': 'center',
    #'box-shadow': '0px 0px 0px 4px rgba(180, 160, 255, 0.253)',
    'cursor': 'pointer',
    'transition-duration':' 0.3s',
    'overflow': 'hidden',
    'position': 'relative',
    
    ':hover' : {
        'width': '140px',
        'border-radius': '50px',
        'transition-duration': '0.3s',
        'background-color': 'rgb(181, 160, 255)',
        'align-items': 'center',
        'transition-duration': '0.3s',
        ':before' : {
            'font-size': '16px',
            'opacity': '1',
            'bottom': 'unset',
            'transition-duration': '0.3s',
        },
    },
    ':before': {
        'position': 'absolute',
        'bottom': '-20px',
        'color': 'white',
        'content': "'Back to Top'",
        'font-size': '0px',
    }
}
