import tkinter as tk
from tkinter import messagebox
from tkinter import *
from PIL import ImageTk, Image
import tkinter.ttk as ttk

def validate_login():
    
    username = entry_username.get()
    password = entry_password.get()
    incom_value = combobox.get()

    # Check if the combobox value is selected
    if not incom_value or incom_value == "불편한 점을 고르세요":
        messagebox.showerror("경고", "사유를 선택해주세요.")
        return

    # 로그인 정보 확인
    if username == "hllee" and password == "1029":
        messagebox.showinfo("로그인 성공", "로그인에 성공했습니다.")
        open_map_window()  # Open the map window
    else:
        messagebox.showerror("로그인 실패", "잘못된 사용자 이름 또는 비밀번호입니다.")

#login 이후 지도
def open_map_window():
    #community page
    def open_com_window():

        new_window.destroy()

        new_window2 = tk.Tk()
        new_window2.title("Community Window")
        new_window2.geometry("300x500")
        # Load the image
        image_path = "img/com_label.png"
        image = Image.open(image_path)
        image = image.resize((300, 100), Image.ANTIALIAS)  # Resize the image to fit the window

        # Convert the image to Tkinter-compatible format
        com_image = ImageTk.PhotoImage(image)

        # Create a label and set the image as the background
        background_label = tk.Label(new_window2, image=com_image)
        background_label.place(x=0, y=0, width=300, height=100)
        #첫번째 게시글
        def open_com1_window():
            new_window2.destroy()

            new_window3 = tk.Tk()
            new_window3.title("Community Window 1")
            new_window3.geometry("300x500")
            # Load the image
            image_path = "img/게시글.png"
            image = Image.open(image_path)
            image = image.resize((300, 500), Image.ANTIALIAS)  # Resize the image to fit the window

            # Convert the image to Tkinter-compatible format
            com_img = ImageTk.PhotoImage(image)

            # Create a label and set the image as the background
            background_label = tk.Label(new_window3, image=com_img)
            background_label.place(x=0, y=0, relwidth=1, relheight=1)

            new_window3.mainloop()

        image = Image.open("img/com1.png")
        image = image.resize((300,100),Image.ANTIALIAS)
        btn1_img = ImageTk.PhotoImage(image)
        btn1 = tk.Button(new_window2, width=300, height=100, image=btn1_img, command=open_com1_window)
        btn1.place(x=0,y=100)

        image = Image.open("img/com2.png")
        image = image.resize((300,100),Image.ANTIALIAS)
        btn2_img = ImageTk.PhotoImage(image)
        btn2 = tk.Button(new_window2, width=300, height=100, image=btn2_img)
        btn2.place(x=0,y=200)

        image = Image.open("img/com3.png")
        image = image.resize((300,100),Image.ANTIALIAS)
        btn3_img = ImageTk.PhotoImage(image)
        btn3 = tk.Button(new_window2, width=300, height=100, image=btn3_img)
        btn3.place(x=0,y=300)

        image = Image.open("img/com4.png")
        image = image.resize((300,100),Image.ANTIALIAS)
        btn4_img = ImageTk.PhotoImage(image)
        btn4 = tk.Button(new_window2, width=300, height=100, image=btn4_img)
        btn4.place(x=0,y=400)

        new_window2.mainloop()


    #길찾기 선택 버튼 - 버스, 지하철, 도보
    def open_new_window():
        #지하철
        def open_sub_window():
            new_window1.destroy()

            new_sub = tk.Tk()
            new_sub.title("Subway")
            new_sub.geometry("300x500")

            # Load the image
            image_path = "img/지하철.png"
            image = Image.open(image_path)
            image = image.resize((300, 500), Image.ANTIALIAS)  # Resize the image to fit the window

            # Convert the image to Tkinter-compatible format
            bg_image = ImageTk.PhotoImage(image)

            # Create a label and set the image as the background
            background_label = tk.Label(new_sub, image=bg_image)
            background_label.place(x=0, y=0, relwidth=1, relheight=1)

            #btn = tk.Button(new_sub, width=50, height=50, command=open_new_window)
            #btn.place(x=0,y=200)

            new_sub.mainloop()
        #버스
        def open_bus_window():
            new_window1.destroy()

            new_bus = tk.Tk()
            new_bus.title("Subway")
            new_bus.geometry("300x500")

            # Load the image
            image_path = "img/버스.png"
            image = Image.open(image_path)
            image = image.resize((300, 500), Image.ANTIALIAS)  # Resize the image to fit the window

            # Convert the image to Tkinter-compatible format
            bg_image = ImageTk.PhotoImage(image)

            # Create a label and set the image as the background
            background_label = tk.Label(new_bus, image=bg_image)
            background_label.place(x=0, y=0, relwidth=1, relheight=1)


            new_bus.mainloop()
        #도보
        def open_walk_window():
            new_window1.destroy()

            new_walk = tk.Tk()
            new_walk.title("walk")
            new_walk.geometry("300x500")

            # Load the image
            image_path = "img/도보.png"
            image = Image.open(image_path)
            image = image.resize((300, 500), Image.ANTIALIAS)  # Resize the image to fit the window

            # Convert the image to Tkinter-compatible format
            bg_image = ImageTk.PhotoImage(image)

            # Create a label and set the image as the background
            background_label = tk.Label(new_walk, image=bg_image)
            background_label.place(x=0, y=0, relwidth=1, relheight=1)

            

            new_walk.mainloop()

        new_window.destroy()

        new_window1 = tk.Tk()
        new_window1.title("Select Window")
        new_window1.geometry("300x500")

        # Load the image
        image_path = "img/sel_top.png"
        image = Image.open(image_path)
        image = image.resize((300, 200), Image.ANTIALIAS)  # Resize the image to fit the window

        # Convert the image to Tkinter-compatible format
        sel_image = ImageTk.PhotoImage(image)

        # Create a label and set the image as the background
        background_label = tk.Label(new_window1, image=sel_image)
        background_label.place(x=0, y=0, width=300, height=200)

        image = Image.open("img/btn1.png")
        image = image.resize((300,100),Image.ANTIALIAS)
        btn1_img = ImageTk.PhotoImage(image)
        btn1 = tk.Button(new_window1, width=300, height=100, image=btn1_img, command=open_sub_window)
        btn1.place(x=0,y=200)

        image = Image.open("img/btn2.png")
        image = image.resize((300,100),Image.ANTIALIAS)
        btn2_img = ImageTk.PhotoImage(image)
        btn2 = tk.Button(new_window1, width=300, height=100, image=btn2_img, command=open_bus_window)
        btn2.place(x=0,y=300)

        image = Image.open("img/btn3.png")
        image = image.resize((300,100),Image.ANTIALIAS)
        btn3_img = ImageTk.PhotoImage(image)
        btn3 = tk.Button(new_window1, width=300, height=100, image=btn3_img, command=open_walk_window)
        btn3.place(x=0,y=400)

        new_window1.mainloop()

    # Destroy the current window
    window.destroy()

    # Create a new window
    new_window = tk.Tk()
    new_window.title("Map Window")
    new_window.geometry("300x500")

    # Load the image
    image_path = "img/map.jpeg"
    image = Image.open(image_path)
    image = image.resize((300, 500), Image.ANTIALIAS)  # Resize the image to fit the window

    # Convert the image to Tkinter-compatible format
    background_image = ImageTk.PhotoImage(image)

    # Create a label and set the image as the background
    background_label = tk.Label(new_window, image=background_image)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

    input_text = Entry(new_window, width=28)
    input_text.place(x=1,y=10)
    
    image_path = "img/search.png"
    image = Image.open(image_path)
    image = image.resize((27, 25), Image.ANTIALIAS)  # Resize the image to fit the window
    btnimg = ImageTk.PhotoImage(image)

    button_search = tk.Button(new_window, width=27, height=25, image=btnimg, command=open_new_window)
    button_search.place(x=265,y=10)
    
    image_path = "img/warn.png"
    image = Image.open(image_path)
    image = image.resize((25, 25), Image.ANTIALIAS)  # Resize the image to fit the window
    warnimg = ImageTk.PhotoImage(image)

    def showAlert():
        messagebox.showerror("주의","요철이 심한 길입니다.")

    button_warn = tk.Button(new_window, width=25, height=25, image=warnimg, command=showAlert)
    button_warn.place(x=215,y=260)

    #community button
    image_path = "img/com.png"
    image = Image.open(image_path)
    image = image.resize((150, 60), Image.ANTIALIAS)  # Resize the image to fit the window
    comimg = ImageTk.PhotoImage(image)

    button_com = tk.Button(new_window, width=150, height=60, image=comimg, command=open_com_window)
    button_com.place(x=150,y=440)

    #home button
    image_path = "img/home.png"
    image = Image.open(image_path)
    image = image.resize((150, 60), Image.ANTIALIAS)  # Resize the image to fit the window
    homeimg = ImageTk.PhotoImage(image)

    button_home = tk.Button(new_window, width=150, height=60, image=homeimg)
    button_home.place(x=0,y=440)


    new_window.mainloop()


# 윈도우 생성
window = tk.Tk()
window.title("로그인 페이지")
window.geometry("300x500")

# 사용자 이름 레이블과 입력 필드
label_username = tk.Label(window, text="사용자 이름")
label_username.pack()
entry_username = tk.Entry(window)
entry_username.pack()

# 비밀번호 레이블과 입력 필드
label_password = tk.Label(window, text="비밀번호")
label_password.pack()
entry_password = tk.Entry(window, show="*")
entry_password.pack()

# combobox
label_incom = tk.Label(window, text="사유(필수 입력 사항)")
label_incom.pack()
incom = ["휠체어", "지팡이", "기타"]
combobox = ttk.Combobox(window, height=3, values=incom)
combobox.set("불편한 점을 고르세요")
combobox.pack()

# 로그인 버튼
button_login = tk.Button(window, text="로그인", command=validate_login)
button_login.pack()

# 윈도우 실행
window.mainloop()
