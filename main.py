from extra.aula import rodar

@rodar
def main():
  import time 
  from gpiozero import LED, Button, LightSensor, MotionSensor, Buzzer
  import random
  from datetime import datetime
  from datetime import timedelta
  import requests
  from signal import pause

  
  led1=LED(21)
  led2=LED(22)
  led3=LED(23)
  led4=LED(24)
  led5=LED(25)
  led6=LED(26)
  pir= MotionSensor(27)
  ls= LightSensor(8)
  bz= Buzzer(16)
  bzz= Buzzer(17)
  bzzz= Buzzer(18)
  botao1= Button(11)
  botao2= Button(12)
  botao3= Button(13)
  botao4= Button(14)


  while True:
    if botao1.is_pressed:
      print("MODO MANUAL ATIVADO!")
      print("SISTEMA LIGADO!")
      led1.on()
      time.sleep(3)
      if not botao1.is_pressed:
        print("SISTEMA STAND-BY!")
        led1.off()
    if botao2.is_pressed:
      print("MODO MOVIMENTO ATIVADO!")
      led2.on()
      pir.wait_for_motion()
      print("MOVIMENTO ENCONTRADO!")
      led3.blink(0.1, 0.15, 5)
      bz.beep(0.1, 0.15, 2)
      led3.blink(0.1, 0.15, 5)
      led3.on()
      print("SISTEMA LIGADO!")
      time.sleep(3)
      if not botao2.is_pressed:
        print("SISTEMA STAND-BY!")
        led2.off()
        led3.off()
        bz.off()
    if botao3.is_pressed:
      print("MODO SONO ATIVADO!")
      led4.on()
      ls.wait_for_dark()
      led5.blink(0.1, 0.15, 2)
      bzz.beep(0.1, 0.15, 2)
      led5.on()
      time.sleep(3)
      if not botao3.is_pressed:
        print("SISTEMA STAND-BY!")
        led4.off()
        led5.off()
        bzz.off()
    if botao4.is_pressed:
      print("SISTEMA DESATIVADO!")
      led6.on()
      bzzz.beep(0.1, 0.15, 2)
      led1.off()
      led2.off()
      led3.off()
      led4.off()
      led5.off()
      bz.off()
      bzz.off()
      time.sleep(5)
      if not botao4.is_pressed:
        break
      
        
    
    
    
  
      
  
    