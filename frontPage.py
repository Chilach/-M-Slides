from manim import *

black =        '#282c34'
white =        '#abb2bf'
light_red =    '#e06c75'
dark_red =     '#be5046'
green =        '#98c379'
light_yellow = '#e5c07b'
dark_yellow =  '#d19a66'
blue =         '#61afef'
magenta =      '#c678dd'
cyan =         '#56b6c2'
gutter_grey =  '#4b5263'
light_grey =   '#5c6370'

class slide1(Scene):
    def page1(self):

        self.camera.background_color = black

        title = Tex(
            r'[M]Slides Project',
            color = blue,
            font_size = 100
        ).move_to([0, 3, 0])

        subtitle = Tex(
            r'Python Slides to Replace \LaTeX\ Beamer',
            color = white,
            font_size = 60
        ).next_to(title, DOWN)

        authorname1 = Tex(
            r'Felipe Calderón',
            color = blue,
            font_size = 70
        )

        faculty1 = Tex(
            r'Faculty of Physics',
            color = light_red,
            font_size = 40
        ).next_to(authorname1, DOWN)

        uni1 = Tex(
            r"Universidad del Valle",
            color = light_red,
            font_size = 40
        ).next_to(faculty1, DOWN)

        authorname2 = Tex(
            r'Julian Mejía',
            color = blue,
            font_size = 70
        ).next_to(authorname1, 4*RIGHT)

        faculty2 = Tex(
            r'Faculty of Mathematics',
            color = light_red,
            font_size = 40
        ).next_to(authorname2, DOWN)

        uni2 = Tex(
            r"Universidad del Valle",
            color = light_red,
            font_size = 40
        ).next_to(faculty2, DOWN)

        date = Tex(
            r'Nüremberg Conference, April 2022',
            color = white,
            font_size = 50
        )

        author1 = VGroup(authorname1, faculty1, uni1)
        author2 = VGroup(authorname2, faculty2, uni2)

        authors = VGroup(author1, author2).next_to(subtitle, 3*DOWN)

        date.next_to(authors, 5*DOWN)

        self.add(
            title,
            subtitle,
            authors,
            date
        )
    def construct(self):
        self.page1()
