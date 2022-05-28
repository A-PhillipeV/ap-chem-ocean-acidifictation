#from pickletools import decimalnl_long
from cProfile import label
from decimal import Decimal
from chanim import *
from manim import *
config.background_color = WHITE # a mistake that must be done

class IntroToGases(Scene):
    def construct(self):
        factory = ImageMobject("C:/Manim/manim-main/Pictures/factory_png.png").scale(.5).to_edge(DL).shift(2*UP)

        ground = VGroup(
            Line(start=10*LEFT, stroke_width = 25,color = BLACK).shift(1.5*DOWN),
            Line(start=.9*RIGHT, end = 3*DOWN + 5*RIGHT, stroke_width = 25, color = BLACK).shift(1.5*DOWN),
        )
        water = Polygon([1,-1.5,0],[5,-4.5,0],[8,-4.5,0],[8,-1.5,0]).set_fill(BLUE_A, 1)
        #plane = Axes(color = BLACK)


        decimal_a = DecimalNumber()
        value_a = ValueTracker(0.001)
        background_infomation = VGroup(
            VGroup(
                Tex("t ="),
                decimal_a,
            ).arrange(RIGHT),
            Tex("dt= 10 yr/s"),
        ).arrange(DOWN).to_edge(UR).set_color(BLACK)


        concentrations = Group(
            MathTex("M[CO_{2}]:"),
            DecimalNumber(.0935, num_decimal_places=4)
        ).arrange(RIGHT).next_to(factory, RIGHT).set_color(BLACK)
        value_b = ValueTracker(.0935)

        math_shit = Group(
            MathTex(r"\frac{mol}{L}=\frac{ppm}{1000*\frac{g}{mol}}=\frac{}{1000*44.01}").scale(.65),
        ).next_to(concentrations, DOWN).shift(RIGHT).set_color(BLACK)
        ppm = DecimalNumber(412.5).scale(.65).next_to(math_shit[0][0][21], .5*UP).set_color(BLACK)
        value_c = ValueTracker(412.5)


        decimal_a.add_updater(lambda x: decimal_a.set_value(value_a.get_value()))
        ppm.add_updater(lambda z: ppm.set_value(value_c.get_value()+10))
        concentrations[1].add_updater(lambda y: concentrations[1].set_value(value_c.get_value()/(1000*44.01)))
        co2 = Group(
            MathTex("CO_2").scale(.5).set_color(BLACK).shift(2*UP),
            MathTex("CO_2").scale(.5).set_color(BLACK).shift(UR),
            MathTex("CO_2").scale(.5).set_color(BLACK).shift(2*UR),
            MathTex("CO_2").scale(.5).set_color(BLACK).shift(1.5*UL),
            MathTex("CO_2").scale(.5).set_color(BLACK).shift(3*LEFT+1*UP),
            
            MathTex("CO_2").scale(.5).set_color(BLACK).shift(3*UP+RIGHT),
            MathTex("CO_2").scale(.5).set_color(BLACK).shift(4.5*UR),
            MathTex("CO_2").scale(.5).set_color(BLACK).shift(3.5*UR),
            MathTex("CO_2").scale(.5).set_color(BLACK).shift(3*UL),
            MathTex("CO_2").scale(.5).set_color(BLACK).shift(6*LEFT+1*UP),
        ).set_color(WHITE)
        #self.add(factory,ground, water, background_infomation, concentrations, math_shit, ppm, co2)


        self.play(
            FadeIn(
                Group(factory, ground, water, background_infomation)
            )
        )
        self.wait(3)
        self.play(
            FadeIn(Group(concentrations), shift=UP),
            FadeIn(Group(math_shit, ppm), shift=LEFT),
        )
        self.wait(3)
        self.play(
            AnimationGroup(value_a.animate.set_value(100),rate_func = linear),
            AnimationGroup(value_b.animate.set_value(10), rate_func = rush_into),
            AnimationGroup(value_c.animate.set_value(412.5*1.12**10), rate_func = linear),

            co2.animate(run_time=10).shift(4*UP).set_color(BLACK),
            run_time = 10,
        )
        self.wait(4)

