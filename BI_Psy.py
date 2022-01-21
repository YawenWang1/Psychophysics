# -*- coding: utf-8 -*-   #noqa
""".
"""
import os
import datetime
import numpy as np
import time
from psychopy.gui import wxgui as gui
from psychopy import visual, core, monitors, logging, event,data
import psychopy.tools.monitorunittools as p2d
#Psychopy1.8.5
from psychopy.visual import filters
#from psychopy import filters

# -----------------------------------------------------------------------------
# *** Define general parameters

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
# Event 9: Probing area Height: 3, Width: 6 , loc : right, inducers: down
# Event 10: Probing area Height: 4, Width: 6 , loc : right, inducers: down
# Event 11: Probing area Height: 5, Width: 6 , loc : right, inducers: down
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
# Distance between observer and monitor [cm]:
varMonDist = 64.0  # [99.0] for 7T scanner - Nova coil
#varMonDist = 19.0  # [99.0] for 7T scanner - Visual coil
# Width of monitor [cm]:
varMonWdth = 38.0  # [30.0] for 7T scanner - Nova coil
#varMonWdth = 33.0  # [30.0] for 7T scanner - Visual coil
# Width of monitor [pixels]:
varPixX = 1280#[1920.0] 7T scanner
# Height of monitor [pixels]:
varPixY = 1024 # [1200.0] for 7T scanner
# Pixel intensity of uniform background (rest):
#lstClrBckrgd = [-0.71, -0.71, -0.71]
lstClrBckrgd = [-1, -1,-1]
# -----------------------------------------------------------------------------


# -----------------------------------------------------------------------------
# *** GUI

# Name of the experiment:
strExpNme = 'Brightness_Induction'

# Get date string as default session name:
strDate = str(datetime.datetime.now())
lstDate = strDate[0:10].split('-')
strDate = (lstDate[0] + lstDate[1] + lstDate[2])

# List with runs to choose from:
lstRuns = [str(x).zfill(2) for x in range(1, 5)]
lstRuns.append('Dummy') # ['01', '02', '03', '04' 'Dummy']

# Dictionary with experiment metadata:
dicExpInfo = {'Run': lstRuns,
    'Test mode': ['No', 'Yes'],
    'Subject_ID': strDate,
    'Eye_tracking':['No', 'Yes']}

# Pop-up GUI to let the user select parameters:
objGui = gui.DlgFromDict(dictionary=dicExpInfo,
title=strExpNme)

# On some systems (windows) the return values from the GUI are not as expected.
# Set their types explicitly:
dicExpInfo['Run'] = str(dicExpInfo['Run'])
dicExpInfo['Test mode'] = str(dicExpInfo['Test mode'])
dicExpInfo['Subject_ID'] = str(dicExpInfo['Subject_ID'])
dicExpInfo['Eye_tracking'] = str(dicExpInfo['Eye_tracking'])
# Close if user presses 'cancel':
if objGui.OK is False:
    core.quit()

# Testing (if True, timer is displayed):
if dicExpInfo['Test mode'] == 'Yes':
    lgcTest = True
else:
    lgcTest = False

# Testing (if True, timer is displayed):
if dicExpInfo['Eye_tracking'] == 'Yes':
    lgcEye = True
else:
    lgcEye = False


# -----------------------------------------------------------------------------
# *** Logging

# Set clock:
objClck = core.Clock()

# Set clock for logging:
logging.setDefaultClock(objClck)

# Add time stamp and experiment name to metadata:
dicExpInfo['Date'] = data.getDateStr().encode('utf-8') #'2019_Oct_11_1516'
dicExpInfo['Experiment_Name'] = strExpNme

# Path of this file:
strPthMain = os.path.dirname(os.path.abspath(__file__))
#print strPthMain
# Get parent path:
# Goes back two layers parents directory from the file
# join two or more pathnames component, inserting '/' as needed
strPthPrnt = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
# print strPthPrnt
# Path of logging folder (parent to subject folder):
strPthLog = (strPthPrnt
+ os.path.sep #'/'
+ 'log')

# If it does not exist, create subject folder for logging information
# pertaining to this session:
if not os.path.isdir(strPthLog):
    os.makedirs(strPthLog)

# Path of subject folder:
strPthSub = (strPthLog
+ os.path.sep
+ str(dicExpInfo['Subject_ID'])
)

