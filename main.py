import tkinter
import tkinter.messagebox
import customtkinter
import activity
import plan
import time
import win32api
import random
import _thread
# def appui_try():
# window = Tk()
# window.geometry('350x200')
# window.title("Welcome to LikeGeeks app")
# lbl = Label(window, text="Hello", font= ("Arial Bold", 20))
# lbl.grid(column=0, row=0)
#
# txt = Entry(window, width=10)
# txt.grid(column=1, row=0)
# txt.focus()
#
# def clicked():
#     res = "Welcome to " + txt.get()
#
#     lbl.configure(text=res)
#
# btn = Button(window, text="Click Me", bg="orange", fg="red", command= clicked)
# btn.grid(column=2, row=0)
#
# from tkinter import filedialog
# # file = filedialog.askopenfilename(filetypes=(("Text files", "*.txt"), ("all files", "*.*")))
#
# # dir = filedialog.askdirectory()
# #
# # from os import path
# # file = filedialog.askopenfilename(initialdir=path.dirname("../"))
#
# from tkinter import Menu
# menu = Menu(window)
# new_item = Menu(menu, tearoff=0)
# new_item.add_command(label='New')
# menu.add_cascade(label='File', menu=new_item)
# window.config(menu=menu)
#
# window.mainloop()
# pass

# def make_table(window, list, total_rows, total_columns):
#     # code for creating table
#     for i in range(total_rows):
#         for j in range(total_columns):
#             # border_color = Frame(window, width=10, background="black")
#             # e = Label(border_color, text=list[i][j], fg='blue',
#             #           font = ('Arial', 16, 'bold'))
#             #
#             #
#             # e.pack(padx=1, pady=1)
#             # border_color.grid(row=i, column=j)
#             # # e.insert(END, list[i][j])
#
#             e = Label(window, width=10, text=list[i][j], fg='blue',
#                       font=('Arial', 16, 'bold'), borderwidth = 1, relief = "groove")
#             e.grid(row=i, column=j)
#

dtime = activity.get_date()
wdates = activity.get_weekdates()

customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"


