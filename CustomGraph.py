import pyqtgraph as pg
from pyqtgraph import QtCore, QtGui

class CustomGraph(pg.GraphicsObject):
	def __init__(self, data, widget_lst):
		pg.GraphicsObject.__init__(self)
		self.region_lst = []
		for i in reversed(range(len(widget_lst))):
			if (i != 0 and i != 7):
				widget_lst[i].plot(y=data)
				widget_lst[i].setXRange(*self.region_lst[6-i].getRegion(), padding=0)

				g_start = widget_lst[i].getViewBox().viewRange()[0][0]
				g_end = widget_lst[i].getViewBox().viewRange()[0][1]
				width = g_end - g_start
				region = pg.LinearRegionItem([g_start + 2*width/5, g_start + 3*width/5])
				region.setZValue(-10)
				widget_lst[i].addItem(region)
				self.region_lst.append(region)

			elif (i == 7):
				widget_lst[i].plot(y=data)
				region = pg.LinearRegionItem([2*len(data)/5, 3*len(data)/5])
				region.setZValue(-10)
				widget_lst[i].addItem(region)
				self.region_lst.append(region)

			else:
				widget_lst[i].plot(y=data)
				widget_lst[i].setXRange(*self.region_lst[6-i].getRegion(), padding=0)
			
		self.region_lst.reverse()

		self.region_lst[6].sigRegionChanged.connect(lambda: self.updatePlot(self.region_lst[6], widget_lst[6]))
		widget_lst[6].sigXRangeChanged.connect(lambda: self.updateRegion(self.region_lst[6], widget_lst[6]))
		self.region_lst[5].sigRegionChanged.connect(lambda: self.updatePlot(self.region_lst[5], widget_lst[5]))
		widget_lst[5].sigXRangeChanged.connect(lambda: self.updateRegion(self.region_lst[5], widget_lst[5]))
		self.region_lst[4].sigRegionChanged.connect(lambda: self.updatePlot(self.region_lst[4], widget_lst[4]))
		widget_lst[4].sigXRangeChanged.connect(lambda: self.updateRegion(self.region_lst[4], widget_lst[4]))
		self.region_lst[3].sigRegionChanged.connect(lambda: self.updatePlot(self.region_lst[3], widget_lst[3]))
		widget_lst[3].sigXRangeChanged.connect(lambda: self.updateRegion(self.region_lst[3], widget_lst[3]))
		self.region_lst[2].sigRegionChanged.connect(lambda: self.updatePlot(self.region_lst[2], widget_lst[2]))
		widget_lst[2].sigXRangeChanged.connect(lambda: self.updateRegion(self.region_lst[2], widget_lst[2]))
		self.region_lst[1].sigRegionChanged.connect(lambda: self.updatePlot(self.region_lst[1], widget_lst[1]))
		widget_lst[1].sigXRangeChanged.connect(lambda: self.updateRegion(self.region_lst[1], widget_lst[1]))
		self.region_lst[0].sigRegionChanged.connect(lambda: self.updatePlot(self.region_lst[0], widget_lst[0]))
		widget_lst[0].sigXRangeChanged.connect(lambda: self.updateRegion(self.region_lst[0], widget_lst[0]))


		self.picture = QtGui.QPicture()
						
	def paint(self, p, *args):
		p.drawPicture(0, 0, self.picture)

	def boundingRect(self):
		return QtCore.QRectF(self.picture.boundingRect())

	def updatePlot(self, region, connect_graph):
		connect_graph.setXRange(*region.getRegion(), padding=0)

	def updateRegion(self, region, connect_graph):
		region.setRegion(connect_graph.getViewBox().viewRange()[0])
