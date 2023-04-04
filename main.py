from manim import *
# or: from manimlib import *
from manim_slides import Slide

class BasicExample(Slide):

    
    def smallwait(self):
        self.wait(0.3)
    
    def construct(self):
        SLIDES = [self.introduction,  self.dom]

        for slide in SLIDES:
            Vmobjects = slide()
            self.play(FadeOut(Vmobjects)) 
            self.clear()

    def introduction(self):
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
                Text("Introduction").scale(2.5),
                Text('"JavaScript is to Java as ham is to a hamster."'),
                Text("JavaScript != Java"),
                Text("JavaScript is a lightweight, interpreted programming language."),
                Text("It is designed for creating network-centric applications."),
                Text("It is easy to learn. \U0001F609"),
                    ).arrange(DOWN, buff=0.55).scale(0.5)
        warnings = VGroup(
                Text("Warning!").scale(2.9),
                Text("Oamenii slabi de inima sa nu se uite la ecran pentru restul prezentarii!"),
                Text("Ati fost avertizati!"),
                    ).arrange(DOWN, buff=0.55).scale(0.5)


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
        self.next_slide()

        self.play(ReplacementTransform(content, intro, run_time=0.5))
        self.next_slide()

        self.play(FadeOut(intro))
        self.clear()
        self.play(Write(warnings[0]))
        self.start_loop()
        self.play(Indicate(warnings[0], color=RED, scale_factor=1.5))
        self.play(Write(warnings[1:]))
        self.end_loop()
        return VGroup(warnings )

    
    def dom(self):
        rect = Rectangle(width=6, height=4, color=BLUE)
        text = Text("Body Text").scale(1.5)
        rect_text = VGroup(rect, text)
        rect_text.arrange(DOWN)
        rect_text.set_width(6)
        rect_text.set_height(3)
        rect_text.move_to(ORIGIN)

        # Create three divs nested below the rectangle
        div1 = Rectangle(width=2, height=1, color=YELLOW)
        id1 = Text("id1").scale(0.7).next_to(div1, DOWN)
        div1_id = VGroup(div1, id1).next_to(rect_text, DOWN, buff=0.5)

        div2 = Rectangle(width=2, height=1, color=YELLOW)
        id2 = Text("id2").scale(0.7).next_to(div2, DOWN)
        div2_id = VGroup(div2, id2).next_to(div1_id, DOWN, buff=0.5)

        div3 = Rectangle(width=2, height=1, color=YELLOW)
        id3 = Text("id3").scale(0.7).next_to(div3, DOWN)
        div3_id = VGroup(div3, id3).next_to(div2_id, DOWN, buff=0.5)

        # Add everything to the scene
        self.play(Create(rect_text))
        self.play(Create(div1_id))
        self.play(Create(div2_id))
        self.play(Create(div3_id))
        self.wait()