class App(customtkinter.CTk):
    WIDTH = 1000
    HEIGHT = 620

    def __init__(self):
        super().__init__()
        self.stopsignal = 1
        self.title("oldcalender 0.1.0")
        self.geometry(f"{App.WIDTH}x{App.HEIGHT}")
        self.protocol("WM_DELETE_WINDOW", self.on_closing)  # call .on_closing() when app gets closed

        # ============ create two frames ============

        # configure grid layout (2x1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.frame_left = customtkinter.CTkFrame(master=self,
                                                 width=180,
                                                 corner_radius=0)
        self.frame_left.grid(row=0, column=0, sticky="nswe")

        self.frame_right = customtkinter.CTkFrame(master=self)
        self.frame_right.grid(row=0, column=1, sticky="nswe", padx=20, pady=20)

        # ============ frame_left ============

        # configure grid layout (1x11)
        self.frame_left.grid_rowconfigure(0, minsize=10)  # empty row with minsize as spacing
        self.frame_left.grid_rowconfigure(5, weight=1)  # empty row as spacing
        self.frame_left.grid_rowconfigure(8, minsize=20)  # empty row with minsize as spacing
        self.frame_left.grid_rowconfigure(11, minsize=10)  # empty row with minsize as spacing

        self.label_1 = customtkinter.CTkLabel(master=self.frame_left,
                                              text="Old calendar",
                                              text_font=("Roboto Medium", -16))  # font name and size in px
        self.label_1.grid(row=1, column=0, pady=10, padx=10)

        self.entry_1 = customtkinter.CTkEntry(master=self.frame_left,
                                              placeholder_text="Start T(2022 9 18 4 22)",
                                              width=140,
                                              height=25,
                                              border_width=2,
                                              corner_radius=10)

        self.entry_1.grid(row=2, column=0, pady=10, padx=20)

        self.entry_2 = customtkinter.CTkEntry(master=self.frame_left,
                                              placeholder_text="End T(2022 9 18 5 12)",
                                              width=140,
                                              height=25,
                                              border_width=2,
                                              corner_radius=10)

        self.entry_2.grid(row=3, column=0, pady=10, padx=20)

        self.entry_3 = customtkinter.CTkEntry(master=self.frame_left,
                                              placeholder_text="Name",
                                              width=140,
                                              height=25,
                                              border_width=2,
                                              corner_radius=10)

        self.entry_3.grid(row=4, column=0, pady=10, padx=20)

        self.entry_4 = customtkinter.CTkEntry(master=self.frame_left,
                                              placeholder_text="Annotate",
                                              width=140,
                                              height=25,
                                              border_width=2,
                                              corner_radius=10)

        self.entry_4.grid(row=5, column=0, pady=10, padx=20)

        self.button_1 = customtkinter.CTkButton(master=self.frame_left,
                                                text="Add Event",
                                                command=self.button_event)
        self.button_1.grid(row=6, column=0, pady=10, padx=20)

        self.label_mode = customtkinter.CTkLabel(master=self.frame_left, text="Appearance Mode:")
        self.label_mode.grid(row=9, column=0, pady=0, padx=20, sticky="w")

        self.optionmenu_1 = customtkinter.CTkOptionMenu(master=self.frame_left,
                                                        values=["Light", "Dark", "System"],
                                                        command=self.change_appearance_mode)
        self.optionmenu_1.grid(row=10, column=0, pady=10, padx=20, sticky="w")

        # ============ frame_right ============

        # configure grid layout (3x7)
        self.frame_right.rowconfigure((0, 1, 2, 3), weight=1)
        self.frame_right.rowconfigure(7, weight=10)
        self.frame_right.columnconfigure((0, 1), weight=1)
        self.frame_right.columnconfigure(2, weight=0)

        # ============ frame_info ============

        # ============ frame_right ============
        self.lst = [['', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'],
                    ['Sept.', '12', '13', '14', '15', '16', '17', '18']]
        for i in range(24):
            self.lst.append([str(i) + ':00-' + str(i) + ':30', '', '', '', '', '', '', ''])
            self.lst.append([str(i) + ':30-' + str(i + 1) + ':00', '', '', '', '', '', '', ''])

        textlst = ''
        for i in self.lst:
            for j in i:
                space = 10
                if i.index(j) == 0: space = 11
                textlst = textlst + j + ' ' * (space - len(j)) + '|'
            textlst = textlst + '\n'
            for k in i:
                space = 10
                if i.index(k) == 0: space = 11
                textlst = textlst + '-' * space + '|'
            textlst = textlst + '\n'

        # total_rows = len(lst)
        # total_columns = len(lst[0])

        # set default values
        # create scrollable textbox

        self.tk_textbox = tkinter.Text(self.frame_right, height=50, width=90, background='grey', fg='white')
        self.tk_textbox.grid(row=0, column=0, sticky="nsew")
        self.tk_textbox.insert(tkinter.INSERT, textlst)

        # create CTk scrollbar
        self.ctk_textbox_scrollbar = customtkinter.CTkScrollbar(self.frame_right, command=self.tk_textbox.yview)
        self.ctk_textbox_scrollbar.grid(row=0, column=1, sticky="ns")

        # connect textbox scroll event to CTk scrollbar
        self.tk_textbox.configure(yscrollcommand=self.ctk_textbox_scrollbar.set)

        self.optionmenu_1.set("System")

        self.activities = activity.Activity()



    def update_textbox(self, plan_c, start_tuple, end_tuple):         # TODO use self.activities.daily act to solve over 1 day problem
        weekdaynum = start_tuple[2]-wdates[0] + 1
        for i in range(24):
            if i<=start_tuple[3]:
                lmaxh = i
                lmaxm = 0                  # 0 for 0-29, 1 for 30-60()
                if start_tuple[4] >= 30:
                    lmaxm = 1
            if i>=end_tuple[3]:
                uminh = i
                uminm = 1
                if end_tuple[4] < 30:
                    uminm = 0
                break
        starttimeloc = 2*lmaxh+lmaxm+2
        endtimeloc = 2*uminh+uminm+2
        for j in range(starttimeloc,endtimeloc):
            self.lst[j][weekdaynum] = '##########'
        self.lst[endtimeloc][weekdaynum] = plan_c.name[0:10]+'#' * (10 - len(plan_c.name[0:10]))



    def refresh_calendar(self):
        self.tk_textbox.delete(1.0, 99.0)

        textlst = ''
        for i in self.lst:
            for j in i:
                space = 10
                if i.index(j) == 0: space = 11
                textlst = textlst + j + ' ' * (space - len(j)) + '|'
            textlst = textlst + '\n'
            for k in i:
                space = 10
                if i.index(k) == 0: space = 11
                textlst = textlst + '-' * space + '|'
            textlst = textlst + '\n'

        self.tk_textbox = tkinter.Text(self.frame_right, height=50, width=90, background='grey', fg='white')
        self.tk_textbox.grid(row=0, column=0, sticky="nsew")
        self.tk_textbox.insert(tkinter.INSERT, textlst)


    def islegal(self, str):
        return len(str) != 0
        # TODO

    def button_event(self):
        # print("Button pressed")

        start_str = self.entry_1.get()
        end_str = self.entry_2.get()
        name = self.entry_3.get()
        annotate = self.entry_4.get()

        if self.islegal(start_str) and self.islegal(end_str):
            start_t=start_str.split()
            end_t=end_str.split()
            start_tuple=(int(start_t[0]), int(start_t[1]), int(start_t[2]), int(start_t[3]), int(start_t[4]))
            end_tuple=(int(end_t[0]), int(end_t[1]), int(end_t[2]), int(end_t[3]), int(end_t[4]))
            plan_c = plan.Plan(name=name,annotate=annotate,periods=[(start_tuple, end_tuple)])    # TODO for multiple periods
            self.activities.create(plan_c)
            self.update_textbox(plan_c, start_tuple, end_tuple)
            self.refresh_calendar()


    def change_appearance_mode(self, new_appearance_mode):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def on_closing(self):
        self.stopsignal=0
        self.destroy()

    def alarm_thread_bg(self):
        while self.stopsignal:
            for i in self.activities.daily_act[dtime[2]]:
                print(str(time.localtime(time.time()).tm_min),((i[1])[0])[1])
                if time.localtime(time.time()).tm_min==((i[1])[0])[1]:
                    for i in range(5):
                        win32api.Beep(random.randint(37, 2000), random.randint(750, 3000))    # TODO might need to add a stop to this or it's going to beep for a whole minute

            time.sleep(5)




if __name__ == '__main__':
    app = App()
    try:
        _thread.start_new_thread(app.alarm_thread_bg, ())
    except:
        print("Error: Cannot start thread")

    app.mainloop()
