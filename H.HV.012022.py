from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen,ScreenManager
from kivy.core.window import Window
import pywhatkit as kit
from kivymd.uix.datatables import MDDataTable
from kivy.metrics import dp
from kivymd.uix.pickers import MDDatePicker
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView
import psycopg2
from kivy.lang import Builder
Window.size=(400,680)
class Welcome(Screen):
    pass
class WDYO(Screen):
    pass
conn = psycopg2.connect(host="localhost", database="demo", user="postgres", password="1587", port="5432")
c = conn.cursor()

class InsertData(Screen):
    conn = psycopg2.connect(host="localhost", database="demo", user="postgres", password="1587", port="5432")
    c = conn.cursor()

    c.execute(
        """CREATE TABLE if not exists concreate_Bon (id int PRIMARY KEY NOT NULL,Location VARCHAR (20) NOT NULL ,block_num VARCHAR (6) NOT NULL,Structure VARCHAR (20) NOT NULL,Quantity REAL NOT NULL,Content REAL NOT NULL,Operator VARCHAR (20) NOT NULL,DRIVER VARCHAR (50),TRUCK VARCHAR (20),execution VARCHAR (20),Pump VARCHAR (20),mytimestamp TIMESTAMP NOT NULL DEFAULT NOW()::DATE)""")
    conn.commit()
    print("good connection ")
    conn.close()
    bons_num = 0
    def insert_data(self):
        bn=self.ids.bn_number.text,
        Location=self.ids.spinner_id1.text,
        block_num=self.ids.BL_NUM.text,
        Structure=self.ids.spinner_id2.text,
        Quantity=self.ids.qu_id.text,
        Content=self.ids.spinner_id3.text,
        Operator=self.ids.spinner_id4.text
        DRIVER=self.ids.spinner_id5.text,
        TRUCK=self.ids.spinner_id6.text,
        Pump=self.ids.spinner_id7.text
        execution=self.ids.spinner_id8.text

        self.whats()

        c.execute("INSERT INTO concreate_Bon(id ,Location,block_num,Structure,Quantity,Content,Operator,DRIVER,TRUCK,Pump,execution ) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(bn,Location,block_num,Structure,Quantity,Content,Operator,DRIVER,TRUCK,Pump,execution))
        conn.commit()
        print("Data Inserted Successfully")
        conn.close()
        InsertData.bons_num += 1
        @classmethod
        def show_bons_num(cls):
            return (f"we have {cls.bons_num} bons")

    def get_fullinfo(self):
        return (f"BON Number {self.ids.bn_number.text} has been downloded\n ===================\n LOCATION :- {self.ids.spinner_id1.text}"
                f"\n Block number :- { self.ids.BL_NUM.text} \n Structure :-{self.ids.spinner_id2.text}\n Quantity = {self.ids.qu_id.text} M"
                f"\n Content {self.ids.spinner_id3.text} cement \n Operator :-{self.ids.spinner_id4.text}  \nDRIVER:-{self.ids.spinner_id5.text}  \nTRUCK :-{self.ids.spinner_id6.text}\nPUMP:{self.ids.spinner_id7.text} : \nexecution :{self.ids.spinner_id8.text}")


    def whats(self):

       return kit.sendwhatmsg_to_group_instantly(f"https://chat.whatsapp.com/LFfNpJhE6ZD7dPABKnrGdc",f'{self.get_fullinfo()}')



class Inquri(Screen):
    pass



class SuccessScreen(Screen):
    def total(self):
        conn = psycopg2.connect(host="localhost", database="demo", user="postgres", password="1587", port="5432")
        c = conn.cursor()
        c.execute("SELECT SUM (quantity) FROM concreate_Bon")
        records=c.fetchone()
        word=""
        for record in records:
            word=f"{word} = {record} M3"
            self.ids.sea.text=f' TOTAL QUANTITY {word}'
        conn.commit()
        conn.close()

    def total400(self):
        conn = psycopg2.connect(host="localhost", database="demo", user="postgres", password="1587", port="5432")
        c = conn.cursor()
        c.execute("SELECT SUM (quantity) FROM concreate_Bon WHERE content='400'")
        records=c.fetchone()
        word=""
        for record in records:
            word=f"{word} = {record} M3"
            self.ids.sea2.text=f' TOTAL QUANTITY 400 {word}'
        conn.commit()
        conn.close()

    def total350(self):
        conn = psycopg2.connect(host="localhost", database="demo", user="postgres", password="1587", port="5432")
        c = conn.cursor()
        c.execute("SELECT SUM (quantity) FROM concreate_Bon WHERE content='350'")
        records=c.fetchone()
        word=""
        for record in records:
            word=f"{word} = {record} M3"
            self.ids.sea3.text=f' TOTAL QUANTITY 350 {word} '
        conn.commit()
        conn.close()

    def total250(self):
        conn = psycopg2.connect(host="localhost", database="demo", user="postgres", password="1587", port="5432")
        c = conn.cursor()
        c.execute("SELECT SUM (quantity) FROM concreate_Bon WHERE content='250'")
        records=c.fetchone()
        word=""
        for record in records:
            word=f"{word} = {record} M3"
            self.ids.sea4.text=f' TOTAL QUANTITY 250 {word}'


        conn.commit()
        conn.close()



# class DataTableLayout(Screen):
#     def date_pick(self):
#         date_dialog=MDDatePicker(year=2024)
#         date_dialog.open()













    # def fetch_last_bon(self):
    #     conn = psycopg2.connect(host="localhost", database="demo", user="postgres", password="1587", port="5432")
    #     c = conn.cursor()
    #     c.execute("SELECT * FROM concreate_Bon WHERE Operator ='FARAHAT' ")
    #     records = c.fetchall()
    #     word = ""
    #     for record in records:
    #         word = f"{word}\n{record}"
    #         self.ids.sew.text = f'{word}'
    #     conn.commit()
    #     conn.close()



class MyScreenManager(ScreenManager):
    pass

class MyApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = 'Light'
        self.theme_cls.primary_hue = 'A700'
        return MyScreenManager()
    def spinner_clicked(self,text):
        pass
if __name__=="__main__":
    MyApp().run()