# If it does not exist, create subject folder for logging information
# pertaining to this session:
if not os.path.isdir(strPthSub):
    os.makedirs(strPthSub)

# Name of log file:
strPthLog = (strPthSub
+ os.path.sep
+ '{}_{}_Run_{}_{}'.format(dicExpInfo['Subject_ID'],
dicExpInfo['Experiment_Name'],
dicExpInfo['Run'],
dicExpInfo['Date'])

)
#print strPthLog
#'20190920_GreyBcgrd_Run_03_2019_Sep_20_1622'
# Create a log file and set logging verbosity:
fleLog = logging.LogFile(strPthLog + '.log', level=logging.DATA)# 'logging.DATA=25'

# Log parent path:
fleLog.write('Parent path: ' + strPthPrnt + '\n')

# Log run:
fleLog.write('Run: ' + str(dicExpInfo['Run']) + '\n')

# Log condition:
fleLog.write('Test mode: ' + dicExpInfo['Test mode'] + '\n')
fleLog.write('Subject_ID: ' + dicExpInfo['Subject_ID'] + '\n')
fleLog.write('Eye_tracking: ' + dicExpInfo['Eye_tracking'] + '\n')

# Set console logging verbosity:
logging.console.setLevel(logging.WARNING)
# -----------------------------------------------------------------------------


# -----------------------------------------------------------------------------
# *** Setup
#
newGrid = np.array([[0.69,166,2.231],#lum, first value revers to min lum value, second value refers to max lum value and third value corresponds to gamma
                    [0.69,37.7,2.42],#r
                    [0.69,112.5,2.282],#g
                    [0.69,10.3,2.033]],#b
                    )
#calmonitor= Monitor(name='test2', width=38,
#            distance=64,
#            gamma=2.231,)
#calmonitor.setGammaGrid(newGrid)
# Create monitor object:
#objMon = monitors.Monitor('test2',
#width=varMonWdth,
#distance=varMonDist)
#objMon.setGammaGrid(newGrid)
objMon = monitors.Monitor('testMonitor',
width=varMonWdth,
distance=varMonDist)
objMon.setGammaGrid(newGrid)

fix_accuracy = p2d.deg2pix(3,objMon)
# Range is allowed the eyes to move 
fleLog.write('fix_accuracy: ' + str(fix_accuracy) + '\n')
# Set size of monitor:
objMon.setSizePix([varPixX, varPixY])

# Log monitor info:
fleLog.write(('Monitor distance: varMonDist = '
+ str(varMonDist)
+ ' cm'
+ '\n'))
fleLog.write(('Monitor width: varMonWdth = '
+ str(varMonWdth)
+ ' cm'
+ '\n'))
fleLog.write(('Monitor width: varPixX = '
+ str(varPixX)
+ ' pixels'
+ '\n'))
fleLog.write(('Monitor height: varPixY = '
+ str(varPixY)
+ ' pixels'
+ '\n'))

# Set screen:
objWin = visual.Window(
    size=(varPixX, varPixY),
    screen=0,
    winType='pyglet',  # winType : None, ‘pyglet’, ‘pygame’
    allowGUI=False,
    allowStencil=True,
    fullscr=True,
    monitor=objMon,
    color=lstClrBckrgd,
    colorSpace='rgb',
    units='deg',
    blendMode='avg'
    )
frameNum = objWin.getActualFrameRate()
#frameNum = objWin.getActualFrameRate(nIdentical=60,nMaxFrames=100, nWarmUpFrames=10, threshold=1)
#ValSweep = 1 / frameNum
# Sinusodial upwards
xUp = np.linspace(0,.5*np.pi,frameNum+1)
xDown = np.linspace(.5*np.pi,np.pi,frameNum+1)
DownStep = np.cos(xDown)
UpStep = np.sin(xUp)
print(len(UpStep),len(DownStep))
# print ValSweep
# flipinterval = objWin.frameIntervals
# print objWin.frameIntervals
# -----------------------------------------------------------------------------

# -----------------------------------------------------------------------------
# *** Experimental stimuli
# Probing square at induction condition
ProbSquare = visual.Rect(
    objWin,
    units="deg",
    width=12,
    height=6,
    lineColorSpace="rgb",
    fillColorSpace="rgb",
    lineColor=[-0.76,-0.76,-0.76],
    fillColor=[-0.76,-0.76,-0.76]
    )
