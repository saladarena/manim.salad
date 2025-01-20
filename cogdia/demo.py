from cogdia.diagram import Diagram
from cogdia.renderer import Renderer

if __name__ == "__main__":
    dia = Diagram("diala")
    renderer = Renderer("lal", dia)
    renderer.render()
