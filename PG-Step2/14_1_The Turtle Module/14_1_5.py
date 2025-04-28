import turtle as t


def is_rhomb(side1=200, side2=100):
    t.shape('turtle')
    for _ in range(2):
        t.forward(side1)
        t.left(120)
        t.forward(side2)
        t.left(60)


is_rhomb()
t.mainloop()
