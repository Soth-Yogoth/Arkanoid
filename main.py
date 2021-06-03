from tkinter import *
import time

root = Tk()
root.geometry("800x600")
canvas = Canvas(root, highlightthickness=0)
canvas.pack(fill="both", expand=True)

bottom = canvas.create_line(20, 580, 780, 580, fill="white", tags="bottom")
horizontal_barriers = [canvas.create_line(80, 230, 220, 230, fill="black"),
                       canvas.create_line(480, 140, 640, 140, fill="black"),
                       canvas.create_line(480, 230, 640, 230, fill="black"),
                       canvas.create_line(20, 0, 780, 0, fill="black")]

vertical_barriers = [canvas.create_line(480, 140, 480, 230, fill="black"),
                     canvas.create_line(640, 140, 640, 230, fill="black"),
                     canvas.create_line(20, 0, 20, 580, fill="black"),
                     canvas.create_line(780, 0, 780, 580, fill="black")]

diagonal_barriers = [canvas.create_line(80, 230, 150, 120, fill="black"),
                     canvas.create_line(220, 230, 150, 120, fill="black")]


def game(x, y):

    score = 0
    blocks = [canvas.create_rectangle(120, 30, 190, 60, fill="orange"),
              canvas.create_rectangle(220, 30, 280, 60, fill="orange"),
              canvas.create_rectangle(500, 30, 560, 60, fill="orange"),
              canvas.create_rectangle(600, 100, 660, 130, fill="orange"),
              canvas.create_rectangle(700, 100, 760, 130, fill="orange"),
              canvas.create_rectangle(280, 100, 360, 130, fill="orange")]
    caret = canvas.create_rectangle(400, 540, 580, 560, outline="black", fill="black", tags="caret")
    ball = canvas.create_oval(440, 500, 460, 520, fill="black", tags="ball")

    def move_right(event):

        if canvas.coords(caret)[2] < 780:
            canvas.move(caret, 5, 0)
            pass

    def move_left(event):

        if canvas.coords(caret)[0] > 25:
            canvas.move(caret, -5, 0)
            pass

    root.bind('<Right>', move_right)
    root.bind('<Left>', move_left)

    while score < 120:

        time.sleep(0.01)
        overlap = canvas.find_overlapping(canvas.coords(ball)[0], canvas.coords(ball)[1],
                                          canvas.coords(ball)[2], canvas.coords(ball)[3])[0]
        for block in blocks:
            if overlap == block:
                canvas.move(ball, x, y)
                canvas.delete(block)
                score += 20
                y = -y

        for barrier in vertical_barriers:
            if overlap == barrier:
                canvas.move(ball, -2 * x, -2 * y)
                x = -x

        for barrier in horizontal_barriers:
            if overlap == barrier:
                canvas.move(ball, -2 * x, -2 * y)
                y = -y

        for barrier in diagonal_barriers:
            if overlap == barrier:
                canvas.move(ball, -2 * x, -2 * abs(y))
                x = -x
                y = -abs(y)

        if overlap == caret:
            canvas.move(ball, -2 * x, -2 * y)
            y = -y

        if overlap == bottom:
            break

        canvas.move(ball, x, y)
        canvas.update()

    if score < 120:
        label = Label(text="Game over", font='Arial 40')
        label.place(x=200, y=200)

    else:
        label = Label(text="Victory", font='Arial 40')
        label.place(x=200, y=200)

    def restart():

        canvas.delete(caret)
        canvas.delete(ball)
        label.place_forget()
        button.place_forget()
        for block in blocks:
            canvas.delete(block)
        game(2, -2)

    button = Button(text="Restart", font='Arial 20', command=restart)
    button.place(x=200, y=300)


game(2, -2)

root.mainloop()
