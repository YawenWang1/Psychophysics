#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 16 14:35:05 2022

@author: yawen
"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rcParams
DestPth = "/media/g/P04/Psychophysics/"

Lum_Decre_pt37 =  [0.10227273, 0.008556703, 0.08530823, 0.11923722]

Lum_Incre_pt37 =  [-0.07227273, 0.008556703,-0.08923722,-0.05530823]


Lum_Decre_pt76 = [0.11688312, 0.0076992, 0.10167023, 0.132096008]

Lum_Incre_pt76 = [-0.02337662, 0.0076992, -0.03858951, -0.008163732]

rcParams['font.family'] = 'sans-serif'
rcParams['font.sans-serif'] = ['Arial']
# figPth='/media/g/P01/Review/Figures/'
rc={'font.size': 9.0,
 'axes.labelsize': 12.0,
 'axes.titlesize': 11.0,
 'xtick.labelsize': 11.0,
 'ytick.labelsize': 11.0,
 'legend.fontsize': 9.0,
 'axes.linewidth': 1.25,
 'grid.linewidth': 1.0,
 'lines.linewidth': 2.0,
 'lines.markersize': 5.0,
 'patch.linewidth': 1.0,
 'xtick.major.width': 2,
 'ytick.major.width': 2,
 'xtick.minor.width': 1.0,
 'ytick.minor.width': 1.0,
 'xtick.major.size': 2.0,
 'ytick.major.size': 2.0,
 'xtick.minor.size': 1.0,
 'ytick.minor.size': 1.0,
 'legend.title_fontsize': 10.0}


fig = plt.figure(dpi=300)

plt.rcParams.update(**rc)
ax = plt.subplot(111)
ax.bar(['Lum Decre', 'Lum Incre'],[Lum_Decre_pt37[0],Lum_Incre_pt37[0]],
        color=['dimgray','lightgray'],edgecolor='k')
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
plt.ylim([-0.15,0.21])
for i, p in enumerate(ax.patches):
    print(i, p) 
    x0 = p.get_x()
    w = p.get_width()
    h = p.get_height()
    if i == 0:  # select which dictionary to use
         d = Lum_Decre_pt37 
    else:
         d =  Lum_Incre_pt37   
    min_y = d[2]
    max_y = d[3]
    # plt.axvline(x+w/2, min_y, max_y, color='k',linewidth=2)  
    # Plot 95% CI
    plt.vlines(x=x0+w/2, ymin=min_y, ymax=max_y, colors='k')
    # Plot SE
    # plt.errorbar(x=x0+w/2,y=d[0],yerr=d[2],color='k',capsize=5)
    
plt.ylabel("Change of Perceived Luminance")
# statistical annotation
x1, x2 = 0, 1   # columns 'Sat' and 'Sun' (first column: 0, see plt.xticks())
y, h, col = np.max([Lum_Decre_pt37[0],Lum_Incre_pt37[0]]) + 0.04, 0.02, 'k'
plt.plot([x1, x1, x2, x2], [y, y+h, y+h, y], lw=2, c=col)
plt.text((x1+x2)*.5, y+h, "***", ha='center', va='bottom', color=col,fontsize=14) 
plt.savefig(DestPth + 'All_sub_lum_stat_pt37.png',dpi=300)
plt.savefig(DestPth + 'All_sub_lum_stat_pt37.svg',dpi=300)


fig = plt.figure(dpi=300)

plt.rcParams.update(**rc)
ax = plt.subplot(111)
ax.bar(['Lum Decre', 'Lum Incre'],[Lum_Decre_pt76[0],Lum_Incre_pt76[0]],
        color=['dimgray','lightgray'],edgecolor='k',label=['Lum Decre', 'Lum Incre'])
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
plt.ylim([-0.15,0.21])
for i, p in enumerate(ax.patches):
    print(i, p) 
    x0 = p.get_x()
    w = p.get_width()
    h = p.get_height()
    if i == 0:  # select which dictionary to use
         d = Lum_Decre_pt76 
    else:
         d =  Lum_Incre_pt76   
    min_y = d[2]
    max_y = d[3]
    # plt.axvline(x+w/2, min_y, max_y, color='k',linewidth=2)  
    # Plot 95% CI
    plt.vlines(x=x0+w/2, ymin=min_y, ymax=max_y, colors='k')
    # Plot SE
    # plt.errorbar(x=x0+w/2,y=d[0],yerr=d[2],color='k',capsize=5)
# statistical annotation
x1, x2 = 0, 1   # columns 'Sat' and 'Sun' (first column: 0, see plt.xticks())
y, h, col = np.max([Lum_Decre_pt76[0],Lum_Incre_pt76[0]]) + 0.04, 0.02, 'k'
plt.plot([x1, x1, x2, x2], [y, y+h, y+h, y], lw=2, c=col)
plt.text((x1+x2)*.5, y+h, "***", ha='center', va='bottom', color=col,fontsize=14)    
plt.ylabel("Change of Perceived Luminance")
plt.savefig(DestPth + 'All_sub_lum_stat_pt76.png',dpi=300)
plt.savefig(DestPth + 'All_sub_lum_stat_pt76.svg',dpi=300)



