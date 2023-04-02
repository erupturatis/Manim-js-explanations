from manim import *
from manim.opengl import *


class CreateCircle(Scene):
    idx = 0
    def construct(self):
        circle = Circle()  # create a circle
        circle.set_fill(PINK, opacity=0.5)  # set the color and transparency
        self.play(Create(circle))  # show the circle on screen
        self.interactive_embed()

    def state1(self):
        self.play(Write(Text("Hello World").scale(1)))
    
    def state2(self):
        self.play(Write(Text("Hllo 2").scale(2)))

    def on_key_press(self, symbol, modifiers):
        from pyglet.window import key
        if symbol == key.SPACE:
            if self.idx == 0:
                self.state1()
            
            if self.idx == 1:
                self.state2()
            self.idx += 1      
        
        super().on_key_press(symbol, modifiers)
