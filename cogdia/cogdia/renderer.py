from cogdia.diagram import Diagram
from manim import *
from cogdia.phy_renderer_manim import ManimRenderer

class Renderer :
    def __init__(self, name : str, diagram : Diagram):
        self.name = name
        self.diagram = diagram

    def render(self):
        with tempconfig({'quality': 'low_quality', 'preview': True}):
            scene = ManimRenderer(self.diagram)
            scene.render()
