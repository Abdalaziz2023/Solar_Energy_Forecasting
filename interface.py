from tkinter import *
from PIL import ImageTk, Image

class Interface:
    def __init__(self,root):
        self.root = root
        self.root.title("Solar Radiation and Power Prediction")
        self.root.geometry("1366x768+0+0")



        

        Dataframe = Frame(self.root,relief=RIDGE,bg= "springgreen")
        Dataframe.place(x = 0 ,y = 0,width=1360,height=800)

        lbltitle = Label(Dataframe,relief=RIDGE,text = "Solar Radiation and Solar Power Prediction",bg="white",font=("times new roman",50,"bold"))
        lbltitle.pack(side= TOP,fill=X)


        






if __name__ == "__main__":
   root = Tk()
   app = Interface(root)
   root.mainloop()