from tkinter import *   #ham tao giao dien
game = Tk ()            #tao man hinh cua so game
game.title("Cờ Caro")      #ten game

lb1 = Label(game, text = "Cờ Caro", font = ("Arial", 18), fg = "red")
lb1.pack()

screen = Canvas(master = game, width = 700, height = 600, background = "white")
screen.pack()

#tao o :(x1,y1,x2,y2)
rect = screen.create_line(200, 100, 200, 600)
rect = screen.create_line(225, 100, 225, 600)
rect = screen.create_line(250, 100, 250, 600)
rect = screen.create_line(275, 100, 275, 600)
rect = screen.create_line(300, 100,300 , 600)
rect = screen.create_line(325, 100,325 , 600)
rect = screen.create_line(350, 100,350 , 600)
rect = screen.create_line(375, 100,375 , 600)
rect = screen.create_line(400, 100,400 , 600)
rect = screen.create_line(425, 100,425 , 600)
rect = screen.create_line(450, 100,450 , 600)
rect = screen.create_line(475, 100,475 , 600)
rect = screen.create_line(500, 100,500 , 600)
rect = screen.create_line(525, 100,525 , 600)
rect = screen.create_line(550, 100,550 , 600)
rect = screen.create_line(575, 100,575 , 600)
rect = screen.create_line(600, 100,600 , 600)
rect = screen.create_line(625, 100,625 , 600)
rect = screen.create_line(650, 100,650 , 600)
rect = screen.create_line(675, 100,675 , 600)

rect = screen.create_line(0, 100,700, 100)
rect = screen.create_line(200, 125,700, 125)
rect = screen.create_line(200, 150,700, 150)
rect = screen.create_line(200, 175,700, 175)
rect = screen.create_line(200, 200,700, 200)
rect = screen.create_line(200, 225,700, 225)
rect = screen.create_line(200, 250,700, 250)
rect = screen.create_line(200, 275,700, 275)
rect = screen.create_line(200, 300,700, 300)
rect = screen.create_line(200, 325,700, 325)
rect = screen.create_line(200, 350,700, 350)
rect = screen.create_line(200, 375,700, 375)
rect = screen.create_line(200, 400,700, 400)
rect = screen.create_line(200, 425,700, 425)
rect = screen.create_line(200, 450,700, 450)
rect = screen.create_line(200, 475,700, 475)
rect = screen.create_line(200, 500,700, 500)
rect = screen.create_line(200, 525,700, 525)
rect = screen.create_line(200, 550,700, 550)
rect = screen.create_line(200, 575,700, 575)
rect = screen.create_line(200, 600,700, 600)

screen.update()





game.mainloop()         #chay game
