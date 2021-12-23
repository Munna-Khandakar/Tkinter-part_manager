from tkinter import *

# create windoe object
app = Tk()

# part
part_text = StringVar()
part_label = Label(app, text='Part Name', font=('bold,14'), pady=20)
part_label.grid(row=0, column=0, sticky=W)
part_entry = Entry(app, textvariable=part_text)
part_entry.grid(row=0, column=1)

# customer
customer_text = StringVar()
customer_label = Label(app, text='Customer Name', font=('bold,14'))
customer_label.grid(row=0, column=2, sticky=W)
customer_entry = Entry(app, textvariable=customer_text)
customer_entry.grid(row=0, column=3)

# retailer
retailer_text = StringVar()
retailer_label = Label(app, text='Retailer Name', font=('bold,14'))
retailer_label.grid(row=1, column=0, sticky=W)
retailer_entry = Entry(app, textvariable=retailer_text)
retailer_entry.grid(row=1, column=1)

# parts list (Listbox)
parts_list = Listbox(app, height=8,width=50)

# price
price_text = StringVar()
price_label = Label(app, text='Price Name', font=('bold,14'))
price_label.grid(row=1, column=2, sticky=W)
price_entry = Entry(app, textvariable=price_text)
price_entry.grid(row=1, column=3)

app.title('part Manager')
app.geometry('700x350')


# start pprogram
app.mainloop()