# Out - Inducers
OutInducer = visual.Rect(
    objWin,
    units="deg",
    width=16.6,
    height=10,
    lineColorSpace="rgb",
    fillColorSpace="rgb",
    lineColor=[0,0,0],
    fillColor=[0,0,0])

# Mask - Inducers
# Define a functio to generate noise image for masking phase
def makeFilteredNoise(res, radius, shape='gauss'):
    noise = np.random.random([res,res])
    kernel = filters.makeMask(res, shape=shape, radius=radius)
    filteredNoise = filters.conv2d(kernel, noise)
    filteredNoise = (filteredNoise-filteredNoise.min())/(filteredNoise.max()-filteredNoise.min())*2-1
    return filteredNoise
MskNoise = makeFilteredNoise(1000,0.001)

MaskInducer = visual.ImageStim(
    objWin,
    image=MskNoise,
    size=(16.6,10),
    units="deg",
    mask = None)
#---------------------------------------------------------------------------------
#***Fixation
objFix = visual.TextStim(objWin,
    text='+',
    font="Courier New",
    pos=(0, 0),
    color=[1.0, -1.0, -1.0],
    colorSpace='rgb',
    opacity=1.0,
    contrast=1.0,
    ori=0.0,
    height=1,
    antialias=True,
    alignHoriz='center',
    alignVert='center',
    flipHoriz=False,
    flipVert=False,
    autoLog=False
    )
objFixResp = visual.TextStim(objWin,
    text='+',
    font="Courier New",
    pos=(0, 0),
    color=[-1.0, 1.0, -1.0],
    colorSpace='rgb',
    opacity=1.0,
    contrast=1.0,
    ori=0.0,
    height=1,
    antialias=True,
    alignHoriz='center',
    alignVert='center',
    flipHoriz=False,
    flipVert=False,
    autoLog=False
    )
objFixDrift = visual.TextStim(objWin,
    text='+',
    font="Courier New",
    pos=(0, 0),
    color=[-1.0, -1.0, 1.0],
    colorSpace='rgb',
    opacity=1.0,
    contrast=1.0,
    ori=0.0,
    height=1,
    antialias=True,
    alignHoriz='center',
    alignVert='center',
    flipHoriz=False,
    flipVert=False,
    autoLog=False
    )
#------------------------------------------------------------------------------
#Define wait message
objRest = visual.TextStim(objWin,
    text='Have a break',
    font="Courier New",
    pos=(0, 0),
    color=[1.0, -1.0, -1.0],
    colorSpace='rgb',
    opacity=1.0,
    contrast=1.0,
    ori=0.0,
    height=4,
    antialias=True,
    alignHoriz='center',
    alignVert='center',
    flipHoriz=False,
    flipVert=False,
    autoLog=False
    )
# -----------------------------------------------------------------------------
# Define variables for exp. settings
# Height conditons for the probing area
aryHgt= [j for i in range(6) for j in range(3,7)]
# Width conditions for the probing area
tmpWdt = [12,12,12,12,3,4,5,6,3,4,5,6]
aryWdt = [j for i in range(2) for j in tmpWdt]
#Number of repetition for different condition
basisEven_rect , basisEven_sqr =  4, 4
numTrlEvem_rect, numTrlEvem_sqr = 20, 10
arySweep,   aryLeRgt        = 2, 2
# Total Trial Number
totTrial      =  (basisEven_rect * numTrlEvem_rect  * arySweep
+basisEven_sqr * numTrlEvem_sqr * aryLeRgt *arySweep)
# Index to reach every condtions
EvenType      = [i for i in range(1,25)]
# --------------------------------------------------------------------------
# Assign events for rect prob and square prob
Even_rect = [1,2,3,4,13,14,15,16]
Even_sqr  = [i for i in EvenType if i not in Even_rect]
EvenTrial = [i for j in range(numTrlEvem_rect) for i in Even_rect ]
for j in range(numTrlEvem_sqr):
    for i in Even_sqr:
        EvenTrial.append(i)
        seed = np.random.randint(0, 10000)
        np.random.seed(seed)
        np.random.shuffle(EvenTrial)
        Pos = []
        for id in EvenTrial:
            if id in [5,6,7,8,17,18,19,20]:
                Pos.append(-3)
            elif id in [9,10,11,12,21,22,23,24]:
                Pos.append(-4)
            else:
                Pos.append(0)

