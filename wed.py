#!/usr/bin/micropython
import ev3dev2.motor as em
import utime as t
from ev3dev2.led import Leds
from ev3dev2.sound import Sound
from ev3dev2.sensor.lego import ColorSensor

def moveMtr(mtr, power, sec):
    mtr.on(em.SpeedPercent(power))
    t.sleep(sec)
    mtr.off()

def moveMtrEnd(mtr,power):
    mtr.on(em.SpeedPercent(power))
    mtr.wait_until_not_moving()
    mtr.off()

color_sensor = ColorSensor()

sound = Sound()
sound.beep()

light = Leds()
light.set_color("LEFT","GREEN")
light.set_color("RIGHT","GREEN")

m1=em.LargeMotor(em.OUTPUT_A)
m2=em.LargeMotor(em.OUTPUT_B)
m3=em.MediumMotor(em.OUTPUT_C)
moveMtrEnd(m1,-15) #back to init position.

#moveMtr(m1,+25,0.8)
#moveMtrEnd(m1,-15)
#rotate plate
#moveMtr(m2,25,1.03)
#move medium motor
moveMtrEnd(m3,25)
moveMtr(m3,-45,0.86)

#read first color from sensor as raw rgb values
read_color = color_sensor.rgb 
print(read_color)
for j in range(4):
    for i in range(4):
        m2.on_for_degrees(em.SpeedPercent(30),273)
        read_color = color_sensor.rgb 
        print(read_color)
    moveMtrEnd(m3,25)
    m3.reset()
    moveMtr(m1,+25,0.4)
    m2.on_for_degrees(em.SpeedPercent(30),341)
    m2.on_for_degrees(em.SpeedPercent(30),-88)
    moveMtrEnd(m1,-15)
    moveMtrEnd(m3,25)
    moveMtr(m3,-45,0.8)
    m3.reset()

moveMtrEnd(m3,25)
t.sleep(0.2)
m1.reset()
m2.reset()
m3.reset()


light.set_color("LEFT","RED")
light.set_color("RIGHT","RED")
