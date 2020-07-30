#!/usr/bin/micropython
import ev3dev2.motor as em
from ev3dev2.sound import Sound
m1=em.LargeMotor(em.OUTPUT_A)
m2=em.LargeMotor(em.OUTPUT_B)
m3=em.MediumMotor(em.OUTPUT_C)
m1.reset()
m2.reset()
m3.reset()
sound = Sound()
sound.beep()