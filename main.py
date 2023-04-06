from manim import *
# or: from manimlib import *
from manim_slides import Slide

class BasicExample(Slide):
    
    def smallwait(self):
        self.wait(0.3)
    
    def construct(self):
        SLIDES = [self.basics]

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
        return VGroup(warnings)

    def possibilities(self):
        square = Rectangle(height=7, width=10, color=ORANGE)
        ax = Axes(x_range=[-3, 3], x_length=15)
        curve = ax.plot(lambda x: np.sin(x), color=ORANGE)
        possibilities = VGroup(
                Text("Possibilities : ").scale(2.5),
                Text("We can create games"),
                Text("We can create animations"),
                Text("We can create websites, web apps"),
                Text("etc."),
                Text("You can do anything you want, ").scale(0.35),
                Text("if you know how to code it or masochism is your thing.").scale(0.35)
                    ).arrange(DOWN, buff=0.55).scale(0.85)
        links = VGroup(
                Text("https://greensock.com/").set_color(GREEN), 
                Text("https://github.com/").set_color(BLUE)
                    ).arrange(DOWN, buff=1.55).scale(1.5)
        self.play(Write(possibilities, run_time=4), Create(square, run_time=4))
        self.next_slide()
        self.play(FadeOut(square))
        self.smallwait()
        self.play(ReplacementTransform(possibilities, links, run_time=0.75))
        self.play(Create(curve, run_time=4))
        self.smallwait()
        self.play(FadeOut(curve))
        self.next_slide()
        return VGroup(links)

    def basics(self):
        code_var = Code (code=
            """
            <script>

                if (condition) {
                    var varVariable = "True";
                }

                console.log(varVariable);

                var varVariable = "False";

                console.log(varVariable);
            </script>""",
            language="javascript")
        
        code_let_err = Code (code=
            """
            <script>

                if (condition) {
                    let letVariable = "True";
                }

                console.log(letVariable);

                let letVariable = "False";

                console.log(letVariable);
            </script>""",
            language="javascript")
        
        code_let_ok = Code (code=
            """
            <script>

                if (condition) {
                    let letVariable = "True";
                    console.log(letVariable);
                }

                letVariable = "False";

            </script>""",
            language="javascript")
        
        code_const = Code (code=
            """
            <script>

                if (condition) {
                    const constVari = "True";
                    console.log(constVari);
                }

                constVari = "False";

            </script>""",
            language="javascript")
        
        letVSconst = VGroup( Text ("let = const ,"),
                             Text ("dar la const nu poate fi modificata valoarea")
                            ).arrange(DOWN).scale(0.5)
        arrows = VGroup(CurvedArrow(start_point=np.array([-1,0,0]),
                                     end_point=np.array([2,2,0])), 
                        CurvedArrow(start_point=np.array([-1,-1,0]),
                                     end_point=np.array([2,0,0])) 
                        )
        varGlobal = Text("var este globala").scale(0.5)
        varRedefine = Text("var poate fi redefinita").scale(0.5)
        dar = Text("Dar!").scale(1.5)
        varOld =  VGroup(
                        Text ("var este veche"),
                        Text ("si nu se utilizeaza in proiectele moderne")
                        ).arrange(DOWN).scale(0.5)
        errLet = Text("let nu poate fi folosita in afara blocului").scale(0.5).set_color(RED)
        errLetredefine = Text("let nu poate fi redefinita").scale(0.5).set_color(RED)
        stroke = Line(start=[2,-0.8,0], end=[6,-0.8,0], color=RED)

        self.clear()

        #plane = NumberPlane()
        #self.add(plane)

        self.play(Write(code_var))
        self.next_slide()

        self.play(code_var.animate.shift(LEFT*4))
        self.smallwait()
        self.play(Create(arrows[0]), Create(arrows[1]))
        self.play(varGlobal.animate.shift(UP*2.2+RIGHT*3))
        self.play(varRedefine.animate.shift(RIGHT*3.5+UP*0.2))
        self.next_slide()

        self.play(FadeIn(dar.move_to(RIGHT*3.5+DOWN))) #aici apare Varga
        self.play(FadeIn(varOld.move_to(RIGHT*3.5+DOWN*2)))
        self.next_slide()

        self.play(FadeOut(dar), FadeOut(varOld), FadeOut(arrows), FadeOut(varGlobal), FadeOut(varRedefine))
        #aici se poate baga foto cu js pe diferite browsere
        self.play(code_var.animate.shift(RIGHT*4))
        self.play(ReplacementTransform(code_var, code_let_err))
        self.play(code_let_err.animate.shift(LEFT*4))
        self.smallwait()
        self.play(Create(arrows[0]), Create(arrows[1]))
        self.play(FadeIn(errLet.move_to(UP*2.2+RIGHT*3)))
        self.play(FadeIn(errLetredefine.move_to(RIGHT*3.5+UP*0.2)))
        self.next_slide()

        self.play(FadeOut(arrows), FadeOut(errLet), FadeOut(errLetredefine))
        self.play(code_let_err.animate.shift(RIGHT*4))
        self.play(ReplacementTransform(code_let_err, code_let_ok)) #bug
        self.smallwait()
        code_let_err.remove
        self.next_slide()
        
        self.play(FadeOut(code_let_ok))
        self.play(Write(code_let_ok.move_to(LEFT*4)), Write(code_const.move_to(RIGHT*4)))
        self.play(FadeIn(letVSconst.move_to(DOWN*2.2)))
        self.next_slide()
        self.play(FadeOut(letVSconst))
        self.play(Create(stroke))
        self.next_slide()
        
        return VGroup(code_const, code_let_ok, stroke)

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
