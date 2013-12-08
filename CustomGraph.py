#!/usr/bin/python
# -*- coding: utf-8 -*-

import copy
import pyqtgraph as pg
from pyqtgraph import QtCore, QtGui

class CustomGraph(pg.GraphicsObject):
	def __init__(self, data, widget_lst):

		#recursive update에 사용됨
		self.pre_empt = 0

		pg.GraphicsObject.__init__(self)
		self.region_lst = []
		self.old_region_lst = []
		for i in reversed(range(len(widget_lst))):
			if (i != 7):
				widget_lst[i].plot(y=data)
				widget_lst[i].setXRange(*self.region_lst[6-i].getRegion(), padding=0)

				g_start = widget_lst[i].getViewBox().viewRange()[0][0]
				g_end = widget_lst[i].getViewBox().viewRange()[0][1]
				width = g_end - g_start
				region = pg.LinearRegionItem([g_start + 2*width/5, g_start + 3*width/5])
				region.setZValue(-10)
				widget_lst[i].addItem(region)
				self.region_lst.append(region)
				self.old_region_lst+=[[region.getRegion()[0], region.getRegion()[1]]]

			else:
				widget_lst[i].plot(y=data)
				region = pg.LinearRegionItem([2*len(data)/5, 3*len(data)/5])
				region.setZValue(-10)
				widget_lst[i].addItem(region)
				self.region_lst.append(region)
				self.old_region_lst+=[[region.getRegion()[0], region.getRegion()[1]]]
			
		self.region_lst.reverse()

		# move의 정도를 계산하기 위해 예전 region값을 넣어 놓는다.
		self.old_region_lst.reverse()

		self.region_lst[7].sigRegionChanged.connect(lambda: self.updatePlot(7, widget_lst))
		self.region_lst[6].sigRegionChanged.connect(lambda: self.updatePlot(6, widget_lst))
		self.region_lst[5].sigRegionChanged.connect(lambda: self.updatePlot(5, widget_lst))
		self.region_lst[4].sigRegionChanged.connect(lambda: self.updatePlot(4, widget_lst))
		self.region_lst[3].sigRegionChanged.connect(lambda: self.updatePlot(3, widget_lst))
		self.region_lst[2].sigRegionChanged.connect(lambda: self.updatePlot(2, widget_lst))
		self.region_lst[1].sigRegionChanged.connect(lambda: self.updatePlot(1, widget_lst))
		self.region_lst[0].sigRegionChanged.connect(lambda: self.updatePlot(0, widget_lst))

#		self.region_lst[6].sigRegionChanged.connect(lambda: self.updatePlot(self.region_lst[6], widget_lst[6]))
#		widget_lst[6].sigXRangeChanged.connect(lambda: self.updateRegion(self.region_lst[6], widget_lst[6]))
#		self.region_lst[5].sigRegionChanged.connect(lambda: self.updatePlot(self.region_lst[5], widget_lst[5]))
#		widget_lst[5].sigXRangeChanged.connect(lambda: self.updateRegion(self.region_lst[5], widget_lst[5]))
#		self.region_lst[4].sigRegionChanged.connect(lambda: self.updatePlot(self.region_lst[4], widget_lst[4]))
#		widget_lst[4].sigXRangeChanged.connect(lambda: self.updateRegion(self.region_lst[4], widget_lst[4]))
#		self.region_lst[3].sigRegionChanged.connect(lambda: self.updatePlot(self.region_lst[3], widget_lst[3]))
#		widget_lst[3].sigXRangeChanged.connect(lambda: self.updateRegion(self.region_lst[3], widget_lst[3]))
#		self.region_lst[2].sigRegionChanged.connect(lambda: self.updatePlot(self.region_lst[2], widget_lst[2]))
#		widget_lst[2].sigXRangeChanged.connect(lambda: self.updateRegion(self.region_lst[2], widget_lst[2]))
#		self.region_lst[1].sigRegionChanged.connect(lambda: self.updatePlot(self.region_lst[1], widget_lst[1]))
#		widget_lst[1].sigXRangeChanged.connect(lambda: self.updateRegion(self.region_lst[1], widget_lst[1]))
#		self.region_lst[0].sigRegionChanged.connect(lambda: self.updatePlot(self.region_lst[0], widget_lst[0]))
#		widget_lst[0].sigXRangeChanged.connect(lambda: self.updateRegion(self.region_lst[0], widget_lst[0]))


		self.picture = QtGui.QPicture()
						
	def paint(self, p, *args):
		p.drawPicture(0, 0, self.picture)

	def boundingRect(self):
		return QtCore.QRectF(self.picture.boundingRect())

	# loop로 동작하여 모든 level의 그래프를 업데이트함
	def updatePlot(self, level, widget_lst):
		
		#lock이 걸려있으면 동작하지 않음
		if (self.pre_empt == 1):
			return

		#lock on
		self.pre_empt = 1

		for level in range(level, 0, -1):

			next_level = level - 1

			if (next_level==-1):
				next_level = 7

			# region이 얼마나 움직였는지 계산.
			cur_move = self.region_lst[level].getRegion()[0] - self.old_region_lst[level][0]
			next_move = cur_move

			# 다음 그래프의 리젼을 계산
			next_region = [self.region_lst[next_level].getRegion()[0] + next_move, self.region_lst[next_level].getRegion()[1] + next_move]

			#old_region_lst update
			cur_region = self.region_lst[level].getRegion()
			self.old_region_lst[level][0] = cur_region[0]
			self.old_region_lst[level][1] = cur_region[1]

			#다음 그래프와 레인지와 리젼을 바꾼다.
			if (next_level != 7):
				widget_lst[next_level].setXRange(*self.region_lst[level].getRegion(), padding=0)
			self.region_lst[next_level].setRegion(next_region)

		#lock off
		self.pre_empt = 0

	def updateRegion(self, region, connect_graph):
		region.setRegion(connect_graph.getViewBox().viewRange()[0])

	def restoreRegion(self, width_lst):
		width_region_lst = zip(width_lst, self.region_lst)

		for (width, region) in width_region_lst:
			region.setRegion(width)

	# Scroll function
	# operace once per 50ms
	# level = 1 ~ 8

	def scroll(self, widget, level, degree):

		runthrough_time = [5, 10, 20]
		vel = runthrough_time[degree]
		g_start = widget.getViewBox().viewRange()[0][0]
		g_end = widget.getViewBox().viewRange()[0][1]

		one_step = ((g_end - g_start) / vel) * 0.05
		#print(one_step)

		new_region = [self.region_lst[8-level].getRegion()[0] + one_step, self.region_lst[8-level].getRegion()[1] + one_step]

#		if (new_region[1] > g_end):
#			new_region[0] = g_end - (self.region_lst[8-level].getRegion()[1] - self.region_lst[8-level].getRegion()[0])
#			new_region[1] = g_end
#			self.region_lst[8-level].setRegion(new_region)
#			return False

		self.region_lst[8-level].setRegion(new_region)
		return True
