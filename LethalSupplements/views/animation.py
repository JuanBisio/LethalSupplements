#import reflex as rx 
#from '@splinetool/react-spline' import Spline
#
#export default function App() {
#  return (
#    <Spline scene="https://prod.spline.design/up1SQcRLq1s6yks3/scene.splinecode" />
#  );
#}
#
#class Spline(rx.Component):
#    """Spline component."""
#
#    library = "@splinetool/react-spline"
#    tag = "Spline"
#    scene: Var[
#        str
#    ] = "https://prod.spline.design/joLpOOYbGL-10EJ4/scene.splinecode"
#    is_default = True
#
#    lib_dependencies: list[str] = ["@splinetool/runtime"]
#
#
#spline = Spline.create
#
#
#def spline_example():
#    return rx.center(
#        spline(),
#        overflow="hidden",
#        width="100%",
#        height="30em",
#    )
#