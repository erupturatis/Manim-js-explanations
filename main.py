from manim import *
# or: from manimlib import *
from manim_slides import Slide

class BasicExample(Slide):
    
    def smallwait(self):
        self.wait(0.3)
    
    def construct(self):
        # finalArr = self.animConstructor(self.introduction, self.basics, self.domAndAnims) 
        # SLIDES = [*self.animConstructor(self.domAndAnims)]
        SLIDES = [*self.introduction(), *self.basics(), *self.domAndAnims()]

        for slide in SLIDES:
            Vmobjects = slide()
            self.play(FadeOut(Vmobjects)) 
            self.clear()

    def animConstructor(self, *args):
        arr = []
        for arg in args:
            arr = [*arr, *arg()]
        return arr
    
    def introduction (self):
        return [self.introduction, self.what_to_learn,
                self.js_detached_from_reality, self.possibilities,self.basics]
    
    def basics (self):
        return [self.basics] # continue with dom manipulation, animations, etc
    
    def domAndAnims(self):
        return [self.dom, self.anims, self.graphicalInterfaces]



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
        self.play(Write(warnings[1:]), run_time=4)
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

            {} + [];

            {} + {};

            [] + [];""",
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
        arr_obj = Text("'[object Object]'").set_color(GREEN)
        arr_arr = Text("''").scale(1.5).set_color(GREEN)
        obj_arr = Text("'[object Object]'").set_color(GREEN)
        obj_obj = Text("'[object Object][object Object]'").set_color(GREEN)
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
        self.play(Write(arr_obj.move_to(UP*2+LEFT*0.3)), Write(obj_arr.move_to(UP*0.8).align_to(arr_obj, LEFT)))
        self.next_slide()
        self.play(Write(obj_obj.move_to(DOWN*0.7).align_to(arr_obj, LEFT)))
        self.next_slide()
        self.play(Write(arr_arr.move_to(DOWN*2).align_to(arr_obj, LEFT)))
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

    def basicLag(self, time, *args):
        basicgr = VGroup(*args)
        self.play(Create(basicgr, lag_ratio = 0.2, run_time = time))
        return basicgr

    def dom(self):
        rect = Rectangle(width=3, height=2, color=BLUE)
        self.play(Create(rect))
        self.play(rect.animate.shift(LEFT*3 + UP*2))
        text = Text("html").scale(1)
        text.next_to(rect, UP)

        self.play(Write(text))
        self.next_slide()

        squarearr = [ Square(side_length=0.25, stroke_width=0.5, color=BLUE) for i in range(100) ]
        groupsquare = VGroup(*squarearr) 
        # arrange in grid 20x20
        groupsquare.arrange_in_grid(10,10)
        # move to center right
        groupsquare.move_to(RIGHT*3.5+UP*2)
        # create and add a slight delay between each animation
        self.play(Create(groupsquare, lag_ratio=0.2, run_time=6))
        self.next_slide()
        
        div1 = Rectangle(width=2, height=1, color=BLUE_A)
        div2 = Rectangle(width=2, height=1, color=BLUE_A)
        div3 = Rectangle(width=2, height=1, color=BLUE_A)

        div1.next_to(rect, DOWN, buff=1.25)
        
        div2.next_to(div1, LEFT, buff=1)
        div3.next_to(div1, RIGHT, buff=1)

        self.play(FadeOut(groupsquare))
        grdivs = self.basicLag(1, div1, div2, div3)
        # puts a text with id of div at the bottom of each div
        self.next_slide()
        iddiv1 = Text("#rosca").scale(0.5)
        iddiv2 = Text("#vasilepepe").scale(0.5)
        iddiv3 = Text("#varga").scale(0.5)

        iddiv1.next_to(div1, DOWN, buff=0.5)
        iddiv2.next_to(div2, DOWN, buff=0.5)
        iddiv3.next_to(div3, DOWN, buff=0.5)
        
        grids = self.basicLag(1, iddiv1, iddiv2, iddiv3)
        self.next_slide()
        # show function for working with the dom
        fn1dom = Code(code = """
            const div = document.getElementById("rosca");            
        """, language='javascript').scale(0.5)
        
        fn2dom = Code(code = """
            const div = document.getElementById("vasilepepe"); 
        """, language='javascript').scale(0.5)

        fn3dom = Code(code = """
            const div = document.getElementById("varga");
        """, language='javascript').scale(0.5)

        fn1dom.move_to(RIGHT*4 + UP*2)
        fn2dom.move_to(RIGHT*4 + UP*2)
        fn3dom.move_to(RIGHT*4 + UP*2)
        self.play(Write(fn1dom))

        self.play(ReplacementTransform(fn1dom, fn2dom))
        self.play(ReplacementTransform(fn2dom, fn3dom))

        self.next_slide()
        
        self.play(FadeOut(fn3dom))
        
        fn1query = Code(code = """ roscadiv = document.querySelector("#rosca"); """, language='javascript').scale(0.5)
        fn1getElementById = Code(code = """ roscadiv = document.getElementById("rosca"); """, language='javascript').scale(0.5)

        fn1query.move_to(RIGHT*4 + UP*2)
        fn1getElementById.next_to(fn1query, DOWN, buff=0.5)
        
        self.play(Write(fn1query))
        self.play(Write(fn1getElementById))
        
        self.next_slide()

        self.play(FadeOut(fn1getElementById))

        manipulateStyle = Code(code = """ rosca.style.backgroundColor = "red"; """, language='javascript').scale(0.5)
        manipulateClass = Code(code = """ rosca.classList.add("red"); """, language='javascript').scale(0.5)
        manipulateInnerHTML = Code(code = """ rosca.innerHTML = "mortimati inchid usa"; """, language='javascript').scale(0.5)

        manipulateStyle.next_to(fn1query, DOWN, buff=0.5)
        manipulateClass.next_to(manipulateStyle, DOWN, buff=0.5)
        manipulateInnerHTML.next_to(manipulateClass, DOWN, buff=0.5) 
        
        self.play(Write(manipulateStyle))
        self.play(Write(manipulateClass))
        self.play(Write(manipulateInnerHTML))
        self.next_slide()
        
        child = Code(code = """ 
        const babyrosca = document.createElement("div"); 
        babyrosca.classList.add("cevaoropsit");
        rosca.appendChild(babyrosca); 
           """, language='javascript').scale(0.5)
        
        child.next_to(manipulateInnerHTML, DOWN, buff=0.5)
        self.play(Write(child))
        self.next_slide()

    def anims(self):
        animTex = Text("Animations").scale(1.25)
        animTex.move_to(UP*2.5)
        self.play(Write(animTex))
        self.next_slide()
        # makes animTex smaller in scale and shifted up 
        self.play(animTex.animate.scale(0.5).shift(UP*1))

        transTex = Text("Transition").scale(0.75)
        keyframeTex = Text("Keyframes").scale(0.75)
        engineTex = Text("Animation Engine").scale(0.75)

        keyframeTex.next_to(animTex, DOWN, buff=1)
        transTex.next_to(keyframeTex, LEFT, buff=1)
        engineTex.next_to(keyframeTex, RIGHT, buff=1)
        self.play(Write(transTex), Write(keyframeTex), Write(engineTex))
        self.next_slide()
        # presents transition based animation
        self.play(engineTex.animate.scale(0.3).next_to(animTex, LEFT), keyframeTex.animate.scale(0.3).next_to(animTex, RIGHT), transTex.animate.scale(1).next_to(animTex, DOWN*1.5))
        self.next_slide()

        cssSquare = Code (code=
            """
            .square {
                width: 100px;
                height: 100px;
                position: absolute;
                transition: all 1s ease-in-out;
            }
                """,
            language="javascript").scale(0.5)

        cssStat1 = Code (code=
            """
