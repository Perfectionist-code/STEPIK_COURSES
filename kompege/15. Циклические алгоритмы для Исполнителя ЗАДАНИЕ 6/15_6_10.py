#from turtle import *

#tracer(0)
#screensize(5000, 5000)
#r = 20
#for _ in range(3):
    #down()
    #for i in range(2):
        #fd(7 * r)
        #rt(90)
        #fd(7 * r)
        #rt(90)
    #up()
    #fd(6 * r)
    #rt(90)
    #fd(6 * r)
    #lt(90)
#up()
#for x in range(-50, 50):
    #for y in range(-50, 50):
        #goto(x * r, y * r)
        #dot(3, 'red')
#update()
#mainloop()

counter = 0
for _ in range(5):
    word = input()
    if 'р' in word:
        counter = counter + 1

print(counter)