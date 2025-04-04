"""
This example shows how to insert text into a scene using TextItem. This class 
is for displaying text that is anchored to a particular location in the data
coordinate system, but which is always displayed unscaled. 

For text that scales with the data, use QTextItem. 
For text that can be placed in a layout, use LabelItem.
"""

import numpy as np

import pyqtgraph as pg
from pyqtgraph.Qt import QtCore

x = np.linspace(-20, 20, 1000)
y = np.sin(x) / x
plot = pg.plot()   ## create an empty plot widget
plot.setYRange(-1, 2)
plot.setWindowTitle('pyqtgraph example: text')
curve = plot.plot(x,y)  ## add a single curve

## Create text object, use HTML tags to specify color/size
text = pg.TextItem(html='<div style="text-align: center"><span style="color: #d1d4dc;">This is the</span><br><span style="color: #FF0; font-size: 16pt;">PEAK</span></div>', anchor=(-0.3,0.5), angle=45, border='w', fill=(0, 0, 255, 100))
plot.addItem(text)
text.setPos(0, y.max())

## Draw an arrowhead next to the text box
arrow = pg.ArrowItem(pos=(0, y.max()), angle=-45)
plot.addItem(arrow)


## Set up an animated arrow and text that track the curve
curvePoint = pg.CurvePoint(curve)
plot.addItem(curvePoint)
text2 = pg.TextItem("test", anchor=(0.5, -1.0))

text2.setParentItem(curvePoint)
arrow2 = pg.ArrowItem(angle=90)
arrow2.setParentItem(curvePoint)

## update position every 10ms
index = 0
def update():
    global curvePoint, index
    index = (index + 1) % len(x)
    curvePoint.setPos(float(index)/(len(x)-1))
    text2.setPos(x[index], y[index])
    text2.setText('[%0.1f, %0.1f]' % (x[index], y[index]))
    
timer = QtCore.QTimer()
timer.timeout.connect(update)
timer.start(10)

if __name__ == '__main__':
    pg.exec()
