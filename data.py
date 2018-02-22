from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
import pymysql


class ScreenManagement(ScreenManager):
    pass


class MainScreen(Screen):

    def login(self, uname_txt, pin_txt):
        '''if uname_txt == "test" and pin_txt == "test":
           self.parent.current = 'homepage'''
           
        conn=pymysql.connect(host="localhost",user="root",password='',db="py_db")
        mycur = conn.cursor()
        
        #if username_text == "root" and password_text == "123":
        if uname_txt=="" or pin_txt=="":
            label = self.ids.success
            label.text="Please enter the required field"
        elif uname_txt!="" or pin_txt!="":
            mycur.execute("select * from user_info where user_name='%s' and user_password ='%s'"%(uname_txt,pin_txt))
            
            data=mycur.fetchone()
            #print(data)
            
            if data is not None:
                self.parent.current = 'homepage' 
                
            if data is None:
                label = self.ids.success
                label.text="login fake"     


class HomePage(Screen):
    pass

class Registration(Screen):
    def regis(self, *args):
        username = self.ids.username_input
        username_text = username.text
        
        useremail = self.ids.useremail_input
        useremail_text = useremail.text
        
        userphone = self.ids.userphone_input
        userphone_text = userphone.text
        
        userpassword = self.ids.userpassword_input
        userpassword_text = userpassword.text
        
        conn=pymysql.connect(host="localhost",user="root",password='',db="py_db")
        print('connected')
        
        mycur = conn.cursor()
        
        #sql= "insert into py_tbl values(username_text,password_text)"
        mycur.execute('insert into user_info values ("%s","%s","%s","%s","%s")' % ('',username_text,useremail_text,userphone_text,userpassword_text))
        conn.commit()
        label = self.ids.success
        label.text="Registration successful"


class Pass(App):
    
    title = "Login Screen"

    def build(self):
        return ScreenManagement()


if __name__ == "__main__":
    Pass().run()