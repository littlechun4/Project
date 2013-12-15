#!/usr/bin/python
# -*- coding: utf-8 -*-

import copy
import pyqtgraph as pg
from datetime import datetime
import time
from bisect import bisect_left
from pyqtgraph import QtCore, QtGui


def getListRange(start, end, lst):
    '''정렬된 타임스탬프의 레인지를 입력받아 그 인덱스의 레인지를 출력해주는 코드'''

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
                #그래프를 그리고 XRange를 설정
                widget_lst[i].plot(x=times, y=data)
                widget_lst[i].setXRange(*self.region_lst[6-i].getRegion(), padding=0)

                #XRange를 포함하는 Data의 index range를 구함
                lst_range = getListRange(widget_lst[i].getViewBox().viewRange()[0][0], widget_lst[i].getViewBox().viewRange()[0][1], times)
                new_data = data[lst_range[0]:lst_range[1]+1]

                #Min, Max값을 구하고 이에 따른 YRange 설정
                widget_lst[i].setYRange(min(new_data), max(new_data), padding=0)

                #초기 Region설정
                g_start = widget_lst[i].getViewBox().viewRange()[0][0]
                g_end = widget_lst[i].getViewBox().viewRange()[0][1]
                width = g_end - g_start

                region = pg.LinearRegionItem([g_start + 2*width/5, g_start + 3*width/5])
                region.setZValue(-10)
                widget_lst[i].addItem(region)
                self.region_lst.append(region)
                self.old_region_lst+=[[region.getRegion()[0], region.getRegion()[1]]]

            else:
                #그래프를 그리고 XRange를 설정
                widget_lst[i].plot(x=times, y=data)
                widget_lst[i].setXRange(times[0], times[len(times)-1], padding = 0)
                #widget_lst[i].getViewBox().enableAutoRange(axis=widget_lst[i].getViewBox().YAxis, enable=self.autorange)
                
                #YRange 설정
                widget_lst[i].setYRange(min(data), max(data), padding=0)

                time_interval = times[len(times)-1] - times[0]
                #초기 Region설정
                region = pg.LinearRegionItem([times[0] + 2*time_interval/5, times[0] + 3*time_interval/5])
                region.setZValue(-10)
                widget_lst[i].addItem(region)
                self.region_lst.append(region)
                self.old_region_lst+=[[region.getRegion()[0], region.getRegion()[1]]]
            
        self.region_lst.reverse()

        # move의 정도를 계산하기 위해 예전 region값을 넣어 놓는다.
        self.old_region_lst.reverse()

        #region이 변했을 때 자동으로 updatePlot이 불려지도록 연결시켜놓는다.
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

    
    def updatePlot(self, level, widget_lst):

        '''하나의 region이 변했을 때 자동으로 불러져서 변경사항을 처리함'''

        #lock이 걸려있으면 동작하지 않음
        if (self.pre_empt == 1):
            return
        
        #lock on
        self.pre_empt = 1

        left_move = self.region_lst[level].getRegion()[0] - self.old_region_lst[level][0]
        right_move = self.region_lst[level].getRegion()[1] - self.old_region_lst[level][1]

        # 리전의 넓이가 변하지 않음 -> It's Scroll!
        if(left_move==right_move):

            for level in range(level, 0, -1):

                #다음레벨 계산
                next_level = level - 1

                if (next_level==-1):
                    next_level = 7

                # region이 얼마나 움직였는지 계산.
                cur_move = left_move
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
                    lst_range = getListRange(new_xrange[0], new_xrange[1], self.times)
                    new_data = self.data[lst_range[0]:lst_range[1]+1]

                    widget_lst[next_level].setYRange(min(new_data), max(new_data), padding=0, update=True)

                #다음 레벨의 Region변환 self.pre_empt가 설정되어 있으므로 트리거는 X!
                self.region_lst[next_level].setRegion(next_region)
                
        #region의 넓이가 변함 -> It's not Scroll!
        else:
            #가장 상위 레벨의 그래프일때는 리전이 변환되어도 아무런 일도 안함
            if(level != 0):
                next_level = level - 1

                #old_region_lst update
                cur_region = self.region_lst[level].getRegion()
                self.old_region_lst[level][0] = cur_region[0]
                self.old_region_lst[level][1] = cur_region[1]
                #Region에 맞게 X레인지 변환
                widget_lst[next_level].setXRange(*cur_region, padding=0)
                new_xrange = [widget_lst[next_level].getViewBox().viewRange()[0][0], widget_lst[next_level].getViewBox().viewRange()[0][1]]
                #범위에 맞게 Y레인지 변환
                lst_range = getListRange(new_xrange[0], new_xrange[1], self.times)
                new_data = self.data[lst_range[0]:lst_range[1]+1]

                widget_lst[next_level].setYRange(min(new_data), max(new_data), padding=0, update=True)

        #lock off
        self.pre_empt = 0

    def updateRegion(self, region, connect_graph):
        region.setRegion(connect_graph.getViewBox().viewRange()[0])

    def restoreRegion(self, width_lst):
        width_region_lst = zip(width_lst, self.region_lst)

        for (width, region) in width_region_lst:
            region.setRegion(width)

    
    def scroll(self, widget, level, vel, curve_arrow):
        ''' Scroll을 처리한다.
        타이머에 의해 250ms마다 한번씩 호출됨
        level = 1 ~ 8'''
        #시작, 끝의 범위를 지정한다.
        g_start = widget.getViewBox().viewRange()[0][0]
        g_end = widget.getViewBox().viewRange()[0][1]
        
        #0.25초 단위로 움직임
        one_step = vel*250

        #한번 Scroll후의 region 계산
        new_region = [self.region_lst[8-level].getRegion()[0] + one_step, self.region_lst[8-level].getRegion()[1] + one_step]

        #Region범위를 벗어나면 스크롤을 멈춘다.
        if(new_region[1] > g_end):
            return False

        #CurveArrow도 같이 움직임
        region_mid = (new_region[0] + new_region[1])/2
        new_index = bisect_left(self.times, region_mid)
        if(curve_arrow != 0):
            curve_arrow.setIndex(new_index)
        #print(new_pos)
