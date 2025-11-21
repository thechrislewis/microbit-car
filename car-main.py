# A simple car control class for a two-motor car using the micro:bit
# uses the Motor class from motor.py


from microbit import *   
import neopixel
from motor import Motor


class Car:
    
    # Initialize the car with two motors
    def __init__(self, left_motor_pin, right_motor_pin):

        self.left_motor = Motor(left_motor_pin)
        self.right_motor = Motor(right_motor_pin)
        self.motor_centre = 75  # midpoint speed for motors to stop
        self.gears = 10  # number of speed increments
        
        display.show(Image.HEART)        

        
    # Stop the car
    def stop(self):
        self.left_motor.stop()
        self.right_motor.stop()
        
        #display on microbit
        display.show(Image('99999:'
                           '90009:'
                           '90009:'
                           '90009:'
                           '99999'))
        
    # Move the car forward
    def forward(self, gear):
        '''gear: value between 0 and 10
        forward(5)'''
        
        # calculate left and right motor values based on speed. Each increment is midpoint / gears
        # offset from midpoint
        
        speed1 = (self.motor_centre - 1) + (gear * (self.motor_centre / self.gears))
        speed2 = (self.motor_centre + 1) - (gear * (self.motor_centre / self.gears))

        #display on microbit
        display.show(Image.ARROW_N)
        
        self.left_motor.run(speed1)
        self.right_motor.run(speed2)
        
        
        
    # Move the car backward
    def backward(self, gear):
        '''gear: value between 0 and 10
        forward(5)'''
        
        speed1 = (self.motor_centre + 1) + (gear * (self.motor_centre / self.gears))
        speed2 = (self.motor_centre - 1) - (gear * (self.motor_centre / self.gears))

        #display on microbit
        display.show(Image.ARROW_S)
        
        self.left_motor.run(speed2)
        self.right_motor.run(speed1)
        
       

    # Turn the car left
    def left(self, speed): # For you to complete
        pass
    
    def right(self, speed): # For you to complete
        pass


# functions outside of class. 

def countdown(seconds): # countdown from given seconds on microbit display
        for i in range(seconds, 0, -1):
            display.show(str(i))
            sleep(1000)
        display.clear()
        
def main(): # main function to test car class

    car.forward(1)
    sleep(3000)
    car.forward(5)
    sleep(3000)
    car.backward(1)
    sleep(3000)
    car.backward(9)
    sleep(3000)
    car.stop()


if __name__ == "__main__":

    car = Car(pin2, pin1)
    
    while True: # wait for button A or B to start
        if button_a.is_pressed():
            main()
           
        elif button_b.is_pressed():
            car.stop()
       
