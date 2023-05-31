from tkinter import *
from tkinter import ttk
import random
import time
import datetime
from tkinter import messagebox
from tkcalendar import Calendar 

from tkinter import filedialog
import pandas as pd

from functools import partial





class Progrm:
    def __init__(self,root):
        self.root = root
        self.root.title("Solar Prediction System")
        self.root.geometry("1366x768+0+0")

        ########### variables ##########

        
        gander = StringVar()
    
       
        lbltitle = Label(self.root,bd = 20,relief=RIDGE,text = "Prediction of solar radiation for solar energy production",fg = "black",bg="springgreen",font=("times new roman",30,"bold"))
        lbltitle.pack(side= TOP,fill=X)


        ########### data frame #######
        Dataframe = Frame(self.root,bd= 20,relief=RIDGE)
        Dataframe.place(x = 0 ,y = 130,width=1360,height=300)

        dataframelift = Label(Dataframe,bd=5,relief=RIDGE,padx=5,font=("times new roman",12,"bold"))
        dataframelift.place(x = 0 , y=5,width=400,height=250)

        dataframemidel = Label(Dataframe,bd=5,relief=RIDGE,padx=5,font=("times new roman",12,"bold"))
        dataframemidel.place(x = 460 , y=5,width=400,height=250)

        dataframeright = Label(Dataframe,bd=5,relief=RIDGE,padx=10,font=("times new roman",12,"bold"),text="Prescription")
        dataframeright.place(x = 920 , y=5,width=400,height=250) 

        ############# buttons ############
        Buttonframe = Frame(self.root,bd= 20,relief=RIDGE,bg= "white")
        Buttonframe.place(x = 0 ,y = 420,width=1360,height=75)

        ############# Deteils frame ############
        Detailsframe = Frame(self.root,bd=2,relief=RIDGE)
        Detailsframe.place(x = 0 ,y = 500,width=1360,height=200)

        ############ data ##################

        lablgender = Label(dataframelift,text= "Solar Cell",font=("times new roman",12,"bold"),padx=2,pady=6)
        lablgender.grid(row = 3,column =1)
        txtgender = ttk.Combobox(dataframelift,font=("times new roman",12,"bold"),width= 31,textvariable=gander)
        txtgender["value"] = ("","Si (crystaline cell)","Si (DS Wafer cell)","Si thin transfer submodule")
        txtgender.grid(row = 3,column=4)

        #============== Calendar
        # Add Calendar
        cal = Calendar(dataframelift,selectmode = 'day',year = 2020,month = 5,day = 20)
        cal.grid(row = 4,column = 4)


       
    

        ##############
       

        def Gander():
            n = txtgender.get()
            return str(n)

        



        def rect():
            gander.set("")
            return
            


        def exit_fun():
            exitbtn =messagebox.askyesno("Are you sure you want to exit?")
            if exitbtn > 0:
                root.destroy()



        # ========= import data
        file_name = []
        

        def Importdata():
            filename = filedialog.askopenfilename(initialdir = "/",
										title = "Select a File",
										filetypes = (("Text files",
														"*.csv*"),
													("all files",
														"*.*")))
            file_name.append(filename)
        
        # def ReadData():
        #         df = pd.read_csv(Importdata())
        #         print(df.head(10))


        
        



        ############### Buttons #######################
       


        btnprescriptionData = Button(Buttonframe,text="Import Data",font=("times new roman",12,"bold"),bg= "springgreen",width=24,height = 1,command= Importdata)
        btnprescriptionData.grid(row=0,column=1)

        ReadData = Button(Buttonframe,text="Read Data",font=("times new roman",12,"bold"),bg= "springgreen",width=24,height = 1)
        ReadData.grid(row=0,column=2)    

        btnUpdate = Button(Buttonframe,text="Predict",font=("times new roman",12,"bold"),bg= "springgreen",width=24,height = 1)
        btnUpdate.grid(row=0,column=3)    


        btnDelete = Button(Buttonframe,text="Solar power",font=("times new roman",12,"bold"),bg= "springgreen",width=24,height = 1)
        btnDelete.grid(row=0,column=4)    


        btnClear = Button(Buttonframe,text="Clear data",font=("times new roman",12,"bold"),bg= "springgreen",width=24,height = 1,command= rect)
        btnClear.grid(row=0,column=5)    


        btnExit = Button(Buttonframe,text="Exit",font=("times new roman",12,"bold"),bg= "springgreen",width=20,height = 1,command=exit_fun)
        btnExit.grid(row=0,column=6) 

        # ################# Table ###############
        # ################# scrolbar ############
        
        scroll_x = ttk.Scrollbar(Detailsframe,orient = HORIZONTAL)
        scroll_y = ttk.Scrollbar(Detailsframe,orient= VERTICAL)
        self.hospetal_table = ttk.Treeview(Detailsframe,columns=("Data","Time","Temperature","Pressure","Humidity","WindDirection","Speed","TimeSunRise",
                    "TimeSunSet"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side = BOTTOM,fill=X)
        scroll_y.pack(side = RIGHT,fill= Y)
        self.hospetal_table.pack()


        scroll_x.config(command=self.hospetal_table.xview())
        scroll_y.config(command=self.hospetal_table.yview())

        # scroll_x = ttk.Scrollbar(command= self.hospetal_table.xview)
        scroll_y = ttk.Scrollbar(command= self.hospetal_table.yview)
        
        self.hospetal_table.heading("Data",text = "Date")
        self.hospetal_table.heading("Time",text = "Time")
        self.hospetal_table.heading("Temperature",text = "Temperature")
        self.hospetal_table.heading("Pressure",text = "Pressure")
        self.hospetal_table.heading("Humidity",text = "Humidity")
        self.hospetal_table.heading("WindDirection",text = "WindDirection")
        self.hospetal_table.heading("Speed",text = "Speed")
        self.hospetal_table.heading("TimeSunRise",text = "TimeSunRise")
        self.hospetal_table.heading("TimeSunSet",text = "TimeSunSet")
       

        self.hospetal_table["show"] = "headings"

        
        self.hospetal_table.column("Data",width = 100)
        self.hospetal_table.column("Time",width = 100)
        self.hospetal_table.column("Temperature",width = 100)
        self.hospetal_table.column("Pressure",width = 100)
        self.hospetal_table.column("Humidity",width = 100)
        self.hospetal_table.column("WindDirection",width = 100)
        self.hospetal_table.column("Speed",width = 100)
        self.hospetal_table.column("TimeSunRise",width = 100)
        self.hospetal_table.column("TimeSunSet",width = 100)


        
       
        


        self.hospetal_table.pack(fill = BOTH,expand=1)

        
                        
        # x = []

        # a,b,c,d,e,f,h,i,j,k,l,m = str(x[11]),str(x[10]),str(x[9]),str(x[8]),str(x[7]),str(x[6]),str(x[5]),str(x[4]),str(x[3]),str(x[2]),str(x[1]),str(x[0])
        # self.hospetal_table.insert(parent = '', index='end',text = '',values = (a,b,c,d,e,f,h,i,j,k,l,m))
        # self.hospetal_table.pack()

        def ReadData():
                df = pd.read_csv(file_name[0])
                df = df.copy()
                df = df.drop(['UNIXTime','Radiation'],axis=1)
                for i in range(20):
                    a,b,c,d,e,f,h,i,j = str(df["Data"][i]),str(df["Time"][i]),str(df["Temperature"][i]),str(df["Pressure"][i]),str(df["Humidity"][i]),str(df["WindDirection(Degrees)"][i]),str(df["Speed"][i]),str(df["TimeSunRise"][i]),str(df["TimeSunSet"][i])
                    self.hospetal_table.insert(parent = '', index='end',text = '',values = (a,b,c,d,e,f,h,i,j))
                    self.hospetal_table.pack()


        ReadData = Button(Buttonframe,text="Read Data",font=("times new roman",12,"bold"),bg= "springgreen",width=24,height = 1,command= ReadData)
        ReadData.grid(row=0,column=2) 


        def Delete():
            self.hospetal_table.delete(*self.hospetal_table.get_children())
            self.Solar_rad_table.delete(*self.Solar_rad_table.get_children())


        btnClear = Button(Buttonframe,text="Clear data",font=("times new roman",12,"bold"),bg= "springgreen",width=24,height = 1,command= Delete)
        btnClear.grid(row=0,column=5)


        



        #=================== Solar radiation prediction ============

        scroll_x = ttk.Scrollbar(dataframemidel,orient = HORIZONTAL)
        scroll_y = ttk.Scrollbar(dataframemidel,orient= VERTICAL)
        self.Solar_rad_table = ttk.Treeview(dataframemidel,columns=("Time","Radiation"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side = BOTTOM,fill=X)
        scroll_y.pack(side = RIGHT,fill= Y)
        self.Solar_rad_table.pack()


        scroll_x.config(command=self.Solar_rad_table.xview())
        scroll_y.config(command=self.Solar_rad_table.yview())

        # scroll_x = ttk.Scrollbar(command= self.hospetal_table.xview)
        scroll_y = ttk.Scrollbar(command= self.Solar_rad_table.yview)
        
        
        self.Solar_rad_table.heading("Time",text = "Time")
        self.Solar_rad_table.heading("Radiation",text = "Radiation")
       

        self.Solar_rad_table["show"] = "headings"

        
    
        self.Solar_rad_table.column("Time",width = 100)
        self.Solar_rad_table.column("Radiation",width = 100)

    
        self.Solar_rad_table.pack(fill = BOTH,expand=1)


    # ===========================
        def Solar_predict():
            if (len(file_name) == 0):
                messagebox.ERROR("Error","Pleas Enter csv file")

            else:
                import numpy as np
                import pandas as pd
                import re
                from sklearn.preprocessing import StandardScaler
                from sklearn.model_selection import train_test_split
                import optuna
                import xgboost as xgb
                import joblib

                data = pd.read_csv(file_name[0])
                data = data.head(20)
                data['Month'] = data['Data'].apply(lambda x: re.search(r'^\d+', x).group(0)).astype(np.int)
                data['Day'] = data['Data'].apply(lambda x: re.search(r'(?<=\/)\d+(?=\/)', x).group(0)).astype(np.int)
                data['Year'] = data['Data'].apply(lambda x: re.search(r'(?<=\/)\d+(?=\s)', x).group(0)).astype(np.int)
                data = data.drop('Data', axis=1)

                data['Hour'] = data['Time'].apply(lambda x: re.search(r'^\d+', x).group(0)).astype(np.int)
                data['Minute'] = data['Time'].apply(lambda x: re.search(r'(?<=:)\d+(?=:)', x).group(0)).astype(np.int)
                data['Second'] = data['Time'].apply(lambda x: re.search(r'\d+$', x).group(0)).astype(np.int)

                data = data.drop('Time', axis=1)

                data['SunriseHour'] = data['TimeSunRise'].apply(lambda x: re.search(r'^\d+', x).group(0)).astype(np.int)
                data['SunriseMinute'] = data['TimeSunRise'].apply(lambda x: re.search(r'(?<=:)\d+(?=:)', x).group(0)).astype(np.int)

                data['SunsetHour'] = data['TimeSunSet'].apply(lambda x: re.search(r'^\d+', x).group(0)).astype(np.int)
                data['SunsetMinute'] = data['TimeSunSet'].apply(lambda x: re.search(r'(?<=:)\d+(?=:)', x).group(0)).astype(np.int)

                data = data.drop(['TimeSunRise', 'TimeSunSet'], axis=1)

                data = data.drop(['Year', 'SunriseHour'], axis=1)

                y = data['Radiation'].copy()
                X = data.drop('Radiation', axis=1).copy()
                
                scaler = StandardScaler()
                X = scaler.fit_transform(X)


                # X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.7, random_state=100)

                # X_train, X_val, y_train, y_val = train_test_split(X_train, y_train, train_size=0.8, random_state=200)

                dtest = xgb.DMatrix(X,label = y)

                loaded_model = joblib.load("complite_model.joblib")
                return loaded_model.predict(dtest)
            

        def fillsolartable():
                df = pd.read_csv(file_name[0])
                df = df.head(20)
                Data = Solar_predict()
                for i in range(20):
                    a,b = str(df["Time"][i]),str(Data[i])
                    self.Solar_rad_table.insert(parent = '', index='end',text = '',values = (a,b))
                    self.Solar_rad_table.pack()


        btnUpdate = Button(Buttonframe,text="Predict",font=("times new roman",12,"bold"),bg= "springgreen",width=24,height = 1,command= fillsolartable)
        btnUpdate.grid(row=0,column=3)  


     #=================== Solar power prediction ============

        scroll_x = ttk.Scrollbar(dataframeright,orient = HORIZONTAL)
        scroll_y = ttk.Scrollbar(dataframeright,orient= VERTICAL)
        self.Solar_power_table = ttk.Treeview(dataframeright,columns=("Time","Power"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side = BOTTOM,fill=X)
        scroll_y.pack(side = RIGHT,fill= Y)
        self.Solar_power_table.pack()


        scroll_x.config(command=self.Solar_power_table.xview())
        scroll_y.config(command=self.Solar_power_table.yview())

        # scroll_x = ttk.Scrollbar(command= self.hospetal_table.xview)
        scroll_y = ttk.Scrollbar(command= self.Solar_power_table.yview)
        
        
        self.Solar_power_table.heading("Time",text = "Time")
        self.Solar_power_table.heading("Power",text = "Power")
       

        self.Solar_power_table["show"] = "headings"

        
    
        self.Solar_power_table.column("Time",width = 100)
        self.Solar_power_table.column("Power",width = 100)

    
        self.Solar_power_table.pack(fill = BOTH,expand=1)

        



    

if __name__ == "__main__":
   root = Tk()
   app = Progrm(root)
   root.mainloop()