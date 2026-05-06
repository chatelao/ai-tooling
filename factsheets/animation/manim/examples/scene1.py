from manim import *

class BasicShapes(Scene):
    def construct(self):
        ring = Annulus(inner_radius=0.5, outer_radius=1, color=BLUE)
        square = Square(color=ORANGE, fill_opacity=0.5)
        triangle = Triangle().shift(RIGHT * 3)

        self.add(ring)
        self.play(ring.animate.shift(LEFT * 3))
        self.play(Create(square))
        self.play(FadeIn(triangle, shift=UP))
        self.wait()
