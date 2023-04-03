
from manim import *
# or: from manimlib import *
from manim_slides import Slide

class BasicExample(Slide):
    def construct(self):
        circle = Circle(radius=3, color=BLUE)
        dot = Dot()

        self.play(GrowFromCenter(circle))
        self.next_slide()  # Waits user to press continue to go to the next slide

        self.play(Write(Text("Hello  world")))
        self.next_slide()  # Waits user to press continue to go to the next slide

        self.play(Write(Text("Especially javascript").scale(0.2).move_to(DOWN)))