.class1 {
  background-color: red;
  left: -100px;
}
                """,
            language="javascript").scale(0.5)

        cssStat2 = Code (code=
            """
.class2 {
  background-color: blue;
  left: 100px;
}
                """,
            language="javascript").scale(0.5)
        
        
        cssStat1.next_to(cssSquare, DOWN + LEFT, buff=0.5)
        cssStat2.next_to(cssSquare, DOWN + RIGHT, buff=0.5)

        self.play(Write(cssSquare), Write(cssStat1), Write(cssStat2))
        
        self.next_slide()
        
        jsCode = Code (code=
            """
            const button = document.querySelector('.mySexyButton');
            button.addEventListener("click", () => {
                const square = document.querySelector('.square');
                square.classList.remove('class1');
                square.classList.add('class2');
            });
            """,    
            language="javascript").scale(0.5)
        
        jsCode.next_to(cssSquare, DOWN, buff=0.75)
        self.play(Write(jsCode))

        self.next_slide()
        # unmounts transition and mounts keyframe animation
        # fades out all the code
        self.play( FadeOut(cssSquare), FadeOut(cssStat1), FadeOut(cssStat2), FadeOut(jsCode))
        self.play(transTex.animate.scale(0.3).next_to(animTex, LEFT), keyframeTex.animate.scale(10/3).next_to(animTex, DOWN*1.5), engineTex.animate.scale(1).next_to(animTex, RIGHT ))

        self.next_slide()

        cssSquare2 = Code (code=
            """
            .square {
                width: 100px;
                height: 100px;
                position: relative;
            }
                """,
            language="javascript").scale(0.5)
        cssSquare2.next_to(keyframeTex, DOWN, buff=0.5)
        
        trigger= Code (code = """
         .trigger {
            animation: classTransition 1s ease-in-out forwards;
         }

        @keyframes classTransition {
          from {
            background-color: red;
            left: -100px;
          }
          to {
            background-color: blue;
            right: -100px;
          }
        }
        """, language="javascript").scale(0.35) 
        
        trigger.next_to(cssSquare2, DOWN, buff=0.5)

        self.play(Write(cssSquare2), Write(trigger))
        self.next_slide()
        
        jsCode2 = Code (code=
            """
            const square = document.querySelector('.square');
            button.classList.add('trigger');
            """, language="javascript").scale(0.5)
        
        jsCode2.next_to(trigger, DOWN, buff=0.75)
        self.play(Write(jsCode2))
        
        self.next_slide()
        # unmounts keyframe and mounts animation engine
        # fades out all the code
        self.play( FadeOut(cssSquare2), FadeOut(trigger), FadeOut(jsCode2))
        self.play(transTex.animate.scale(1).next_to(animTex, LEFT), keyframeTex.animate.scale(0.3).next_to(animTex, RIGHT), engineTex.animate.scale(10/3).next_to(animTex, DOWN*1.5))
        
        animEnginesList = Text("Animejs, FramerMotion, etc ...").scale(0.5)
        animEnginesList.next_to(engineTex, DOWN, buff=0.3)
        self.play(Write(animEnginesList))
        
        exCodeEngine = Code (
            code = """ 
