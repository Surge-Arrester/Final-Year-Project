from Tkinter import *
import math
import time
import RPi.GPIO as GPIO

GPIO.setwarnings(False)         #stops it from telling me i'm using pi assigned pins


GPIO.setmode(GPIO.BOARD)        #Sets programming of pin number instead of purpose

                                #Names given on the     :Purpose in program
                                #datasheet              :

GPIO.setup(3, GPIO.OUT)         #I2C1 SDA               : MCU Pulse
GPIO.setup(5, GPIO.OUT)         #I2C1 SCL               : Simulated ADC Pulse
GPIO.setup(7, GPIO.OUT)         #GPIO 4                 : ensures JK starts low
GPIO.setup(8, GPIO.OUT)         #UART TXD               :
GPIO.setup(10, GPIO.OUT)        #UART RXD               :
GPIO.setup(11, GPIO.OUT)        #GPIO 17                :
GPIO.setup(12, GPIO.OUT)        #GPIO 18                : Shift Register clock
GPIO.setup(13, GPIO.IN)         #GPIO 27                : Button
GPIO.setup(15, GPIO.OUT)         #GPIO 22                : Shift /Load register
GPIO.setup(16, GPIO.IN)         #GPIO 23                : 8 Bit Counter MSB
GPIO.setup(18, GPIO.IN)         #GPIO 24                :   .
GPIO.setup(19, GPIO.IN)         #SP10 MOSI              :   .
GPIO.setup(21, GPIO.IN)         #SP10 MISO              :   .
GPIO.setup(22, GPIO.IN)         #GPIO 25                :   .   
GPIO.setup(23, GPIO.IN)         #SP10 SCLK              :   .
GPIO.setup(24, GPIO.IN)         #SP10 CEO N             :   .
GPIO.setup(26, GPIO.IN)         #SP10 CE1 N             : 8-Bit Counter LSB


pin_outputs=[3, 5, 7, 8, 10, 11, 12] #in case we need faster reference later
pin_inputs=[13, 15, 16, 18, 19, 21, 22, 23, 24, 26]


