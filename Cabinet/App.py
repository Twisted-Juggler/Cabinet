import tkinter as tk
import tkinter.font as font
from Main import MainProgram
from ProfileSys import ProfileSystem as Ps

foreground_color = '#F1F1F1'
background_colors = '#0E0E0E'

window = tk.Tk()
window.geometry('1200x650')
window.title('Cabinet')


# -- Info Window -- #
# Opens a window giving instructions on
# how to use the program

def info():
    window2 = tk.Tk()
    window2.title('How to')
    label_font = font.Font(size=50)

    newframe = tk.Frame(master=window2, width=300, height=300, bg=background_colors)
    newframe.pack()

    information = tk.Label(
        master=newframe,
        fg=foreground_color,
        bg=background_colors,
        text='''
        Welcome to Cabinet! To get started, just copy and paste the path
        of the folder you wish to sort and paste it
        into the 'Sort Folder' textbox, then do the same for the folder you want it sorted in 
        to and paste it in the \'Cabinet\' textbox. Now press sort and all the files will be sorted!
        Once sorted, it will save the location of the directories last used and will automatically fill them
        in by default.''')

    information['font'] = label_font
    information.pack(fill=tk.BOTH, expand=True)

    exit_button = tk.Button(
        master=newframe,
        fg=background_colors,
        text='Exit',
        command=window2.destroy,
        relief=tk.FLAT)

    exit_button['font'] = label_font
    exit_button.pack()

    window2.mainloop()


# -- GUI -- #
# Below is all the code used to make the user
# interface for Cabinet

def gui():
    input_font = font.Font(size=15)
    title_font = font.Font(size=50)
    button_font = font.Font(size=15)
    label_font = font.Font(size=20)

    frame = tk.Frame(master=window, width=300, height=300, bg=background_colors)
    frame.pack(fill=tk.BOTH, expand=True)

    title = tk.Label(
        master=frame,
        text='Cabinet',
        fg=foreground_color,
        bg=background_colors,
        font='Arial')

    title['font'] = title_font
    title.pack(fill=tk.Y, padx=50, pady=15)

    origin_label = tk.Label(
        master=frame,
        fg=foreground_color,
        bg=background_colors,
        text='Sort Folder')

    origin_input = tk.Entry(
        master=frame,
        bg=foreground_color,
        fg=background_colors,
        font='Helvetica')

    destination_label = tk.Label(
        master=frame,
        fg=foreground_color,
        bg=background_colors,
        text='Cabinet Folder')

    destination_input = tk.Entry(
        master=frame, bg=foreground_color,
        fg=background_colors,
        font='Helvetica')

    origin_label.pack(fill=tk.Y, pady=15)
    origin_input['font'] = input_font

    origin_input.pack(fill=tk.Y, ipady=10, ipadx=50, pady=5)
    origin_label['font'] = label_font

    destination_input['font'] = input_font
    destination_label['font'] = label_font

    destination_label.pack(fill=tk.Y, pady=5)
    origin_input.pack(fill=tk.Y, ipady=10, ipadx=50, pady=15)
    destination_input.pack(fill=tk.Y, ipady=10, ipadx=50, pady=15)

# -- Sort -- #
# The sort function runs MainProgram.py, fills
# in path information, and sorts all the files.

    def sort():
        main_origin = origin_input.get()
        main_destination = destination_input.get()

        Ps.write_profiles(main_origin, main_destination)

        MainProgram.folders(Ps.Profiles().content[0], Ps.Profiles().content[1])
        MainProgram.sorting(Ps.Profiles().content[0], Ps.Profiles().content[1])

    origin_input.insert(0, Ps.Profiles().content[0])
    destination_input.insert(0, Ps.Profiles().content[1])

    begin = tk.Button(
        master=frame,
        bg=foreground_color,
        fg=background_colors,
        text='Sort',
        command=sort,
        relief=tk.FLAT)

    begin['font'] = button_font
    begin.pack(fill=tk.Y, ipady=10, ipadx=50, pady=15)

    info_button = tk.Button(
        master=frame,
        bg=foreground_color,
        fg=background_colors,
        text='How to',
        command=info,
        relief=tk.FLAT)

    info_button['font'] = button_font
    info_button.pack(fill=tk.Y, ipady=5, ipadx=25, pady=15)

    exit_button = tk.Button(
        master=frame,
        bg=foreground_color,
        fg=background_colors,
        text='Exit',
        command=window.destroy,
        relief=tk.FLAT)

    exit_button['font'] = button_font
    exit_button.pack(fill=tk.Y, ipady=5, ipadx=40, pady=15)


gui()
window.mainloop()
