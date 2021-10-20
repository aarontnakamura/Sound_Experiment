#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2021.1.4),
    on Wed Oct 20 16:21:47 2021
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '2021.1.4'
expName = 'Sound-Questions-Experiment-Set'  # from the Builder filename that created this script
expInfo = {'participant': '', 'session': '001'}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='/Users/aarontnakamura/Desktop/TD_Sound_Experiment/Sound-Questions-Experiment-Set_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# Setup the Window
win = visual.Window(
    size=[1792, 1120], fullscr=True, screen=0, 
    winType='pyglet', allowGUI=True, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "Sound1"
Sound1Clock = core.Clock()
soundstimuli = sound.Sound('A', secs=-1.0, stereo=True, hamming=True,
    name='soundstimuli')
soundstimuli.setVolume(1.0)

# Initialize components for Routine "Question1_Happy"
Question1_HappyClock = core.Clock()
Happy_rating_text = visual.TextStim(win=win, name='Happy_rating_text',
    text='幸福感の度合いを教えてください\xa0\n(１＝低い、７＝高い）',
    font=None,
    pos=(0, 0), height=0.04, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
Happy_rating = visual.RatingScale(win=win, name='Happy_rating', marker='triangle', size=1.0, pos=[0.0, -0.4], choices=['1', '2', '3', '4', '5', '6', '7'], tickHeight=-1)

# Initialize components for Routine "Querstion2_Sad"
Querstion2_SadClock = core.Clock()
Sad_rating_text = visual.TextStim(win=win, name='Sad_rating_text',
    text='悲壮感の度合いを教えてください\xa0\n(１＝低い、７＝高い）',
    font=None,
    pos=(0, 0), height=0.04, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
Sad_rating = visual.RatingScale(win=win, name='Sad_rating', marker='triangle', size=1.0, pos=[0.0, -0.4], choices=['1', '2', '3', '4', '5', '6', '7'], tickHeight=-1)

# Initialize components for Routine "Queastion3_Joy"
Queastion3_JoyClock = core.Clock()
Joy_rating_text = visual.TextStim(win=win, name='Joy_rating_text',
    text='喜楽感の度合いを教えてください\xa0\n(１＝低い、７＝高い）',
    font=None,
    pos=(0, 0), height=0.04, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
Joy_rating = visual.RatingScale(win=win, name='Joy_rating', marker='triangle', size=1.0, pos=[0.0, -0.4], choices=['1', '2', '3', '4', '5', '6', '7'], tickHeight=-1)

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# set up handler to look after randomisation of conditions etc
question_loop = data.TrialHandler(nReps=26.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('soundLoop.xlsx'),
    seed=None, name='question_loop')
thisExp.addLoop(question_loop)  # add the loop to the experiment
thisQuestion_loop = question_loop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisQuestion_loop.rgb)
if thisQuestion_loop != None:
    for paramName in thisQuestion_loop:
        exec('{} = thisQuestion_loop[paramName]'.format(paramName))

for thisQuestion_loop in question_loop:
    currentLoop = question_loop
    # abbreviate parameter names if possible (e.g. rgb = thisQuestion_loop.rgb)
    if thisQuestion_loop != None:
        for paramName in thisQuestion_loop:
            exec('{} = thisQuestion_loop[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "Sound1"-------
    continueRoutine = True
    routineTimer.add(10.000000)
    # update component parameters for each repeat
    soundstimuli.setSound(audio, secs=10.0, hamming=True)
    soundstimuli.setVolume(1.0, log=False)
    # keep track of which components have finished
    Sound1Components = [soundstimuli]
    for thisComponent in Sound1Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    Sound1Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Sound1"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = Sound1Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=Sound1Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # start/stop soundstimuli
        if soundstimuli.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            soundstimuli.frameNStart = frameN  # exact frame index
            soundstimuli.tStart = t  # local t and not account for scr refresh
            soundstimuli.tStartRefresh = tThisFlipGlobal  # on global time
            soundstimuli.play(when=win)  # sync with win flip
        if soundstimuli.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > soundstimuli.tStartRefresh + 10.0-frameTolerance:
                # keep track of stop time/frame for later
                soundstimuli.tStop = t  # not accounting for scr refresh
                soundstimuli.frameNStop = frameN  # exact frame index
                win.timeOnFlip(soundstimuli, 'tStopRefresh')  # time at next scr refresh
                soundstimuli.stop()
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Sound1Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Sound1"-------
    for thisComponent in Sound1Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    soundstimuli.stop()  # ensure sound has stopped at end of routine
    question_loop.addData('soundstimuli.started', soundstimuli.tStartRefresh)
    question_loop.addData('soundstimuli.stopped', soundstimuli.tStopRefresh)
    
    # set up handler to look after randomisation of conditions etc
    trials = data.TrialHandler(nReps=1.0, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='trials')
    thisExp.addLoop(trials)  # add the loop to the experiment
    thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            exec('{} = thisTrial[paramName]'.format(paramName))
    
    for thisTrial in trials:
        currentLoop = trials
        # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
        if thisTrial != None:
            for paramName in thisTrial:
                exec('{} = thisTrial[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "Question1_Happy"-------
        continueRoutine = True
        # update component parameters for each repeat
        Happy_rating.reset()
        # keep track of which components have finished
        Question1_HappyComponents = [Happy_rating_text, Happy_rating]
        for thisComponent in Question1_HappyComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        Question1_HappyClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "Question1_Happy"-------
        while continueRoutine:
            # get current time
            t = Question1_HappyClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=Question1_HappyClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *Happy_rating_text* updates
            if Happy_rating_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                Happy_rating_text.frameNStart = frameN  # exact frame index
                Happy_rating_text.tStart = t  # local t and not account for scr refresh
                Happy_rating_text.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Happy_rating_text, 'tStartRefresh')  # time at next scr refresh
                Happy_rating_text.setAutoDraw(True)
            # *Happy_rating* updates
            if Happy_rating.status == NOT_STARTED and t >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                Happy_rating.frameNStart = frameN  # exact frame index
                Happy_rating.tStart = t  # local t and not account for scr refresh
                Happy_rating.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Happy_rating, 'tStartRefresh')  # time at next scr refresh
                Happy_rating.setAutoDraw(True)
            continueRoutine &= Happy_rating.noResponse  # a response ends the trial
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in Question1_HappyComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "Question1_Happy"-------
        for thisComponent in Question1_HappyComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        trials.addData('Happy_rating_text.started', Happy_rating_text.tStartRefresh)
        trials.addData('Happy_rating_text.stopped', Happy_rating_text.tStopRefresh)
        # store data for trials (TrialHandler)
        trials.addData('Happy_rating.response', Happy_rating.getRating())
        trials.addData('Happy_rating.rt', Happy_rating.getRT())
        trials.addData('Happy_rating.started', Happy_rating.tStart)
        trials.addData('Happy_rating.stopped', Happy_rating.tStop)
        # the Routine "Question1_Happy" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "Querstion2_Sad"-------
        continueRoutine = True
        # update component parameters for each repeat
        Sad_rating.reset()
        # keep track of which components have finished
        Querstion2_SadComponents = [Sad_rating_text, Sad_rating]
        for thisComponent in Querstion2_SadComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        Querstion2_SadClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "Querstion2_Sad"-------
        while continueRoutine:
            # get current time
            t = Querstion2_SadClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=Querstion2_SadClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *Sad_rating_text* updates
            if Sad_rating_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                Sad_rating_text.frameNStart = frameN  # exact frame index
                Sad_rating_text.tStart = t  # local t and not account for scr refresh
                Sad_rating_text.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Sad_rating_text, 'tStartRefresh')  # time at next scr refresh
                Sad_rating_text.setAutoDraw(True)
            # *Sad_rating* updates
            if Sad_rating.status == NOT_STARTED and t >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                Sad_rating.frameNStart = frameN  # exact frame index
                Sad_rating.tStart = t  # local t and not account for scr refresh
                Sad_rating.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Sad_rating, 'tStartRefresh')  # time at next scr refresh
                Sad_rating.setAutoDraw(True)
            continueRoutine &= Sad_rating.noResponse  # a response ends the trial
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in Querstion2_SadComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "Querstion2_Sad"-------
        for thisComponent in Querstion2_SadComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        trials.addData('Sad_rating_text.started', Sad_rating_text.tStartRefresh)
        trials.addData('Sad_rating_text.stopped', Sad_rating_text.tStopRefresh)
        # store data for trials (TrialHandler)
        trials.addData('Sad_rating.response', Sad_rating.getRating())
        trials.addData('Sad_rating.rt', Sad_rating.getRT())
        trials.addData('Sad_rating.started', Sad_rating.tStart)
        trials.addData('Sad_rating.stopped', Sad_rating.tStop)
        # the Routine "Querstion2_Sad" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "Queastion3_Joy"-------
        continueRoutine = True
        # update component parameters for each repeat
        Joy_rating.reset()
        # keep track of which components have finished
        Queastion3_JoyComponents = [Joy_rating_text, Joy_rating]
        for thisComponent in Queastion3_JoyComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        Queastion3_JoyClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "Queastion3_Joy"-------
        while continueRoutine:
            # get current time
            t = Queastion3_JoyClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=Queastion3_JoyClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *Joy_rating_text* updates
            if Joy_rating_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                Joy_rating_text.frameNStart = frameN  # exact frame index
                Joy_rating_text.tStart = t  # local t and not account for scr refresh
                Joy_rating_text.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Joy_rating_text, 'tStartRefresh')  # time at next scr refresh
                Joy_rating_text.setAutoDraw(True)
            # *Joy_rating* updates
            if Joy_rating.status == NOT_STARTED and t >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                Joy_rating.frameNStart = frameN  # exact frame index
                Joy_rating.tStart = t  # local t and not account for scr refresh
                Joy_rating.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Joy_rating, 'tStartRefresh')  # time at next scr refresh
                Joy_rating.setAutoDraw(True)
            continueRoutine &= Joy_rating.noResponse  # a response ends the trial
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in Queastion3_JoyComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "Queastion3_Joy"-------
        for thisComponent in Queastion3_JoyComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        trials.addData('Joy_rating_text.started', Joy_rating_text.tStartRefresh)
        trials.addData('Joy_rating_text.stopped', Joy_rating_text.tStopRefresh)
        # store data for trials (TrialHandler)
        trials.addData('Joy_rating.response', Joy_rating.getRating())
        trials.addData('Joy_rating.rt', Joy_rating.getRT())
        trials.addData('Joy_rating.started', Joy_rating.tStart)
        trials.addData('Joy_rating.stopped', Joy_rating.tStop)
        # the Routine "Queastion3_Joy" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed 1.0 repeats of 'trials'
    
    thisExp.nextEntry()
    
# completed 26.0 repeats of 'question_loop'


# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
