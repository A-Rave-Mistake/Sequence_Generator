# --- LICENSE ---

    # Copyright (C) 2022 Adrian Urbaniak (FancySnacks)

    # This program is free software: you can redistribute it and/or modify
    # it under the terms of the GNU General Public License as published by
    # the Free Software Foundation, either version 3 of the License, or
    # (at your option) any later version.

    # This program is distributed in the hope that it will be useful,
    # but WITHOUT ANY WARRANTY; without even the implied warranty of
    # MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    # GNU General Public License for more details.

    # You should have received a copy of the GNU General Public License
    # along with this program.  If not, see <https://www.gnu.org/licenses/>.



# --- SCRIPT BEGINS HERE ---

from tkinter import *
from tkinter import ttk, filedialog
import main
import functions



class MainWindow:

    def __init__(self):
        self.root = Tk()
        self.root.title("Generator")
        self.root.resizable(False, False)

        # Settings
        self.num_of_results = StringVar(self.root)
        self.num_of_results.set("1")

        self.match_file_length = BooleanVar(self.root)
        self.match_file_length.set(False)

        self.separator = StringVar(self.root)
        self.separator.set(", ")

        self.use_new_lines = BooleanVar(self.root)
        self.use_new_lines.set(True)

        self.allow_duplicates = BooleanVar(self.root)
        self.allow_duplicates.set(True)

        self.order_list = ["Ordered (1 -> n)", "Random", "Random (Unique)", "Random (Sequence)"]
        self.order = StringVar(self.root)
        self.order.set("Ordered (1 -> n)")

        # Start With / End With Settings
            # Sequence
        self.s_start_with = StringVar(self.root)
        self.s_start_with.set("")
        self.s_end_with = StringVar(self.root)
        self.s_end_with.set("")
            # Results
        self.start_with = StringVar(self.root)
        self.start_with.set("")
        self.end_with = StringVar(self.root)
        self.end_with.set("")




        # Window Size
        self.window_height = 710
        self.window_width = 465
        self.x = int((self.root.winfo_screenwidth() / 2) - (self.window_width / 2))
        self.y = int((self.root.winfo_screenheight() / 2) - (self.window_height / 2))
        self.root.geometry("{}x{}+{}+{}".format(self.window_width, self.window_height, self.x, self.y))


        # Main Frame

        self.Overlord = Frame(self.root)
        self.Overlord.pack(fill=BOTH, expand=True)

        self.canvas = Canvas(self.Overlord)
        self.canvas.pack(side=LEFT, fill=BOTH, expand=True)

        # Main frame scrollbar
        self.scrollbar = Scrollbar(self.Overlord, orient=VERTICAL, command=self.canvas.yview)
        self.scrollbar.pack(side=RIGHT, fill=Y)

        # Connect scrollbar to the canvas to allow scrolling
        self.canvas.config(yscrollcommand=self.scrollbar.set)
        self.canvas.bind('<Configure>', lambda e: self.canvas.configure(scrollregion = self.canvas.bbox("all")))

        self.mainFrame = Frame(self.canvas)
        self.canvas.create_window((0,0), window=self.mainFrame, anchor="nw")

        # Bind scrollbar to mouse wheel manually because it doesn't seem to work by itself
        self.canvas.bind_all("<MouseWheel>", self.on_mousewheel)


        # Settings Container
        self.SettingsFrame = Frame(self.mainFrame)
        self.SettingsFrame.grid(row=0, sticky=W)

        self.SettingsLabel = Label(self.SettingsFrame, text="// Settings", padx=5, pady=5, font=("Arial", 12, "bold"))
        self.SettingsLabel.grid(row=0, column=0, sticky=W)

            # Number of Results
        self.Settings_NumOfResults_Label = Label(self.SettingsFrame, text="No. of Results: ", padx=5, font=("Arial", 10))
        self.Settings_NumOfResults_Label.grid(row=1, column=0, sticky=W)

        self.Settings_NumOfResults_Input = Entry(self.SettingsFrame, textvariable=self.num_of_results, width=10, font=("Arial", 10))
        self.Settings_NumOfResults_Input.grid(row=1, column=1, sticky=W)

        self.Settings_FileEnd_Label = Label(self.SettingsFrame, text="Match File Length", padx=5, font=("Arial", 10))
        self.Settings_FileEnd_Label.grid(row=1, column=2, sticky=E)

        self.Settings_FileEnd_Check = Checkbutton(self.SettingsFrame, variable=self.match_file_length, width=2, font=("Arial", 10))
        self.Settings_FileEnd_Check.grid(row=1, column=3, sticky=E)

        self.Settings_FileEnd_Label.grid_forget()
        self.Settings_FileEnd_Check.grid_forget()

            # Seperator Entry
        self.Settings_Seperator_Label = Label(self.SettingsFrame, text="Separate with: ", padx=5, font=("Arial", 10), pady=5)
        self.Settings_Seperator_Label.grid(row=2, column=0, sticky=W)

        self.Settings_Seperator_Input = Entry(self.SettingsFrame, textvariable=self.separator, width=5, font=("Arial", 13))
        self.Settings_Seperator_Input.grid(row=2, column=1, sticky=W)

            # New Line Wrapping
        self.Settings_newline_Label = Label(self.SettingsFrame, text="New line wrapping ", padx=5, font=("Arial", 10))
        self.Settings_newline_Label.grid(row=3, column=0, sticky=W)

        self.Settings_newline_Input = Checkbutton(self.SettingsFrame, variable=self.use_new_lines)
        self.Settings_newline_Input.grid(row=3, column=1, sticky=W)

            # Allow Duplicates

        self.Settings_duplicates_Label = Label(self.SettingsFrame, text="Allow duplicate combinations ", padx=5, font=("Arial", 10))
        self.Settings_duplicates_Label.grid(row=4, column=0, sticky=W)

        self.Settings_duplicates_Input = Checkbutton(self.SettingsFrame, variable=self.allow_duplicates)
        self.Settings_duplicates_Input.grid(row=4, column=1, sticky=W)

            # Start Sequence With
        self.Settings_StartSeqWith_Label = Label(self.SettingsFrame, text="Start sequence with: ", padx=5, font=("Arial", 10), pady=5)
        self.Settings_StartSeqWith_Label.grid(row=5, column=0, sticky=W)

        self.Settings_StartSeqWith_Input = Entry(self.SettingsFrame, textvariable=self.s_start_with, width=10, font=("Arial", 10))
        self.Settings_StartSeqWith_Input.grid(row=5, column=1, sticky=W)

            # End Sequence With
        self.Settings_EndSeqWith_Label = Label(self.SettingsFrame, text="End sequence with: ", padx=5, font=("Arial", 10), pady=5)
        self.Settings_EndSeqWith_Label.grid(row=6, column=0, sticky=W)

        self.Settings_EndSeqWith_Input = Entry(self.SettingsFrame, textvariable=self.s_end_with, width=10, font=("Arial", 10))
        self.Settings_EndSeqWith_Input.grid(row=6, column=1, sticky=W)

            # Start Results With
        self.Settings_StartRWith_Label = Label(self.SettingsFrame, text="Start results with: ", padx=5,
                                              font=("Arial", 10), pady=5)
        self.Settings_StartRWith_Label.grid(row=7, column=0, sticky=W)

        self.Settings_StartRWith_Input = Entry(self.SettingsFrame, textvariable=self.start_with, width=10,
                                              font=("Arial", 10))
        self.Settings_StartRWith_Input.grid(row=7, column=1, sticky=W)

            # End Results With
        self.Settings_EndRWith_Label = Label(self.SettingsFrame, text="End results with: ", padx=5, font=("Arial", 10),
                                            pady=5)
        self.Settings_EndRWith_Label.grid(row=8, column=0, sticky=W)

        self.Settings_EndRWith_Input = Entry(self.SettingsFrame, textvariable=self.end_with, width=10,
                                            font=("Arial", 10))
        self.Settings_EndRWith_Input.grid(row=8, column=1, sticky=W)


        # Generator Config Container
        self.GeneratorFrame = Frame(self.mainFrame, pady=15)
        self.GeneratorFrame.grid(row=1, sticky=W+E)

        self.GeneratorLabel = Label(self.GeneratorFrame, text="// Generators", padx=5, pady=5, font=("Arial", 12, "bold"))
        self.GeneratorLabel.grid(row=0, column=0, sticky=W)

        self.order_menu = OptionMenu(self.GeneratorFrame, self.order, *self.order_list)
        self.order_menu.grid(row=1, column=0, sticky=W)

        self.GeneratorContainer = Frame(self.GeneratorFrame)
        self.GeneratorContainer.grid(row=2, column=0)

            # Generator Master
        self.generator_master = GeneratorContainer(self.GeneratorContainer, self, self.root)
        self.add_generator()

        self.ButtonFrame = Frame(self.GeneratorFrame, padx=10, pady=5)
        self.ButtonFrame.grid(row=3, column=0, sticky=W)

        self.GeneratorCreateButton = Button(self.ButtonFrame, text="Add Input", padx=5, pady=3, command=self.add_generator)
        self.GeneratorCreateButton.grid(row=0, column=0)

        self.GeneratorClearButton = Button(self.ButtonFrame, text="Clear All", padx=5, pady=3,command=self.clear_generators)
        self.GeneratorClearButton.grid(row=0, column=1)


        # Output Container
        self.OutputFrame = Frame(self.mainFrame, pady=15)
        self.OutputFrame.grid(row=3, sticky=W)

        self.OutputLabel = Label(self.OutputFrame, text="// Output", padx=5, pady=5, font=("Arial", 12, "bold"))
        self.OutputLabel.grid(row=0, column=0, sticky=W)

        self.OutputPreviewFrame = Frame(self.OutputFrame)
        self.OutputPreviewFrame.grid(row=1, column=0)

            # Scrollbar
        self.output_scrollbar = Scrollbar(self.OutputPreviewFrame)
        self.output_scrollbar.grid(row=0, column=3, rowspan=2, sticky=E + S + N)

            # Result Preview
        self.OutputPreview = Text(self.OutputPreviewFrame, height=5, padx=5, pady=5, width=49, yscrollcommand=self.output_scrollbar.set)
        self.OutputPreview.grid(row=0, column=0, columnspan=2, sticky=W+E)

        self.output_scrollbar.config(command=self.OutputPreview.yview)

            # Generate and Save As Buttons
        self.SaveButtonFrame = Frame(self.OutputFrame, padx=10, pady=10)
        self.SaveButtonFrame.grid(row=2, sticky=W)

        self.OutputGenerateButton = Button(self.SaveButtonFrame, text="Generate", padx=2, pady=2, font=("Arial", 10), command=self.generate_output)
        self.OutputGenerateButton.grid(row=0, column=0, sticky=W)

        self.OutputSaveButton = Button(self.SaveButtonFrame, text="Save As", padx=2, pady=2, font=("Arial", 10), command=self.save_file_as)
        self.OutputSaveButton.grid(row=0, column=1, sticky=W)

        self.OutputInfoLabel = Label(self.SaveButtonFrame, text="Unsaved!", font=("Arial", 10))
        self.OutputInfoLabel.grid(row=0, column=3, sticky=W)

        self.AuthorInfoLabel = Label(self.SaveButtonFrame, text=" Copyright (C) 2022 Adrian Urbaniak (FancySnacks) using GNU GPL 3.0 License", pady=10, font=("Arial", 7))
        self.AuthorInfoLabel.grid(row=1, column=0, columnspan=8, sticky=W)


        self.root.mainloop()



    # Detect mouse scroll and scroll the content
    # (canvas can't automatically assign mousewheel to scrollbars as it seems)
    def on_mousewheel(self, event):
        if self.mainFrame.winfo_height() > 765:
            self.canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")


    # Add New Generator
    def add_generator(self):
        self.generator_master.add_generator()

    def clear_generators(self):
        self.generator_master.clear_generators()


    def update_canvas(self):
        self.root.update_idletasks()
        self.canvas.configure(scrollregion=self.canvas.bbox('all'))


    # save output as a file
    def save_file_as(self):
        file = filedialog.asksaveasfile(initialdir="/",
                                        mode='w',
                                        defaultextension=".txt",
                                        title="Save As",
                                        filetypes=(("Text Files", "*.txt"),
                                                  ("All Files", "*.*")
                                                  ))
        if file:
            self.OutputInfoLabel.config(text="Saved!")
            file = open(file.name, "w")
            file.write(main.session.result)


    # generate results
    def generate_output(self):

        functions.generate_output(
                                self.generator_master,
                                self.num_of_results.get(),
                                self.separator.get(),
                                self.use_new_lines.get(),
                                self.start_with.get(),
                                self.end_with.get(),
                                self.match_file_length.get(),
                                self.s_start_with.get(),
                                self.s_end_with.get()
                                )


    def insert_output(self):
        self.OutputPreview.insert(0.0, "{0}{1}{2}".format(self.s_start_with.get(), main.session.result, self.s_end_with.get()))

    def output_clear(self):
        self.OutputPreview.delete(0.0, END)



