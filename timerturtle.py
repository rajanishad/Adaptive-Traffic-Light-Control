import time
import turtle
import sys

wn=turtle.Screen()
wn.title("stop light")
wn.bgcolor("black")


pen=turtle.Turtle()
pen.color("white")
pen.speed(0)
pen.width(5)
pen.penup()
pen.goto(100,100)
pen.pendown()
pen.fd(200)
pen.penup()
pen.goto(100,100)
pen.lt(90)
pen.pendown()
pen.fd(170)
pen.penup()
pen.goto(-100,100)
pen.pendown()
pen.fd(170)
pen.penup()
pen.goto(-100,100)
pen.pendown()
pen.lt(90)
pen.fd(200)
pen.penup()
pen.goto(-100,-100)
pen.pendown()
pen.fd(200)
pen.penup()
pen.goto(-100,-100)
pen.pendown()
pen.lt(90)
pen.fd(170)
pen.penup()
pen.goto(100,-100)
pen.pendown()
pen.fd(170)
pen.penup()
pen.goto(100,-100)
pen.pendown()
pen.lt(90)
pen.fd(200)
pen.penup()
pen.hideturtle()

class Timer(turtle.Turtle):
    def __init__(self, x, y, c, p, sec):
        turtle.Turtle.__init__(self)
        self.sec = sec
        self.pensize = p
        self.ht()
        self.color(c)
        self.penup()
        self.goto(x, y)
        self.write(time.strftime("%M:%S", time.gmtime(self.sec)), False
                   , align="center", font=("Arial", self.pensize, "bold"))
    def start(self):
        self.clear()
        self.write(time.strftime("%M:%S", time.gmtime(self.sec)), False
                   , align="center", font=("Arial", self.pensize, "bold"))
        self.sec -= 1

        if self.sec != -1:
            wn.ontimer(self.start, 1000)
        time.sleep(1)
    def stop(self):
        self.clear()

class Stoplight():
    def __init__(self,x,y):
        self.pen=turtle.Turtle()
        self.pen.penup()
        self.pen.hideturtle()
        self.pen.speed(0)
        self.pen.color("white")
        self.pen.goto(x-30,y+60)
        self.pen.pendown()
        self.pen.fd(60)
        self.pen.rt(90)
        self.pen.fd(120)
        self.pen.rt(90)
        self.pen.fd(60)
        self.pen.rt(90)
        self.pen.fd(120)
        
        self.color=""
        
        self.red_light=turtle.Turtle()
        self.yellow_light=turtle.Turtle()
        self.green_light=turtle.Turtle()
        
        self.red_light.speed(0)
        self.yellow_light.speed(0)
        self.green_light.speed(0)

        self.red_light.color("grey")
        self.yellow_light.color("grey")
        self.green_light.color("grey")

        self.red_light.shape("circle")
        self.yellow_light.shape("circle")
        self.green_light.shape("circle") 
              
        self.red_light.penup()
        self.yellow_light.penup()
        self.green_light.penup()         

        self.red_light.goto(x,y+40)
        self.yellow_light.goto(x,y)
        self.green_light.goto(x,y-40)
    
    def change_color(self,color):    
        self.red_light.color("grey")
        self.yellow_light.color("grey")
        self.green_light.color("grey") 
        
        if color=="red":
            self.red_light.color("red")  
            self.color="red" 
        elif color=="yellow":
            self.yellow_light.color("yellow")  
            self.color="yellow"   
        elif color=="green":
            self.green_light.color("green")  
            self.color="green" 
        else:
            print("error:unknown color{}".format(color))
            
stoplight1=Stoplight(0,200)
stoplight2=Stoplight(200,0)
stoplight3=Stoplight(0,-200)
stoplight4=Stoplight(-200,0)

while True:
    
    stoplight1.change_color("red")
    stoplight2.change_color("red")
    stoplight3.change_color("red")
    stoplight4.change_color("red")


    t1=int(input("enter value of t1= \n"))



    
    stoplight1.change_color("green")
    timer1= Timer(0, 100, "white", 20, t1)
    timer1.start() 

   
    

   

    t2=int(input("enter value of t2= \n"))



    stoplight1.change_color("red")
    stoplight2.change_color("green")
    timer2= Timer(100, 0, "white", 20, t2)
    timer2.start()
   





    t3=int(input("enter value of t3= \n"))



    stoplight2.change_color("red")
    stoplight3.change_color("green")
    timer3= Timer(0, -100, "white", 20, t3)
    timer3.start()

 


    t4=int(input("enter value of t4= \n"))

    stoplight3.change_color("red")
    stoplight4.change_color("green")
    timer4= Timer(-100, 0, "white", 20, t4)
    timer4.start()


    timer1.stop()
    timer2.stop()
    timer3.stop()
    timer4.stop()




               
 
 
 
            



wn.mainloop()