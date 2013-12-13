import pyqtgraph as pg
import time
import datetime
from pyqtgraph import QtCore, QtGui

class CustomGraph(pg.GraphicsObject):
	def __init__(self, times, data, widget_lst):
		pg.GraphicsObject.__init__(self)
		self.region_lst = []
		for i in reversed(range(len(widget_lst))):
			if (i != 0 and i != 7):
				widget_lst[i].plot(x=times, y=data)
				widget_lst[i].setXRange(*self.region_lst[6-i].getRegion(), padding=0)

				g_start = widget_lst[i].getViewBox().viewRange()[0][0]
				g_end = widget_lst[i].getViewBox().viewRange()[0][1]
				width = g_end - g_start
				region = pg.LinearRegionItem([g_start + 2*width/5, g_start + 3*width/5])
				region.setZValue(-10)
				widget_lst[i].addItem(region)
				self.region_lst.append(region)

			elif (i == 7):
				widget_lst[i].plot(x=times, y=data)
				region = pg.LinearRegionItem([times[2*len(times)/5], times[3*len(times)/5]])
				region.setZValue(-10)
				widget_lst[i].addItem(region)
				self.region_lst.append(region)

			else:
				widget_lst[i].plot(x=times, y=data)
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

	def restoreRegion(self, width_lst):
		width_region_lst = zip(width_lst, self.region_lst)

		for (width, region) in width_region_lst:
			region.setRegion(width)

class CustomAxis(pg.AxisItem):
    def tickStrings(self, values, scale, spacing):
        strns = []
        rng = max(values)-min(values)
        #if rng < 120:
        #    return pg.AxisItem.tickStrings(self, values, scale, spacing)
        if rng < 3600:
			string = '%M:%S'
        elif rng >= 3600 and rng < 3600*24:
            string = '%H:%M:%S'
        elif rng >= 3600*24 and rng < 3600*24*30:
            string = '%d'
        elif rng >= 3600*24*30 and rng < 3600*24*30*24:
            string = '%m'
        elif rng >=3600*24*30*24:
            string = '%Y'
        for x in values:
            try:
                strns.append(time.strftime(string, time.localtime(x)))
            except ValueError:  ## Windows can't handle dates before 1970
                strns.append('')
                #self.setLabel(text=label)
        return strns