# Contains all generators
class GeneratorContainer:

    def __init__(self, parent, master, window_root):
        self.root = parent
        self.master = master
        self.window_root = window_root
        self.generators = []

    def add_generator(self):
        new_generator = Generator(self, self.root, len(self.generators)+1, self.window_root)
        self.generators.append(new_generator)
        self.master.update_canvas()

    def remove_generator(self, index):
        self.generators.pop(index)
        print(self.generators)

    def clear_generators(self):
        for gen in self.generators:
            gen.remove_generator()

    def update_indexes(self):
        for i in range(0, len(self.generators)):
            self.generators[i].index.set(i+1)
            self.generators[i].index_label.config(text="[{}]".format(i+1))

    def get_shortest_file(self):
        lines = []
        for gen in self.generators:
            file = open(gen.filepath, "r")
            file_contents = file.readlines()
            num_of_lines = sum(1 for line in file_contents)
            lines.append(num_of_lines)
            file.close()
        return int(min(lines))



class Generator:

    def __init__(self, master, parent, index, window_root):
        self.master = master
        self.root = parent
        self.window_root = window_root
        self.index = StringVar(self.root)
        self.index.set(index)


        # Settings
        self.filepath = StringVar(self.root)
        self.filepath.set("")
        self.file_selected = BooleanVar(self.root)
        self.file_selected.set(False)

        self.input_type = StringVar(self.root)
        self.input_type.set("lowercase letters")

        self.options_list = ["lowercase letters",
                             "uppercase letters",
                             "numbers",
                             "random lowercase letters",
                             "random uppercase letters",
                             "random numbers",
                             "random symbols",
                             "random chars (aA123#/)",
                             "custom text file",
                             "custom input"
                             ]

        self.start_with = StringVar(self.root)
        self.start_with.set("")
        self.end_with = StringVar(self.root)
        self.end_with.set("")

        self.order_type = StringVar(self.root)
        self.order_type.set("Ordered (1 -> n)")
        self.order_list = ["Ordered (1 -> n)", "Random", "Random (Unique)"]

        self.custom_text = StringVar(self.root)
        self.custom_text.set("")

        self.num_of_lines = StringVar(self.root)
        self.num_of_lines.set("")


        # Widget
        self.Overlord = Frame(self.root, padx=5, pady=3)
        self.Overlord.pack()

        self.MainFrame = Frame(self.Overlord, padx=5, borderwidth=2, relief="groove", pady=10)
        self.MainFrame.grid(sticky=E+W)

        self.index_label = Label(self.MainFrame, text="[{}]".format(self.index.get()), padx=5, pady=12, font=("Arial", 10, "bold"))
        self.index_label.grid(row=0, column=0, sticky=W)

        self.input_label = Label(self.MainFrame, text="Input: ", padx=5,font=("Arial", 10))
        self.input_label.grid(row=0, column=1, sticky=W)

        # Input Dropdown Menu
        self.input_menu = OptionMenu(self.MainFrame, self.input_type, *self.options_list, command=self.switch)
        self.input_menu.grid(row=0, column=2, sticky=W)

        # Start / End With Settings
        self.startwith_Label = Label(self.MainFrame, text="Start with: ", padx=5,font=("Arial", 10))
        self.startwith_Label.grid(row=1, column=0, sticky=W, columnspan=2)

        self.startwith_Input = Entry(self.MainFrame, textvariable=self.start_with, width=8, font=("Arial", 10))
        self.startwith_Input.grid(row=1, column=2, sticky=W)

        self.endwith_Label = Label(self.MainFrame, text="End with: ", padx=5,font=("Arial", 10))
        self.endwith_Label.grid(row=1, column=3, sticky=W)

        self.endwith_Input = Entry(self.MainFrame, textvariable=self.end_with, width=8, font=("Arial", 10))
        self.endwith_Input.grid(row=1, column=4, sticky=W)

        # Custom File Path
        self.filepath_Frame = Frame(self.MainFrame, padx=5, pady=5)
        self.filepath_Frame.grid(row=2, column=0, columnspan=4, sticky=W)

        # V This should be deleted but keeping it for now as a reference V
        #self.filepath_label = Label(self.filepath_Frame, font=("Arial", 8))
        #self.filepath_label.grid(row=0, column=0, columnspan=2, sticky=W)

        self.filepath_entry = Entry(self.filepath_Frame, font=("Arial", 8), width=25)
        self.filepath_entry.grid(row=0, column=0, columnspan=2, sticky=W)
        self.filepath_entry.insert(0, "[FILEPATH]")

        self.order_menu = OptionMenu(self.filepath_Frame, self.order_type, *self.order_list)
        self.order_menu.grid(row=0, column=3, sticky=W)

        self.filepath_length = Label(self.filepath_Frame, textvariable=self.num_of_lines, font=("Arial", 8), padx=5)
        self.filepath_length.grid(row=0, column=2, sticky=W)

        self.filepath_Frame.grid_forget()

        # Custom Input
        self.custom_entry_Frame = Frame(self.MainFrame, padx=3, pady=5)
        self.custom_entry_Frame.grid(row=2, column=0, columnspan=4, sticky=W)

        self.custom_entry_label = Label(self.custom_entry_Frame, text="Text Input: ", font=("Arial", 10))
        self.custom_entry_label.grid(row=0, column=0, sticky=W)

        self.custom_entry = Entry(self.custom_entry_Frame, textvariable=self.custom_text)
        self.custom_entry.grid(row=0, column=1, sticky=W)

        self.custom_entry_Frame.grid_forget()

        # Browse File Button
        self.browse_button = Button(self.MainFrame, text="Browse...", font=("Arial", 10), state=DISABLED, command=self.browse_files)
        self.browse_button.grid(row=0, column=3, sticky=W)

        # Remove Generator Button
        self.remove_button_frame = Frame(self.MainFrame, padx=15)
        self.remove_button_frame.grid(row=0, column=4, sticky=W)

        self.remove_button = Button(self.remove_button_frame, text="X", fg="red", font=("Arial", 10), command=self.remove_generator)
        self.remove_button.grid(row=0, column=0, sticky=E)


    # Remove Generator From Container
    def remove_generator(self):
        self.Overlord.destroy()
        self.master.remove_generator(int(self.index.get())-1)
        self.master.update_indexes()
        del self


    # show filepath info widget if user wants to use custom text file
    def switch(self, choice):
        if choice == "custom text file":
            self.custom_entry_Frame.grid_forget()
            self.browse_button.config(state=NORMAL)
            self.insert_filepath(self.file_selected.get())
            self.master.master.Settings_FileEnd_Label.grid(row=1, column=2, sticky="E")
            self.master.master.Settings_FileEnd_Check.grid(row=1, column=3, sticky="E")
        elif choice == "custom input":
            self.custom_entry_Frame.grid(row=2, column=0, columnspan=4, sticky=W)
            self.browse_button.config(state=DISABLED)
            self.filepath_entry.delete(0, END)
            self.master.master.Settings_FileEnd_Label.grid_forget()
            self.master.master.Settings_FileEnd_Check.grid_forget()
        else:
            self.browse_button.config(state=DISABLED)
            self.filepath_entry.delete(0, END)
            self.filepath_Frame.grid_forget()
            self.custom_entry_Frame.grid_forget()
            self.master.master.Settings_FileEnd_Label.grid_forget()
            self.master.master.Settings_FileEnd_Check.grid_forget()


    # insert filepath info into a entry box
    def insert_filepath(self, not_empty):
        self.filepath_entry.delete(0, END)
        print(not_empty)
        if not_empty:
            self.filepath_entry.insert(0, self.filepath)
        else:
            self.filepath_entry.insert(0, "[FILEPATH]:")
        self.filepath_Frame.grid(row=2, column=0, columnspan=4, sticky=W)



    # select custom text file
    def browse_files(self):
        try:
            filename = filedialog.askopenfilename(initialdir="/",
                                                    title="Select a File",
                                                    filetypes=(("Text Files", "*.txt"),
                                                                ("All Files", "*.*")
                                                                ))
        except Exception as e:
            print(e)
        else:
            # save filepath
            if filename:
                self.filepath = filename
                self.file_selected.set(True)
                # line count
                file = open(self.filepath, "r")
                self.file_contents = file.readlines()
                self.content_lines_unique = self.file_contents
                self.num_of_lines.set("({0} lines)".format(str(sum(1 for line in self.file_contents))))
                file.close()
        finally:
            self.insert_filepath(self.file_selected.get())




class Session:

    def __init__(self, result, file_contents, content_lines_unique, num_of_lines, generators_unique, combinations_unique):
        self.result = result
        self.file_contents = file_contents
        self.content_lines_unique = content_lines_unique
        self.file_num_of_lines = num_of_lines
        self.generators_unique = generators_unique
        self.combinations_unique = combinations_unique

    def reset_values(self):
        self.result = ""
        self.file_contents = {}
        self.content_lines_unique = {}
        self.file_num_of_lines = 0
        self.generators_unique = []
        self.combinations_unique = []

    def insert_file_contents(self, generator):
        file = open(generator.filepath, "r")
        if generator.index.get() not in self.file_contents.keys():
            self.file_contents[generator.index.get()] = (file.readlines(), sum(1 for line in file))
            file.close()
        if generator.index.get() not in self.content_lines_unique.keys():
            file = open(generator.filepath, "r")
            self.content_lines_unique[generator.index.get()] = (file.readlines(), sum(1 for line in file))
            file.close()
        file.close()
        print(self.file_contents)
        print(self.content_lines_unique)

    def remove_line(self, generator, line_index):
        tuple = self.content_lines_unique[generator.index.get()]
        tuple[0].pop(line_index)
