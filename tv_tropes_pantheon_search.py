# Created by Lapsem on TV Tropes
# Begin date: January 7th, 2024

# INFORMATION: The pantheon_data.csv file has a size limit of about 2.147 gigabytes ((2^31) - 1 bytes) -- which I've
# heard is the maximum that any Python variable can be.
# Additionally, LibreOffice only permits a spreadsheet with 1,048,576 rows, but it's very unlikely for THIS limit to
# ever be reached.

import tkinter
from tkinter import ttk


class UserInterface:
    def retrieve_data(self):
        # The purpose of this function is to grab the pantheon
        # data from a .csv file, and load it into a list of
        # lists to be loaded in whenever the user performs a
        # search.
        pantheon_table = open('pantheon_data.csv', 'r', encoding='utf-8')
        pantheon_table = pantheon_table.read().split('\n')

        sorted_table = []
        for x in pantheon_table:
            feeder_list = []
            sorted_table.append(feeder_list)
            if ', ' in x:
                for y in x.split('\"'):
                    if ', ' not in y:
                        for z in y.split(','):
                            if ('' != z) and (',' not in z):
                                feeder_list.append(z)
                for z in range(len(x.split('\"'))):
                    if (z % 2) == 1:
                        feeder_list.insert(z, x.split('\"')[z])
            else:
                for y in x.split(','):
                    feeder_list.append(y)

        finished_table = []
        for x in sorted_table:
            if len(x) == 7:
                feeder_list_2 = []
                finished_table.append(feeder_list_2)
                for y in x:
                    z = y.replace('NULL', '')
                    z = z.replace('’', '\'')
                    z = z.replace('\'\'', '\"')
                    feeder_list_2.append(z)

        return finished_table

    def __init__(self):
        self.sort_method = ''
        self.used_search_button = False
        self.pantheon_data = self.retrieve_data()
        self.completed_search = []
        self.table_entry_count = 0

        self.keyword_trope = ''
        self.keyword_deity = ''
        self.keyword_namespace = ''
        self.keyword_work = ''
        self.keyword_hall = ''
        self.keyword_house = ''

        self.sort_method_trope = 0
        self.sort_method_deity = 0
        self.sort_method_namespace = 0
        self.sort_method_work = 0
        self.sort_method_rank = 0
        self.sort_method_hall = 0
        self.sort_method_house = 0

        self.main_window = tkinter.Tk()
        self.main_window.title('TV Tropes Pantheon Search Database')
        self.main_window.iconphoto(False, tkinter.PhotoImage(file="icon.png"))
        self.main_window.geometry('1170x600')
        self.main_window.minsize(800, 600)
        self.main_window.config(bg='#3C4B5E')

        self.upper_frame = tkinter.Frame(self.main_window)
        self.uppermost_frame = tkinter.Frame(self.upper_frame)
        self.upper_left_frame = tkinter.Frame(self.upper_frame)
        self.upper_right_frame = tkinter.Frame(self.upper_frame)
        self.middle_frame = tkinter.Frame(self.main_window)
        self.label_frame = tkinter.Frame(self.middle_frame)
        self.button_frame = tkinter.Frame(self.middle_frame)
        self.bottom_frame = tkinter.Frame(self.main_window)

        self.label_information = tkinter.Label(
            self.uppermost_frame,
            width=45,
            text='Welcome to the TV Tropes Pantheon Search \nDatabase, coded in Python by Lapsem! (v1.1)\n\n'
                 'To use multiple keywords,\nseparate them with three semicolons (;;;). \n\n'
                 'Click the headers after performing \na search to sort the results!',
            font=('Liberation Mono', 8),
            bg='#709EBD',
            fg='#F9EC37'
        )

        self.frame_keyword_trope = tkinter.Frame(self.upper_left_frame)
        self.frame_keyword_deity = tkinter.Frame(self.upper_left_frame)
        self.frame_keyword_namespace = tkinter.Frame(self.upper_left_frame)
        self.frame_keyword_work = tkinter.Frame(self.upper_left_frame)
        self.frame_keyword_hall = tkinter.Frame(self.upper_left_frame)
        self.frame_keyword_house = tkinter.Frame(self.upper_left_frame)

        self.frame_checkbox_overdeity = tkinter.Frame(self.upper_right_frame)
        self.frame_checkbox_greater_god = tkinter.Frame(self.upper_right_frame)
        self.frame_checkbox_intermediate_god = tkinter.Frame(self.upper_right_frame)
        self.frame_checkbox_lesser_god = tkinter.Frame(self.upper_right_frame)
        self.frame_checkbox_demigod = tkinter.Frame(self.upper_right_frame)
        self.frame_checkbox_quasideity = tkinter.Frame(self.upper_right_frame)
        self.frame_checkbox_ambiguous_rank = tkinter.Frame(self.upper_right_frame)

        self.frame_search_button = tkinter.Frame(self.button_frame)

        self.label_keyword_trope = tkinter.Label(
            self.frame_keyword_trope,
            text='    Trope:',
            font=('Liberation Mono', 8)
        )
        self.entry_keyword_trope = tkinter.Entry(
            self.frame_keyword_trope,
            width=20
        )

        self.label_keyword_deity = tkinter.Label(
            self.frame_keyword_deity,
            text='    Deity:',
            font=('Liberation Mono', 8)
        )
        self.entry_keyword_deity = tkinter.Entry(
            self.frame_keyword_deity,
            width=20
        )

        self.label_keyword_namespace = tkinter.Label(
            self.frame_keyword_namespace,
            text='Namespace:',
            font=('Liberation Mono', 8)
        )
        self.entry_keyword_namespace = tkinter.Entry(
            self.frame_keyword_namespace,
            width=20
        )

        self.label_keyword_work = tkinter.Label(
            self.frame_keyword_work,
            text='     Work:',
            font=('Liberation Mono', 8)
        )
        self.entry_keyword_work = tkinter.Entry(
            self.frame_keyword_work,
            width=20
        )

        self.label_keyword_hall = tkinter.Label(
            self.frame_keyword_hall,
            text='     Hall:',
            font=('Liberation Mono', 8)
        )
        self.entry_keyword_hall = tkinter.Entry(
            self.frame_keyword_hall,
            width=20
        )

        self.label_keyword_house = tkinter.Label(
            self.frame_keyword_house,
            text='    House:',
            font=('Liberation Mono', 8)
        )
        self.entry_keyword_house = tkinter.Entry(
            self.frame_keyword_house,
            width=20
        )

        # This part governs the deity-rank checkboxes.
        self.var_checkbox_overdeity = tkinter.IntVar()
        self.var_checkbox_greater_god = tkinter.IntVar()
        self.var_checkbox_intermediate_god = tkinter.IntVar()
        self.var_checkbox_lesser_god = tkinter.IntVar()
        self.var_checkbox_demigod = tkinter.IntVar()
        self.var_checkbox_quasideity = tkinter.IntVar()
        self.var_checkbox_ambiguous_rank = tkinter.IntVar()

        self.var_checkbox_overdeity.set(1)
        self.var_checkbox_greater_god.set(1)
        self.var_checkbox_intermediate_god.set(1)
        self.var_checkbox_lesser_god.set(1)
        self.var_checkbox_demigod.set(1)
        self.var_checkbox_quasideity.set(1)
        self.var_checkbox_ambiguous_rank.set(1)

        self.checkbox_overdeity = tkinter.Checkbutton(
            self.frame_checkbox_overdeity,
            text='Overdeity       ',
            font=('Liberation Mono', 8),
            variable=self.var_checkbox_overdeity
        )
        self.checkbox_greater_god = tkinter.Checkbutton(
            self.frame_checkbox_greater_god,
            text='Greater God     ',
            font=('Liberation Mono', 8),
            variable=self.var_checkbox_greater_god
        )
        self.checkbox_intermediate_god = tkinter.Checkbutton(
            self.frame_checkbox_intermediate_god,
            text='Intermediate God',
            font=('Liberation Mono', 8),
            variable=self.var_checkbox_intermediate_god
        )
        self.checkbox_lesser_god = tkinter.Checkbutton(
            self.frame_checkbox_lesser_god,
            text='Lesser God      ',
            font=('Liberation Mono', 8),
            variable=self.var_checkbox_lesser_god
        )
        self.checkbox_demigod = tkinter.Checkbutton(
            self.frame_checkbox_demigod,
            text='Demigod         ',
            font=('Liberation Mono', 8),
            variable=self.var_checkbox_demigod
        )
        self.checkbox_quasideity = tkinter.Checkbutton(
            self.frame_checkbox_quasideity,
            text='Quasideity      ',
            font=('Liberation Mono', 8),
            variable=self.var_checkbox_quasideity
        )
        self.checkbox_ambiguous_rank = tkinter.Checkbutton(
            self.frame_checkbox_ambiguous_rank,
            text='Ambiguous Rank  ',
            font=('Liberation Mono', 8),
            variable=self.var_checkbox_ambiguous_rank
        )

        self.button_search = tkinter.Button(
            self.frame_search_button,
            text='Search',
            font=('Liberation Mono', 8),
            command=self.perform_search,
            bg='#F9BF29'
        )

        self.label_total = tkinter.Label(
            self.label_frame,
            text='Total results: '
        )
        self.results_count = tkinter.StringVar()
        self.results_count.set('0')
        self.display_total = tkinter.Label(
            self.label_frame,
            width=15,
            textvariable=self.results_count,
            font=('Liberation Mono', 8),
            fg='#3C4B5E'
        )

        self.label_keyword_trope.pack(side='left')
        self.entry_keyword_trope.pack(side='right')
        self.label_keyword_deity.pack(side='left')
        self.entry_keyword_deity.pack(side='right')
        self.label_keyword_namespace.pack(side='left')
        self.entry_keyword_namespace.pack(side='right')
        self.label_keyword_work.pack(side='left')
        self.entry_keyword_work.pack(side='right')
        self.label_keyword_hall.pack(side='left')
        self.entry_keyword_hall.pack(side='right')
        self.label_keyword_house.pack(side='left')
        self.entry_keyword_house.pack(side='right')

        self.button_search.pack(side='left')

        self.label_information.pack()

        self.frame_keyword_trope.pack()
        self.frame_keyword_deity.pack()
        self.frame_keyword_namespace.pack()
        self.frame_keyword_work.pack()
        self.frame_keyword_hall.pack()
        self.frame_keyword_house.pack()

        self.checkbox_overdeity.pack()
        self.checkbox_greater_god.pack()
        self.checkbox_intermediate_god.pack()
        self.checkbox_lesser_god.pack()
        self.checkbox_demigod.pack()
        self.checkbox_quasideity.pack()
        self.checkbox_ambiguous_rank.pack()

        self.frame_checkbox_overdeity.pack()
        self.frame_checkbox_greater_god.pack()
        self.frame_checkbox_intermediate_god.pack()
        self.frame_checkbox_lesser_god.pack()
        self.frame_checkbox_demigod.pack()
        self.frame_checkbox_quasideity.pack()
        self.frame_checkbox_ambiguous_rank.pack()

        self.frame_search_button.pack()

        self.uppermost_frame.pack(side='top')
        self.upper_frame.pack()
        self.upper_left_frame.pack(side='left')
        self.upper_right_frame.pack(side='right')
        self.display_total.pack(side='bottom')
        self.label_total.pack(side='bottom')
        self.label_frame.pack()
        self.button_frame.pack()
        self.middle_frame.pack()
        self.bottom_frame.pack()

        # For displaying the results of the search
        self.results_table = tkinter.ttk.Treeview(self.bottom_frame)
        self.results_table.pack(side='left')

        self.results_table['columns'] = ['trope', 'deity', 'namespace', 'work_name', 'rank', 'hall', 'house']
        self.results_table.column('#0', width=0, stretch=False)
        self.results_table.column('trope', anchor='w', width=130, minwidth=130)
        self.results_table.column('deity', anchor='w', width=130, minwidth=130)
        self.results_table.column('namespace', anchor='w', width=130, minwidth=130)
        self.results_table.column('work_name', anchor='w', width=130, minwidth=130)
        self.results_table.column('rank', anchor='w', width=130, minwidth=130)
        self.results_table.column('hall', anchor='w', width=130, minwidth=130)
        self.results_table.column('house', anchor='w', width=130, minwidth=130)

        # I would've had these headings all use the same function and pass different arguments to it, but it turns out
        # that Python didn't permit doing that for the 'command' bit for a heading.
        self.results_table.heading('#0', text='', anchor='center')
        self.results_table.heading('trope', text='Trope', anchor='center', command=self.sort_trope)
        self.results_table.heading('deity', text='Deity', anchor='center', command=self.sort_deity)
        self.results_table.heading('namespace', text='Namespace', anchor='center', command=self.sort_namespace)
        self.results_table.heading('work_name', text='Work Name', anchor='center', command=self.sort_work)
        self.results_table.heading('rank', text='Rank', anchor='center', command=self.sort_rank)
        self.results_table.heading('hall', text='Hall', anchor='center', command=self.sort_hall)
        self.results_table.heading('house', text='House', anchor='center', command=self.sort_house)

        self.scrollbar = ttk.Scrollbar(self.bottom_frame, orient=tkinter.VERTICAL, command=self.results_table.yview)
        self.results_table.configure(yscrollcommand=self.scrollbar.set)
        self.scrollbar.pack(side='right', fill=tkinter.Y)

        self.button_unsort = tkinter.Button(
            text='Reset Sort',
            font=('Liberation Mono', 8),
            command=self.reset_sort,
            bg='#F9EC37'
        )
        self.button_unsort.pack()

        tkinter.mainloop()

    def perform_search(self):
        preliminary_results = self.pantheon_data

        self.keyword_trope = str(self.entry_keyword_trope.get())
        self.keyword_deity = str(self.entry_keyword_deity.get())
        self.keyword_namespace = str(self.entry_keyword_namespace.get())
        self.keyword_work = str(self.entry_keyword_work.get())
        self.keyword_hall = str(self.entry_keyword_hall.get())
        self.keyword_house = str(self.entry_keyword_house.get())

        # This for loop takes the pantheon data and, if each entry doesn't meet the criteria for the search, it gets
        # removed, leaving only the result-entries that fill all of the provided criteria.
        sorted_results = []
        for x in range(0, 7):
            if x == 0 and self.keyword_trope != '' and self.keyword_trope != ';;;':
                for y in preliminary_results:
                    if ';;;' in self.keyword_trope:
                        for z in self.keyword_trope.split(';;;'):
                            if z in y[0]:
                                if y not in sorted_results:
                                    sorted_results.append(y)
                    else:
                        if self.keyword_trope in y[0]:
                            sorted_results.append(y)
                preliminary_results = sorted_results
                sorted_results = []
            elif x == 1 and self.keyword_deity != '' and self.keyword_deity != ';;;':
                for y in preliminary_results:
                    if ';;;' in self.keyword_deity:
                        for z in self.keyword_deity.split(';;;'):
                            if z in y[1]:
                                if y not in sorted_results:
                                    sorted_results.append(y)
                    else:
                        if self.keyword_deity in y[1]:
                            sorted_results.append(y)
                preliminary_results = sorted_results
                sorted_results = []
            elif x == 2 and self.keyword_namespace != '' and self.keyword_namespace != ';;;':
                for y in preliminary_results:
                    if ';;;' in self.keyword_namespace:
                        for z in self.keyword_namespace.split(';;;'):
                            if z in y[2]:
                                if y not in sorted_results:
                                    sorted_results.append(y)
                    else:
                        if self.keyword_namespace in y[2]:
                            sorted_results.append(y)
                preliminary_results = sorted_results
                sorted_results = []
            elif x == 3 and self.keyword_work != '' and self.keyword_work != ';;;':
                for y in preliminary_results:
                    if ';;;' in self.keyword_work:
                        for z in self.keyword_work.split(';;;'):
                            if z in y[3]:
                                if y not in sorted_results:
                                    sorted_results.append(y)
                    else:
                        if self.keyword_work in y[3]:
                            sorted_results.append(y)
                preliminary_results = sorted_results
                sorted_results = []
            elif x == 4:
                rank_keywords = []
                if self.var_checkbox_overdeity.get() == 1:
                    rank_keywords.append('Overdeity')
                if self.var_checkbox_greater_god.get() == 1:
                    rank_keywords.append('Greater God')
                if self.var_checkbox_intermediate_god.get() == 1:
                    rank_keywords.append('Intermediate God')
                if self.var_checkbox_lesser_god.get() == 1:
                    rank_keywords.append('Lesser God')
                if self.var_checkbox_demigod.get() == 1:
                    rank_keywords.append('Demigod')
                if self.var_checkbox_quasideity.get() == 1:
                    rank_keywords.append('Quasideity')
                if self.var_checkbox_ambiguous_rank.get() == 1:
                    rank_keywords.append('Ambiguous Rank')
                for y in preliminary_results:
                    if y[4] in rank_keywords:
                        sorted_results.append(y)
                preliminary_results = sorted_results
                sorted_results = []
            elif x == 5 and self.keyword_hall != '':
                for y in preliminary_results:
                    if ';;;' in self.keyword_hall:
                        if ';;;' == self.keyword_hall:
                            if y[5] == '':
                                sorted_results.append(y)
                        else:
                            for z in self.keyword_hall.split(';;;'):
                                if z in y[5]:
                                    if y not in sorted_results:
                                        sorted_results.append(y)
                    else:
                        if self.keyword_hall in y[5]:
                            sorted_results.append(y)
                preliminary_results = sorted_results
                sorted_results = []
            elif x == 6 and self.keyword_house != '' and self.keyword_house != ';;;':
                for y in preliminary_results:
                    if ';;;' in self.keyword_house:
                        for z in self.keyword_house.split(';;;'):
                            if z in y[6]:
                                if y not in sorted_results:
                                    sorted_results.append(y)
                    else:
                        if self.keyword_house in y[6]:
                            sorted_results.append(y)
                preliminary_results = sorted_results
                sorted_results = []
        self.completed_search = preliminary_results
        self.sort_results(True)

    def sort_results(self, used_search_button):
        if self.sort_method == 'trope':
            if not used_search_button:
                self.sort_method_trope = self.sort_method_trope + 1
                if self.sort_method_trope > 1:
                    self.sort_method_trope = 0

            def sort_trope(deity):
                if deity[0][0] == 'A' and deity[0][1].isupper():
                    return deity[0].lower().replace('a', '', 1)
                elif deity[0].startswith('An') and deity[0][2].isupper():
                    return deity[0].lower().replace('an', '', 1)
                elif deity[0].startswith('La') and deity[0][2].isupper():
                    return deity[0].lower().replace('la', '', 1)
                elif deity[0].startswith('The') and deity[0][3].isupper():
                    return deity[0].lower().replace('the', '', 1)
                elif deity[0].startswith('TabletopGame/'):
                    return deity[0].lower().replace('tabletopgame/', '', 1)
                elif deity[0].startswith('UsefulNotes/'):
                    return deity[0].lower().replace('usefulnotes/', '', 1)
                else:
                    return deity[0].lower()

            if self.sort_method_trope < 1:
                self.completed_search.sort(key=sort_trope, reverse=True)
            else:
                self.completed_search.sort(key=sort_trope)
        elif self.sort_method == 'deity':
            if not used_search_button:
                self.sort_method_deity = self.sort_method_deity + 1
                if self.sort_method_deity > 1:
                    self.sort_method_deity = 0

            def sort_deity(deity):
                if deity[1].startswith('The') and deity[0][3] == ' ':
                    return deity[1].lower().replace('the ', '', 1)
                elif ((deity[1].startswith('SCP-')
                       and (len(deity[1]) == 7 or (len(deity[1]) > 7 and deity[1][7] == '-')))
                      or deity[1].startswith('SCP-001')):
                    return deity[1].lower().replace('scp-', 'scp-0', 1)
                elif deity[1].startswith('.'):
                    return deity[1].lower().replace('.', '', 1)
                else:
                    return deity[1].lower()

            if self.sort_method_deity < 1:
                self.completed_search.sort(key=sort_deity, reverse=True)
            else:
                self.completed_search.sort(key=sort_deity)
        elif self.sort_method == 'namespace':
            if not used_search_button:
                self.sort_method_namespace = self.sort_method_namespace + 1
                if self.sort_method_namespace > 1:
                    self.sort_method_namespace = 0

            def sort_namespace(deity):
                if deity[2] == 'NULL':
                    return 0
                else:
                    return deity[2].lower()

            if self.sort_method_namespace < 1:
                self.completed_search.sort(key=sort_namespace, reverse=True)
            else:
                self.completed_search.sort(key=sort_namespace)
        elif self.sort_method == 'work_name':
            if not used_search_button:
                self.sort_method_work = self.sort_method_work + 1
                if self.sort_method_work > 1:
                    self.sort_method_work = 0

            def sort_work(deity):
                try:
                    if deity[3].startswith('The') and deity[3][3].isupper():
                        return deity[3].lower().replace('the', '', 1)
                    elif deity[3][0] == 'A' and deity[3][1].isupper():
                        return deity[3].lower().replace('a', '', 1)
                    elif deity[0].startswith('An') and deity[0][2].isupper():
                        return deity[0].lower().replace('an', '', 1)
                    else:
                        return deity[3].lower()
                except IndexError:
                    return '0'

            if self.sort_method_work < 1:
                self.completed_search.sort(key=sort_work, reverse=True)
            else:
                self.completed_search.sort(key=sort_work)
        elif self.sort_method == 'rank':
            if not used_search_button:
                self.sort_method_rank = self.sort_method_rank + 1
                if self.sort_method_rank > 1:
                    self.sort_method_rank = 0

            def sort_rank(deity):
                if deity[4] == 'Overdeity':
                    return 0
                elif deity[4] == 'Greater God':
                    return 1
                elif deity[4] == 'Intermediate God':
                    return 2
                elif deity[4] == 'Lesser God':
                    return 3
                elif deity[4] == 'Demigod':
                    return 4
                elif deity[4] == 'Quasideity':
                    return 5
                elif deity[4] == 'Ambiguous Rank':
                    return 6

            if self.sort_method_rank < 1:
                self.completed_search.sort(key=sort_rank, reverse=True)
            else:
                self.completed_search.sort(key=sort_rank)
        elif self.sort_method == 'hall':
            if not used_search_button:
                self.sort_method_hall = self.sort_method_hall + 1
                if self.sort_method_hall > 1:
                    self.sort_method_hall = 0

            def sort_hall(deity):
                return deity[5].lower()

            if self.sort_method_hall < 1:
                self.completed_search.sort(key=sort_hall, reverse=True)
            else:
                self.completed_search.sort(key=sort_hall)
        elif self.sort_method == 'house':
            if not used_search_button:
                self.sort_method_house = self.sort_method_house + 1
                if self.sort_method_house > 1:
                    self.sort_method_house = 0

            def sort_house(deity):
                return deity[6].lower()

            if self.sort_method_house < 1:
                self.completed_search.sort(key=sort_house, reverse=True)
            else:
                self.completed_search.sort(key=sort_house)
            pass
        self.display_results()

    def sort_trope(self):
        self.sort_method_deity = 0
        self.sort_method_namespace = 0
        self.sort_method_work = 0
        self.sort_method_rank = 0
        self.sort_method_hall = 0
        self.sort_method_house = 0

        self.sort_method = 'trope'
        self.sort_results(False)

    def sort_deity(self):
        self.sort_method_trope = 0
        self.sort_method_namespace = 0
        self.sort_method_work = 0
        self.sort_method_rank = 0
        self.sort_method_hall = 0
        self.sort_method_house = 0

        self.sort_method = 'deity'
        self.sort_results(False)

    def sort_namespace(self):
        self.sort_method_trope = 0
        self.sort_method_deity = 0
        self.sort_method_work = 0
        self.sort_method_rank = 0
        self.sort_method_hall = 0
        self.sort_method_house = 0

        self.sort_method = 'namespace'
        self.sort_results(False)

    def sort_work(self):
        self.sort_method_trope = 0
        self.sort_method_deity = 0
        self.sort_method_namespace = 0
        self.sort_method_rank = 0
        self.sort_method_hall = 0
        self.sort_method_house = 0

        self.sort_method = 'work_name'
        self.sort_results(False)

    def sort_rank(self):
        self.sort_method_trope = 0
        self.sort_method_deity = 0
        self.sort_method_namespace = 0
        self.sort_method_work = 0
        self.sort_method_hall = 0
        self.sort_method_house = 0

        self.sort_method = 'rank'
        self.sort_results(False)

    def sort_hall(self):
        self.sort_method_trope = 0
        self.sort_method_deity = 0
        self.sort_method_namespace = 0
        self.sort_method_work = 0
        self.sort_method_rank = 0
        self.sort_method_house = 0

        self.sort_method = 'hall'
        self.sort_results(False)

    def sort_house(self):
        self.sort_method_trope = 0
        self.sort_method_deity = 0
        self.sort_method_namespace = 0
        self.sort_method_work = 0
        self.sort_method_rank = 0
        self.sort_method_hall = 0

        self.sort_method = 'house'
        self.sort_results(False)

    def reset_sort(self):
        self.sort_method = ''
        self.sort_method_trope = 0
        self.sort_method_deity = 0
        self.sort_method_namespace = 0
        self.sort_method_work = 0
        self.sort_method_rank = 0
        self.sort_method_hall = 0
        self.sort_method_house = 0

        self.perform_search()

    def display_results(self):
        if self.table_entry_count > 0:
            for x in range(self.table_entry_count):
                self.results_table.delete(str(x))
        self.table_entry_count = 0
        for individual_entry in self.completed_search:
            self.results_table.insert('', tkinter.END, iid=str(self.table_entry_count), text=individual_entry[0],
                                      values=[individual_entry[0], individual_entry[1], individual_entry[2],
                                              individual_entry[3], individual_entry[4], individual_entry[5],
                                              individual_entry[6]])
            self.table_entry_count = self.table_entry_count + 1
        self.results_count.set(self.table_entry_count)


my_gui = UserInterface()