#       if (new_region[1] > g_end):
#           new_region[0] = g_end - (self.region_lst[8-level].getRegion()[1] - self.region_lst[8-level].getRegion()[0])
#           new_region[1] = g_end
#           self.region_lst[8-level].setRegion(new_region)
#           return False


        #새로운 Region을 적용한다 -> 자동으로 updatePlot함수 호출!
        self.region_lst[8-level].setRegion(new_region)
        return True

    def parameterScroll(self, target_x, widget_lst):
        '''ROI와 Arrow가 double click되었을 때 대상이 가운데에 오도록 Region과 Xrange를 조정'''
        if(self.pre_empt == 1):
            return

        self.pre_empt = 1

        #target_x(ROI, Arrow의 좌표)가 가운데로 올 수 있도록 각 레벨의 Region과 XRange를 조정한다.
        for i in range(7, -1, -1):
            region_mid = (self.region_lst[i].getRegion()[0] + self.region_lst[i].getRegion()[1])/2
            self.region_lst[i].setRegion([self.region_lst[i].getRegion()[0] + (target_x - region_mid), self.region_lst[i].getRegion()[1] + (target_x - region_mid)])

            #최상위 레벨의 경우 XRange를 변환시키지 않음!
            if(i != 0):
                #Region에 맞게 X레인지 변환
                widget_lst[i-1].setXRange(*self.region_lst[i].getRegion(), padding=0)
                new_xrange = [widget_lst[i-1].getViewBox().viewRange()[0][0], widget_lst[i-1].getViewBox().viewRange()[0][1]]
                #범위에 맞게 Y레인지 변환
                lst_range = getListRange(new_xrange[0], new_xrange[1], self.times)
                new_data = self.data[lst_range[0]:lst_range[1]+1]

                widget_lst[i-1].setYRange(min(new_data), max(new_data), padding=0, update=True)


        self.pre_empt = 0

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
