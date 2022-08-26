from tkinter import *
from tkinter import ttk
import random
from bubble_sort_code import bubble_sort
from insertion_sort_code import insertion_sort
from selection_sort_code import selection_sort
from merge_sort_code import merge_sort
from quick_sort_code import quick_sort

root = Tk()
root.title('Sorting Algorithm Visualizer')
root.config(bg="#023047")
root.geometry("800x750")
root.resizable(False, False)
select_algorithm = StringVar()
array = []

top_heading = Label(root, text="Let's Do Sorting !", bg="#023047", fg="white", font=("Courier New", 35, "bold"), padx=10, pady=20)
top_heading.grid(row=0, column = 1, padx = 23)

# Sorting array
def sorting():
    global array

    if select_algorithm.get() == "Bubble Sort":
        bubble_sort(array, draw_rectangular_elements, sorting_speed.get())
    elif select_algorithm.get() == "Insertion Sort":
        insertion_sort(array, draw_rectangular_elements, sorting_speed.get())
    elif select_algorithm.get() == "Selection Sort":
        selection_sort(array, draw_rectangular_elements, sorting_speed.get())
    elif select_algorithm.get() == "Merge Sort":
        merge_sort(array, draw_rectangular_elements, sorting_speed.get())
    elif select_algorithm.get() == "Quick Sort":
        quick_sort(array, draw_rectangular_elements, sorting_speed.get())
# Creating array
def Generate_array():
    global array
    lower_bound = int(lower_val.get())
    upper_bound = int(upper_val.get())
    size = int(array_size.get())
    array = []
    for i in range(size):
        array.append(random.randrange(lower_bound, upper_bound + 1))
    draw_rectangular_elements(array, ['#FF5003' for x in range(len(array))])

def draw_rectangular_elements(array, elements_color):
    canvas_for_array.delete("all")
    canvas_height = 360
    canvas_width = 739
    bar_width = canvas_width / (len(array))
    border_offset = 0
    spacing = 10
    normalized_array = [ x/max(array) for x in array]

    for i, height in enumerate(normalized_array):
        # top left corner
        x0 = i * bar_width + border_offset + spacing
        y0 = canvas_height - height * 341
        # bottom right corner
        x1 = (i + 1) * bar_width + border_offset
        y1 = canvas_height
        canvas_for_array.create_rectangle(x0, y0, x1, y1, fill=elements_color[i])
        canvas_for_array.create_text(x0, y0, anchor=SW, text=str(array[i]))

    root.update_idletasks()
    # 370 749

# Frame designing
frame_with_options = Frame(root, width=750, height = 200, background = "#249ea0", highlightbackground = "#249eA0", padx = 30, pady = 25)
frame_with_options.grid(row=1, column=1, pady=4)

# Select an algorithm
choose_frame = Frame(frame_with_options, pady = 8)
choose_frame.grid(row=0, column=0, padx=28, pady=15)
Label(choose_frame, text="Select an algorithm").grid(row=0, column=0)
algorithm_menu = ttk.Combobox(choose_frame, textvariable=select_algorithm, values=['Bubble Sort', 'Insertion Sort', 'Selection Sort', 'Merge Sort', 'Quick Sort'], width = 15)
algorithm_menu.grid(row=1, column=0, padx=10)
algorithm_menu.current(0)

# Set Sorting Speed
sorting_speed = Scale(frame_with_options, from_=0.2, to=2.0, resolution=0.2, orient=HORIZONTAL, label="Set Sorting Speed", highlightbackground="white")
sorting_speed.grid(row=0, column=1, padx=28, pady=15)

# START Sorting
Button(frame_with_options, text="START SORTING", command=sorting, padx=8, pady=18).grid(row=0, column=2, padx=28, pady=15)

# Setting limits
limits = Frame(frame_with_options, padx=7, pady=7)
limits.grid(row=1, column=0, padx=28, pady=15)
Label(limits, text="Lower Bound : ").grid(row=0, column=0)
lower_val = Entry(limits, width=5)
lower_val.grid(row=0, column=1)
Label(limits, text="Upper Bound : ").grid(row=1, column=0)
upper_val = Entry(limits, width=5)
upper_val.grid(row=1, column=1)

# Setting array Size
array_size = Scale(frame_with_options, from_=3, to=25, resolution=1, orient=HORIZONTAL, label ="Set Array Size")
array_size.grid(row=1, column=1, padx = 28, pady = 15)

# Creating array
Button(frame_with_options, text="CREATE ARRAY", command=Generate_array, padx=9, pady = 18).grid(row=1, column=2, padx = 28, pady = 15)

canvas_for_array = Canvas(root, width=746, height=370, bg="#b8d5cd", highlightbackground="#b8d5cd")
canvas_for_array.grid(row=2, column=1, padx=23, pady=20)

"""
#F4A896 -> Pinkish
#358597 -> greenish bluish
#39FF13 -> bright green
"""
root.mainloop()