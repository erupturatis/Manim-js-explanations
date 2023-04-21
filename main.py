from manim import *
# or: from manimlib import *
from manim_slides import Slide

class BasicExample(Slide):
    
    def smallwait(self):
        self.wait(0.3)
    
    def construct(self):
        SLIDES = [self.introduction, self.what_to_learn,
                self.js_detached_from_reality, self.possibilities,self.basics]

        for slide in SLIDES:
            Vmobjects = slide()
            self.play(FadeOut(Vmobjects)) 
            self.clear()
    
    def sectiunea_1 (self):
        return [self.introduction, self.what_to_learn,
                self.js_detached_from_reality, self.possibilities]
    
    def sectiunea_2 (self):
        return [self.basics] # continue with dom manipulation, animations, etc

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
        self.next_slide()
        
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
    
    def what_to_learn(self):
        intro = VGroup( Text("What should").scale(2.5),
                        Text("you learn").scale(2.5)).arrange(DOWN, buff=0.55)
        img1 = ImageMobject("html_logo.png").scale(1.2)
        img2 = ImageMobject("css_logo.png").scale(0.27)
        img3 = ImageMobject("react_logo.png").scale(0.35)
        img4 = ImageMobject("nodejs_logo.png").scale(0.25)
        img5 = ImageMobject("tailwind_logo.png")

        img6 = ImageMobject("babel_logo.png").scale(0.3)
        img7 = ImageMobject("webpack_logo.png").scale(0.25)
        img8 = ImageMobject("mysql_logo.png").scale(0.3)
        img9 = ImageMobject("vitejs-logo.png").scale(0.3)
        img10 = ImageMobject("nginx_logo.png").scale(0.3)
        gr = Group()
        gr.add(img1, img2, img3, img4, img5, img6, img7, img8, img9, img10)
        gr.arrange_in_grid(2, 5, buff=0.5).scale_to_fit_width(15)
        gr.move_to([0.4,0.2,0])

        txt = Text("E putin si usor!!! \U0001F609").scale(1.5)

        self.play(Write(intro))
        self.next_slide()
        self.play(FadeOut(intro))
        self.play(AnimationGroup(*[FadeIn(img) for img in gr], lag_ratio=0.5, rate_func=rush_into))
        self.smallwait()
        self.play(Write(txt))
        self.next_slide()
        self.play(FadeOut(gr))
        return VGroup(txt)
    
    def js_detached_from_reality(self):
        code_js = Code (code= 
            """
            [] + {};

            [] + [];

            {} + {};

            {} + [];""",
            language="javascript",
            background_stroke_width=0,
            font_size=48)
        code_js_bool = Code (code=
            """
            0 == '0';

            0 == [];

            [] == '0';""",
            language="javascript",
            background_stroke_width=0,
            font_size=60)
        code_js_arith = Code (code=
            """
            const x = 1 + '1';

            const y = 1 - '1';

            const z = +[];
            
            ('b' + 'a'+ +'a' + 'a').toLowerCase();""",
            language="javascript",
            background_stroke_width=0,
            font_size=48)
        arr_obj = Text("'[object object]'").set_color(GREEN)
        arr_arr = Text("''").scale(1.5).set_color(GREEN)
        obj_arr = Text("0").scale(2.5).set_color(RED_A)
        obj_obj = Text("'[object object][object object]'").set_color(GREEN)
        txt_true = Text("True").scale(2.5).set_color(GREEN)
        txt_true2 = Text("True").scale(2.5).set_color(GREEN)
        txt_false = Text("False").scale(2.5).set_color(RED_A)
        txt_x = Text("x = '11'").scale(1.5).set_color_by_gradient(DARK_BLUE, GREEN)
        txt_y = Text("y = 0").scale(1.5).set_color_by_gradient(DARK_BLUE, GREEN)
        txt_z = Text("z = 0").scale(1.5).set_color_by_gradient(DARK_BLUE, GREEN)
        txt_banana = Text("'banana'").scale(1.5).set_color_by_gradient(YELLOW, YELLOW_D, YELLOW)

        code_js.to_edge(LEFT, buff=0.5)
        self.play(Write(code_js))
        self.next_slide()
        self.play(Write(arr_obj.move_to(UP*2+LEFT*0.3)))
        self.next_slide()
        self.play(Write(arr_arr.move_to(UP*0.8).align_to(arr_obj, LEFT)))
        self.next_slide()
        self.play(Write(obj_obj.move_to(DOWN*0.7).align_to(arr_obj, LEFT)))
        self.next_slide()
        self.play(Write(obj_arr.move_to(DOWN*2).align_to(arr_obj, LEFT)))
        self.next_slide()
        self.play(FadeOut(arr_obj), FadeOut(arr_arr), FadeOut(obj_arr), FadeOut(obj_obj))
        self.play(ReplacementTransform(code_js, code_js_bool.to_edge(LEFT, buff=0.5)))
        self.play(Write(txt_true.next_to(code_js_bool, RIGHT, buff=0.85).align_to(code_js_bool, UP)))
        self.play(Write(txt_true2.next_to(code_js_bool, RIGHT, buff=0.85)))
        self.next_slide()
        self.play(Write(txt_false.next_to(code_js_bool, RIGHT, buff=0.85).align_to(code_js_bool, DOWN)))
        self.next_slide()
        self.play(FadeOut(txt_true), FadeOut(txt_true2), FadeOut(txt_false))
        self.play(ReplacementTransform(code_js_bool, code_js_arith.to_edge(LEFT, buff=0.5)))
        self.next_slide()
        self.play(Write(txt_x.move_to(UP*2+RIGHT*3)))
        self.next_slide()
        self.play(Write(txt_y.move_to(UP*0.8).align_to(txt_x, LEFT)))
        self.next_slide()
        self.play(Write(txt_z.move_to(DOWN*0.5).align_to(txt_x, LEFT)))
        self.next_slide()
        self.play(Write(txt_banana.next_to(code_js_arith, DOWN, buff=0.35)))
        self.next_slide()


        return VGroup(code_js_arith, txt_x, txt_y, txt_z, txt_banana)

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
        intro_basic = Text ("Now lets get down on business").scale(1.5).set_color_by_gradient(RED, DARK_BLUE, RED)
        intro_basic2 = Text ("We will start with the basics").scale(1.5).set_color_by_gradient(ORANGE, DARK_BLUE, ORANGE)
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
        img = ImageMobject("robert_varga_bg").scale(0.75)
        varOld =  VGroup(
                        Text ("var este veche"),
                        Text ("si nu se utilizeaza in proiectele moderne")
                        ).arrange(DOWN).scale(0.5)
        errLet = Text("let nu poate fi folosita in afara blocului").scale(0.5).set_color(RED)
        errLetredefine = Text("let nu poate fi redefinita").scale(0.5).set_color(RED)
        stroke = Line(start=[2,-0.8,0], end=[6,-0.8,0], color=RED)
        for_loops = Text("for loops").scale(1.5)
        for_classic = Text("for clasic")
        for_of = Text("for of")
        for_each_ef = Text("for each + arrow function")
        for_each = Text("for each")
        for_in = Text("for in + object.values")

        code_for_classic = Code (code=
            """
                const arr = ['JS', 'is', 'inCurCat']
                
                for (let i = 0; i < arr.length; i++) {
                    console.log(arr[i]);
                }""",
            language="javascript")
        code_for_of = Code (code=
            """
                const arr = ['JS', 'is', 'inaCurate']
                
                for (let i = 0; i < arr.length; i++) {
                    console.log(arr[i]);
                }
                
                for (const e of arr) {
                    console.log(e);
                }""",
            language="javascript")
        code_for_each_ef = Code (code=
            """
                const arr = ['JS', 'is', 'accurate']
                
                for (let i = 0; i < arr.length; i++) {
                    console.log(arr[i]);
                }
                
                arr.forEach(e => console.log(e));

                for (const e of arr) {
                    console.log(e);
                }""",
            language="javascript")
        code_for_each = Code (code=
            """
                const arr = ['JS', 'is', 'interesting']
                
                for (let i = 0; i < arr.length; i++) {
                    console.log(arr[i]);
                }
                
                arr.forEach(console.log(e));

                for (const e of arr) {
                    console.log(e);
                }""",
            language="javascript")
        code_for_in = Code (code=
            """
                const NotArray = {primul: 'Ion', alDoilea: 'Jason', alTreilea : 'Vasile'}
                
                for (const key in NotArray) {
                    console.log(NotArray[key]);
                }
                
                for (const e of Object.values(NotArray)) {
                    console.log(e);
                }""",
            language="javascript")

        self.clear()

        self.play(Write(intro_basic))
        self.wait(2)
        self.play(ReplacementTransform(intro_basic, intro_basic2))
        self.next_slide()

        self.play(FadeOut(intro_basic2))
        self.clear()
        self.play(Write(code_var))
        self.next_slide()

        self.play(code_var.animate.shift(LEFT*4))
        self.smallwait()
        self.play(Create(arrows[0]), Create(arrows[1]))
        self.play(varGlobal.animate.shift(UP*2.2+RIGHT*3))
        self.play(varRedefine.animate.shift(RIGHT*3.5+UP*0.2))
        self.next_slide()

        self.play(FadeIn(dar.move_to(RIGHT*3.5+DOWN)),
                  img.move_to(RIGHT*10+DOWN*5).rotate(0.75).animate.shift(LEFT*4+UP*2))
        self.wait(1)
        self.play(img.animate.shift(RIGHT*4+DOWN*2).rotate(-0.75))
        self.play(FadeOut(img), FadeIn(varOld.move_to(RIGHT*3.5+DOWN*2)))
        self.next_slide()

        self.play(FadeOut(dar), FadeOut(varOld), FadeOut(arrows), FadeOut(varGlobal), FadeOut(varRedefine))
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
        self.play(ReplacementTransform(code_let_err, code_let_ok))
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

        self.play(FadeOut(code_let_ok), FadeOut(code_const), FadeOut(stroke))
        self.play(Write(for_loops.move_to(UP*2.2)))
        self.play(Write(code_for_classic))
        self.play(FadeOut(for_loops))
        self.play(Write(for_classic.move_to(UP*2.2)))
        self.next_slide()
        self.play(FadeOut(for_classic))
        self.play(ReplacementTransform(code_for_classic, code_for_of))
        self.play(Write(for_of.move_to(UP*2.2)))
        self.next_slide()
        self.play(FadeOut(for_of))
        self.play(ReplacementTransform(code_for_of, code_for_each_ef))
        self.play(Write(for_each_ef.move_to(UP*2.4)))
        self.next_slide()
        self.play(FadeOut(for_each_ef))
        self.play(ReplacementTransform(code_for_each_ef, code_for_each))
        self.play(Write(for_each.move_to(UP*2.4)))
        self.next_slide()
        self.play(FadeOut(for_each))
        self.play(ReplacementTransform(code_for_each, code_for_in))
        self.play(Write(for_in.move_to(UP*2.2)))
        self.next_slide()
        
        return VGroup(code_for_in, for_in)

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
