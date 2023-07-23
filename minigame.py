from tkinter import ttk
import tkinter as tk
import sv_ttk
import pyrebase
import sys
import random
import requests

fbcfg = {
    'apiKey': "AIzaSyBN6iHuE_jxYrX7bSngoXrm8xxYEYGjH4Q",
    'authDomain': "guessuerinfo.firebaseapp.com",
    'databaseURL': "https://guessuerinfo-default-rtdb.asia-southeast1.firebasedatabase.app",
    'projectId': "guessuerinfo",
    'storageBucket': "guessuerinfo.appspot.com",
    'messagingSenderId': "162146078926",
    'appId': "1:162146078926:web:ec9820e46c00a7f12fc09f",
    'measurementId': "G-HWQ0RPN8VE"
}
fb = pyrebase.initialize_app(fbcfg)
db = fb.database()

def exit():
    sys.exit()

def about():
    CustomMessageBox(title='About',message='This App is created by NotiOff\nYou can buy or witdraw credit\nby sending direct mail to \n"hahccn@gmail.com".\nYou can start play with\n100 Free credit.\nIn Guess Game, if you win,\nYou get 10 Time to bet amount.\nIn Coin Flip, if you win,\nYou get 2 time to bet amount.\nIn Multiple Choice, if you win,\nYou get 4 time to bet amount.')

def forget():
    CustomMessageBox(title='Forget Password',message='You can sent direct email to \n"hahccn@gmail.com" \nfor reset your password.')

class RegisterFrame(ttk.Frame):
    def __init__(self,container):
        super().__init__(container)
        self.pack()
        self.label1 = ttk.Label(self,text='Register',font=('Arial 15 bold'))
        self.label1.grid(row=0,column=0,columnspan=2,padx=5,pady=5)
        self.label2 = ttk.Label(self,text='Username')
        self.label2.grid(row=1,column=0,padx=5,pady=5)
        self.entry1 = ttk.Entry(self,width=25)
        self.entry1.grid(row=1,column=1,padx=5,pady=5)
        self.label7 = ttk.Label(self, text='Email')
        self.label7.grid(row=2, column=0, padx=5, pady=5)
        self.entry4 = ttk.Entry(self, width=25)
        self.entry4.grid(row=2, column=1, padx=5, pady=5)
        self.label3 = ttk.Label(self,text='Password')
        self.label3.grid(row=3,column=0,pady=5,padx=5)
        self.entry2 = ttk.Entry(self,width=25,show='*')
        self.entry2.grid(row=3,column=1,padx=5,pady=5)
        self.label4 = ttk.Label(self,text='Re Enter\nPassword')
        self.label4.grid(row=4,column=0,pady=5,padx=5)
        self.entry3 = ttk.Entry(self,width=25,show='*')
        self.entry3.grid(row=4,column=1,padx=5,pady=5)
        self.label5 = ttk.Label(self)
        self.label5.grid(row=5,column=0,columnspan=2,padx=5,pady=5)
        self.button1 = ttk.Button(self,text='Register',command=self.registerbtn)
        self.button1.grid(row=6,column=0,columnspan=2,pady=5,padx=5,sticky='nesw')
        self.button2 = ttk.Button(self,text='Back',command=self.backbtn)
        self.button2.grid(row=7,column=0,pady=5,padx=5)
        self.label6 = ttk.Label(self,text='Powered by NotiOff',font=('Arial 8'))
        self.label6.grid(row=8,column=1,pady=5,padx=5,sticky='es')


    def registerbtn(self):
        newusername = self.entry1.get()
        newpassword = str(self.entry2.get())
        renewpassword = str(self.entry3.get())
        newemail = self.entry4.get()
        class data:
            def __init__(self,password,credit,email):
                self.password = password
                self.credit = credit
                self.email = email
        if newusername in db.child('UserInfo').get().val():
            text = 'Username already exist!!'
            fg = 'red'
            self.label5.config(text=text, foreground=fg)
            self.entry1.delete(0,tk.END)
            self.entry2.delete(0, tk.END)
            self.entry3.delete(0, tk.END)
            self.entry4.delete(0, tk.END)
        else:
            if "@" in newemail:
                if newpassword == renewpassword:
                    newcredit = 100
                    newdata = data(newpassword,newcredit,newemail)
                    newdata = newdata.__dict__
                    self.entry1.delete(0, tk.END)
                    self.entry2.delete(0, tk.END)
                    self.entry3.delete(0, tk.END)
                    self.entry4.delete(0, tk.END)
                    db.child('UserInfo').child(newusername).set(newdata)
                    CustomMessageBox(title='Congrate',message='Congratulation, Account Created')
                    RegisterFrame.destroy(self)
                    LoginFrame(app)
                else:
                    text = 'Password must be same!!'
                    fg = 'red'
                    self.label5.config(text=text, foreground=fg)
                    self.entry1.delete(0, tk.END)
                    self.entry2.delete(0, tk.END)
                    self.entry3.delete(0, tk.END)
                    self.entry4.delete(0, tk.END)
            else:
                text = 'Username must be username!!'
                fg = 'red'
                self.label5.config(text=text, foreground=fg)
                self.entry1.delete(0, tk.END)
                self.entry2.delete(0, tk.END)
                self.entry3.delete(0, tk.END)
                self.entry4.delete(0, tk.END)



    def backbtn(self):
        RegisterFrame.destroy(self)
        LoginFrame(app)

    

