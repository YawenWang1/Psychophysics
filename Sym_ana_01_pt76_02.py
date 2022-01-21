#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 21:34:53 2019
# #############################################################################
# Event type
# --------------------------------------------------------------------------
# Event 1: Probing area Height: 3, Width: 12  inducers: down
# Event 2: Probing area Height: 4, Width: 12  inducers: down
# Event 3: Probing area Height: 5, Width: 12  inducers: down
# Event 4: Probing area Height: 6, Width: 12  inducers: down
# Event 5: Probing area Height: 3, Width: 3 , loc : left, inducers: down
# Event 6: Probing area Height: 4, Width: 4 , loc : left, inducers: down
# Event 7: Probing area Height: 5, Width: 5 , loc : left, inducers: down
# Event 8: Probing area Height: 6, Width: 6 , loc : left, inducers: down
# Event 9: Probing area Height: 6, Width: 6 , loc : right, inducers: down
# Event 10: Probing area Height: 6, Width: 6 , loc : right, inducers: down
# Event 11: Probing area Height: 6, Width: 6 , loc : right, inducers: down
# Event 12: Probing area Height: 6, Width: 6 , loc : right, inducers: up
# Event 13: Probing area Height: 3, Width: 12  inducers: up
# Event 14: Probing area Height: 4, Width: 12  inducers: up
# Event 15: Probing area Height: 5, Width: 12  inducers: up
# Event 16: Probing area Height: 6, Width: 12  inducers: up
# Event 17: Probing area Height: 3, Width: 3 , loc : left, inducers: up
# Event 18: Probing area Height: 4, Width: 4 , loc : left, inducers: up
# Event 19: Probing area Height: 5, Width: 5 , loc : left, inducers: up
# Event 20: Probing area Height: 6, Width: 6 , loc : left, inducers: up
# Event 21: Probing area Height: 6, Width: 6 , loc : right, inducers: up
# Event 22: Probing area Height: 6, Width: 6 , loc : right, inducers: up
# Event 23: Probing area Height: 6, Width: 6 , loc : right, inducers: up
# Event 24: Probing area Height: 6, Width: 6 , loc : right, inducers: up
# --------------------------------------------------------------------------
# Event:[ 1 -4 & 13-16] repeat 20 times
# Event:[ 5 -12 & 17-24] repeat 10 times
# #############################################################################
@author: wangyawen
"""

import os
import csv
import glob
import numpy as np
# the module to plot
import seaborn as sns
# the module to re-organize the data
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import rcParams
import pingouin as pg
TxtPth = "/media/g/P04/Psychophysics/0.76/"

os.chdir(TxtPth)
All_Cond = np.hstack([np.arange(1,12).astype(int),np.arange(13,24).astype(int)])
Cond_01  = [int(x) for i in range(2) for x in range(1,12)]
TxtFiles = glob.glob(TxtPth + '*.txt')
AllCsvs = []
AllSortedCond = []
left_cond = [5,6,7,8,17,18,19,20]

# Since condition 12 and 24 are the same, so remove 12 and 24 in the analysis
# right_cond = [9,10,11,12,21,22,23,24]
right_cond = [9,10,11,21,22,23]


lst = [str(i) for i in All_Cond]
left_dict, right_dict, center_dict= {} ,{},{}
TrialOrder = []
P_LUM = []
P_MED = []
P_MEAN = []
Subj  = []
dfObj00, dfObj01 = pd.DataFrame(),pd.DataFrame()
lst_shape = ['Rectangular', 'Square Left', 'Square Right']
lst_begin = [1,5,9]

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

filecounter = 0
for file in TxtFiles:
    filecounter += 1
    tmpval = (filecounter-1)* (len(TxtFiles))+ 1
    curr_Dict= {}
    currFile = open(file,'r')
#    load the txt file
    currTxtFile = csv.reader(currFile,
                             delimiter = '\n',
                             skipinitialspace=True)
#    read the txt file
    currCsv = []
    for lstTmp in currTxtFile:
        for strtmp in lstTmp:
            currCsv.append(strtmp[:])
#   for all the people         
    AllCsvs.append(currCsv)    
    left_counter,right_counter,center_counter = -1, -1, -1
    trialOrder = []
    trialGroup = []
    lum = []
    
    P_lum , P_median, P_mean= [], [], []
    for trialid in currCsv:
        tmp = trialid.split()
        trialOrder.append(int(tmp[1]))
        if int(tmp[1]) < 13:
              trialGroup.append(int(tmp[1]))
              lum.append('Lum Decre')
        else:
              trialGroup.append(int(tmp[1]) - 12)
              lum.append('Lum Incre')
        P_lum.append(float(tmp[3]))
    cond_group = [lst_shape[j] for i in trialGroup for j in range(len(lst_begin)) if (i >= lst_begin[j]) and (i<= (lst_begin[j]+3)) ]     
    curr_Dict = {'Condition': trialOrder,
            'P_lum': P_lum,
            'P_lum_vs_Base':[x-float(tmp[2]) for x in P_lum],
            'Condition_Group':trialGroup,
            'Luminance': lum,
            'Cond_Group_Shape': cond_group,
            'Subject':['sub-0'+str(filecounter) for i in range(len(P_lum))]}
    TrialOrder.append(trialOrder)
    pd_curr = pd.DataFrame(data=curr_Dict)
    # Remove 12 and 24 condition
    pd_curr_rec = pd_curr.loc[(pd_curr["Condition"] != 12) & (pd_curr["Condition"] !=24)]
    dfObj00 = dfObj00.append(pd_curr_rec)


    median_lst, mean_lst, lum_01= [], [], []
    for i in All_Cond:
        currCond = []
        if i < 12:
             lum_01.append('Lum Decre')
        else:
             lum_01.append('Lum Incre')
        for trialid in currCsv:
            tmp = trialid.split()
            if (str(i) == tmp[1]):
                currCond.append(float(tmp[3]))
        median_lst.append(np.median(currCond))
        mean_lst.append(np.mean(currCond))
    
    P_LUM.append(P_lum)
    P_MED.append(median_lst)
    P_MEAN.append(mean_lst)
    dict_2 = {'Condition':All_Cond,
              'Condition_grp':Cond_01,
              'Luminance':lum_01,
              'M_Plum':median_lst,
              'M_Plum_vs_Base':[x-float(tmp[2]) for x in median_lst],
              'Mean_Plum':mean_lst,
              'Mean_Plum_vs_Base':[x-float(tmp[2]) for x in mean_lst],
              'Subject':['sub-0'+str(filecounter) for i in range(len(All_Cond))]}     
    pd_mplum = pd.DataFrame(data=dict_2)
    dfObj01 = dfObj01.append(pd_mplum)
    plt.figure(tmpval,dpi=300)
    plt.rcParams.update(**rc)
    # sns.swarmplot(x='Condition',y='P_lum_vs_Base',data=pd_curr_rec, ax= ax)

    ax = sns.violinplot(x='Condition_Group',y='P_lum_vs_Base',hue='Luminance',
                data=pd_curr_rec,palette=['white','dimgray'],saturation=0.01,
                scale="count",inner=None)
    ax = sns.stripplot(x='Condition_Group',y='P_lum_vs_Base',hue='Luminance',
                       data=pd_curr_rec,palette=['lightgray','dimgray'],
                       edgecolor='black',linewidth=0.3,
                       size=3, dodge=True)    
    ax = sns.stripplot(x='Condition_grp',y='M_Plum_vs_Base',hue='Luminance',
                       hue_order= ["Lum Incre", "Lum Decre"],
                       data=pd_mplum, palette=['lightgray','dimgray'],
                       marker="^",size=5,linewidth=0.5,dodge=True)
    handles, labels = ax.get_legend_handles_labels()
    ax.legend(handles[:2], labels[:2])
    # add the horizontal line
    ax.hlines(0.0,0,10,colors='k',linestyle=':',label="Base Lum")
    plt.xlabel("Probing Area Conditon")
    plt.ylabel("Change of Perceived Luminance")

    plt.ylim([-0.5,0.5])
    plt.show()
    # plt.savefig('subj_'+str(filecounter)+'_allCond_CPL.png',dpi=300)
    # plt.savefig('subj_'+str(filecounter)+'_allCond_CPL.svg',dpi=300)
    plt.savefig('subj_'+str(filecounter)+'_allCond_CPL_mdm.png',dpi=300)
    plt.savefig('subj_'+str(filecounter)+'_allCond_CPL_mdm.svg',dpi=300)
    

    plt.close('all')

# Save the dataframe     
dfObj00.to_excel(TxtPth + 'All_subjects_lum_pt76.xls')
dfObj00.to_csv(TxtPth + 'All_subjects_lum_pt76.csv')


import statsmodels.api as sm
from scipy import stats
 
# =============================================================================
# Plot the group average across conditions overlaid with error bars    
# =============================================================================
# # #%% settings for the group plot
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
#-----------------------------------------------------------------------------    
# Calculate the mean across subjects and standard errors
mean_ary = np.mean(np.asarray(P_MED),axis=0) - (-0.76)
err = stats.sem(np.asarray(P_MED),axis=0)
# Barplot 
plt.figure(dpi=300)
plt.rcParams.update(**rc)
# add the horizontal line
plt.axhline(0,0.05,0.95,color='k',linestyle=':',label="No Change")
ax = sns.barplot(x='Condition_grp',y='M_Plum_vs_Base',hue='Luminance',
             hue_order= ["Lum Decre", "Lum Incre"], ci=None,
             data=dfObj01,palette=['dimgray','lightgray'],edgecolor='k',
             dodge=True) 
# ax = sns.barplot(x='Condition_Group',y='P_lum_vs_Base',hue='Luminance',
#              hue_order= ["Lum Decre", "Lum Incre"], ci=None,
#              data=dfObj00,palette=['dimgray','lightgray'],edgecolor='k',
#              dodge=True) 
# ax = sns.barplot(x='Condition_grp',y='Mean_Plum_vs_Base',hue='Luminance',
#                  hue_order= ["Lum Incre", "Lum Decre"],
#                  data=dfObj01,palette=['lightgray','dimgray'], 
#                  dodge=True) 
# ax = sns.barplot(x='Condition_grp',y='M_Plum_vs_Base',hue='Luminance',
#                        data=dfObj01,palette=['lightgray','dimgray'],
#                        dodge=True) 
plt.ylim([-0.15,0.21])
# Add standard errors to the barplot
for i, p in enumerate(ax.patches):
    print(i, p) 
    x0 = p.get_x()
    w = p.get_width()
    h = p.get_height()
    # if i < len(ax.patches)/2:  # select which dictionary to use
    #     d = i 
    # if i > len(ax.patches)/2:
    #     d = i - 1    
    min_y = mean_ary[i] - err[i]
    max_y = mean_ary[i] + err[i]
    # plt.axvline(x+w/2, min_y, max_y, color='k',linewidth=2)    
    # plt.vlines(x=x0+w/2, ymin=min_y, ymax=max_y, colors='k')
    plt.errorbar(x=x0+w/2,y=mean_ary[i],yerr=err[i],color='k',capsize=5)
# Hide borders of the ax
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
# Change the labels  
plt.xlabel("Probing Area Conditon")
plt.ylabel("Change of Perceived Luminance")
plt.title("N = {}".format(str(len(TxtFiles))))
plt.show()   
# Save 
plt.savefig('All_sub_allCond_CPL_mdm_pt76.png',dpi=300)
plt.savefig('All_sub_allCond_CPL_mdm_pt76.svg',dpi=300)


Cond_grp_01 = [lst_shape[j] for i in dfObj01["Condition_grp"] for j in range(len(lst_begin)) if (i >= lst_begin[j]) and (i<= (lst_begin[j]+3)) ]     
dfObj01["Configure"] = Cond_grp_01
dfObj01.to_excel(TxtPth + 'All_subjects_lum_pt76_anova.xls')
dfObj01.to_csv(TxtPth + 'All_subjects_lum_pt76_anova.csv') 

# Statistics
res = pg.rm_anova(data=dfObj01, dv='M_Plum_vs_Base', subject='Subject', within=['Luminance', 'Condition_grp'],detailed=True)
res.to_csv(TxtPth + 'Group_two_way_rm_anova_pt76_pg.csv')

plt.close('all')