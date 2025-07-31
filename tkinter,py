from tkinter import *
from tkinter import colorchooser

# ---------------------- WINDOW SETUP ----------------------
# Create the main application window
windoe = Tk()

# Set the window size: format is 'widthxheight' (note: use lowercase 'x', not uppercase)
windoe.geometry('500x500')

# Set the title that appears at the top of the window
windoe.title('My First GUI')

# Set the window icon
# Make sure 'icon.png' is in the same folder or use the full path
icon = PhotoImage(file='icon.png')
windoe.iconphoto(True, icon)  # Sets the small icon on the top-left of the window

# Set the background color of the window
# You can use standard color names or hex codes
windoe.config(background='#0000bb')  # Deep blue background

# ---------------------- LABEL WIDGET ----------------------
# Label is used to display static text or images
label = Label(
    windoe,
    text='Hello World',
    font=('Arial', 40, 'bold'),  # Font format: (family, size, style)
    fg='#00ff00',  # Foreground (text) color
    bg='#ff0000',  # Background color of label
    padx=20,       # Horizontal padding inside label
    pady=20,       # Vertical padding inside label
    image=icon,    # You can place an image with the text
    compound='bottom'  # Positions text relative to the image (top/bottom/left/right)
)
label.pack()  # Packs the label into the window (centers by default)

# Tip: label.place(x=0, y=0) lets you place widgets precisely using coordinates

# ---------------------- BUTTON WIDGET ----------------------
# Buttons perform actions when clicked

def click():
    print('You clicked the button')

button = Button(
    windoe,
    text='Click Me',
    command=click,  # Function to call when clicked
    font=('Arial', 40, 'bold'),
    fg='#00ff00',
    bg='#0000ff',
    activeforeground='#ff0000',   # Text color when pressed
    activebackground='#ffffff',   # Background color when pressed
    state=ACTIVE,                 # Use DISABLED to make it unclickable
    image=icon,
    compound='bottom'
)
button.pack()

# ---------------------- ENTRY WIDGET ----------------------
# Entry is used to get a single line of user input

def submit():
    print(entry.get())  # Returns the text entered

def delete():
    entry.delete(0, END)  # Deletes text from position 0 to the end

entry = Entry(
    windoe,
    font=('Arial', 40, 'bold'),
    fg='#00ff00',
    bg='#0000ff'
    # show='*'  # Uncomment to hide input (like for passwords)
)
entry.insert(0, 'spongebob')  # Default text shown in entry

submit_button = Button(windoe, text='Submit', command=submit)
delete_button = Button(windoe, text='Delete', command=delete)

# Packing buttons and entry box
delete_button.pack(side=LEFT)
submit_button.pack(side=LEFT)
entry.pack(side=RIGHT)

# Tip: You can also use entry.config(state=DISABLED) to make it read-only after submit

# ---------------------- CHECKBUTTON (Checkbox) ----------------------
# Checkbuttons allow users to toggle between two states (checked/unchecked)

def display():
    if x.get():  # Returns True if checked, False otherwise
        print('You agree')
    else:
        print("You don’t agree")

x = BooleanVar()  # A variable to store the checkbox state (True/False)

check_button = Checkbutton(
    windoe,
    text='I agree',
    variable=x,
    command=display,
    onvalue=True,
    offvalue=False,
    font=('Arial', 40, 'bold'),
    fg='#00ff00',
    bg='#0000ff',
    activeforeground='#ff0000',
    activebackground='#ffffff',
    state=ACTIVE,
    padx=20,
    pady=20,
    image=icon,
    compound='bottom'
)
check_button.pack()

# ---------------------- RADIOBUTTONS (Single Choice) ----------------------
# Radiobuttons let users choose only one option from a list

food = ['pizza', 'waffle', 'icecream']
y = IntVar()  # Integer variable to store selected option (0, 1, 2...)

def order():
    if y.get() == 0:
        print('You ordered pizza')
    elif y.get() == 1:
        print('You ordered waffle')
    elif y.get() == 2:
        print('You ordered icecream')
    else:
        print('Invalid selection')

for index in range(len(food)):
    radio_button = Radiobutton(
        windoe,
        text=food[index],
        variable=y,
        value=index,  # Associates this button with a specific value
        font=('Arial', 20),
        padx=10,
        pady=5,
        indicatoron=1,  # Set to 0 for a pushbutton look
        command=order
    )
    radio_button.pack()

# Tip: You can assign icons/images to each radio button if needed by creating an image list

# ---------------------- SCALE (SLIDER) ----------------------
# Scale widget allows selecting a value by sliding

def tempsubmit():
    print(f'The temperature is {scale.get()}')

scale = Scale(
    windoe,
    from_=0,
    to=100,  # If from_ > to, the scale is reversed
    length=300,  # Length of the scale in pixels
    orient=VERTICAL,  # Can also be HORIZONTAL
    font=('Arial', 15),
    tickinterval=10,  # Interval for showing scale marks
    troughcolor='#0000ff',  # Track color
    fg='#00ff00',
    bg='#0000ff'
    # showvalue=0  # Uncomment to hide the current value
)
scale.pack()

temp_button = Button(windoe, text='Submit Temp', command=tempsubmit)
temp_button.pack()

from tkinter import *



# Entry box for adding new items
item_entry = Entry(
    windoe,
    font=('Arial', 20),
    fg='#00ff00',
    bg='#0000ff',
    width=20
)
item_entry.pack(pady=10)

# Listbox that supports multiple selections
listbox = Listbox(
    windoe,
    selectmode=MULTIPLE,  # Allows multiple selections
    fg='#00ff00',
    bg='#0000ff',
    font=('Arial', 20),
    width=20,
    height=6
)
listbox.pack()

# Add some initial items (optional)
for item in ['Pizza', 'Burger', 'Ice Cream']:
    listbox.insert(END, item)

# Function to add an item from entry to listbox
def add_item():
    new_item = item_entry.get()
    if new_item.strip():  # Prevent empty entries
        listbox.insert(END, new_item)
        item_entry.delete(0, END)

# Function to delete selected items
def delete_selected():
    selected_indices = list(listbox.curselection())[::-1]  # Reverse to delete safely
    for i in selected_indices:
        listbox.delete(i)

# Function to print selected items
def submit_items():
    selected_indices = listbox.curselection()
    selected_items = [listbox.get(i) for i in selected_indices]
    print("Selected items:", selected_items)

# Add Button
add_btn = Button(windoe, text="Add", command=add_item, font=('Arial', 14))
add_btn.pack(pady=5)

# Delete Button
delete_btn = Button(windoe, text="Delete", command=delete_selected, font=('Arial', 14))
delete_btn.pack(pady=5)

# Submit Button
submit_btn = Button(windoe, text="Submit", command=submit_items, font=('Arial', 14))
submit_btn.pack(pady=5)


#messagebox
def click():
    messagebox.showinfo(title='This is a info message box',message='you are a person')
    messagebox.showwarning(title='warning',message='u have a virus')
    massagebox.showerror(title='warning',message='u have a error', icon='info')

    messagebox.askokcancel()
    #use while True for annoying
    #there are somany massagebox. methords some like the one above returns boolean
    #messagebox.askquestion() gives yes or no
    #messagebox.askyesnocancel() gives True,False,None for yes no cance
    #you can insert keyword parameter icon to chance icon
button=Button(windoe,text='clickme',command=click)
button.pack()
#colorchooser
def color():
    button.config( )
button=Button(windoe,text='clickme',command=color)
#file
