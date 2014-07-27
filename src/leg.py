from browser import svg, doc, html
TAKEONE = "../img/tk01.jpg"
BLOG = "../img/Blog2C.png"
ALIEN = "../img/alien0.png"
RLEG = "../img/Blogpernadireita.png"
RLX = "40px"
SPEECH = "../img/speech.png"

class LegTakeOne:
    def __init__(self, place):
        #self.img = svg.image(href=TAKEONE, x= "0px", y="0px",  width="1024px", lenght="860px")
        self.img = svg.image(href=TAKEONE, x= "0px", y="0px",  width="1024px", height="860px")
        place <= self.img

class Blog:
    def __init__(self, place):
        def set_target_x(ev):
            print(self.x, self.target_x)
            self.x = self.target_x
        self.x = 0
        it = self.it = svg.g(id="theblogguy", transform="translate(0,600)", className="hander")
        self.lleg = svg.image(href=RLEG, x= "50px", y="85px", width=RLX, height=RLX)
        self.rleg = svg.image(href=RLEG, x= "20px", y="85px", width=RLX, height=RLX)
        self.img = svg.image(href=BLOG, x= "0px", y="0px", width="100px", height="100px")
        self.go = svg.rect(id="theblog", x="0px", y="700px", width="1024px", height="40px")
        self.go.style.fillOpacity = 0.3
        self.go.onclick = self.goer
        self.tlk = svg.image(href=SPEECH, x= "40px", y="-90px", width="100px", height="100px")
        self.tlk.style.opacity = 0
        self.talk()
        place <= self.go
        place <= self.it
        it <= self.lleg
        it <= self.rleg
        it <= self.img
        it <= self.tlk
        it.onanimationend = set_target_x
        #it.onclick = self.walk
        self.ax = self.anim()
        self.ar = self.walk()
    def anim(self):
        def set_target_x(ev):
            print(self.x, self.target_x)
            self.x = self.target_x -80
        targ = 300
        dur = targ * 8
        animatex = self.anim = svg.animateTransform(
            attributeType="xml", attributeName="transform", begin="theblog.click",
            type="translate", to= "%d, 600" % targ, additive="replace", fill="freeze",
            dur="%dms" % dur, repeatCount="1")
        animatex.setAttribute("from", "%d, 600" % 0)
        animatex.onend = set_target_x
        self.it <= animatex
    def goer(self, ev=0):
        print(ev.clientX)
        targ = self.target_x = ev.clientX
        dur = targ * 4
        paces = (dur + 400) // 600
        self.anim.setAttribute("to", "%d, 600" % (targ - 80))
        self.anim.setAttribute("from", "%d, 600" % (self.x))
        self.anim.setAttribute("dur", "%dms" % dur)
        self.anirl.setAttribute("repeatCount", paces)
        self.anill.setAttribute("repeatCount", paces)
        self.speech.setAttribute("to", 50//abs(targ-400))
    def walk(self, ev=0):
        targ = 300
        pace = 30
        dur = targ *2
        rc = 15 //2
        animatex = self.anirl = svg.animateTransform(
            attributeType="xml", attributeName="transform", begin="theblog.click",
            type="translate", to= "%d, 0" % pace, additive="replace", fill="freeze",
            dur="%dms" % dur, repeatCount=rc)
        animatex.setAttribute("from", "%d, 0" % 0)
        self.rleg <= animatex
        animatex =  self.anill =svg.animateTransform(
            attributeType="xml", attributeName="transform", begin="theblog.click",
            type="translate", to= "%d, 0" % -pace, additive="replace", fill="freeze",
            dur="%dms" % dur, repeatCount=rc)
        animatex.setAttribute("from", "%d, 0" % 0)
        self.lleg <= animatex
    def talk(self):
        animateo = self.speech = svg.animate(id="animation1",
             attributeName="opacity",
             to="0", dur="2s",
             begin="0s;alien0.click")
        animateo.setAttribute("from", "0")
        self.tlk <= animateo



class Alien:
    def __init__(self, place):
        it = self.it = svg.g(id="alien0", transform="translate(400,600)", Class="hander")
        self.img = svg.image(href=ALIEN, x= "0px", y="0px", width="100px", height="120px")
        place <= self.it
        it <= self.img


class Leg:
    GAME = None
    def __init__(self):
        doc[html.HEAD][0] <= ".hander:hover {cursor: hand; cursor: pointer;}"
        #Leg.GAME = svg.svg(width="1024px", lenght="860px")
        Leg.GAME = svg.svg(width="1024", height="860")
        doc["main"] <= Leg.GAME
        LegTakeOne(Leg.GAME)
        Blog(Leg.GAME)
        Alien(Leg.GAME)

if __name__ == "__main__":
    print("LEG version 0.1")
    Leg()