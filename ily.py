
''' 
MIT License

Copyright (c) 2022 ishandev1337

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

''''


from tkinter.font import BOLD
import turtle 

t = turtle.Turtle()
turtle.Screen().bgcolor("black")

t.penup()
t.goto(-230,175)
t.pendown()

t.pencolor("white")
t.pensize(15)
t.forward(100)
t.backward(50)
t.right(100)
t.forward(170)
t.right(90)
t.forward(50)
t.backward(100)

t.penup()
t.goto(0,0)
t.pendown()

t.color('red')
t.begin_fill()
t.right(130)
t.forward(133)
t.circle(50,200)
t.right(140)
t.circle(50,200)
t.forward(133)
t.end_fill()

t.penup()
t.goto(140,175)
t.pendown()

t.pencolor('white')
t.right(40)
t.forward(120)
t.circle(60,180)
t.forward(120)


t.penup()
t.goto(-150,-150)
t.pendown()
# t.write('Ishan', font=("Arial", 50 , "bold"))


t.hideturtle()
turtle.done()
