
from manim import *
# or: from manimlib import *
from manim_slides import Slide

class BasicExample(Slide):
    def smallwait(self):
        self.wait(0.5)
    
    def construct(self):
        circle = Circle(radius=3.85, color=BLUE)
        hello = Text("Hello  world")
        java = Text("Javascript").set_color_by_gradient(RED, ORANGE, RED)
        authors = Text("This presentation is made by Iulian and Eugen").set_color_by_gradient(YELLOW, ORANGE, YELLOW)
        content = VGroup(
                Text("Introduction"),
                Text("Basics of javascript (get down on business)"),
                Text("DOM manipulation"),
                Text("Animations")                         
                    ).arrange(DOWN, buff=1.5).scale(0.75)
        intro = VGroup(
                Text("Introduction").scale(2.1),
                Text("JavaScript is to Java as ham is to a hamster."),
                Text("JavaScript != Java"),
                Text("JavaScript is a lightweight, interpreted programming language."),
                Text("It is designed for creating network-centric applications."),
                Text("It is complimentary to and integrated with Java."),
                Text("It is easy to learn. \U0001F609"),
                    ).arrange(DOWN, buff=1.5).scale(0.75)


        self.play(GrowFromCenter(circle))
        self.smallwait()
        self.play(Write(hello.scale(2.1)))
        self.smallwait()
        self.play(ReplacementTransform(hello, java.scale(2.1), run_time=0.5))
        self.play(Write(authors.scale(0.5).move_to(DOWN)))
        self.next_slide()  # Waits user to press continue to go to the next slide
        
        self.play(FadeOut(circle), FadeOut(java), FadeOut(authors))
        self.clear()
        self.play(Write(content,  run_time=4))