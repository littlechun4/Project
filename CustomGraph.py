#!/usr/bin/python
# -*- coding: utf-8 -*-

import copy
import pyqtgraph as pg
from datetime import datetime
import time
from pyqtgraph import QtCore, QtGui

#정렬된 타임스탬프의 레인지를 입력받아 그 인덱스의 레인지를 출력해주는 코드
def getListRange(start, end, lst):

    m = 0
    n = len(lst)-1

    while (m <= n):
        
        if(lst[m] == start):
            s = m
            break
        elif(lst[n] == start):
            s = n
            break

        if (m+1 == n):
            s = m
            break

        l = int((m+n)/2)
        if(lst[l] > start):
            n = l
        elif(lst[l] < start):
            m = l
        else:
            s = l
            break

    m = 0
    n = len(lst)-1

    while (m <= n):

        if(lst[n] == end):
            e = n
            break
        elif(lst[m] == end):
            e = m
            break
        
        if(m+1 == n):
            e = n
            break

        l = int((m+n)/2)
        if(lst[l] > end):
            n = l
        elif(lst[l] < end):
            m = l
        else:
            e = l
            break

    return [s, e]

class CustomGraph(pg.GraphicsObject):       
    def __init__(self, data, widget_lst, times):

        #save data, stamp
        self.data = data
        self.times = times

        #recursive update에 사용됨
        self.pre_empt = 0

        #y's autorage level
        self.autorange = 1

        pg.GraphicsObject.__init__(self)
        self.region_lst = []
        self.old_region_lst = []
        self.y_min = []
        self.y_max = []
        for i in reversed(range(len(widget_lst))):
            if (i != 7):
                #axis = CustomAxis(orientation='bottom')
                #widget_lst[i].addItem(axis)
                widget_lst[i].plot(x=times, y=data)
                widget_lst[i].setXRange(*self.region_lst[6-i].getRegion(), padding=0)

                lst_range = getListRange(widget_lst[i].getViewBox().viewRange()[0][0], widget_lst[i].getViewBox().viewRange()[0][1], times)
                new_data = data[lst_range[0]:lst_range[1]+1]
                self.y_min += [min(new_data)]
                self.y_max += [max(new_data)]
                widget_lst[i].setYRange(min(new_data), max(new_data), padding=0)

                g_start = widget_lst[i].getViewBox().viewRange()[0][0]
                g_end = widget_lst[i].getViewBox().viewRange()[0][1]
                width = g_end - g_start
                region = pg.LinearRegionItem([g_start + 2*width/5, g_start + 3*width/5])
                region.setZValue(-10)
                widget_lst[i].addItem(region)
                self.region_lst.append(region)
                self.old_region_lst+=[[region.getRegion()[0], region.getRegion()[1]]]

            else:
                #axis = CustomAxis(orientation='bottom')
                #widget_lst[i].addItem(axis)
                widget_lst[i].plot(x=times, y=data)
                widget_lst[i].setXRange(times[0], times[len(times)-1], padding = 0)
                #widget_lst[i].setAutoPan(y=True)
                widget_lst[i].getViewBox().enableAutoRange(axis=widget_lst[i].getViewBox().YAxis, enable=self.autorange)
                self.y_min += [0]
                self.y_max += [0]

                time_interval = times[len(times)-1] - times[0]
                region = pg.LinearRegionItem([times[0] + 2*time_interval/5, times[0] + 3*time_interval/5])
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

