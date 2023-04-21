from tkinter import *
import random
root=Tk()

root.title("Lucky Friend Wheel")
root.geometry("500x500")

country_name = Entry(root)
capital_name = Entry(root)

country_list=Label(root)
capital_list=Label(root)
country_number=Label(root)
capital_number=Label(root)

list1=[]
list2=[]

def addCountry():
    country_nme=country_name.get()
    list1.append(country_nme)
    country_list["text"]="CountryList:"+str(list1)
def addCapital():
    capital_nme=capital_name.get()
    list2.append(capital_nme)
    capita_list["text"]="CountryList:"+str(list1)

def random_number():
    length = len(list1)
    random_no = random.randint(0, lenght-1)
    random_number_label["text"] = str(random_no)
    generated_random_no = list1[random_no]
    country_name[text] = "Your country name is"+str(generated_random_no)
    length1 = len(list2)
    random_no1 = random.randint(0, lenght-1)
    random_number_label1["text"] = str(random_no)
    generated_random_no1 = list1[random_no]
    capital_name[text] = "Your capital name is"+str(generated_random_no)
root.mainloop()
