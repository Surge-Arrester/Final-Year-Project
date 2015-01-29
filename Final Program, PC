from Tkinter import *
import math
import matplotlib.pyplot as plt
import numpy as np

class App:
    def __init__(self):
        
        self.master=Tk()
        self.master.title("Location of an Acoustic Event - Cameron Hargreaves")

        self.M0x=StringVar()
        self.M0y=StringVar()
        self.M1x=StringVar()                #Defining the various variables to be used later
        self.M1y=StringVar()
        self.sound_speed=StringVar()
        self.clock_speed=StringVar()
        self.samplenumber=StringVar()
        self.R0=StringVar()
        self.R1=StringVar()
        self.x1=StringVar()
        self.y1=StringVar()
        self.x2=StringVar()
        self.y2=StringVar()
        self.Coord1x=StringVar()
        self.Coord1y=StringVar()
        self.Coord2x=StringVar()
        self.Coord2y=StringVar()

        
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
        
    def runprogram(self):
        M0x= float(self.x0entry.get())
        M0y= float(self.y0entry.get())
        M1x= float(self.x1entry.get())
        M1y= float(self.y1entry.get())

        self.sound_speed=int(self.Soundentry.get())
        self.clock_speed=1E6*int(self.CLKentry.get())
        self.time=1/self.clock_speed
        self.samples=int(self.sampleentry.get())

    
        R0=float(self.R0entry.get())
        R1=float(self.R1entry.get())

        #Calculating exact co-ordinates
        Gamma=((R1**2)-(R0**2)+(M0x**2)-(M1x**2)\
               +(M0y**2)-(M1y**2))/(2*(M0y-M1y))
        
        Beta=(-(M0x-M1x)/(M0y-M1y))

        A=(1+Beta)

        B=((2*Beta*Gamma)-(2*M0x)-(2*M0y*Beta))

        C=((M0x**2)+(Gamma**2)-(2*M0y*Gamma)+(M0y**2)-(R0**2))

        x1=(-B+(math.sqrt((B**2)-(4*A*C))))/(2*A)

        y1=((R1**2)-(R0**2)-(2*(M0x-M1x)*x1)+(M0x**2)-(M1x**2)+(M0y**2)-(M1y**2))/(2*(M0y-M1y))

        x2=(-B-(math.sqrt((B**2)-(4*A*C))))/(2*A)
                               
        y2=((R1**2)-(R0**2)-(2*(M0x-M1x)*x2)+(M0x**2)-(M1x**2)+(M0y**2)-(M1y**2))/(2*(M0y-M1y))
        
        self.Coord1x.set("%.2f" %x1)
        self.Coord1y.set("%.2f" %y1)
        self.Coord2x.set("%.2f" %x2)
        self.Coord2y.set("%.2f" %y2)

        #Giving the plot some labels

        plt.ylabel('Y Co-ordinates')
        plt.xlabel('X-Co-ordinates')

        #plot the data

        plt.axis ((0, 10, 0, 10))   #so the original axis shows just (0,0) to (10, 10)

        plt.plot ([-10,10],[0,0], 'k') #prints the axis
        plt.plot ([0,0], [-10,10], 'k')
        
        plt.plot (M0x, M0y, 'bo')       #The two microphones are added
        plt.plot (M1x, M1y, 'bo')

        if x1>=0 and y1>=0:           
            plt.plot ([M0x, x1],[M0y, y1], 'r--')    #Plotting the radius of the first
            plt.plot ([M1x, x1],[M1y, y1], 'r--')    #Co-ordinates

            
            plt.plot ([x1, x1],[0, y1], 'b') #Plotting the X Co-ordinate of the first set
            plt.plot ([0, x1], [y1, y1], 'r') #Plotting the Y Co-ordinate of the first set

            plt.text (x1, 0, "%.2f" %(x1))    #adding labels on the axis
            plt.text (0, y1, "%.2f" %(y1))
            
        if x2>=0 and y2>=0: 
            plt.plot ([M0x, x2],[M0y, y2], 'b--')    #Plotting the radius of the
            plt.plot ([M1x, x2],[M1y, y2], 'b--')    #second set of co-ordinates
            
            plt.plot ([x2, x2],[0, y2], 'b') #Plotting the X Co-ordinate of the second set
            plt.plot ([0, x2], [y2, y2], 'r') #Plotting the Y Co-ordinate of the second set

            plt.text (x2, 0, "%.2f" %(x2))
            plt.text (0, y2, "%.2f" %(y2))
        
        plt.title('Location of Acoustic Event')
        plt.show()



App()

