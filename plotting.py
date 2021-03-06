# -*- coding: utf-8 -*-
"""
Created on Thu Dec 15 08:52:57 2016
@author: DoctaWong
"""
'''
x = cards 
y = performance
'''

import pylab

def performance_plot():
  '''
  Plots PassMark scores of flagship Nvidia video cards, 2010 to 2016
  '''
  year = [2010, 2011, 2012, 2014, 2015, 2016]
  high_end = [4353, 5014, 5694, 7987, 9588, 11983]
  mid_range = [3604, 4411, 5374, 6107, 8572, 10989]
  
  #axis labeling
  pylab.title('Quadratic Growth of Video Card Performance Per Year')
  pylab.ylabel('PassMark Score')
  pylab.xlabel('Year')
  pylab.ylim([0,15000])
  
  #plots data for high end and mid range video cards
  pylab.plot(year,high_end, 'ro')
  pylab.plot(year,mid_range, 'bo')
  
  #creates and plots a curve for high end video cards
   a, b, c = pylab.polyfit(year, high_end, 2)
  high_end_curve = a*pylab.array(year)**2 + b*pylab.array(year) + c
  pylab.plot(year, high_end_curve, 'r-', label = 'high end')

  #creates and plots a curve for low end video cards
  a, b, c = pylab.polyfit(year, mid_range, 2)
  mid_range_curve = a*pylab.array(year)**2 + b*pylab.array(year) + c
  pylab.plot(year, mid_range_curve, 'b-', label = 'mid range')
  pylab.legend(loc = "lower right")
