import tkinter as tk
from tkinter import ttk

win = tk.Tk()
win.title('Level Frame')

label_frame = ttk.LabelFrame(win, text='Enter your details below')
label_frame.grid(row=0, column=0,padx=40)

labels = ['Enter ur name : ', 'Enter ur age: ', 'Enter ur gender: ', 'Country : ',
          'State : ', 'City : ']

for i in range(len(labels)):
    current_level = 'level' + str(i)
    current_leve = ttk.Label(label_frame, text=labels[i])
    current_leve.grid(row=i, column=0, sticky=tk.W, padx=2, pady=2)

# entry box

user_info = {
    'name': tk.StringVar(),
    'age': tk.StringVar(),
    'gender': tk.StringVar(),
    'country': tk.StringVar(),
    'state': tk.StringVar(),
    'city': tk.StringVar()
}
counter = 0
for i in user_info:
    current_entrybox = 'entry' + i
    current_entrybox = ttk.Entry(label_frame, width=16, textvariable=user_info[i])
    current_entrybox.grid(row=counter, column=1, padx=2, pady=2)
    counter += 1


def submit():
    # print(user_info['name'].get())
    # print(user_info.get('age').get())
    # print(user_info.get('gender').get())
    # print(user_info.get('country').get())
    # print(user_info.get('city').get())
    # print(user_info.get('state').get())
    # for i in user_info:
    #     print(user_info[i].get())
    for key, value in user_info.items():
        print("{} : {}".format(key, value.get()))
    # print(user_info)


submit_but = ttk.Button(label_frame, text='Submit', command=submit)
submit_but.grid(row=6, columnspan=2)

win.mainloop()
