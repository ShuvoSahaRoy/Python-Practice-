import tkinter as tk
from tkinter import ttk
from csv import DictWriter
import os
win = tk.Tk()
win.title('User Interface')

# create level
name_level = ttk.Label(win, text='Enter your name : ')
name_level.grid(row=0, column=0, sticky=tk.W)

email_level = ttk.Label(win, text='Enter your email : ')
email_level.grid(row=1, column=0, sticky=tk.W)

age_level = ttk.Label(win, text='Enter your age : ')
age_level.grid(row=2, column=0, sticky=tk.W)

gender_level = ttk.Label(win, text='Enter your gender : ')
gender_level.grid(row=3, column=0, sticky=tk.W)

# create entry box
name_var = tk.StringVar()
name_entrybox = ttk.Entry(win, width=16, textvariable=name_var)
name_entrybox.grid(row=0, column=1)
name_entrybox.focus()

email_var = tk.StringVar()
email_entrybox = ttk.Entry(win, width=16, textvariable=email_var)
email_entrybox.grid(row=1, column=1)

age_var = tk.StringVar()
age_entrybox = ttk.Entry(win, width=16, textvariable=age_var)
age_entrybox.grid(row=2, column=1)

# create combo box
gender_var = tk.StringVar()
gennder_combobox = ttk.Combobox(win, width=13, textvariable=gender_var)
gennder_combobox['values'] = ('Male', 'Female', 'Other')
gennder_combobox.current(0)
gennder_combobox.grid(row=3, column=1)

# radio button
usertype = tk.StringVar()
radiobtn1 = ttk.Radiobutton(win, text='Student', value='Student', variable=usertype)
radiobtn1.grid(row=4, column=0)

radiobtn2 = ttk.Radiobutton(win, text='Teacher', value='Teacher', variable=usertype)
radiobtn2.grid(row=4, column=1)

# check button
checkbtn_var = tk.IntVar()
checkbtn = ttk.Checkbutton(win, text='Check yes or not', variable=checkbtn_var)
checkbtn.grid(row=5, columnspan=3)


# create button
#def action():
    # user_name = name_var.get()
    # user_email = email_var.get()
    # user_age = age_var.get()
    # print("Your name {},  your age {} , ur email {}".format(user_name, user_age, user_email))
    # user_gender = gender_var.get()
    # user_type = usertype.get()
    # if checkbtn_var.get() == 0:
    #     subscribed = 'NO'
    # else:
    #     subscribed = 'YES'
    # print(user_gender, user_type, subscribed)
    # # To write in txt file
    # with open('info.txt', 'a') as f:
    #     f.write(f'{user_name},{user_age},{user_email},{user_gender},{user_type},{subscribed}\n')
    #
    # name_entrybox.delete(0, tk.END)
    # age_entrybox.delete(0, tk.END)
    # email_entrybox.delete(0, tk.END)
    # name_level.configure(foreground='Blue')
    # submit_button.configure(foreground ='Blue')  # for button ttk doesn't support color. need to use tk method

def action():
    user_name = name_var.get()
    user_email = email_var.get()
    user_age = age_var.get()
    print("Your name {},  your age {} , ur email {}".format(user_name, user_age, user_email))
    user_gender = gender_var.get()
    user_type = usertype.get()
    if checkbtn_var.get() == 0:
        subscribed = 'NO'
    else:
        subscribed = 'YES'
    print(user_gender, user_type, subscribed)
        # to write in csv file
    with open('file operation/file.csv', 'a') as f:
        dict_writer = DictWriter(f, fieldnames=['UserName', 'User Email', 'User Age', 'User Gender',
                                                    'User Type', 'Subscribed'])
        if os.stat('file operation/file.csv').st_size==0:
             dict_writer.writeheader()

        dict_writer.writerow({
            'UserName': user_name,
            'User Email': user_email,
            'User Age': user_age,
            'User Gender': user_gender,
            'User Type': user_type,
            'Subscribed': subscribed }
        )
        name_entrybox.delete(0, tk.END)
        age_entrybox.delete(0, tk.END)
        email_entrybox.delete(0, tk.END)
        name_level.configure(foreground='Blue')


submit_button = ttk.Button(win, text='Submit', command=action)
submit_button.grid(row=6, column=0)

win.mainloop()
