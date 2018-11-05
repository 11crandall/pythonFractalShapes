import turtle, math, _thread, time, random

def colorshift(bill):
    color = "#%06x" % random.randint(0, 0xFFFFFF)
    bill.pencolor(color)
def fractalLine(bill,sides,instances,length,toRadius,heading=0):
    
    #wn.title("Drawing fractal at level "+str(instances)+'.')
    

    bill.setheading(heading)
    colorshift(bill)
    if instances == 0:#no breaks, just a line
    #add decrementing color generation
        bill.forward(length)

    else:#loop starts stacking here
        spikeLen=(toRadius)/math.sin(math.radians(85))
        fractalLen=(length/2)-(toRadius)/math.tan(math.radians(85))
        toRadius = toRadius/math.tan(180/sides)
        fractalLine(bill,sides,(instances-1),fractalLen,toRadius,heading)
        heading-=85
        fractalLine(bill,sides,(instances-1),spikeLen,toRadius,heading)
        heading+=170
        fractalLine(bill,sides,(instances-1),spikeLen,toRadius,heading)
        heading-=85
        fractalLine(bill,sides,(instances-1),fractalLen,toRadius,heading)



def fractalShape(level,length,sides,heading=0,pos=(0,0), speed=0):
    bills = [turtle.Turtle() for x in range(sides)]
    wn=turtle.Screen()
    #change background color???
    wn.bgcolor("gray")

    for bill in bills:
        bill.hideturtle()  
        bill.up()
        bill.setposition(pos[0],pos[1])
        bill.down()    
        bill.speed(speed)

        #add color???
        colorshift(bill)
        _thread.start_new_thread(fractalLine,(bill,sides,level,length,(length/(2*math.tan(math.radians(180/sides))))*.95,heading))

        pos = (pos[0] + length * math.cos(math.radians(heading)), pos[1] + length * math.sin(math.radians(heading)))
        heading-=360 / sides


#Proof it works
boxCoord = [(-500, -100), (-250, -100), (0, -100), (250, -100)]
wn = turtle.Screen()

for x in range(4):
   _thread.start_new_thread(fractalShape,(x,80,6,0, boxCoord[x], 5))

#_thread.start_new_thread(fractalShape,(0,100,8,0, boxCoord[0], 5))
#_thread.start_new_thread(fractalShape,(3,100,8,0, boxCoord[3], 5))
# _thread.start_new_thread(fractalShape,(4, 500, 11, 360/11, (-1000, 300), 0))
turtle.exitonclick()