class ReactionEquation(Scene):
    def construct(self):

        #chem stuff
        chem_eq = MathTex(r"CO_2+H_2O+CO_3^{2-}\rightleftharpoons 2HCO_3^-").set_color(BLACK).to_edge(UP).scale(1.75)
        co2_fig = ChemObject(r"O=C=O").next_to(chem_eq[0][1], 1.5*DOWN).set_color(BLACK)
        h2o_fig = ChemObject(r"H-[:30]O-[:-30]H}").set_color(BLACK)
        co3_fig = ChemObject(r"O=C(-[1]O^{-})-[7]O^{-}").set_color(BLACK)
        hco3_1 = ChemObject(r"H-O-[1]C(=[2]O)-[7]O^{-}").set_color(BLACK)
        hco3_2 = ChemObject(r"H-O-[1]C(-[2]O^{-})=[7]O").set_color(BLACK)

        #rxn
        reactants = Group(co2_fig, h2o_fig, co3_fig).arrange(RIGHT, buff=1).next_to(chem_eq[0][5],DOWN)
        products = Group(hco3_1, hco3_2).scale(.75).arrange(DOWN).next_to(chem_eq[0][16], DOWN)

        #imgs
        factory = ImageMobject("C:/Manim/manim-main/Pictures/factory_png.png").scale(.275).next_to(co2_fig[0][3],DOWN)
        ocean = ImageMobject("C:/Manim/manim-main/Pictures/ocean.jpg").scale(.75).next_to(h2o_fig[0][2], 2*DOWN)
        
        self.play(
            Write(chem_eq)
        )
        self.wait()
        self.play(
            FadeIn(reactants, shift=UP, lag_ratio = .75),
            FadeIn(products, shift=LEFT, lag_ratio = .75),
            run_time=3
        )
        self.wait()
        self.play(
            FadeIn(Group(factory,ocean, Tex("?").next_to(co3_fig[0][3],5*DOWN).set_color(BLACK).scale(5)), shift=UP, lag_ratio=2),
            run_time = 4
        )
        self.wait(2)

class FocusCO3(Scene):
    def construct(self):
        co3 = MathTex("[CO_3^{2-}]").scale(2.5).set_color(BLACK).to_edge(RIGHT)
        
        graphs = ImageMobject("C:/Manim/manim-main/Pictures/co3_graph.png").scale(1.25)
        animals = Group(
            ImageMobject("C:/Manim/manim-main/Pictures/dinoflag.jpg").scale(.75).to_edge(RIGHT),
            ImageMobject("C:/Manim/manim-main/Pictures/mullusc.jpg").scale(.1).to_edge(RIGHT).shift(2*DOWN),
        )

        infographics = VGroup(
            Text("Dinoflagates \"live almost exclusively in estuaries and along the shores in shallow water\"").set_color(BLACK).scale(.375).next_to(graphs,DOWN).shift(2*LEFT),
            MathTex(r"\text{Average annual } [CO_3^{2-}] \text{ in (c) Atlantic and (d) Indopacific basins.}").set_color(BLACK).scale(.35).next_to(graphs,UP).shift(2*LEFT),
        )
        eq = MathTex(r"CaCO_3 \rightleftharpoons Ca^+ + CO_3^{2-}").set_color(BLACK).next_to(graphs,UP).shift(2*LEFT)
        self.wait()
        self.play(
            FadeIn(co3, shift=LEFT, run_time=2)
        )
        self.wait()
        self.play(
            FadeIn(graphs.shift(2*LEFT)),
            FadeIn(infographics[1], shift=DOWN)
        )
        self.wait(2)
        self.play(
            co3.animate.shift(2*UP),
            FadeIn(animals, lag_ratio=2),
            FadeIn(infographics[0], shift=UP),

            run_time = 6
        )
        self.wait(2)
        self.play(
            FadeOut(infographics[1]),
            FadeIn(eq, shift=DOWN)
        )
        self.wait(5)

