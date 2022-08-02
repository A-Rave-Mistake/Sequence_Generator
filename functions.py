import menus
import main
import string
import random


# constants
LOWERCASE = string.ascii_lowercase
UPPERCASE = string.ascii_uppercase
NUMBERS = string.digits
SYMBOLS = string.punctuation
CHARS = ''.join([UPPERCASE, LOWERCASE, NUMBERS, SYMBOLS])



def initialize():
    main.MainWindow = menus.MainWindow()


# generate sequence
def generate_output(generator_master, total_results, separator, use_new_lines, c_start_with, c_end_with, match_file_length, s_start_with, s_end_with):
    main.session = menus.Session()
    generator_master.master.output_clear()
    num_of_results = int(total_results) if not match_file_length else generator_master.get_shortest_file()
    index = 0
    out_isvalid = True

    # loop n times depending on how many combinations we want
    for i in range(0, num_of_results):
        index = i
        main.session.result += c_start_with

        # loop through every generator
        if generator_master.master.order.get() == "Ordered (1 -> n)":
            # loop through every generator, starting from index 1 to the last one
            for generator in generator_master.generators:
                generator_id = generator_master.generators[generator_master.generators.index(generator)]
                gen_startwith = generator_id.start_with.get()
                gen_endwith = generator_id.end_with.get()

                if construct_combination(generator_id, index, gen_startwith, gen_endwith) != None:
                    out_isvalid = True
                else:
                    out_isvalid = False

            if out_isvalid == True:
                main.session.result += "{separator}{comb_endwith}".format(
                    separator=separator if index != num_of_results - 1 else "", comb_endwith=c_end_with)

            if use_new_lines:
                main.session.result += "\n"

        # use random generator order
        elif generator_master.master.order.get() == "Random":
            for generator in generator_master.generators:
                generator_id = random.choice(generator_master.generators)
                gen_startwith = generator_id.start_with.get()
                gen_endwith = generator_id.end_with.get()

                if construct_combination(generator_id, index, gen_startwith, gen_endwith) != None:
                    out_isvalid = True
                else:
                    out_isvalid = False

            if out_isvalid == True:
                main.session.result += "{separator}{comb_endwith}".format(
                    separator=separator if index != num_of_results - 1 else "", comb_endwith=c_end_with)

            if use_new_lines:
                main.session.result += "\n"

        # use random generator order
        elif generator_master.master.order.get() == "Random (Sequence)":
            generator_id = random.choice(generator_master.generators)
            gen_startwith = generator_id.start_with.get()
            gen_endwith = generator_id.end_with.get()

            if construct_combination(generator_id, index, gen_startwith, gen_endwith) != None:
                out_isvalid = True
            else:
                out_isvalid = False

            if out_isvalid == True:
                main.session.result += "{separator}{comb_endwith}".format(
                    separator=separator if index != num_of_results - 1 else "", comb_endwith=c_end_with)

            if use_new_lines:
                main.session.result += "\n"

        # same as above elif but each generator can be used only once
        elif generator_master.master.order.get() == "Random (Unique)":
            main.session.generators_unique.clear()
            for i in range(0, len(generator_master.generators)):
                main.session.generators_unique.append(str(i))

            for generator in generator_master.generators:
                idg = str(random.choice(main.session.generators_unique))
                generator_id = generator_master.generators[int(idg)]
                gen_startwith = generator_id.start_with.get()
                gen_endwith = generator_id.end_with.get()

                if construct_combination(generator_id, index, gen_startwith, gen_endwith) != None:
                    out_isvalid = True
                else:
                    out_isvalid = False

                remove_generator(idg)

            if out_isvalid == True:
                main.session.result += "{separator}{comb_endwith}".format(
                    separator=separator if index != num_of_results - 1 else "", comb_endwith=c_end_with)

            if use_new_lines:
                main.session.result += "\n"


    insert_output(generator_master.master)
    main.session = None


def insert_output(master):
    master.insert_output()


def construct_combination(generator_id, index, gen_startwith, gen_endwith):
    output = str(get_input(generator_id, index)).replace("\n", "")

    if output != "None":
        stra = "{gen_startwith}{result}{gen_endwith}".format(gen_startwith = gen_startwith,
                                                                                    result = output,
                                                                                    gen_endwith = gen_endwith,
                                                                                    )
        main.session.result += stra
        return stra
    else:
        print("No such item exists")
        return None


# get input type of target generator and return result
def get_input(generator, index):

    input = generator.input_type.get()

    if input == "lowercase letters":
        try:
            return (LOWERCASE[index])
        except:
            return None

    elif input == "uppercase letters":
        try:
            return (UPPERCASE[index])
        except:
            return None

    elif input == "numbers":
        return index

    elif input == "random lowercase letters":
        return random.choice(LOWERCASE)

    elif input == "random uppercase letters":
        return random.choice(UPPERCASE)

    elif input == "random numbers":
        return random.randint(0,9)

    elif input == "random symbols":
        return random.choice(SYMBOLS)

    elif input == "random chars (aA123#/)":
        return CHARS[random.randint(0, len(CHARS)-1)]

    elif input == "custom text file":
        main.session.insert_file_contents(generator)

        if generator.order_type.get() == "Ordered (1 -> n)":
            return get_file_line(index)
        elif generator.order_type.get() == "Random":
            return get_random_line_from_file(False)
        else:
            return get_random_line_from_file(True)
    elif input == "custom input":
        return generator.custom_text.get()
    else:
        return None


def get_file_line(index):
    try:
        return main.session.file_contents[index]
    except Exception as e:
        print("No item with such index")
        return None

def get_random_line_from_file(b_no_duplicates):
    if b_no_duplicates:
        try:
            choice = random.choice(main.session.content_lines_unique)
            index = main.session.content_lines_unique.index(choice)
            content = main.session.file_contents[index]
            remove_line(index)
            return content
        except Exception as e:
            print("No item with such index")
            return None
    else:
        index = random.randint(0, main.session.num_of_lines-1)
        return main.session.file_contents[index]

def remove_line(index):
    main.session.remove_line(index)

def remove_generator(ref):
    main.session.generators_unique.remove(ref)

def toggle_check(b_show):
    if b_show:
        main.MainWindow.Settings_FileEnd_Label.grid(row=1, column=2, sticky="E")
        main.MainWindow.Settings_FileEnd_Check.grid(row=1, column=3, sticky="E")
    else:
        main.MainWindow.Settings_FileEnd_Label.grid_forget()
        main.MainWindow.Settings_FileEnd_Label.grid_forget()