# pip install tkcalendar

from tkinter import *
from tkcalendar import Calendar
from tkinter import messagebox
from datetime import date
from tkinter import ttk

# Defining Window
window = Tk()
window.title('Age CAlculator')
window.geometry('1300x600')
window['bg'] = 'MediumOrchid1'

# Title
label_title = Label(window, text='Age Calculator', bg='MediumOrchid1', fg='DarkOrchid4')
label_title.configure(font=('Arial Rounded MT Bold', 45))
label_title.place(x=300, y=1)


label_showAge = Label(window, text='', bg='MediumOrchid1', fg='DarkOrchid4', width=20,
justify='left')
label_showAge.configure(font=('Arial Rounded MT Bold', 30))
label_showAge.place(x='800', y='125')

# calender
cal = Calendar(window, selectmode='day',
               year=date.today().year, month=date.today().month,
               day=date.today().day, date_pattern='y/mm/dd')
cal.configure(background='Black')
cal.place(x='550', y='140')

# Functions
def add():
    date_select=cal.get_date()
    date_select=date_select.split('/')
    
    # Add Selected Value in input 
    year_entry.delete(0, 'end')
    year_entry.insert(0, date_select[0])
    month_entry.delete(0,'end')
    month_entry.insert(0, date_select[1])
    day_entry.delete(0, 'end')
    day_entry.insert(0, date_select[2])

def clear():
    year_entry.delete(0, 'end')
    month_entry.delete(0,'end')
    day_entry.delete(0, 'end')
    label_showAge.configure(text='')
   
def cal_age():
    try:
        year=int(year_entry.get())
        month=int(month_entry.get())
        day=int(day_entry.get())

        if year>date.today().year or year <= 0 or len(str(year)) != 4:
            messagebox.showwarning('Warning', 'Invalid Year')
            year_entry.delete(0, 'end')

        elif month>12 or month <= 0 or len(str(month))>2:
            messagebox.showwarning('Warning', 'Invalid Month')
            month_entry.delete(0,'end')

        elif day>31 or day <= 0 or len(str(day))>2:
            messagebox.showwarning('Warning', 'Invalid Day')
            day_entry.delete(0, 'end')

        
        else:
            # Todays Date
            today_year=date.today().year
            today_month=date.today().month
            today_day=date.today().day

            if year==today_year and month>today_month:
                messagebox.showwarning('Warning', 'Enter Valid Date')
                clear()
            
            else:
                
                if day>today_day and month >= today_month:
                    cal_day=(today_day + 30) - day
                    cal_month=((today_month - 1) + 12) - month
                    cal_year=(today_year - 1) - year
                    label_showAge.config(text=f'Year\t{abs(cal_year)}\nMonth\t{abs(cal_month)}\nDay\t{abs(cal_day)}')



                elif day>today_day and month<today_month:
                    cal_day=(today_day + 30) - day
                    cal_month=today_month  - month
                    cal_year=today_year - year
                    label_showAge.config(text=f'Year\t{abs(cal_year)}\nMonth\t{abs(cal_month)}\nDay\t{abs(cal_day)}')

                elif day==today_day and month==today_month:
                    cal_day=today_day - day
                    cal_month=today_month - month
                    cal_year=today_year - year
                    label_showAge.config(text=f'Happy Birthday\n      Year {abs(cal_year)} ')
                    
                else:
                    cal_day=today_day - day
                    cal_month=today_month - month
                    cal_year=today_year - year
                    label_showAge.config(text=f'Year\t{abs(cal_year)}\nMonth\t{abs(cal_month)}\nDay\t{abs(cal_day)}')

    except ValueError as v:
        messagebox.showwarning('Warning', 'Please,Enter Numbers Only ')
        clear()

# Arrangement
# Labels
#year
year_label=Label(window, text='Year', bg='MediumOrchid1', fg='DarkOrchid4')
year_label.configure(font=('Arial Rounded MT Bold', 30))
year_label.place(x=150, y=125)
# month
month_label=Label(window, text='Month', bg='MediumOrchid1', fg='DarkOrchid4')
month_label.configure(font=('Arial Rounded MT Bold', 30))
month_label.place(x=150, y=200)
# day
day_label=Label(window, text='Day', bg='MediumOrchid1', fg='DarkOrchid4')
day_label.configure(font=('Arial Rounded MT Bold', 30))
day_label.place(x=150, y=275)

style=ttk.Style(window)
style.theme_use('clam')

# Input Box
# year
year_entry=Entry(window, bd='5')
year_entry.place(x=350, y=140)
# month
month_entry=Entry(window, bd='5')
month_entry.place(x=350, y=215)
#day
day_entry=Entry(window, bd='5')
day_entry.place(x=350, y=285)

# buttons
button_getage=Button(window, text='Age', command=cal_age, height=1, width=8,
borderwidth=5)
button_getage.configure(fg='Black', bg='DarkOrchid2', font=('bold'))
button_getage.place(x='200', y='370')

button_add=Button(window, text='Add', command=add, height=1, width=8,
borderwidth=5)

button_add.configure(fg='Black', bg='DarkOrchid2', font=('bold'))
button_add.place(x='625', y='370')

button_clear=Button(window, text='Clear', command=clear, height=1,
width=8,
borderwidth=5)
button_clear.configure(fg='Black', bg='DarkOrchid2', font=('bold'))
button_clear.place(x='350', y='370')

window.mainloop()