class App:
    def __init__(self):
        
        self.master=Tk()
        self.master.title("My GUI")

        self.M0x=StringVar()
        self.M0y=StringVar()
        self.M1x=StringVar()
        self.M1y=StringVar()
        self.sound_speed=StringVar()
        self.clock_speed=StringVar()
        self.samples=StringVar()
        self.R0=StringVar()
        self.R1=StringVar()
        self.C0=StringVar()
        self.C1=StringVar()
        self.x1=StringVar()
        self.y1=StringVar()
        self.x2=StringVar()
        self.y2=StringVar()
        self.Coord1x=StringVar()
        self.Coord1y=StringVar()
        self.Coord2x=StringVar()
        self.Coord2y=StringVar()
        self.Chan0bin=[]
        self.Chan0=[]

        
        self.Mic0xtext=Label(self.master, text="Mic0 Co-ord X=")
        self.Mic0xtext.grid(row=0,column=0)

        self.x0entry=StringVar()
        self.Mic0xEntry = Entry(self.master,textvariable=self.x0entry)
        self.Mic0xEntry.grid(row=0, column=1)
        
        self.Mic0ytext=Label(self.master, text="Mic0 Co-ord Y=")
        self.Mic0ytext.grid(row=1,column=0)
        
        self.y0entry=StringVar()
        self.Mic0yEntry = Entry(self.master,textvariable=self.y0entry)
        self.Mic0yEntry.grid(row=1, column=1)
               
        self.Mic1xtext=Label(self.master, text="Mic1 Co-ord X=")
        self.Mic1xtext.grid(row=2,column=0)

        self.x1entry=StringVar()       
        self.Mic1xEntry = Entry(self.master, textvariable=self.x1entry)
        self.Mic1xEntry.grid(row=2, column=1)
        
        self.Mic1ytext=Label(self.master, text="Mic1 Co-ord Y=")
        self.Mic1ytext.grid(row=3,column=0)
        
        self.y1entry=StringVar()
        self.Mic1yEntry = Entry(self.master, textvariable=self.y1entry)
        self.Mic1yEntry.grid(row=3, column=1)

        self.updatecoordinates=Button(self.master, text="Update Microphone Co-ordinates",
                                 command=self.updatecoordinates)
        
        self.ClockSpeed=Label(self.master, text="Clock Speed (MHz) :")
        self.ClockSpeed.grid(row=0,column=3)

        self.CLKentry=StringVar()
        self.ClockSpeedEntry = Entry(self.master, textvariable=self.CLKentry)
        self.ClockSpeedEntry.grid(row=0, column=4)

        self.Speed_Sound=Label(self.master, text="Speed of Sound: ")
        self.Speed_Sound.grid(row=1,column=3)

        self.Soundentry=StringVar()
        self.Speed_Sound = Entry(self.master, textvariable=self.Soundentry)
        self.Speed_Sound.grid(row=1, column=4)

        self.samples=Label(self.master, text="Samples: ")
        self.samples.grid(row=2,column=3)

        self.sampleentry=StringVar()
        self.sample_entry= Entry(self.master, textvariable=self.sampleentry)
        self.sample_entry.grid(row=2, column=4)
        
        self.updatevalues=Button(self.master, text="Update Values",
                                 command=self.updatevalues)

        self.runprogram=Button(self.master, text="Run the program",
                               command=self.runprogram)
        self.runprogram.grid(row=27, column=27)

        
        self.R0length=Label(self.master, text="Radius 0: ")
        self.R0length.grid(row=0, column=5)

        self.R0entry=StringVar()
        self.R0_entry=Entry(self.master, textvariable=self.R0entry)
        self.R0_entry.grid(row=0,column=6)

        self.R1length=Label(self.master, text="Radius 1: ")
        self.R1length.grid(row=1, column=5)

        self.R1entry=StringVar()
        self.R1_entry=Entry(self.master, textvariable=self.R1entry)
        self.R1_entry.grid(row=1,column=6)

        self.C0label=Label(self.master, text="Count Channel 0: ")
        self.C0label.grid(row=0, column=7)

        self.X1Label=Label(self.master, text="First Co-ordinates (")
        self.X1Label.grid(row=7,column=0)

        
        self.coordinate1=Label(self.master, textvariable=self.Coord1x)
        self.coordinate1.grid(row=7,column=1)

        self.X1Label=Label(self.master, text=",")
        self.X1Label.grid(row=7,column=2)

        self.coordinate1=Label(self.master, textvariable=self.Coord1y)
        self.coordinate1.grid(row=7,column=3)

        self.co1close=Label(self.master, text=")")
        self.co1close.grid(row=7,column=4)

        
        self.X2Label=Label(self.master, text="Second Co-ordinates (")
        self.X2Label.grid(row=8,column=0)

        
        self.coordinate2=Label(self.master, textvariable=self.Coord2x)
        self.coordinate2.grid(row=8,column=1)

        self.X2Label=Label(self.master, text=",")
        self.X2Label.grid(row=8,column=2)

        self.coordinate2=Label(self.master, textvariable=self.Coord2y)
        self.coordinate2.grid(row=8,column=3)

        self.co2close=Label(self.master, text=")")
        self.co2close.grid(row=8,column=4)        


        
###################################################################################
        self.master.mainloop()

    def updatecoordinates(self):
        self.M0x= float(self.x0entry.get())
        self.M0y= float(self.y0entry.get())
        self.M1x= float(self.x1entry.get())
        self.M1y= float(self.y1entry.get())


    def updatevalues(self):
        self.sound_speed=int(self.Soundentry.get())
        self.clock_speed=1E6*int(self.CLKentry.get())
        self.time=1/self.clock_speed
        self.samples=int(self.sampleentry.get())
        self.R0=float(self.R0entry.get())
        self.R1=float(self.R1entry.get())
    
        
        
    def runprogram(self):
        self.M0x= float(self.x0entry.get())
        self.M0y= float(self.y0entry.get())
        self.M1x= float(self.x1entry.get())
        self.M1y= float(self.y1entry.get())

        self.sound_speed=int(self.Soundentry.get())     #reads in speed of sound from GUI
        self.clock_speed=1E6*int(self.CLKentry.get())   #converts clock from GUI to MHz
        self.time=1/self.clock_speed                #the minimum resoluton the device can detect
        self.samples=float(self.sampleentry.get())    #number of samples
        self.R0=float(self.R0entry.get())   #takes in radii from GUI
        self.R1=float(self.R1entry.get())   #will be overwritten in program
        self.Chan0bin=[]     #These two lists will be used later in the program
        Chan0=[]     #to store binary count and converted integers

