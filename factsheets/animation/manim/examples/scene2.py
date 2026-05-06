from manim import *

class MathFormula(Scene):
    def construct(self):
        formula = MathTex(
            r"e^{i\pi} + 1 = 0",
            font_size=72
        )
        self.play(Write(formula))
        self.play(formula.animate.set_color(YELLOW))
        self.wait()
