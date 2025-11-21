'''
# This is a tutorial to teach python classes by creating a program to control a robot car.
# the car is able to move forward, backward, turn left, turn right, and stop.
# two motors power the wheels. The motors are in counterpoised directions.
# The left motor needs to run forward to move the car forward, while the right motor needs to run backward.
# left motor is on pin2 and right motor is on pin1
# Using bbc microbit code editor https://python.microbit.org/v/2.0

We are using CLASSES for the first time.
CLASSES is the way to create OBJECTS.

A CLASS is a 'thing' you define in software. 
An OBJECT is an instance of the class. 
eg. A Car class is a blueprint for creating Car objects.

Let's look at the Car class as an example.

A Car class is defined by attributes (eg. things the Car possess - number of wheels, colour, make, max speed etc.)
A Car class has METHODS (functions) that allows the object to operate (eg. cars start, stop, drive, turn, reverse etc.)

OBJECTS in python are created ("instantiated") by assigning a variable to the CLASS

Classes in python are capitalised by convention. eg. Car, Motor, Robot etc.
Classes can contain other classes as attributes eg. a Car class can contain Motor classes as attributes.

eg. 
for a Car class
    my_car = Car() - this creates a Car object called my_car
    red_car = Car(colour=red) - this creates a Car object passing the colour red to it.

WE STILL NEED TO DEFINE THE CLASS.

here's an example - use idle or any python editor to run this code
'''

class Car:
    def __init__(self, make, model, year, colour):
        self.make = make
        self.model = model
        self.year = year
        self.colour = colour

    def display_info(self):
        return f"{self.year} {self.make} {self.model} in {self.colour}"
    
    
# create two Car objects
my_car = Car("Toyota", "Corolla", 2020, "Blue")
your_car = Car("Honda", "Civic", 2019, "Red")


# display information about the cars
print(my_car.display_info())
print(your_car.display_info())  



'''
the __init__ method is called when the class is instantiated.
NOTE the use of 'self' to refer to the object itself.

Now we will create a Motor class to control a single motor using PWM on a given pin.

Our Motor class will have methods to run the motor at a given speed and to stop the motor.

Open a new file and
Save as motor.py
'''


from microbit import *

class Motor:
    def __init__(self, motor_pin): # initialize motor with given pin
        ''' Constructor '''
        
        self.pin = motor_pin
        self.pin.set_analog_period(20) # set PWM period to 20ms for motor control
        
    def run(self, speed): # run motor at given speed
        ''' run(speed) - value between 0 and 1023. eg. run(512)'''
        
        speed = max(0, min(1023, speed))  # constrain speed between 0 and 1023
        self.pin.write_analog(speed) # set motor speed
            
    def stop(self): # stop the motor by running motor at speed 0
        '''stop motor'''

        self.run(0)

# code to test class code
if __name__ == "main":
    motor = Motor(pin1)

    motor.run(1)
    sleep(1000)
    motor.stop()


'''
save as motor.py and test by running this file 
    
Now we create a Car class to control the car using two motors
Create a new file and save it as car.py

A simple car control class for a two-motor car using the Motor class from motor.py  
'''

#We will start with a class with empty methods
# we want the car to be able to stop, move forward, move backward, turn left and turn right

# 'pass' means do nothing - we will fill in the methods later

class Car: 
    def __init__(self, left_motor_pin, right_motor_pin):
        ''' This method will be called when the Car object is created'''
        pass
    
    def stop(self):
        ''''''
        pass
        
    def forward(self, gear):
        ''' move forward at given gear (speed)'''
        pass
        
    def backward(self, gear):
        ''' move backward at given gear (speed)'''
        pass
        
    def left(self, gear):
        ''' turn left at given gear (speed)'''
        pass
    
    def right(self, gear):
        ''' turn right at given gear (speed)'''
        pass
    
    if __name__ == "main":
        car = Car(pin2, pin1)
        car.forward(5)
        sleep(2000)
        car.stop()
        sleep(1000)
        
# pass means do nothing - we will fill in the methods later
        
# save as car.py and test by running this file
# What happens when you run this code?
# Nothing happens because all methods are empty.
# Next step is to fill in the methods to make the car move


  
      
from microbit import *   
import neopixel
from motor import Motor


class Car:
    
    # Initialize the car with two motors
    def __init__(self, left_motor_pin, right_motor_pin):

        self.left_motor = Motor(left_motor_pin) # use Motor class to create motor objects
        self.right_motor = Motor(right_motor_pin) # use Motor class to create motor objects
        
        self.motor_centre = 75  # midpoint speed for motors to stop
        self.gears = 10  # number of speed increments
        
        display.show(Image.HEART)  # user feedback that car is ready    

        
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
        '''value between 0 and 10 eg. forward(5)'''
        
        # calculate left and right motor values based on speed. Each increment is midpoint / gears
        # offset from midpoint +- 1 to avoid motor deadzone
        
        speed1 = (self.motor_centre - 1) + (gear * (self.motor_centre / self.gears))
        speed2 = (self.motor_centre + 1) - (gear * (self.motor_centre / self.gears))

        #display on microbit
        display.show(Image.ARROW_N)
        
        self.left_motor.run(speed1)
        self.right_motor.run(speed2)
        
        
        
    # Move the car backward
    def backward(self, gear):
        '''value between 0 and 10. eg. backward(5)'''
        
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
# just for testing purposes

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
       
       
'''
Save as car.py and test by running this file
Next steps:
    add code for left turn and right turn
    
TEST YOUR CODE

 
ADVANCED:

Use inbuilt compass to turn car to a specific heading 
turn by a specific angle
shake to start after a few seconds countdown
follow directions from an array of movements
use in built timer to move for specific time intervals ( move until time in the future reached)

if using microbit v2 add sound effects for each movement

'''