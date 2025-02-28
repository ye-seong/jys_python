from tkinter import * 
from tkinter.messagebox import *
import Homepage_code as w
import tkinter as tk

class Homepage(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('홈페이지')
        self.geometry('1000x700')
        self.curr_user = ""


        # 프레임 미리 생성
        self.mainF = tk.Frame(self)
        self.adminlogF = tk.Frame(self)
        self.adminmodeF = tk.Frame(self)
        self.userF = tk.Frame(self)
        self.accF = tk.Frame(self)
        self.logF = tk.Frame(self)
        self.homeF = tk.Frame(self)
        self.userinfoF = tk.Frame(self)
        self.userlistF = tk.Frame(self)
        self.postlistF = tk.Frame(self)
        
        # 메인화면 출력
        
        self.initWindow()

        # 관리자로그인화면 위젯
        self.adminlogLabel = Label(self.adminlogF, text="관리자 비밀번호를 입력하세요.")
        self.adminlogEntry = Entry(self.adminlogF)
        self.adminlogBtn = Button(self.adminlogF, text="로그인", command=self.AdminLogin)

        # 관리자화면 위젯
        self.adminLabel = Label(self.adminmodeF, text="관리자 화면 입니다.")
        self.adminBtn1 = Button(self.adminmodeF, text="유저정보")
        self.adminBtn2 = Button(self.adminmodeF, text="조회수")
        self.adminBtn3 = Button(self.adminmodeF, text="뒤로가기", command=lambda: self.BackButton(self.adminBtn3))

        # 사용자화면 위젯
        self.userLabel = Label(self.userF, text="사용자 화면 입니다.")
        self.userBtn1 = Button(self.userF, text="회원가입", command=self.show_accF)
        self.userBtn2 = Button(self.userF, text="로그인", command=self.show_userlogF)

        # 회원가입화면 위젯
        self.accLabel = Label(self.accF, text="회원가입 화면 입니다.")
        self.accName = Entry(self.accF)
        self.accId = Entry(self.accF)
        self.accPass = Entry(self.accF)
        self.accBtn = Button(self.accF, text="회원가입", command=self.UserAcc)
        self.accBtn2 = Button(self.accF, text="뒤로가기", command=self.show_userF)

        # 로그인화면 위젯
        self.logLabel = Label(self.logF, text="로그인 화면 입니다.")
        self.logId = Entry(self.logF)
        self.logPass = Entry(self.logF)
        self.logBtn = Button(self.logF, text="로그인", command=self.UserLogin)

        # 홈페이지화면 위젯
        self.homeLabel = Label(self.homeF, text="홈페이지 입니다.")
        self.homeBtn = Button(self.homeF, text="개인정보", command=self.show_userinfoF)
        self.homeBtn2 = Button(self.homeF, text="유저리스트", command=self.show_userlistF)
        self.homeBtn3 = Button(self.homeF, text="자유게시판", command=self.GetPostList)
        self.homeBtn4 = Button(self.homeF, text="탈퇴")
        self.homeBtn5 = Button(self.homeF, text="뒤로가기", command=lambda: self.BackButton(self.homeBtn5))

        # 개인정보화면 위젯
        self.userinfoLabel = Label(self.userinfoF, text="개인정보 화면 입니다.")
        self.userinfoLabel2 = Label(self.userinfoF)
        self.userinfoBtn = Button(self.userinfoF, text="뒤로가기", command=lambda: self.BackButton(self.userinfoBtn))

        # 유저리스트 위젯
        self.userlistLabel = Label(self.userlistF, text="유저리스트 화면 입니다.")
        self.userlistLabel2 = Label(self.userlistF)
        self.userlistBtn = Button(self.userlistF, text="뒤로가기", command=lambda: self.BackButton(self.userlistBtn))

        # 자유게시판 위젯
        self.postlistLabel = Label(self.postlistF, text="자유게시판 화면 입니다.")
      
        
    # pack

    def pack_adminlogF(self):
        self.adminlogLabel.pack(pady=20)
        self.adminlogEntry.pack()
        self.adminlogBtn.pack()

    def pack_adminmodeF(self):
        self.adminLabel.pack(pady=20)
        self.adminBtn1.pack()
        self.adminBtn2.pack()
        self.adminBtn3.pack()
        
    def pack_userF(self):
        self.userLabel.pack(pady=20)
        self.userBtn1.pack()
        self.userBtn2.pack()

    def pack_accF(self):
        self.accLabel.pack()
        self.accName.pack()
        self.accId.pack()
        self.accPass.pack()
        self.accBtn.pack()
        self.accBtn2.pack()

    def pack_userlogF(self):
        self.logLabel.pack()
        self.logId.pack()
        self.logPass.pack()
        self.logBtn.pack()

    def pack_homeF(self):
        self.homeLabel.pack()
        self.homeBtn.pack()
        self.homeBtn2.pack()
        self.homeBtn3.pack()
        self.homeBtn4.pack()
        self.homeBtn5.pack()

    def pack_userinfoF(self):
        self.userinfoLabel.pack()
        info = w.GetUserInfo(self.curr_user)
        self.userinfoLabel2.config(text=info)
        self.userinfoLabel2.pack()
        self.userinfoBtn.pack()

    def pack_userlistF(self):
        self.userlistLabel.pack()
        users = w.GetUserList()
        self.userlistLabel2.config(text=users)
        self.userlistLabel2.pack()
        self.userlistBtn.pack()

    def pack_postlistF(self):
        self.postlistLabel.pack()

    # show Frame

    def show_mainF(self):
        self.adminlogF.pack_forget()
        self.userF.pack_forget()
        self.mainF.pack()

    def show_adminlogF(self):
        self.mainF.pack_forget()
        self.adminlogF.pack()
        self.pack_adminlogF()

    def show_adminmodeF(self):
        self.adminlogF.pack_forget()
        self.adminmodeF.pack()
        self.pack_adminmodeF()

    def show_userF(self):
        self.mainF.pack_forget()
        self.accF.pack_forget()
        self.userF.pack()
        self.pack_userF()

    def show_accF(self):
        self.userF.pack_forget()
        self.accF.pack()
        self.pack_accF()

    def show_userlogF(self):
        self.userF.pack_forget()
        self.logF.pack()
        self.pack_userlogF()

    def show_homeF(self):
        self.logF.pack_forget()
        self.userinfoF.pack_forget()
        self.homeF.pack()
        self.pack_homeF()

    def show_userinfoF(self):
        self.homeF.pack_forget()
        self.userinfoF.pack()
        self.pack_userinfoF()

    def show_userlistF(self):
        self.homeF.pack_forget()
        self.userlistF.pack()
        self.pack_userlistF()

    def show_postlistF(self):
        self.homeF.pack_forget()
        self.postlistF.pack()
        self.pack_postlistF()
        self.PostList()

    # 코드

    def AdminLogin(self):
        password = self.adminlogEntry.get()
        if w.AdminPass(password):
            self.show_adminmodeF()
        else:
            if w.Admin.admin_value:
                showerror('위젯', f'비밀번호를 다시 입력해주세요. ({w.Admin.error_num}회 오류)') 
            else:
                showerror('위젯', f'비밀번호 3회 오류로 접속하실 수 없습니다.')             

    def UserAcc(self):
        name = self.accName.get()
        id = self.accId.get()
        password = self.accPass.get()

        result = w.UserAccount(name, id, password)

        if result == "success":
            showinfo('위젯', '회원가입이 완료 되었습니다.')  
            self.accName.delete(0, tk.END)
            self.accId.delete(0, tk.END)
            self.accPass.delete(0, tk.END)
            self.show_userF()  
        elif result == "name_error":
            showerror('위젯', '같은 이름이 있습니다.')
        elif result == "id_error":
            showerror('위젯', '같은 아이디가 있습니다.')
        else:
            showerror('위젯', '다시 입력 해주세요.')             

    def UserLogin(self):
        id = self.logId.get()
        password = self.logPass.get()

        user = w.UserLogin(id, password)
        self.curr_user = user
        
        if user == "error":
            showerror('위젯', '다시 입력 해주세요.')
        else:
            showinfo('위젯', f'{user}님, 환영합니다!')
            self.show_homeF()

    def BackButton(self, button):
        if button == self.homeBtn5:
            self.homeF.pack_forget()
            self.show_userlogF()
        elif button == self.userinfoBtn:
            self.userinfoF.pack_forget()
            self.show_homeF()
        elif button == self.userlistBtn:
            self.userlistF.pack_forget()
            self.show_homeF()
        elif button == self.adminBtn3:
            self.adminmodeF.pack_forget()

    def GetPostList(self):
        for post in w.post_list:
            print(post.post_title)
            Button(self.postlistF, text=post.post_title).pack()

    def initWindow(self):
        self.mainF.pack()
        Label(self.mainF, text="모드를 선택하세요.").pack(pady=20)
        Button(self.mainF, text="관리자", command=self.show_adminlogF).pack()
        Button(self.mainF, text="사용자", command=self.show_userF).pack()

if __name__=="__main__":
    homepage = Homepage()
    w.LoadUserFromDB(w.user_list)
    w.LoadPostFromDB(w.post_list)
    homepage.mainloop()


