from tkinter import *
import tkinter.messagebox as tm
import matplotlib.pyplot as plt
import pandas as pd
class LoginBox(Frame):
    def __init__(self,myself ):
        super().__init__(myself)

        self.label_username = Label(self, text="Username")
        self.label_password = Label(self, text="Password")

        self.entry_username = Entry(self)
        self.entry_password = Entry(self, show="*")

        self.label_username.grid(row=0, column=0)
        self.label_password.grid(row=1, column=0)
        self.entry_username.grid(row=0, column=1)
        self.entry_password.grid(row=1, column=1)

        self.logbtn = Button(self, text="Login", command=self._login_btn_clicked)
        self.logbtn.grid(column=1)

        self.pack()

    def _login_btn_clicked(self):
        username = self.entry_username.get()
        password = self.entry_password.get()


        if username == "aayush" and password == "project":
            tm.showinfo("Login info", "Welcome Aayush and Group")
            tm.showinfo("Login info","Lets start the project")

            print("Car Name")
            c1 = input("Enter first Car1: ")
            c2 = input("Enter second Car2: ")
            d = {}
            l1 = []
            l2 = []

            print("Distance Travelled by two Cars After an Hour For 4 Hours ")
            print("Enter Distances for Car1: ")
            for i in range(0, 4):
                l1.append(int(input("Enter Distance After Hour:{} : ".format(i + 1))))

            print("Enter Distances for Car2: ")
            for i in range(0, 4):
                l2.append(int(input("Enter Distance After Hour:{} :".format(i + 1))))

            t = [1, 2, 3, 4]

            d['Car_Name'] = [c1, c2]
            d['Total_Distance_Travelled'] = [l1[3], l2[3]]

            k = 0
            l3 = []
            l4 = []
            l5 = [1, 2, 3, 4]
            c3 = [c1, c2]
            p = 0

            for i in range(0, 8):
                l3.append(c3[k] + str(p + 1))
                if k == 0:
                    k = 1
                elif k == 1:
                    k = 0
                p = p + 1

            k = 0
            for i in range(0, 4):
                l4.append(l1[k])
                l4.append(l2[k])
                k = k + 1

            df = pd.DataFrame(d, columns=['Car_Name', 'Total_Distance_Travelled'])

            df.to_csv("car_comparison.csv")
            df1 = pd.read_csv("car_comparison.csv")

            plt.figure(figsize=(20, 8))

            plt.bar(l3, l4, color="pink")

            plt.xlabel("Time_Taken(IN HOURS[1-4])")
            plt.ylabel("Distance_Travelled")
            plt.title("Distance_Comparison_Of_Two_Cars")
            plt.savefig("C:/Users/owner/Desktop/python/bargraph.pdf",format="pdf")
            plt.show()

        else:
            tm.showerror("Login error", "Incorrect information")


root = Tk()
root.title("LoginBox")
lf = LoginBox(root)
root.mainloop()
