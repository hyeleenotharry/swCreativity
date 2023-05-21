import tkinter as tk
from tkinter import messagebox

def validate_login():
    username = entry_username.get()
    password = entry_password.get()

    # 로그인 정보 확인
    if username == "hllee" and password == "1029":
        messagebox.showinfo("로그인 성공", "로그인에 성공했습니다.")
        # 다음 페이지로 이동하는 코드를 작성하세요
    else:
        messagebox.showerror("로그인 실패", "잘못된 사용자 이름 또는 비밀번호입니다.")

# 윈도우 생성
window = tk.Tk()
window.title("로그인 페이지")

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

# 로그인 버튼
button_login = tk.Button(window, text="로그인", command=validate_login)
button_login.pack()

# 윈도우 실행
window.mainloop()
