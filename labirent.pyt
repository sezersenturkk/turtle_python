import turtle
screen=turtle.Screen()
screen.bgcolor("light blue")

labirent=[
    "XXXXX XXXXXXXXXXXXXXXXXXXXXXXXXXX",
    "X     X   X     X     X         X",
    "X XXXXX XXX XXX X XXX X XXXXXXX X",
    "X X       X     X   X X         X",
    "X XXX XXX XXXXXXX XXX X XXX XXX X",
    "X   X     X       X X X   X   X X",
    "X XXXXX XXX XXXXXXXXXXX XXX XXX X",
    "X X     X   X         X X     X X",
    "X XXX X XXX XXXXXXXXX XXX XXXXXXX",
    "X   X X   X                 X   X",
    "X XXX XXX XXX XXXXXXX XXXXXXX X X",
    "X       X   X       X       X   X",
    "XX  XXXX XXX XXXXX XXX XXX XXX  X",
    "X       X     X   X X   X X X   X",
    "X  XXX  X XX    XX X   X     X  X",
    "X                         X  X  X",
    "XXXXXXXXXXXXXXXXXXXXXXXXXXX XXXXX"
]


#OYUNCUNUN BAŞLANGIÇ POZİSYONU
konum_x=245
konum_y=-175



labirent_duvarı=turtle.Turtle()
labirent_duvarı.color("orange")
labirent_duvarı.penup()
labirent_duvarı.shape("square")
labirent_duvarı.speed(0)
def draw_maze():
    for y in range(len(labirent)):
        for x in range(len(labirent[y])):
            screen_x = -400 + (x * 24)
            screen_y = 260 - (y * 24)
            if labirent[y][x] == "X":
                        labirent_duvarı.goto(screen_x, screen_y)
                        labirent_duvarı.stamp()
                        
            

#karakter
hero=turtle.Turtle()
hero.penup()
hero.left(90)
hero.shape("turtle")
hero.color("green")
hero.speed(5)
konum_x=245
konum_y=-175




#karakterin konumu
def hero_position_update():
    global konum_x
    global konum_y
    konum_x=hero.xcor()
    konum_y=hero.ycor()
    
    hero.goto(konum_x,konum_y)


#karakteri hareketi

def move_up():
      ileri=hero.forward(30)
      hero_position_update()

def move_down():
      hero.backward(30)
      hero_position_update()

def move_left():
      hero.left(90)
      hero_position_update()

def move_right():
      hero.right(90)
      hero_position_update()

turtle.listen()
turtle.onkey(move_up, "Up")
turtle.onkey(move_down, "Down")
turtle.onkey(move_left, "Left")
turtle.onkey(move_right, "Right")





    
    

      
















move_down()
move_left()
move_down()
move_up()
hero_position_update()
draw_maze()



















turtle.mainloop()
