from tkinter import *

win = Tk()  #창 생성

win.geometry("1000x500") #창 크기
win.title("Empty Window")   #창 제목
win.option_add("*font", "맑은고딕 25")
win.configure(bg="red")

btn = Button(win, text="버튼")
btn.pack()

win.mainloop()  #창 실행
