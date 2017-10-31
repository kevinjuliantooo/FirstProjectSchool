"""
Kevin
1-09-2017
Reading list program: Show user unread/read books and to add new book as well.
https://github.com/CP1404-JCUS/a1-reading-list-kevinjuliantooo
"""
def menu(data):
    """
    Menu function will show menu section. program will ask user to input. Will open before main function
    :param data: data taken from data.csv file
    :return:
    """
    print("Menu:")
    print("R - List required books ")
    print("C - List completed books")
    print("A - Add new book")
    print("M - Mark a book as completed")
    print("Q - Quit")
    user_input = input(">>>").upper()

    while True:
        book_list = [] # All book in this list
        complete_list = [] # Only complete book
        reading_list = [] # Only reading book

        if user_input == "Q": # The program will end after return data
            return data

        elif user_input == "R": # Show all list in reading_list
            x = 0
            print("Requires books:")
            for each in data:
                data_split = each.split(",")
                book_list.append(data_split)
                if 'r' in data_split[3]:
                    print("\t {:2}. {:50} by {:20} {:2} pages".format(x, data_split[0], data_split[1], data_split[2]))
                x += 1
            print(book_list)
            print(reading_list)
            menu(data) # Back to menu function and bring data

        elif user_input == "C": # Show all list in complete_list
            print("Requires books:")
            x = 0
            for each in data:
                data_split = each.split(",")
                book_list.append(data_split)
                if 'c' in data_split[3]:
                    print("\t {:2}. {:50} by {:20} {:2} pages".format(x, data_split[0], data_split[1], data_split[2]))
                x += 1
            menu(data) # Back to menu function and bring data

        elif user_input == "A": # Ask user to do input
            input_a() # Go to input_a function
            menu(data) #Back to menu function and bring data

        elif user_input == "M": # Ask user to mark reading_list to be complete
            book_pages = [] # All page will putted here
            x = 0
            for each in data:
                data_split = each.split(",")
                book_list.append(data_split)
                if 'r\n' in data_split[3]:
                    reading_list.append(int(x))

            if len(reading_list) == 0:
                print("No required books")
            else:
                print("Requires books:")
                for each in data:
                    data_split = each.split(",")
                    book_list.append(data_split)
                    if 'r\n' in data_split[3]:
                        print("\t {:2}. {:50} by {:20} {:2} pages".format(x, data_split[0], data_split[1], data_split[2]))
                        book_pages.append(data_split[2])
                    elif 'c' in data_split[3]:
                        complete_list.append(int(x))
                    x += 1
                    total_pages = [int(i) for i in book_pages] # Change all string from pages became interger
                print("Total pages for {} books: {}".format(len(reading_list), sum(total_pages)))
                print("Enter the number of a book to mark as completed")
                print(data_split)
                print(complete_list)
                new_mark = []
                while True:
                    try:
                        number_mark = int(input(">>>"))
                        if number_mark in complete_list:
                            print("That book is already completed")
                            break
                        else:
                            print("{} by {} marked as completed".format(book_list[number_mark][0], book_list[number_mark][1]))
                            print("{},{},{},{}".format(book_list[number_mark][0], book_list[number_mark][1], book_list[number_mark][2], 'c'))
                            book_list[number_mark][3] = 'c\n'
                            print(book_list)
                            OUTFILE = open("data.csv", "w")
                            for i in book_list:
                                OUTFILE.write("{},{},{},{}".format(i[0],i[1],i[2],i[3]))
                            #other_data = OUTFILE.readlines()

                            # for i in book_list:
                            #     print(*i, file=OUTFILE, sep= "")

                            OUTFILE.close()

                            #print(len(book_list))
                            #print(reading_list)
                            #for i in book_list:
                            #   if number_mark in new_mark:
                            #       i[3] = 'c'
                            print(book_list)
                            break
                    except ValueError:
                        print("Invalid input; enter a valid number")

                    #new_mark = open("data.csv", "n")
                    #x = 0
                    #for each in data:
                    #data_split = each.split(",")
                        #book_list.append(data_split)
                        #if x == number_mark:
                    #print("{},{},{},{}".format(data_split[0], data_split[1], data_split[2], 'c').replace('r', 'c'), file=new_mark)
                            #print(book_list)
                            #x += 1
                    #data_split[number_mark][3] = 'c'
                    #print(data_split)
                    #break
            menu(data) # Back to menu function and bring data
        else:
            print("Invalid menu choice")
        break

def input_a():
    """
     This function ask user to input title, author, and pages
    :return:
    """

    add_book = [] #Title, Author, and Pages saves here
    while True:
        title = input("Title: ")
        if title == "":
            print("Input can not be blank")
        else:
            add_book.append(title)
            break
    while True:
        author = input("Author: ")
        if author == "":
            print("Input can not be blank")
        else:
            add_book.append(author)
            break
    while True:
        try:
            page = int(input("Pages: "))
            if page < 0:
                print("Number must be >= 0")
                # new_file.wr("{},{},{},r".format(new_book[0], new_book[1], new_book[2]))
        except ValueError:
            print("Invalid input; enter a valid number")
        else:
            add_book.append(page)
            new_book = open("data.csv", "a")
            print("{},{},{},r".format(title, author, page), file=new_book)
            print("{} by {}, ({} pages) added to reading list".format(title, author, page))
            break




def main():
    """
    Main function. everything start from here and end here
    :return:
    """
    TEXTFILE = open("data.csv", "r")
    data = TEXTFILE.readlines()
    TEXTFILE.close()
    print("Hello Guys")
    name = str(input("What is your name??"))
    print("Welcome {}".format(name))
    menu(data)
    print("{} books saved to books.csv".format(len(data)))
    print("Have a nice day :)")
    # Program ended here

main()