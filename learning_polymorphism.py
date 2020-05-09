# Polymorphism means literally many forms 
import turtle
import os

__location__= os.path.realpath(
        os.path.join(os.getcwd(), os.path.dirname(__file__)))
def main():
    filename = input("Please enter drawing filename: ") 
    t = turtle.Turtle()
    screen = t.getscreen()

    global __location__ 
    filename = os.path.join(__location__, filename)
    print(filename)
    file = open(filename, "r")
    command = file.readline().strip()

    while command != "":
        if command == "goto":
            x = float(file.readline())
            y = float(file.readline()) 
            width = float(file.readline()) 
            color = file.readline().strip() 
            t.width(width) 
            t.pencolor(color)
            t.goto(x,y)
        elif command == "circle":
            radius = float(file.readline()) 
            width = float(file.readline()) 
            color = file.readline().strip() 
            t.width(width) 
            t.pencolor(color) 
            t.circle(radius)
        elif command == "beginfill":
            color = file.readline().strip() 
            t.fillcolor(color) 
            t.begin_fill()
        elif command == "endfill":
            t.end_fill()
        elif command == "penup":
            t.penup()
        elif command == "pendown":
            t.pendown()
        else:
            print("Unknown command file:",command)

        command = file.readline().strip()

    file.close()
    t.ht()
    screen.exitonclick()
    print("Program Execution Completed.")

if __name__ == "__main__":
    main()