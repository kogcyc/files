
#from rt import *

def makeLINE(a,b,kolor="#f00",width="0",comment=""):
	return(f'\t\t<line x1="{a.x}" y1="{a.y}" x2="{b.x}" y2="{b.y}" style="stroke:{kolor};stroke-width:{width}" /> <!-- {comment} -->\n')

def makeCIRCLE(a,r=10,fill="#000",fillo="0.0",kolor="#f00",width="0",transform="",comment=""):
	return(f'\t\t<circle cx="{a.x}" cy="{a.y}" r="{r}" style="fill:{fill};fill-opacity:{fillo};stroke:{kolor};stroke-width:{width}" transform="{transform}" /> <!-- {comment} -->\n')

def makeCUBIC(a,b,c,d,fill="#000",fillo="0.0",kolor="#f00",width="8",comment=""):
	return(f'\t\t<path d="M{a.x},{a.y} C{c.x},{c.y} {d.x},{d.y} {b.x},{b.y}" style="fill:{fill};fill-opacity:{fillo};stroke:{kolor};stroke-width:{width}" /> <!-- {comment} -->\n')

def makeARC(a,b,r1,r2,q="0",thing="0 0",fill="#000",fillo="0.0",kolor="#f00",width="8",comment=""):
	return(f'\t\t<path d="M{a.x},{a.y} A {r1} {r2} {q} {thing} {b.x},{b.y}" style="fill:{fill};fill-opacity:{fillo};stroke:{kolor};stroke-width:{width}" /> <!-- {comment} -->\n')

def startPATH(a):
	return(f'\t\t<path d="M{a.x},{a.y} ')

def pathLINETO(a):
	return(f'L{a.x},{a.y} ')

def pathARCTO(a,r1,r2,thing="0 0 1"):
	return(f'A {r1} {r2} {thing} {a.x},{a.y} ')

def pathQTO(q,a):
	return(f'Q {q.x},{q.y} {a.x},{a.y} ')

def endPATH(fill="#000",fillo="1.0",kolor="#f00",width="0",comment=""):
	return(f'Z" style="fill:{fill};fill-opacity:{fillo};stroke:{kolor};stroke-width:{width}" /> <!-- {comment} -->\n')

def makeSVG(svgmiddle):

	svgwidth = 1056
	svgheight = 816
	scalex = 3.77953
	scaley = 3.77953
	translatex = 1056 / 2 / 3.77953
	translatey = -816 / 2 / 3.77953
	transformtranslate = f'{translatex},{translatey}'

	svgtop = f'''<?xml version="1.0" encoding="UTF-8"?>\n
<!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.1//EN" "http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd">\n
<svg xmlns="http://www.w3.org/2000/svg" version="1.1" width="{svgwidth}" height="{svgheight}" viewBox="0 0 {svgwidth} {svgheight}">\n
<rect width="{svgwidth}" height="{svgheight}" style="fill:rgb(255,255,255);stroke-width:0" />\n
\t<g transform="scale({scalex},-{scaley}) translate({transformtranslate})">\n\n'''

	svgbottom = f'''\n\t</g>\n
</svg>\n'''

	return(svgtop+svgmiddle+svgbottom)



