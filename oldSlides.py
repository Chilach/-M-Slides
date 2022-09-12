from manim import *
import numpy as np
#As main idea The code will describe itself on the presentation

class slide1(Scene):
    def page1(self):

        title = MarkupText ( f'[M]Slides',
                font='Iosevka',
                font_size=30,
                color="#ffffff"
        )
        #move_to(x, y, z?)
        title.move_to([0., 0.5, 0.]).scale(4)
        authors = MarkupText ( f'Julian Mejia - Felipe Calderon',
            font='Iosevka',
            font_size=30,
            color="#ffff00"
        )
        authors.next_to(title, DOWN)
        self.add(
           title, authors
        )

    def construct(self):
        self.page1()

class slide2(Scene):
    #config.background_color = "#606060" #This config is global, only enable to compile the slide where it belongs
    def page2(self):
        title1 = MarkupText (
            f'[P]Sarmat Template',
            font='Iosevka',
            font_size=30,
            color="#ffff00"
        )
        title1.move_to([-4.0, 3.0, 0.,]).scale(1.5)
        bullet = MarkupText (
            '• This is a bullet\n• Another bullet\n• The last one',
            font='Iosevka',
            font_size=30,
            color=WHITE
        )
        bullet.next_to(title1, DOWN)

        imagelogo = SVGMobject("manim-logo").move_to([4.0, 1.0, 0.,]).scale(1.5)
        logocaption = MarkupText (
            f'Figure 1: Manim Logo',
            font='Iosevka',
            font_size=30,
            color=WHITE
        )
        logocaption.next_to(imagelogo, DOWN)
        self.add(
            title1, bullet,
            imagelogo, logocaption
        )
    def construct(self):
        self.page2()

class slide3(Scene):
    def page3(self):
        title1 = MarkupText (
            f'Equations',
            font='Iosevka',
            font_size=30,
            color="#ffff00"
        )
        title1.move_to([0.0, 3.0, 0.,]).scale(1.5)
        paragraph1 = MarkupText (
            f'Mathematics are Fun as the shit of newborns',
            font='Iosevka',
            font_size=30,
            color=RED
        )
        paragraph1.next_to(title1, DOWN)
        paragraph2 = MarkupText (
            f'Jhon Cena\' s most haded equation ',
            font='Iosevka',
            font_size=30,
            color=RED
        )
        mathtext = MathTex(
            r"\sin(x + \frac{\pi}{2}) = \cos(x)",
            font_size = 40
        )
        mathtext.next_to(paragraph2, DOWN)
        self.add(
            title1, paragraph1,
            paragraph2, mathtext
        )
    def construct(self):
        self.page3()

#paragraph slide (not recommended, kill the meeting)
class slide4(Scene):
    def page4(self):

        title1 = Tex(
            r"This is a title with \LaTeX",
            color = "#ffffff",
            font_size = 30
        ).move_to([0, 3, 0]).scale(2.5)

        equation1 = MathTex(
            r"e^x = x^0 + x^1 + \frac{1}{2} x^2 + \frac{1}{6} x^3 + \cdots + \frac{1}{n!} x^n + \cdots \tag{2}",
            substrings_to_isolate="x"
        ).set_color_by_tex("x", YELLOW).next_to(title1, DOWN).scale(0.8)

        subtitle1 = Text(
            "Title with Times New Roman",
            color = "#ffff00",
            font = "Times New Roman",
            font_size = 30
        ).move_to([0.0, 0.0, 0.0]).scale(2)

        paragraph = ""\
        "subtitle1 = Text("\
        "   \"Title with Times New Roman,\",\n"\
        "   color = \"#ffff00\",\n"\
        "   font = \"Times New Roman\",\n"\
        "   font_size = 30\n"\
        ").move_to([0.0, 0.0, 0.0]).scale(1)\n"\

        paragraph1 = MarkupText(
            paragraph,
            font='Iosevka',
            font_size=30,
            color="#00ff00"
        ).next_to(subtitle1, 2*DOWN).scale(1)

        self.add(
            title1,
            equation1,
            subtitle1,
            paragraph1
        )
    def construct(self):
        self.page4()