# print Pos
# print EvenTrial
# Define variables for timing
Dur_fix ,  Dur_Chg  = 1 ,1 # s
Dur_Plateu  = 2 # s
# inter trial interval
ITI = np.random.rand(totTrial)+1
#EvenTable     = np.vstack((ITI,EvenTable))
TmeStart = 0.0
pecLum = []

#Presentation
#-------------------------------------------------------------------------------
# Hide the mouse cursor:
event.Mouse(visible=False)
#Get the time
objClck = core.Clock()
if lgcEye:
    # To use eyelink
    import eyeTracker
    eyetracker = eyeTracker.Tracker_EyeLink(win=objWin, clock=objClck, sj='20191111')
    #Didn't use this function in this script 
    #convert eyelink coordinate sytem 800x600 (-400L:400R;-300U:300B) to
    #visual degrees of the current monitor (via the pixel coordinate system of the current monitor)
#    def convert800600todeg(x,y):
#        monsize = []
#        monsize = objWin.size
#        #monsize = win.monitor.getSizePix()
#        monsize = np.array(monsize)/2
#        x = p2d.pix2deg((x/400)*monsize[0],win.monitor)
#        y = p2d.pix2deg((y/300)*monsize[1],win.monitor)
#        return x,y

#-------------------------------------------------------------------------------
# Press e and x to quit the experiment
def func_exit():
    """
    Check whether exit-keys have been pressed.

    The exit keys are 'e' and 'x'; they have to be pressed at the same time.
    This is supposed to make it less likely that they experiment is aborted
    unpurposely.
    """
    # Check keyboard, save output to temporary string:
    lstExit = event.getKeys(keyList=['e', 'x'], timeStamped=False)

    # Whether the list has the correct length (if nothing has happened lstExit
    # will have length zero):
    if len(lstExit) != 0:

        if ('e' in lstExit) and ('x' in lstExit):

            # Log end of experiment:
            logging.data('------Experiment aborted by user.------')

            # Make the mouse cursor visible again:
            event.Mouse(visible=True)

            # Close everyting:
            objWin.close()
            core.quit()
            monitors.quit()
            logging.quit()
            event.quit()

            with open(strPthLog+'.txt','a') as f:
                for l,el in enumerate(pecLum):
                    string = ' '.join(map(str,el))
                    for item in string:
                        f.write(item)
                        f.write('\n')
                        #fleLog.Close()

            # if eyetracker is connected, close the connection as well
            if lgcEye:
                eyetracker.closeConnection()

            return 1

        else:
            return 0

    else:
        return 0
#--------------------------------------------------------------------------------
# Press '4' for to have a break
def restmessage():
    # Check keyboard, save output to temporary string:
    lstBreak = event.getKeys(keyList=['4','3'], timeStamped=False)

    # Whether the list has the correct length (if nothing has happened lstExit
    # will have length zero):
    if len(lstBreak) != 0:

        if '4' in lstBreak :

            # Log end of experiment:
            logging.data('------Resting by user.------')
            return 1
        else:
            return 0
