from browser import svg, doc, html
TAKEONE = "../img/tk01.jpg"
BLOG = "../img/Blog2C.png"
RLEG = "../img/Blogpernadireita.png"
RLX = "40px"

class LegTakeOne:
    def __init__(self, place):
        #self.img = svg.image(href=TAKEONE, x= "0px", y="0px",  width="1024px", lenght="860px")
        self.img = svg.image(href=TAKEONE, x= "0px", y="0px",  width="1024px", height="860px")
        place <= self.img

class Blog:
    def __init__(self, place):
        it = self.it = svg.g(id="theblogguy", transform="translate(0,600)", className="hander")
        self.lleg = svg.image(href=RLEG, x= "50px", y="85px", width=RLX, height=RLX)
        self.rleg = svg.image(href=RLEG, x= "20px", y="85px", width=RLX, height=RLX)
        self.img = svg.image(href=BLOG, x= "0px", y="0px", width="100px", height="100px")
        self.go = svg.rect(id="theblog", x="0px", y="700px", width="1024px", height="40px")
        self.go.style.fillOpacity = 0.3
        self.go.onclick = self.goer
        place <= self.go
        place <= self.it
        it <= self.lleg
        it <= self.rleg
        it <= self.img
        #it.onclick = self.walk
        self.ax = self.anim()
        self.ar = self.walk()
    def anim(self):
        targ = 300
        dur = targ * 15
        animatex = self.anim = svg.animateTransform(
            attributeType="xml", attributeName="transform", begin="theblog.click",
            type="translate", to= "%d, 600" % targ, additive="replace", fill="freeze",
            dur="%dms" % dur, repeatCount="1")
        animatex.setAttribute("from", "%d, 600" % 0)
        self.it <= animatex
    def goer(self, ev=0):
        print(ev.clientX)
        targ = ev.clientX
        dur = targ * 15
        paces = (dur + 400) // 600
        self.anim.setAttribute("to", "%d, 600" % (targ - 80))
        self.anim.setAttribute("dur", "%dms" % dur)
        self.anirl.setAttribute("repeatCount", paces)
        self.anill.setAttribute("repeatCount", paces)
    def walk(self, ev=0):
        targ = 300
        pace = 30
        dur = targ*2
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


class Alien:
    def __init__(self, place):
        it = self.it = svg.g(transform="translate(400,600)", Class="hander")
        self.lleg = svg.image(href=RLEG, x= "50px", y="85px", width=RLX, height=RLX)
        self.rleg = svg.image(href=RLEG, x= "20px", y="85px", width=RLX, height=RLX)
        self.img = svg.image(href=BLOG, x= "0px", y="0px", width="100px", height="100px")
        place <= self.it
        it <= self.lleg
        it <= self.rleg
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