########################################################
####The Program#########################################
########################################################

        a=b=iteration=t0=Chan0=0    #These three variable will be used later in the proram
        GPIO.output(3, False) 
        GPIO.output(5, False)   #ensuring startlow and J-K starts low

        print 'press the button to send the pulse'

        while a==0:
            if GPIO.input(13):  #Button is pressed or enter key pressed
                a=1            #escapes while loop

        
        GPIO.output(3, True)   #these are the two inputs for ADC/MCU pulse
        GPIO.output(7, False)   #Active low JK clear
        time.sleep(1)         #to ensure JK goes low
        GPIO.output(7, True)    #So the JK can clock
        GPIO.output(12, False)
                              #Sends initial pulse to speaker/clears counter
        time.sleep(0.1)
        GPIO.output(3, False) #counter starts counting from this point

        print 'Hey there buddy'

        while iteration<self.samples:
            
            print '\nPulse sent, waiting for signal from Mic.'

            print '\nPress the button to simulate the ADC falling'

            while a!=1:         #waits for the button press
                if GPIO.input(13):
                    GPIO.output(5, True)    #makes ADC high
                    print '\n\nADC high, press button to fall'
                    time.sleep(0.1)
                    a=1     #exits loop

            a=0

            while a!=1:
                if GPIO.input(13):
                    GPIO.output(5, False)   # will trigger J-K to change state
                    print 'ADC Fallen, press the button to load shift register'
                    time.sleep(0.1)
                    a=1

            a=0

            while a!=1:
                if GPIO.input(13):
                    GPIO.output(15, False)  #Loads the shift register
                    print 'Register Loaded, press button to change register to shift'
                    time.sleep(0.1)
                    a=1
            a=0
            
            while a!=1:
                if GPIO.input(13):
                    GPIO.output(15, True)   #chamges register to shift 
                    time.sleep(0.1)
                    a=1

            while b!=16:
                a=0
                print 'press the button to read in the next value from the shift register'
                while a!=1:
                    if GPIO.input(13):
                        self.Chan0bin.append(GPIO.input(8))  #reads in the value
                        print 'Binary value is: ', self.Chan0bin
                        time.sleep(0.1)
                        GPIO.output(12, True) #clocks the register
                        time.sleep(0.1)
                        GPIO.output(12, False)
                        b+=1
                        a=1
            a=0

            print 'Binary output is: ', self.Chan0bin

            while a!=16:
                Chan0+=(self.Chan0bin[a]*(2**(a)))
                a+=1

            print 'Which as an integer is: ', self.Chan            


            iteration+=1



        #Calculating exact co-ordinates
        Gamma=((self.R1**2)-(self.R0**2)+(self.M0x**2)-(self.M1x**2)+(self.M0y**2)-(self.M1y**2))/(2*(self.M0y-self.M1y))

        Beta=(-(self.M0x-self.M1x)/(self.M0y-self.M1y))

        A=(1+Beta)

        B=((2*Beta*Gamma)-(2*self.M0x)-(2*self.M0y*Beta))

        C=((self.M0x**2)+(Gamma**2)-(2*self.M0y*Gamma)+(self.M0y**2)-(self.R0**2))

        self.x1=(-B+(math.sqrt((B**2)-(4*A*C))))/(2*A)

        self.y1=((self.R1**2)-(self.R0**2)-(2*(self.M0x-self.M1x)*self.x1)+(self.M0x**2)-(self.M1x**2)+(self.M0y**2)-(self.M1y**2))/(2*(self.M0y-self.M1y))

        self.x2=(-B-(math.sqrt((B**2)-(4*A*C))))/(2*A)
                               
        self.y2=((self.R1**2)-(self.R0**2)-(2*(self.M0x-self.M1x)*self.x2)+(self.M0x**2)-(self.M1x**2)+(self.M0y**2)-(self.M1y**2))/(2*(self.M0y-self.M1y))

        
        self.Coord1x.set(self.x1)
        self.Coord1y.set(self.y1)
        self.Coord2x.set(self.x2)
        self.Coord2y.set(self.y2)


App()