# -------------------------------------------------------------------------------
objFix.draw()
objWin.flip()
# Present the stimuli
objClck.reset(newT=0.0)
# for varTrial in range(2):
varTrial = 0
while varTrial < totTrial:

    # Check whether exit keys have been pressed:
    if func_exit() == 1:
        break
    if lgcEye:
        # If it's 1st trial, do calibration
        if varTrial == 0:
            # Check whether exit keys have been pressed:
            if func_exit() == 1:
                break
            fixation_counter = objClck.getTime()
            fixation_counter_end = objClck.getTime()
            x_eye_coordinates,y_eye_coordinates = [],[]
            x_eye_coordinates_drift,y_eye_coordinates_drift = [], []


            # Get the mean fixation position around 1.5 seconds
            while fixation_counter <= (1.5 + fixation_counter_end):
                OutInducer.draw()
                objFix.draw()
                objWin.flip()
                eyetracker.preTrial(trial=varTrial,calibTrial=0,win=objWin)
                eyetracker.sendMessage("WaitForFix")
                eye_pos = eyetracker.getSample()
                x_eye_coordinates.append(eye_pos[0])
                y_eye_coordinates.append(eye_pos[1])
                fixation_counter = objClck.getTime()
            # Calculate the mean position of the recorded eye
            newx = np.average(x_eye_coordinates)
            newy = np.average(y_eye_coordinates)
            print(newx, newy)
            fixation = True
            print(fixation)

        # drift correction
        else:
            # Check whether exit keys have been pressed:
            if func_exit() == 1:
                break
            fixation_counter = 0
            OutInducer.draw()
            objFix.draw()
            objWin.flip()
            while fixation_counter != 5:
                OutInducer.draw()
                objFix.draw()
                objWin.flip()
                eyetracker.preTrial(trial=varTrial,calibTrial=0,win=objWin)
                eyetracker.sendMessage("WaitForFix")
                eye_pos = eyetracker.getSample()
                x_eye_coordinates_drift.append(eye_pos[0])
                y_eye_coordinates_drift.append(eye_pos[1])
                fixation_counter += 1
            newxd =  np.average(x_eye_coordinates_drift)
            newyd =  np.average(y_eye_coordinates_drift)
            if (np.absolute((newxd-newx)) > fix_accuracy) :
                newx = newxd
            if (np.absolute((newyd - newy))> fix_accuracy):
                newy = newyd

            fixation = True
            print(fixation)
            # Fixation time
            fixation_counter = objClck.getTime()
            fixation_counter_end = objClck.getTime()
            OutInducer.draw()
            objFix.draw()
            objWin.flip()
            while fixation_counter <= (0.5 + fixation_counter_end):
                eyetracker.preTrial(trial=varTrial, calibTrial=0, win=objWin)
                eyetracker.sendMessage("waitforfix")
                eye_pos = eyetracker.getSample()
                # Judge whether movements of eyes is larger than fix_accuracy
                # Record lose fixation
                if ((newx - fix_accuracy) > eye_pos[0] or eye_pos[0] > (newx + fix_accuracy)) or ((newy - fix_accuracy) > eye_pos[1] or eye_pos[1] > (newy + fix_accuracy)):
                    fixation = False
                    fixation_counter = time.time()
                if func_exit() == 1:
                    break
    else:
        # If there's no eyetracking, fixation is supposed to be fixed
        fixation = True
    # if subj fixates, exp starts
    if fixation:
        varTme01 = objClck.getTime()
        StartPhase = varTme01
        while varTme01 < StartPhase + Dur_fix + Dur_Chg +Dur_Plateu:
            # Short fixation with outside inducers
            while varTme01  < StartPhase + Dur_fix :
                # Check whether exit keys have been pressed:
                if func_exit() == 1:
                    break
                # Check whether to use eyetracker
                if lgcEye:
                    eyetracker.preTrial(trial=varTrial,calibTrial=0,win=objWin)
                    eyetracker.sendMessage("WaitForFix")
                    eye_pos = eyetracker.getSample()
                    print(eye_pos[0],eye_pos[1])
                    print(fix_accuracy)
                    print(newx - fix_accuracy)
                    if ((newx - fix_accuracy) > eye_pos[0] or eye_pos[0] > (newx + fix_accuracy)) or ((newy - fix_accuracy) > eye_pos[1] or eye_pos[1] > (newy + fix_accuracy)):
                        objFixDrift.draw()
                        objWin.flip()
                        time.sleep(0.5)
                        fixation = False
                        break
                OutInducer.draw()
                objFix.draw()
                objWin.flip()
                # Update the time
                varTme01 = objClck.getTime()
            # if subj fixates, present the probing area
            print(fixation)
            if fixation:
                tmpcounter = -1
                while (varTme01  >= StartPhase + Dur_fix) and (varTme01  < StartPhase + Dur_fix + Dur_Chg):
                    tmpcounter += 1
                    # Check whether exit keys have been pressed:
                    if func_exit() == 1:
                        break
                    # Check whether to use eyetracker
                    if lgcEye:
                        eyetracker.preTrial(trial=varTrial,calibTrial=0,win=objWin)
                        eyetracker.sendMessage("WaitForFix")
                        eye_pos = eyetracker.getSample()
                        if ((newx - fix_accuracy) > eye_pos[0] or eye_pos[0] > (newx + fix_accuracy)) or ((newy - fix_accuracy) > eye_pos[1] or eye_pos[1] > (newy + fix_accuracy)):
                            objFixDrift.draw()
                            objWin.flip()
                            time.sleep(0.5)
                            fixation = False
                            break
                    # Choose the up or down sweep for outside inducer
                    if EvenTrial[varTrial]  < 12:
                        OutInducer.lineColor =(DownStep[tmpcounter],DownStep[tmpcounter],DownStep[tmpcounter])
                        OutInducer.fillColor =(DownStep[tmpcounter],DownStep[tmpcounter],DownStep[tmpcounter])
                        if OutInducer.lineColor[0] <= -1:
                            OutInducer.lineColor =(-0.9999, -0.9999, -0.9999)
                            OutInducer.fillColor   =(-0.9999, -0.9999, -0.9999)

                    else:
                        OutInducer.lineColor =(UpStep[tmpcounter],UpStep[tmpcounter],UpStep[tmpcounter])
                        OutInducer.fillColor =(UpStep[tmpcounter],UpStep[tmpcounter],UpStep[tmpcounter])
                        if OutInducer.lineColor[0] >= 1:
                            OutInducer.lineColor =(0.9999, 0.9999 ,0.9999)
                            OutInducer.fillColor =(0.9999, 0.9999 ,0.9999)
                    # Updates the width , height and position of probing area
                    ProbSquare.height =aryHgt[EvenTrial[varTrial]-1]
                    ProbSquare.width =aryWdt[EvenTrial[varTrial]-1]
                    ProbSquare.pos =(Pos[varTrial],0)
                    # Draw OutInducer
                    OutInducer.draw()
                    # Draw Probing area
                    ProbSquare.draw()
                    objFix.draw()
                    objWin.flip()
                    # Update the time
                    varTme01 = objClck.getTime()

            # after sweeping luminance of OutInducer, keep it stable for 2 s
            if fixation:
                while (varTme01  > StartPhase + Dur_fix + Dur_Chg) and (varTme01  < StartPhase + Dur_fix + Dur_Chg +Dur_Plateu):
                    # Check whether exit keys have been pressed:
                    if func_exit() == 1:
                        break
                    # Check whether to use eyetracker
                    if lgcEye:
                        eyetracker.preTrial(trial=varTrial,calibTrial=0,win=objWin)
                        eyetracker.sendMessage("WaitForFix")
                        eye_pos = eyetracker.getSample()
                        if ((newx - fix_accuracy) > eye_pos[0] or eye_pos[0] > (newx + fix_accuracy)) or ((newy - fix_accuracy) > eye_pos[1] or eye_pos[1] > (newy + fix_accuracy)):
                            objFixDrift.draw()
                            objWin.flip()
                            time.sleep(0.5)
                            fixation = False
                            break
                    # Draw OutInducer
                    OutInducer.draw()
                    # Updates the width , height and position of probing area
                    ProbSquare.height =aryHgt[EvenTrial[varTrial]-1]
                    ProbSquare.width =aryWdt[EvenTrial[varTrial]-1]
                    ProbSquare.pos =(Pos[varTrial],0)
                    # Draw probing area
                    ProbSquare.draw()
                    # Draw fixation
                    objFix.draw()
                    objWin.flip()
                    # Update the time
                    varTme01 = objClck.getTime()
            # Recover the OutInducer to gray
            OutInducer.lineColor  =(0.0,0.0,0.0)
            OutInducer.fillColor    =(0.0,0.0,0.0)
            if fixation:
                varResponse = 1
            else:
                varResponse = 0
            # if subj fixates, goes to adaption windows
            # press 1 or 2 to make the probing area ligher or darker
            while varResponse:
                # Draw mask
                MaskInducer.draw()
                # check the exit key
                if func_exit() == 1:
                    break
                # Check key responses
                # '1' up, '2', down, '3' next trial
                lstRsps = event.getKeys(keyList=['1','2','3'], timeStamped=False)
                #Draw Probing area
                ProbSquare.height =aryHgt[EvenTrial[varTrial]-1]
                ProbSquare.width =aryWdt[EvenTrial[varTrial]-1]
                ProbSquare.pos =(Pos[varTrial],0)
                # Judge the response
                if len(lstRsps) == 1 :
                    if lstRsps[0] == '1':
                        ProbSquare.lineColor +=(0.02,0.02,0.02)
                        ProbSquare.fillColor +=(0.02,0.02,0.02)
                        ProbSquare.draw()

                    elif lstRsps[0] == '2':
                        ProbSquare.lineColor -=(0.01,0.01,0.01)
                        ProbSquare.fillColor -=(0.01,0.01,0.01)
                        ProbSquare.draw()
                    else :
                        varResponse = 0
                ProbSquare.draw()
                objFixResp.draw()
                objWin.flip()

            if fixation:
                tmpcolor = ProbSquare.lineColor[0]
                # Recover the original luminance of the probing area
                ProbSquare.lineColor  =(-0.76,-0.76,-0.76)
                ProbSquare.fillColor  =(-0.76,-0.76,-0.76)
                # Draw MaskInducer