class CustomMessageBox(tk.Toplevel):
    def __init__(self, title, message):
        super().__init__()
        self.title(title)
        message_label = ttk.Label(self, text=message)
        message_label.pack(padx=20, pady=10)
        ok_button = ttk.Button(self, text='OK', command=self.destroy)
        ok_button.pack(pady=10)
        self.resizable(False,False)
        self.geometry("+%d+%d" % (self.winfo_screenwidth() // 2 - self.winfo_reqwidth() // 2,self.winfo_screenheight() // 2 - self.winfo_reqheight() // 2))

class LoginFrame(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)
        self.pack()
        self.welcomeLabel = ttk.Label(self,text='Welcome',font=('TimeNewRoman 15 bold'))
        self.welcomeLabel.grid(row=0,column=0,columnspan=2,padx=10,pady=50)
        self.usernameLabel = ttk.Label(self,text='Username')
        self.usernameLabel.grid(row=1,column=0,padx=10,pady=10)
        self.usernameEntry = ttk.Entry(self,width=25)
        self.usernameEntry.grid(row=1,column=1,padx=10,pady=10)
        self.passwordLabel = ttk.Label(self,text='Password')
        self.passwordLabel.grid(row=2,column=0,padx=10,pady=10)
        self.passwordEntry = ttk.Entry(self,width=25,show='*')
        self.passwordEntry.grid(row=2,column=1,padx=10,pady=10)
        self.loginBtn = ttk.Button(self,text='Login',command=self.login)
        self.loginBtn.grid(row=3,column=0,columnspan=2,padx=10,pady=10)
        self.registerBtn = ttk.Button(self,text='Register',command=self.gotoregister)
        self.registerBtn.grid(row=4,column=0,padx=10,pady=10)
        self.changepwdbtn = ttk.Button(self,text='Change/Forget',command=self.changeForget)
        self.changepwdbtn.grid(row=4,column=1,pady=5,padx=5)
        self.credLabel = ttk.Label(self,text='Powered By NotiOff',font=('Arial 8'))
        self.credLabel.grid(row=10,column=1,sticky='es')
        
    def changeForget(self):
        LoginFrame.destroy(self)
        ChangeForgetFrame(app)

    def login(self):
        global username
        username = self.usernameEntry.get()
        password = self.passwordEntry.get()
        if username in db.child('UserInfo').get().val():
            if password == db.child('UserInfo').child(username).child('password').get().val():
                LoginFrame.destroy(self)
                MainFrame(app)
            else:
                CustomMessageBox(title='Error Login!',message='Wrong Password!!')
                self.usernameEntry.delete(0,tk.END)
                self.passwordEntry.delete(0,tk.END)
        else:
            CustomMessageBox(title='Error Login!',message='No Username Found!!')
            self.usernameEntry.delete(0, tk.END)
            self.passwordEntry.delete(0, tk.END)

    def gotoregister(self):
        LoginFrame.destroy(self)
        RegisterFrame(app)


class ChangeForgetFrame(ttk.Frame):
    def __init__(self,container):
        super().__init__(container)
        self.pack()
        self.label1 = ttk.Label(self,text='Change Password',font=('Arial 15 bold'))
        self.label1.grid(row=0,column=0,columnspan=2,pady=10,padx=5)
        self.label6 = ttk.Label(self,text='Username')
        self.label6.grid(row=1,column=0,pady=5,padx=5)
        self.entry4 = ttk.Entry(self,width=25)
        self.entry4.grid(row=1,column=1,padx=5,pady=5)
        self.label2 = ttk.Label(self,text='Old Password')
        self.label2.grid(row=2,column=0,padx=5,pady=5)
        self.entry1 = ttk.Entry(self,show='*',width=25)
        self.entry1.grid(row=2,column=1,padx=5,pady=5)
        self.label3 = ttk.Label(self,text='New Password')
        self.label3.grid(row=3,column=0,padx=5,pady=5)
        self.entry2 = ttk.Entry(self,show='*',width=25)
        self.entry2.grid(row=3,column=1,pady=5,padx=5)
        self.label4 = ttk.Label(self,text='Re Enter\nNew Password')
        self.label4.grid(row=4,column=0,padx=5,pady=5)
        self.entry3 = ttk.Entry(self,show='*',width=25)
        self.entry3.grid(row=4,column=1,pady=5,padx=5)
        self.label7 = ttk.Label(self)
        self.label7.grid(row=5,column=0,columnspan=2,pady=5,padx=5)
        self.button1 = ttk.Button(self,text='Change Password',command=self.changepwd)
        self.button1.grid(row=6,column=0,columnspan=2,padx=5,pady=5)
        self.button2 = ttk.Button(self,text='Forget Password',command=forget)
        self.button2.grid(row=7,column=0,columnspan=2,padx=5,pady=5)
        self.button3 = ttk.Button(self,text='Back',command=self.back)
        self.button3.grid(row=8,column=0,pady=5,padx=5)
        self.label5 = ttk.Label(self,text='Powered by Notioff',font=('Arial 8'))
        self.label5.grid(row=9,column=1,pady=5,padx=5,sticky='es')

    def changepwd(self):
        if self.entry4.get() in db.child('UserInfo').get().val():
            if self.entry1.get() == db.child('UserInfo').child(self.entry4.get()).child('password').get().val():
                if self.entry2.get() == self.entry3.get():
                    db.child("UserInfo").child(self.entry4.get()).update({'password':str(self.entry2.get())})
                    self.label7.config(text='Password successfully changed', foreground='green')
                    self.entry1.delete(0, tk.END)
                    self.entry2.delete(0, tk.END)
                    self.entry3.delete(0, tk.END)
                    self.entry4.delete(0, tk.END)
                else:
                    self.label7.config(text='New passwords must be same!!', foreground='red')
                    self.entry1.delete(0, tk.END)
                    self.entry2.delete(0, tk.END)
                    self.entry3.delete(0, tk.END)
                    self.entry4.delete(0, tk.END)
            else:
                self.label7.config(text='Wrong Password!!', foreground='red')
                self.entry1.delete(0, tk.END)
                self.entry2.delete(0, tk.END)
                self.entry3.delete(0, tk.END)
                self.entry4.delete(0, tk.END)
        else:
            self.label7.config(text='Username does not Exist!!',foreground='red')
            self.entry1.delete(0, tk.END)
            self.entry2.delete(0, tk.END)
            self.entry3.delete(0, tk.END)
            self.entry4.delete(0, tk.END)

    def back(self):
        ChangeForgetFrame.destroy(self)
        LoginFrame(app)
        
class MainFrame(ttk.Frame):
    def __init__(self,container):
        super().__init__(container)
        self.pack()
        self.label1 = ttk.Label(self,text='Choose Game',font=('arial 25 bold'))
        self.label1.grid(row=0,column=0,columnspan=5,padx=10,pady=10)
        self.lable2 = ttk.Label(self,text='Username  -')
        self.lable2.grid(row=1,column=0,padx=5,pady=5)
        self.lable3 = ttk.Label(self,text='{}'.format(username),foreground='red')
        self.lable3.grid(row=1,column=1,padx=5,pady=5)
        self.label4 = ttk.Label(self,text='Credit -')
        self.label4.grid(row=1,column=2,padx=5,pady=5)
        self.label5 = ttk.Label(self,text='{}'.format(db.child("UserInfo").child(username).child('credit').get().val()),foreground='red')
        self.label5.grid(row=1,column=3,padx=5,pady=5)
        self.button1 = ttk.Button(self,text='Guess Game',width=15,command=self.guessgame)
        self.button1.grid(row=2,column=0,padx=5,pady=5,columnspan=2,rowspan=3,sticky='ns')
        self.button2 = ttk.Button(self,text='Coin Flip',width=15,command=self.coinflip)
        self.button2.grid(row=2,column=2,padx=5,pady=5,columnspan=2,rowspan=3,sticky='ns')
        self.label6 = ttk.Label(self,text=' ')
        self.label6.grid(row=2,column=4,padx=5,pady=5)
        self.label7 = ttk.Label(self,text=' ')
        self.label7.grid(row=3,column=4,padx=5,pady=5)
        self.label8 = ttk.Label(self,text=' ')
        self.label8.grid(row=4,column=4,padx=5,pady=5)
        self.button1 = ttk.Button(self,text='Multiple \nChoice',width=15,command=self.multiplechoice)
        self.button1.grid(row=5,column=0,padx=5,pady=5,columnspan=2,rowspan=3,sticky='ns')
        self.label6 = ttk.Label(self,text=' ')
        self.label6.grid(row=5,column=4,padx=5,pady=5)
        self.label7 = ttk.Label(self,text=' ')
        self.label7.grid(row=6,column=4,padx=5,pady=5)
        self.label8 = ttk.Label(self,text=' ')
        self.label8.grid(row=7,column=4,padx=5,pady=5)
        
    def guessgame(self):
        MainFrame.destroy(self)
        GuessGameFrame(app)
        
    def coinflip(self):
        MainFrame.destroy(self)
        CoinFlipFrame(app)
        
    def multiplechoice(self):
        MainFrame.destroy(self)
        MultipleChoiceFrame(app)
        
class MultipleChoiceFrame(ttk.Frame):
    def __init__(self,container):
        super().__init__(container)
        self.pack()
        self.label1 = ttk.Label(self,text='Username  -')
        self.label1.grid(row=0,column=0,padx=5,pady=5)
        self.label2 = ttk.Label(self,text='{}'.format(username),foreground='red')
        self.label2.grid(row=0,column=1,padx=5,pady=5)
        self.label3 = ttk.Label(self,text='Credit -')
        self.label3.grid(row=0,column=2,padx=5,pady=5)
        self.label4 = ttk.Label(self,text='{}'.format(db.child("UserInfo").child(username).child('credit').get().val()),foreground='red')
        self.label4.grid(row=0,column=3,padx=5,pady=5)
        self.label5 = ttk.Label(self,text='Choose difficulty')
        self.label5.grid(row=1,column=0,columnspan=3,padx=5,pady=5)
        self.diffvar = tk.StringVar()
        self.diff = ('easy','medium','hard')
        self.diffmenu = ttk.OptionMenu(self,self.diffvar,self.diff[0],*self.diff,command=self.difficulty)
        self.diffmenu.grid(row=1,column=3,padx=5,pady=5)
        self.button1 = ttk.Button(self,text='Confirm',command=self.confirm1)
        self.label6 = ttk.Label(self,text='Choose amount for bet!')
        self.label7 = ttk.Label(self,text='Amount  :')
        self.entry1 = ttk.Entry(self)
        self.button2 = ttk.Button(self,text='OK',command=self.okBtn)
        self.label8 = ttk.Label(self,text='Choose Catagory')
        self.datavar = tk.StringVar()
        self.data = {'General Knowledge':9,'Book':10,'Flim':11,'Music':12,'Musicals & Theatres':13,'Televation':14,'Video Game':15,'Board Game':16,'Sciences & Nature':17,'Computer Sciences':18,'Mathematics Sciences':19,'Mythology':20}
        self.datamenu = ttk.OptionMenu(self,self.datavar,list(self.data.keys())[0],*list(self.data.keys()),command=self.catagory)
        self.button3 = ttk.Button(self,text='Comfirm',command=self.confirm2)
        self.label9 = ttk.Label(self,text='The Question is below.')
        self.label10 = ttk.Label(self,font=('arial 14 bold'),foreground='blue')
        self.label11 = ttk.Label(self,text='Choose the correct answer!')
        self.button4 = ttk.Button(self,text='Confirm')
        self.label12 = ttk.Label(self)
        
        
        self.backtocatagory = ttk.Button(self,text='Back to Catagory',command=self.backtocatagory)
        self.backtocatagory.grid(row=20,column=0,columnspan=4,sticky='ew',padx=5,pady=5)
        self.logoutbtn = ttk.Button(self,text='Log Out',command=self.logout)
        self.logoutbtn.grid(row=21,column=0,columnspan=4,sticky='ew',padx=5,pady=5)
        
        
        
    def difficulty(self,*args):
        self.button1.grid(row=2,column=0,columnspan=4,padx=5,pady=6)
        
    def confirm1(self):
        self.diffmenu.config(state='disable')
        self.label6.grid(row=3,column=0,columnspan=4,padx=5,pady=5)
        self.label7.grid(row=4,column=0,padx=5,pady=5)
        self.entry1.grid(row=4,column=1,columnspan=2,padx=5,pady=5)
        self.button2.grid(row=4,column=3,padx=5,pady=5)
        self.button1.grid_forget()
        
        
    def okBtn(self):
        global amount
        amount = self.entry1.get()
        try:
            amount = int(amount)
            if amount < 0 or amount > db.child("UserInfo").child(username).child('credit').get().val():
                CustomMessageBox(title='Error',message='Amount must be between \n0 and {}.'.format(db.child("UserInfo").child(username).child('credit').get().val()))
            else:
                self.button2.config(state='disable')
                self.label8.grid(row=5,column=0,columnspan=2,padx=5,pady=5)
                self.datamenu.grid(row=5,column=2,columnspan=2,padx=5,pady=5,sticky='ew')
        except:
            CustomMessageBox(title='Error',message='Amount must be number')      
        
        
    def catagory(self,*args):
        self.button3.grid(row=6,column=0,columnspan=4,padx=5,pady=5)
        
    def confirm2(self):
        self.button3.grid_forget()
        self.datamenu.config(state='disable')
        self.label9.grid(row=7,column=0,columnspan=4,padx=5,pady=5)
        self.response = requests.get('https://opentdb.com/api.php?amount=1&category={}&difficulty={}&type=multiple'.format(self.data[self.datavar.get()],self.diffvar.get()))
        self.question = self.response.json()['results'][0]['question']
        if "&#039;" in self.question:
            self.question=self.question.replace("&#039;","'")
        elif '&quot;' in self.question:
            self.question=self.question.replace('&quot;','"')
        if len(self.question) > 50:
            self.question = self.question[:50]+'\n'+self.question[50:]
        self.label10.config(text=self.question)
        self.label10.grid(row=8,column=0,columnspan=4,padx=5,pady=5)
        self.answers = self.response.json()['results'][0]['incorrect_answers']
        self.answers.append(self.response.json()['results'][0]['correct_answer'])
        random.shuffle(self.answers)
        self.answerVar = tk.StringVar()
        self.answermenu = ttk.OptionMenu(self,self.answerVar,self.answers[0],*self.answers)
        self.label11.grid(row=9,column=0,columnspan=4,padx=5,pady=5)
        self.answermenu.grid(row=10,column=0,columnspan=4,padx=5,pady=5)
        self.button4.grid(row=11,column=0,columnspan=4,padx=5,pady=5)
        
        
        
    def backtocatagory(self):
        MultipleChoiceFrame.destroy(self)
        MainFrame(app)
        
    def logout(self):
        MultipleChoiceFrame.destroy(self)
        LoginFrame(app)
        
    def confirm3(self):
        self.button4.grid_forget()
        if self.answerVar.get() == self.response.json()['results'][0]['correct_answer']:
            text = 'Congrate you choose the correct answer!'
            totalcredits = (amount * 4 ) + db.child("UserInfo").child(username).child('credit').get().val()
        else:
            text = 'Sorry!! you choose the wrong answer.\nThe correct answer is \n{}'.format(self.response.json()['results'][0]['correct_answer'])
            totalcredits = db.child("UserInfo").child(username).child('credit').get().val() - amount
        self.label12.config(text=text)
        self.label12.grid(row=12,column=0,columnspan=4,padx=5,pady=5)
    
    

class GuessGameFrame(ttk.Frame):
    def __init__(self,container):
        super().__init__(container)
        self.pack()
        self.optionvar = tk.StringVar()
        self.userinputnumber = ('1','2','3','4','5','6','7','8','9','10')
        self.randonNumber = random.randint(1,10)
        self.usernameLable1 = ttk.Label(self,text='Username  -')
        self.usernameLable1.grid(row=0,column=0,padx=5,pady=5)
        self.usernameLable2 = ttk.Label(self,text='{}'.format(username),foreground='red')
        self.usernameLable2.grid(row=0,column=1,padx=5,pady=5)
        self.userCreditLabel = ttk.Label(self,text='Credit -')
        self.userCreditLabel.grid(row=0,column=2,padx=5,pady=5)
        self.userCreditLabel1 = ttk.Label(self,text='{}'.format(db.child("UserInfo").child(username).child('credit').get().val()),foreground='red')
        self.userCreditLabel1.grid(row=0,column=3,padx=5,pady=5)
        self.label1 = ttk.Label(self,text='Choose the Number')
        self.label1.grid(row=1,column=0,columnspan=2,padx=10,pady=5)
        self.optionMenu = ttk.OptionMenu(self,self.optionvar,self.userinputnumber[0],*self.userinputnumber,command=self.usrchoice)
        self.optionMenu.grid(row=1,column=2,columnspan=2,padx=30,pady=5)
        self.betamt = ttk.Label(self,text='Choose amount for bet!')
        self.betamtEntry = ttk.Entry(self)
        self.currentbet = ttk.Label(self,text='Amount  :')
        self.okbtn = ttk.Button(self,text='OK',command=self.okButton)
        self.label2 = ttk.Label(self)
        self.label2.grid(row=5,column=0,columnspan=4,padx=10,pady=5)
        self.ranbtn = ttk.Button(self,text='Randon',command=self.ranBtnClick)
        self.ranLabel = ttk.Label(self,font=('Arial 20 bold'))
        self.ranLabel.grid(row=7,column=0,columnspan=4,padx=10,pady=5)
        self.playagain = ttk.Button(self,text='Play Again?',command=self.playagain)
        self.exitbtn = ttk.Button(self,text='Exit',command=exit)
        self.label3 = ttk.Label(self)
        self.label3.grid(row=8,column=0,columnspan=4,padx=10,pady=5)
        self.backtocatagory = ttk.Button(self,text='Back to Catagory',command=self.backtocatagory)
        self.backtocatagory.grid(row=10,column=0,columnspan=4,sticky='ew',padx=5,pady=5)
        self.logoutbtn = ttk.Button(self,text='Log Out',command=self.logout)
        self.logoutbtn.grid(row=11,column=0,columnspan=4,sticky='ew',padx=5,pady=5)
        
    def okButton(self):
        global amount
        amount = self.betamtEntry.get()
        try:
            amount = int(amount)
            if amount < 0 or amount > db.child("UserInfo").child(username).child('credit').get().val():
                CustomMessageBox(title='Error',message='Amount must be between \n0 and {}.'.format(db.child("UserInfo").child(username).child('credit').get().val()))
            else:
                self.label2['text'] = 'Dear {}, \nYou selected "{}".\nTo know the randon number\nPlease click the "Randon" button'.format(username,self.optionvar.get())
                self.ranbtn.grid(row=6,column=0,columnspan=4,padx=10,pady=5)
                self.okbtn.config(state='disable')
                self.optionMenu.config(state='disable')
                self.betamtEntry.config(state='disable')
            
        except:
            CustomMessageBox(title='Error',message='Amount must be number')
        
    def playagain(self):
        GuessGameFrame.destroy(self)
        GuessGameFrame(app)

    def usrchoice(self,*args):
        self.okbtn.grid(row=3,column=3,padx=5,pady=5)
        self.currentbet.grid(row=3,column=0,padx=10,pady=5)
        self.betamt.grid(row=2,column=0,columnspan=4,sticky='nesw',padx=10,pady=5)
        self.betamtEntry.grid(row=3,column=1,columnspan=2,padx=10,pady=5)
        
    def ranBtnClick(self):
        self.randonNumber = random.randint(1,10)
        self.ranLabel['text'] = self.randonNumber
        self.ranbtn.grid_forget()
        if int(self.optionvar.get()) == self.randonNumber:
            totalcredits = (amount * 10 ) + db.child("UserInfo").child(username).child('credit').get().val()
            text = 'Congratulation. You Win.'
        else:
            totalcredits = db.child("UserInfo").child(username).child('credit').get().val() - amount
            text =  'Sorry. You Lose.'
        self.label3['text'] = text
        self.playagain.grid(row=9,column=0,columnspan=2,sticky='nesw',padx=10,pady=5)
        self.exitbtn.grid(row=9,column=2,columnspan=2,sticky='nesw',padx=10,pady=5)
        db.child("UserInfo").child(username).update({'credit':totalcredits})

    def logout(self):
        GuessGameFrame.destroy(self)
        LoginFrame(app)
        
    def backtocatagory(self):
        GuessGameFrame.destroy(self)
        MainFrame(app)

class CoinFlipFrame(ttk.Frame):
    def __init__(self,container):
        super().__init__(container)
        self.pack()
        self.optionvar = tk.StringVar()
        self.userinputhot = ('Head','Tail')
        self.headortail = random.choice(self.userinputhot)
        self.usernameLable1 = ttk.Label(self,text='Username  -')
        self.usernameLable1.grid(row=0,column=0,padx=5,pady=5)
        self.usernameLable2 = ttk.Label(self,text='{}'.format(username),foreground='red')
        self.usernameLable2.grid(row=0,column=1,padx=5,pady=5)
        self.userCreditLabel = ttk.Label(self,text='Credit -')
        self.userCreditLabel.grid(row=0,column=2,padx=5,pady=5)
        self.userCreditLabel1 = ttk.Label(self,text='{}'.format(db.child("UserInfo").child(username).child('credit').get().val()),foreground='red')
        self.userCreditLabel1.grid(row=0,column=3,padx=5,pady=5)
        self.label1 = ttk.Label(self,text='Choose the Number')
        self.label1.grid(row=1,column=0,columnspan=2,padx=10,pady=5)
        self.optionMenu = ttk.OptionMenu(self,self.optionvar,self.userinputhot[0],*self.userinputhot,command=self.usrchoice)
        self.optionMenu.grid(row=1,column=2,columnspan=2,padx=30,pady=5)
        self.betamt = ttk.Label(self,text='Choose amount for bet!')
        self.betamtEntry = ttk.Entry(self)
        self.currentbet = ttk.Label(self,text='Amount  :')
        self.okbtn = ttk.Button(self,text='OK',command=self.okButton)
        self.label2 = ttk.Label(self)
        self.label2.grid(row=5,column=0,columnspan=4,padx=10,pady=5)
        self.ranbtn = ttk.Button(self,text='Flip',command=self.ranBtnClick)
        self.ranLabel = ttk.Label(self,font=('Arial 20 bold'))
        self.ranLabel.grid(row=7,column=0,columnspan=4,padx=10,pady=5)
        self.playagain = ttk.Button(self,text='Play Again?',command=self.playagain)
        self.exitbtn = ttk.Button(self,text='Exit',command=exit)
        self.label3 = ttk.Label(self)
        self.label3.grid(row=8,column=0,columnspan=4,padx=10,pady=5)
        self.backtocatagory = ttk.Button(self,text='Back to Catagory',command=self.backtocatagory)
        self.backtocatagory.grid(row=10,column=0,columnspan=4,sticky='ew',padx=5,pady=5)
        self.logoutbtn = ttk.Button(self,text='Log Out',command=self.logout)
        self.logoutbtn.grid(row=11,column=0,columnspan=4,sticky='ew',padx=5,pady=5)
        
    def okButton(self):
        global amount
        amount = self.betamtEntry.get()
        try:
            amount = int(amount)
            if amount < 0 or amount > db.child("UserInfo").child(username).child('credit').get().val():
                CustomMessageBox(title='Error',message='Amount must be between \n0 and {}.'.format(db.child("UserInfo").child(username).child('credit').get().val()))
            else:
                self.label2['text'] = 'Dear {}, \nYou selected "{}".\nTo get the answer\nPlease click the "Flip" button'.format(username,self.optionvar.get())
                self.ranbtn.grid(row=6,column=0,columnspan=4,padx=10,pady=5)
                self.okbtn.config(state='disable')
                self.optionMenu.config(state='disable')
                self.betamtEntry.config(state='disable')
        except:
            CustomMessageBox(title='Error',message='Amount must be number')
        
    def playagain(self):
        CoinFlipFrame.destroy(self)
        CoinFlipFrame(app)

    def usrchoice(self,*args):
        self.okbtn.grid(row=3,column=3,padx=5,pady=5)
        self.currentbet.grid(row=3,column=0,padx=10,pady=5)
        self.betamt.grid(row=2,column=0,columnspan=4,sticky='nesw',padx=10,pady=5)
        self.betamtEntry.grid(row=3,column=1,columnspan=2,padx=10,pady=5)
        
    def ranBtnClick(self):
        self.ranLabel['text'] = self.headortail
        self.ranbtn.grid_forget()
        if self.optionvar.get() == self.headortail:
            totalcredits = (amount * 2 ) + db.child("UserInfo").child(username).child('credit').get().val()
            text = 'Congratulation. You Win.'
        else:
            totalcredits = db.child("UserInfo").child(username).child('credit').get().val() - amount
            text =  'Sorry. You Lose.'
        self.label3['text'] = text
        self.playagain.grid(row=9,column=0,columnspan=2,sticky='nesw',padx=10,pady=5)
        self.exitbtn.grid(row=9,column=2,columnspan=2,sticky='nesw',padx=10,pady=5)
        db.child("UserInfo").child(username).update({'credit':totalcredits})

    def logout(self):
        CoinFlipFrame.destroy(self)
        LoginFrame(app)
        
    def backtocatagory(self):
        CoinFlipFrame.destroy(self)
        MainFrame(app)

class Main(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry('400x550')
        self.resizable(False,False)
        self.title('Mini Game')
        sv_ttk.set_theme('light')
        menubar = tk.Menu(self)
        self.config(menu=menubar)
        file_menu = tk.Menu(menubar)
        menubar.add_cascade(label='File',menu=file_menu,underline=0)
        file_menu.add_command(label='About',command=about)
        file_menu.add_command(label='Exit',command=exit)
        
if __name__ == '__main__':
    app = Main()
    LoginFrame(app)
    app.mainloop()