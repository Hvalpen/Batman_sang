#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
import math


# Create your objects here.
ev3 = EV3Brick()

#program
ev3.speaker.set_volume(100)
ev3.speaker.play_notes(
    ['D3/8', 'D3/8', 'Db3/8', 'Db3/8', 'C3/8', 'C3/8', 'C#3/8', 'C#3/8', 
    'D3/8', 'D3/8', 'Db3/8', 'Db3/8', 'C3/8', 'C3/8', 'C#3/8', 'C#3/8', 
    'D3/8', 'D3/8', 'Db3/8', 'Db3/8', 'C3/8', 'C3/8', 'C#3/8', 'C#3/8',  
    'G3/4', 'G3/2.',

    'G3/8', 'G3/8', 'Gb3/8', 'Gb3/8', 'F3/8', 'F3/8', 'F#3/8', 'F#3/8',
    'G3/8', 'G3/8', 'Gb3/8', 'Gb3/8', 'F3/8', 'F3/8', 'F#3/8', 'F#3/8',
    'G3/8', 'G3/8', 'Gb3/8', 'Gb3/8', 'F3/8', 'F3/8', 'F#3/8', 'F#3/8',
    'C4/4', 'C4/2.'
    ], tempo=150)

