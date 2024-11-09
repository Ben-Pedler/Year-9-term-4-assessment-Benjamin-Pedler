For my IT project this term, I made a device with micro python and a Pico pi w board. This device consists of two actuators, a potentiometer and a button. This device also consists of two outputs, a buzzer and an LED light.  

When the button is being held down, it allows the function 'adjust_light_and_buzzer' to run. This function allows the potentiometer's value to be read. When the potentiometer is turned, the LED light will dim / get brighter. When the potentiometer value is greater than 65534, the buzzer will sound. The reason I chose this value is because it is one less than the greatest value. When the buzzer sounds, stop turning the potentiometer because it is at its max. 


The components for this device include: 
- Raspberry Pi Pico W 
- Bread board 
- Button 
- potentiometer 
- Buzzer 
- LED Light 
- USBC - Micro USB Cable (For Mac) 
- 10 Wires 
- Resistor 


Pulse Width Modulation (PWM) 
PWM is a series of signals that can set the frequency of outputs. I am using pulse width modulation in my micro python code so that I can easily set the different LED light brightness levels whilst turning the potentiometer. 


Connecting the components 
The LED light is connected to the GPIO Pin 15 and a GND Pin. The ground pin provides a low resistance pathway back to the power source. The GPIO Pin 15 is at the end of the Pico Pi W meaning it is easy to wire. 

The Buzzer is connected to the GPIO Pin 14 and a GND Pin. The ground pin provides a low resistance pathway back to the power source. The GPIO Pin 14 is near the end of the Pico Pi W meaning it is easy to wire. 

The Button is connected to the GPIO Pin 17 and a GND Pin. The ground pin provides a low resistance pathway back to the power source. The GPIO Pin 17 is near the end of the Pico Pi W meaning it is easy to wire. 

The potentiometer is connected to the GPIO Pin 26, a GND Pin and the 3V3(OUT) Pin. The significance with Pin 26 is that the GPIO can double as an analog and digital pin, allowing the potentiometer to have different values from 0 - 65,535. The 3V3(OUT) Pin provides 3.3 volts into the potentiometer. The ground pin provides a low resistance pathway back to the power source. 




References:
https://srituhobby.com/how-to-control-the-brightness-of-the-led-bulb-using-the-raspberry-pi-pico-board/?srsltid=AfmBOoqex0hoMkVLnp63dXkhx7D4rlGMIibCBJHvE_acE_Si9_5_h_1-
https://learn.sparkfun.com/tutorials/pulse-width-modulation/all
https://learn.adafruit.com/getting-started-with-raspberry-pi-pico-circuitpython/potentiometer-and-pwm-led
https://forum.arduino.cc/t/analogread-a2-always-at-1023-max-value-potentiometer-arduino-pro-micro/549802
https://randomnerdtutorials.com/raspberry-pi-pico-pwm-micropython/
https://Chatgpt.com
