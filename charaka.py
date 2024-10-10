import turtle

turtle.bgcolor("blue")
turtle.title("Turtle Graphics Drawing")


ninja = turtle.Turtle()
ninja.speed(10)
ninja.color("red") 

for i in range(13):
    ninja.forward(180)
    ninja.right(3)
    ninja.forward(2)
    ninja.left(65)
    ninja.forward(50)
    ninja.right(32)
    
    ninja.penup()
    ninja.setposition(0, 2)
    ninja.pendown()

    ninja.left(1) 
   
    for j in range(2):
        ninja.forward(40)
        ninja.right(3)
        ninja.forward(2)
        ninja.left(65)
        ninja.forward(50)
        ninja.right(32)

        
        ninja.penup()
        ninja.setposition(0, 2)
        ninja.pendown()

        
        ninja.left(10) 

turtle.done()