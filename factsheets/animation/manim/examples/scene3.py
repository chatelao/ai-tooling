from manim import *

class PlotFunctions(Scene):
    def construct(self):
        ax = Axes(x_range=[-3, 3], y_range=[-1, 8])
        curve = ax.plot(lambda x: x**2, color=RED)
        label = ax.get_graph_label(curve, label="x^2")

        self.play(Create(ax))
        self.play(Create(curve))
        self.play(Write(label))
        self.wait()