#       self.region_lst[6].sigRegionChanged.connect(lambda: self.updatePlot(self.region_lst[6], widget_lst[6]))
#       widget_lst[6].sigXRangeChanged.connect(lambda: self.updateRegion(self.region_lst[6], widget_lst[6]))
#       self.region_lst[5].sigRegionChanged.connect(lambda: self.updatePlot(self.region_lst[5], widget_lst[5]))
#       widget_lst[5].sigXRangeChanged.connect(lambda: self.updateRegion(self.region_lst[5], widget_lst[5]))
#       self.region_lst[4].sigRegionChanged.connect(lambda: self.updatePlot(self.region_lst[4], widget_lst[4]))
#       widget_lst[4].sigXRangeChanged.connect(lambda: self.updateRegion(self.region_lst[4], widget_lst[4]))
#       self.region_lst[3].sigRegionChanged.connect(lambda: self.updatePlot(self.region_lst[3], widget_lst[3]))
#       widget_lst[3].sigXRangeChanged.connect(lambda: self.updateRegion(self.region_lst[3], widget_lst[3]))
#       self.region_lst[2].sigRegionChanged.connect(lambda: self.updatePlot(self.region_lst[2], widget_lst[2]))
#       widget_lst[2].sigXRangeChanged.connect(lambda: self.updateRegion(self.region_lst[2], widget_lst[2]))
#       self.region_lst[1].sigRegionChanged.connect(lambda: self.updatePlot(self.region_lst[1], widget_lst[1]))
#       widget_lst[1].sigXRangeChanged.connect(lambda: self.updateRegion(self.region_lst[1], widget_lst[1]))
#       self.region_lst[0].sigRegionChanged.connect(lambda: self.updatePlot(self.region_lst[0], widget_lst[0]))
#       widget_lst[0].sigXRangeChanged.connect(lambda: self.updateRegion(self.region_lst[0], widget_lst[0]))


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

            #다음 그래프와 X,Y레인지와 리젼을 바꾼다.
            if (next_level != 7):
                #cur_xrange = [widget_lst[next_level].getViewBox().viewRange[0][0], widget_lst[next_level].getViewBox().viewRange[0][0]]
                #X레인지 변환
                widget_lst[next_level].setXRange(*self.region_lst[level].getRegion(), padding=0)
                new_xrange = [widget_lst[next_level].getViewBox().viewRange()[0][0], widget_lst[next_level].getViewBox().viewRange()[0][1]]
                #Y레인지 변환
                
                #min, max값이 바뀌었는지에 대한 flag
                #flag = True
                
                #현재 X범위와 새로운 X범위가 겹침
                #if(cur_xrange[1] > new_xrange[0]):
                #   lst_range = getListRange(cur_xrange[1], new_xrange[1], self.times
                #   lst_range = getListRange(new_xrage[0], new_xrange[1], self.times)
            
                #now_min = widget_lst[next_level].getViewBox().
                
                lst_range = getListRange(new_xrange[0], new_xrange[1], self.times)
                new_data = self.data[lst_range[0]:lst_range[1]+1]

                self.y_min = min(new_data)
                self.y_max = max(new_data)

                widget_lst[next_level].setYRange(self.y_min, self.y_max, padding=0, update=True)

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

#       if (new_region[1] > g_end):
#           new_region[0] = g_end - (self.region_lst[8-level].getRegion()[1] - self.region_lst[8-level].getRegion()[0])
#           new_region[1] = g_end
#           self.region_lst[8-level].setRegion(new_region)
#           return False

        self.region_lst[8-level].setRegion(new_region)
        return True

class CustomAxis(pg.AxisItem):
    def tickStrings(self, values, scale, spacing):
        strns = []

        try:
            rng = max(values) - min(values)
            #if rng < 120:
            #    return pg.AxisItem.tickStrings(self, values, scale, spacing)
            if rng < 1000*60:
                string = '%Mm:%Ss '
            elif rng >= 1000*60 and rng < 1000*3600:
                string = '%Mm:%Ss'
            elif rng >= 1000*3600 and rng < 1000*3600*24:
                string = '%Hh:%Mm:%Ss'
            elif rng >= 1000*3600*24 and rng < 1000*3600*24*30:
                string = '%m/%d'
            elif rng >= 1000*3600*24*30 and rng < 1000*3600*24*30*24:
                string = '%Y/%m'
            elif rng >= 1000*3600*24*30*24:
                string = '%Y'
        except:
            string = '%Mm:%Ss'

        for x in values:
            try:
                if rng < 60:
                    strns.append(datetime.fromtimestamp(x/1000).strftime(string) + str(int(x % 1000)) + "ms")
                else:
                    strns.append(datetime.fromtimestamp(x/1000).strftime(string))
            except ValueError:  ## Windows can't handle dates before 1970
                strns.append('')# -*- coding: utf-8 -*-

        return strns