const square = document.querySelector('.square');

// uses animejs for animation
anime({
  targets: square,
  easing: 'easeInOutQuad',
  duration: 1000,
  background: ['red', 'blue'],
  translateX: ['-100px', '100px'],
  complete: function() {
    // Update the current class after the animation completes
    currentClass = 'class2';
  }
});
            """, language="javascript").scale(0.5)
        
        exCodeEngine.next_to(animEnginesList, DOWN, buff=0.75)
        self.play(Write(exCodeEngine))
        # fades out everything
        self.play(FadeOut(animEnginesList), FadeOut(exCodeEngine))
        # fades out the title and texts
        self.play(FadeOut(animTex), FadeOut(transTex), FadeOut(keyframeTex), FadeOut(engineTex))
        self.next_slide()
        
    def graphicalInterfaces(self):
        graphic = Text("graphical interafaces and animations").scale(0.8)
        graphic.move_to(UP*2.5)
        self.play(Write(graphic))
        self.next_slide()
        
        # creates canvas and svg texts and moves them to the right and left place
        
        canvasTex = Text("Canvas").scale(0.55)
        svgTex = Text("SVG").scale(0.55)
        canvasTex.next_to(graphic, DOWN)
        svgTex.next_to(graphic, DOWN )
        svgTex.shift(LEFT*3.5)
        canvasTex.shift(RIGHT*3.5)
        self.play(Write(canvasTex), Write(svgTex))
        
        svgCode = Code (code= 
            """
