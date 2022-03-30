'''
#
# This program builds an index of words and the pages on which they occur from a datafile "index_data.txt"
# It demonstrates the use of a complex data structure: a dictionary of sets
# from another file.

PUNC = ".,?!'-=+*&^%$#@()[]{}/\\\""
SPACE = " "
COMMA = ","
COLON = ":"


def main():
    index_entries = {}    # create an empty dictionary
    input_file = open("index_data.txt", "r")
    # extract the data from the file
    fields = extract_record(input_file)
    while len(fields) > 0:
        add_word(index_entries, fields[1], fields[0])
        fields = extract_record(input_file)
    input_file.close()

    # output the index listing
    print_index(index_entries)


def extract_record(infile):
    line = infile.readline()
    if line != "":                           # at then end if line is empty
        line = line.strip()
        fields = line.split(COLON)            # split into words - based on :
        page = int(fields[0])
        term = fields[1].strip()
        return [page, term]
    else:
        return []


def add_word(entries, term, page):
    # if term is already in the dictionary, just add the page to the set
    if term in entries:
        page_set = entries[term]
        page_set.add(page)
    # otherwise, create a new set that contains the page and add an entry
    else:
        page_set = set([page])
        entries[term] = page_set


def print_index(entries):
    for key in sorted(entries):
        print(key, end=SPACE)
        page_set = entries[key]
        first = True       # set a boolean flag to print first item
        for page in sorted(page_set):
            if first:
                print(page, end="")
                first = False
            else:
                print(COMMA, page, end="")  # print any subsequent items with a comma
        print()

main()



def upc_code_check(string_input, length_string):
    n = 0
    sum_check = 0
    while n < length_string - 1:
        digit = int(string_input[n])
        odd_even_check = n % 2
        print(odd_even_check)
        if odd_even_check == 0:
            sum_check += (digit * 3)
        else:
            sum_check += (digit * 1)
        n += 1
    last_digit_check = int(string_input[n])
    modulo_check = sum_check % 10
    print(sum_check)
    if modulo_check == 0:
        modulo_check = 0
    else:
        modulo_check = 10 - modulo_check
    if last_digit_check == modulo_check:
        print("-- code: %s valid UPC code." % string_input)
        return True, string_input
    else:
        return False, string_input


def main():
    string_input = str(input("input:"))
    length_string = len(string_input)
    result = upc_code_check(string_input, length_string)
    print(result[0])
    print(result[1])


if __name__ == '__main__':
    main()

'''

