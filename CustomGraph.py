import pyqtgraph as pg
from pyqtgraph import QtCore, QtGui

class CustomGraph(pg.GraphicsObject):
	def __init__(self, data, widget):
		pg.GraphicsObject.__init__(self)
		g = widget.plot(y=data)
		self.picture = QtGui.QPicture()
		region = pg.LinearRegionItem([20000, 30000])
		region.setZValue(10)
		widget.addItem(region)

	def paint(self, p, *args):
		p.drawPicture(0, 0, self.picture)

	def boundingRect(self):
		return QtCore.QRectF(self.picture.boundingRect())