#                MaskInducer.draw()
#                # Draw Fixation
#                objFix.draw()
#                objWin.flip()
                # objWin.getMovieFrame(buffer='back')
                # wait for inter trial interval
                # core.wait(ITI[varTrial])

                strTmp = ('Current trial : '
                    + str(varTrial)+ ' ' + str(EvenTrial[varTrial]) + ' '
                    + str(-0.37) + ' ' + str(tmpcolor)  + ' '
                    + str(aryHgt[EvenTrial[varTrial]-1]) + ' '
                    + str(aryWdt[EvenTrial[varTrial]-1]) + ' '
                    + str(Pos[varTrial]))
                # write in data
                logging.data(strTmp)
                # save key elements
                pecLum.append([varTrial,
                    EvenTrial[varTrial],
                    -0.37,
                    tmpcolor,aryHgt[EvenTrial[varTrial]-1],
                    aryWdt[EvenTrial[varTrial]-1],
                    Pos[varTrial]])
                # check whether to rest
                varTme01 = objClck.getTime()
                tmpvarTme = varTme01
                while varTme01 < (tmpvarTme + ITI[varTrial] ):
                    # Check whether exit keys have been pressed:
                    if func_exit() == 1:
                        break
                    # Draw MaskInducer
                    MaskInducer.draw()
                    # Draw Fixation
                    objFix.draw()
                    objWin.flip()
                    if restmessage():
                        Rest = 1
                        while Rest:
                            objRest.draw()
                            objWin.flip()
                            lstRsps01 = event.getKeys(keyList=['3'], timeStamped=False)
                            if len(lstRsps01) == 1 :
                                if lstRsps01[0] == '3':
                                    break
                            if lgcEye:
                                eyetracker.closeConnection()
                                
                    varTme01 = objClck.getTime()
                # Update trial number
                varTrial += 1
            # Every 60 trials 
            if ((varTrial != 0) and ((varTrial % 60) ==0)):
                print(varTrial) 
                Rest = 1
                while Rest:
                    objRest.draw()
                    objWin.flip()
                    lstRsps01 = event.getKeys(keyList=['3'], timeStamped=False)
                    if len(lstRsps01) == 1 :
                        if lstRsps01[0] == '3':
                            break
    
    else:
        varTrial = varTrial
        # Recover the OutInducer to gray
        OutInducer.lineColor  =(0.0,0.0,0.0)
        OutInducer.fillColor    =(0.0,0.0,0.0)
        # Recover the Probing area to dark gray
        ProbSquare.lineColor  =(-0.76,-0.76,-0.76)
        ProbSquare.fillColor  =(-0.76,-0.76,-0.76)
        OutInducer.draw()
        objFix.draw()
        objWin.flip()
        fixation   =  True

#objWin.saveMovieFrames('test.mp4', clearFrames=False)


# write an extra txt file about relavent infomation

with open(strPthLog+'.txt','a') as f:
    for l,el in enumerate(pecLum):
        string = ' '.join(map(str,el))
        for item in string:
            f.write(item)
        f.write('\n')
            #fleLog.Close()

event.Mouse(visible=True)

# Close everyting:
objWin.close()
core.quit()
logging.quit()
monitors.quit()
event.quit()
if lgcEye:
    eyetracker.closeConnection()


#  Generate movie
#   objWin.getMovieFrame(buffer='front')
# save movie as .mp4 format
# objWin.saveMovieFrames('In_8_prob_w_6_h_3_out_h_4.mp4', clearFrames=False)