class pHLogs(Scene):
    def construct(self):
        ph_eq = MathTex(r"pH=-log[H^+]=-log[H_3O^+]").set_color(BLACK)

        ax = Axes(
            x_range=[0, 6, 1],
            y_range=[0, 14, 2],
            tips=False,
            y_axis_config={"include_numbers": True},
        ).set_color(BLACK)


        ax_2 = Axes(
            x_range=[0, 1, 1],
            y_range=[0, 14, 2],
            tips=False,
            y_axis_config={"include_numbers": True},
        ).set_color(BLACK)

        # x_min must be > 0 because log is undefined at 0.
        graph = ax.plot(lambda x: -1*np.log(x), x_range=[0.000001,10, 0.001], use_smoothing=False).set_color(BLACK)
        graph_2 = ax_2.plot(lambda x: -1*np.log(x), x_range=[0.000001,10, 0.001], use_smoothing=False).set_color(BLACK)
        self.wait()
        self.play(Write(ph_eq))
        self.wait(2)
        self.play(
            Write(ax),
            ph_eq.animate.to_edge(UP),
        )
        self.wait(2)
        self.play(
            Create(graph),
        )
        self.wait(2)
        self.play(
            Transform(ax,ax_2),
            Transform(graph, graph_2),
        )
        self.wait(2)
        derivatove = MathTex(r"\frac{d }{dpH}=-\frac{1}{[H^+/H_3O^+]}").set_color(BLACK).next_to(ph_eq, DOWN).set_color(RED)
        graph_3 = ax_2.plot(lambda x: -1/x, x_range=[0.000001,10, 0.001], use_smoothing=False).set_color(RED)
        self.play(
            FadeIn(derivatove, shift=DOWN),
            Create(graph_3)
        )
        self.wait(3)


class doverdPh(Scene):
    def construct(self):
        derivatove = MathTex(r"\frac{d }{dpH}=-\frac{1}{[H^+/H_3O^+]}").set_color(BLACK)
        framebox1 = SurroundingRectangle(derivatove[0][:4], buff = .1).set_color(RED)
        framebox2 = SurroundingRectangle(derivatove[0][9:], buff = .1).set_color(GREEN)

        #self.add(index_labels(derivatove[0]))
        label1 = Tex("Rate of change of pH").scale(.75).next_to(derivatove[0][3], DOWN).set_color(BLACK)
        label2 = Tex("Concentration of ions").scale(.5).next_to(derivatove[0][13], 1.5*DOWN).set_color(BLACK)

        mod_eq = VGroup(
            DecimalNumber(1/100).scale(2),
            MathTex(r"=|\text{ }-\frac{1}{}\space \text{    }|"),
        ).arrange(RIGHT).set_color(BLACK)
        #mod_eq[1].shift(.25*DOWN+.5*RIGHT)
        #mod_eq[0].shift(2*LEFT+.5**DOWN)
        cH = DecimalNumber(100,num_decimal_places=4).set_color(BLACK).next_to(mod_eq[1][0][3], DOWN)
        mod_eq.add(cH).next_to(derivatove, DOWN)
        cH.shift(.5*RIGHT)
        mod_eq.shift(DOWN)
        mod_eq[1].shift(.5*RIGHT)

        conc = ValueTracker(100)
        cH.add_updater(lambda x: cH.set_value(conc.get_value()))
        mod_eq[0].add_updater(lambda x: mod_eq[0].set_value(1/conc.get_value())).shift(.5*DOWN+2*LEFT)
        
        #mod_eq[1].always

        self.wait(2)
        self.play(
            Write(derivatove)
        )
        self.wait(2)
        self.play(
            Create(framebox2),
            FadeIn(label2, shift=UP)
        )
        self.wait()
        self.play(
            Create(framebox1),
            FadeIn(label1, shift=UP)
        )
        self.wait(2)
        self.play(
            FadeIn(mod_eq, shift=UP)
        )
        self.wait()
        self.play(
            conc.animate(run_time=7).set_value(.0001)
        )
        self.wait(2)



