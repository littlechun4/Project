import pyqtgraph as pg
from pyqtgraph import QtCore, QtGui

class CustomGraph(pg.GraphicsObject):
	def __init__(self, data):
		pg.GraphicsObject.__init__(self)
		g = pg.plot(y=data)
		self.picture = QtGui.QPicture()
		region = pg.LinearRegionItem([30000, 70000])
		region.setZValue(10)

	def paint(self, p, *args):
		p.drawPicture(0, 0, self.picture)

	def boundingRect(self):
		return QtCore.QRectF(self.picture.boundingRect())
