from manim import *
from cogdia.diagram import Diagram


class ManimRenderer(Scene):
    def __init__(self, diagram: Diagram):
        super().__init__()


    def construct(self):
        circle = Circle()  # create a circle
        circle.set_fill(PINK, opacity=0.5)  # set the color and transparency
        self.add(circle)
        #self.play(Create(circle))  # show the circle on screen