<svg width="100" height="100">
  <rect x="10" y="10" width="80" height="80" fill="red" />
  <circle cx="50" cy="50" r="40" fill="blue" />
  <path d="M10 10 L50 90 L90 10" stroke="black" stroke-width="2" fill="none" />
</svg>
            """, language="html").scale(0.35)
        
        svgCode.next_to(svgTex, DOWN, buff=0.25)
        svgPros = Text("Pros").scale(0.45)
        svgPros.next_to(svgCode, DOWN, buff=0.25)
        svgProsList = BulletedList("Scalability: SVG images are vector-based, meaning they can be scaled infinitely without losing resolution or quality",
                                    "Easy to animate and create interactive elements and effects ",
                                      "Doesn't need a complex state management system",
                                      "Very useful for real-tim data visualization and binding (e.g. d3.js)"
                                        ).scale(0.35)
        svgProsList.next_to(svgPros, DOWN, buff=0.25)
        self.play(Write(svgCode), Write(svgPros), Write(svgProsList))
        svgConsList = BulletedList("Complexity: SVG images can be more complex to create than other image formats such as PNG or JPEG. They require knowledge of vector graphics and can be more difficult to edit and modify.",
                                   "Performance: SVG images can be slow to load and render on older browsers and devices, particularly when they contain complex animations or effects."
                                   ).scale(0.35)
        svgCons = Text("Cons").scale(0.45)
        svgCons.next_to(svgProsList, DOWN, buff=0.25)
        svgConsList.next_to(svgCons, DOWN, buff=0.25)
        self.play(Write(svgCons), Write(svgConsList))

        # do the samething for canvas
        canvasCode = Code (code=
            """
                var canvas = document.getElementById("myCanvas");
                var ctx = canvas.getContext("2d");
                // Set initial position and velocity
                var x = 50;
                var y = 50;
                var vx = 2;
                var vy = 1;
                // Define animation function
                function animate() {
                  // Clear canvas
                  ctx.clearRect(0, 0, canvas.width, canvas.height);
                  // Draw circle
                  ctx.beginPath();
                  ctx.arc(x, y, 40, 0, 2 * Math.PI);
                  ctx.fillStyle = "blue";
                  ctx.fill();
                  x += vx;
                  y += vy;
                  requestAnimationFrame(animate);
                }
                animate();
            """, language="html").scale(0.35)
        
        canvasCode.next_to(canvasTex, DOWN, buff=0.25)
        canvasPros = Text("Pros").scale(0.45)
        canvasPros.next_to(canvasCode, DOWN, buff=0.25)
        canvasProsList = BulletedList("Performance: Canvas rendering is more performant than SVG especially for a large number of objects", 
                                      "You get granular control of every pixel on the canvas so you can do anything",
                                        "You can do things like 3d rendering with libraries like threejs").scale(0.35)
        canvasProsList.next_to(canvasPros, DOWN, buff=0.25)
        self.play(Write(canvasCode), Write(canvasPros), Write(canvasProsList))
        canvasConsList = BulletedList("Canvas requires a lot of code to do simple things and complex and good state management").scale(0.35)
        canvasCons = Text("Cons").scale(0.45)
        canvasCons.next_to(canvasProsList, DOWN, buff=0.25)
        canvasConsList.next_to(canvasCons, DOWN, buff=0.25)
        self.play(Write(canvasCons), Write(canvasConsList))
