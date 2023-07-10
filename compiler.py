#!/usr/bin/env python
# coding: utf-8

import csv
from collections import defaultdict


# LEXICAL ANALYZER -------------------------------------------------------------


def read_file(file_name: str) -> str:
    
    # open file as text_file
    with open(file_name, "r") as text_file: 
        
        # save all the data in the file in lines
        lines = text_file.read()
        
        # return lines converted to lowercase
        return lines.lower()


def get_csv(file_name: str) -> list:

    # initializing the following lists
    fields: list = []
    rows_list: list = []
    table: list = []

    # open the CSV file 
    with open(file_name, 'r') as csv_file:
        
        # save the data from csv_file to csv_reader
        csv_reader = csv.reader(csv_file)

        # save the fields row to fields
        fields = next(csv_reader)

        # get each row and save it to rows
        for row in csv_reader:
            rows_list.append(row)
 
    # add the fields to table
    table.append(fields)
    
    # get all the rows from rows_list and add them to table
    for row in rows_list:
        table.append(row)
         
    # returns the table
    return table


def get_dictionary(file_name: str) -> dict:

    # open the CSV file 
    with open(file_name, 'r') as csv_file:
        
        # get an ordered dictionary of the data
        ordered_dict = csv.DictReader(csv_file)
        
        # turn it into a common dictionary by putting it in a list
        into_dictionary = list(ordered_dict)
            
        # return the dictionary by itself
        return into_dictionary[0]


def java_0_DFSM(string: str) -> list:
    
    # variables to help parse 'string'
    current_token: str = ""
        
    token_list: list = []
    current_state: str = "0"
    previous_state: str = "0"
    comment_flag: bool = False
        
    table: list = get_csv("Java_0_DFSA_Table.csv")
    
    any_symbol: list = [" ", "\n"] + table[0][5:19]
        
    # this addresses an edge case without the need to add a new condition
    string += " "

    print("String being parsed: \n\n'" + string + "'")
    
    # going over each individual character in 'string'
    for character in string:

        previous_state = current_state

        
        # COMMENT AND OPERATORS  --------------------------------------------------------


        # if comment_flag is True and previous_state is 11
        if comment_flag and previous_state == "11":
            
            # keep current_state = 11
            current_state = table[12][1]
            
            # if the character is '*' add it to current_token 
            # and set current_state to 12 (go to state 12)
            if character == "*":
                current_token += character
                current_state = table[12][7]
                

            # or current_token is '*' and character is '/' 
            # add '/' to current_token and set current_state to 12 
            # now in state 12 we meet the condition that the comment has ended (go to state 12)
            elif current_token == "*" and character == "/":
                current_token += character
                current_state = table[12][7]
                
                
        # if current_token is '/' and character is anything except '*' (go to state 10)
        elif current_token == "/" and character != "*":
            
            # if current_token is not whitespace add current_token to token_list
            if current_token != " ":
                token_list.append(current_token)
        
            # reset current_token then add character to token_list
            # set current_state = state 10
            current_token = ""
            current_token += character
            current_state = table[10][1]
            
            
        # if current_token is '=' and character is not '=' (go to state 14)
        elif current_token == "=" and character != "=":
            
            # if current_token is not whitespace add current_token to token_list
            if current_token != " ":
                token_list.append(current_token)
        
            # reset current_token then add character to token_list
            # set current_state = state 14
            current_token = ""
            current_token += character
            current_state = table[14][1]
            
            
        # if current_token is '<' and character is not '=' (go to state 17)
        elif current_token == "<" and character != "=":
            
            # if current_token is not whitespace add current_token to token_list
            if current_token != " ":
                token_list.append(current_token)
            
            # reset current_token then add character to token_list
            # set current_state = state 17
            current_token = ""
            current_token += character
            current_state = table[17][1]
            
            
        # if current_token is '>' and character is not '=' (go to state 20)
        elif current_token == ">" and character != "=":
            
            # if current_token is not whitespace add current_token to token_list
            if current_token != " ":
                token_list.append(current_token)
            
            # reset current_token then add character to token_list
            # set current_state = state 20
            current_token = ""
            current_token += character
            current_state = table[20][1]
            
            
        # if current_token is '!' and character is not '=' (go to state 1)
        elif current_token == "!" and character != "=":
            
            # reset current_token then add character to token_list
            # set current_state = state 1
            current_token = ""
            current_state = table[23][1]


        # LETTERS, DIGITS, AND SYMBOLS IF LETTER/DIGIT ADJACENT ----------------------

    
        # if we have a character from any_symbol following a letter (go to state 3)
        elif character in any_symbol and previous_state == "2": 
            
            # if a character from any_symbol is encountered we add the current_token
            # to token_list and proceed with this state to get the symbol individually
            # so long as character is not whitespace
            if character != " ":
                token_list.append(current_token)
                current_token = ""
                current_token += character

            # we have a <variable identifier> set current_state = state 3
            current_state = table[3][1]


        # if we have a digit following a letter (go to state 2)
        elif character.isdigit() and current_state == "2":
            
            # add the character to current_token
            # set current_state = state 2
            current_token += character
            current_state = table[1][3] 

            
        # if we have a letter (state 2)
        elif character.isalpha():
            
            # add the character to current_token
            # set current_state = state 2 
            current_token += character
            current_state = table[1][3]


        # if we have a character from any_symbol following a digit (go to state 4)
        elif character in any_symbol and previous_state == "4": # state 4: digit
            
            # if a character from any_symbol is encountered we add the current_token
            # to token_list and proceed with this state to get the symbol individually
            # so long as character is not whitespace
            if character != " ":
                token_list.append(current_token)
                current_token = ""
                current_token += character
            
            # we have an <integer> set current_state = state 5
            current_state = table[5][1]


        # if we have a digit (go to state 4)
        elif character.isdigit():
            
            # add the digit to current_token
            # set current_state = state 4
            current_token += character
            current_state = table[1][4]
            
        
        # OPERATORS AND COMMENTS ---------------------------------------------------
        
        
        # if we have '/*' as a token and previous_state is 9 (go to state 11)
        elif current_token == "/" and character == "*" and previous_state == "9":
            
            # add the '*' to current_token
            # set current_state = state 11
            current_token += character
            current_state = table[10][7]
            

        # if we have '==' as a token and previous_state is 13 (go to state 15)
        elif current_token == "=" and character == "=" and previous_state == "13":
            
            # add the '=' to current_token
            # set current_state = state 15
            current_token += character 
            current_state = table[14][9]
            
            
        # if we have '<=' as a token and previous_state is 16 (go to state 18)
        elif current_token == "<" and character == "=" and previous_state == "16":
            
            # add the '=' to current_token
            # set current_state = state 18
            current_token += character 
            current_state = table[17][9]
            
            
        # if we have '>=' as a token and previous_state is 19 (go to state 21)
        elif current_token == ">" and character == "=" and previous_state == "19":
            
            # add the '=' to current_token
            # set current_state = state 21
            current_token += character 
            current_state = table[20][9]
            
            
        # if we have '!=' as a token and previous_state is 22 (go to state 23)
        elif current_token == "!" and character == "=" and previous_state == "22":
            
            # add the '=' to current_token
            # set current_state = state 23
            current_token += character 
            current_state = table[23][9]
            
            
        # if we have a '+' sign (go to state 6)
        elif character == "+": 
            
            # add '+' to current_token
            # set current_state = state 6
            current_token += character
            current_state = table[1][5]
            
            
        # if we have a '-' sign (go to state 7)
        elif character == "-": 
            
            # add '-' to current_token
            # set current_state = state 7
            current_token += character
            current_state = table[1][6]

        
        # if we have a '*' sign (go to state 8)
        elif character == "*": 
            
            # add '*' to current_token
            # set current_state = state 8
            current_token += character
            current_state = table[1][7]
            
        
        # if we have a '/' sign (go to state 9)
        elif character == "/": 
            
            # add '/' to current_token 
            # set current_state = state 9
            current_token += character
            current_state = table[1][8]
              
        
        # if we have a '=' sign (go to state 13)
        elif character == "=":
            
            # add '=' to current_token
            # set current_state = state 13
            current_token += character
            current_state = table[1][9]
            
        
        # if we have a '<' sign (go to state 16)
        elif character == "<":
            
            # add '<' to current_token
            # set current_state = state 16
            current_token += character
            current_state = table[1][10]
            
        
        # if we have a '>' sign (go to state 19)
        elif character == ">":
            
            # add '>' to current_token
            # set current_state = state 19
            current_token += character
            current_state = table[1][11]
            
            
        # if we have a '!' sign (go to state 22)
        elif character == "!":
            
            # add '!' to current_token
            # set current_state = state 22
            current_token += character
            current_state = table[1][12]
            
            
        # PARENTHESIS AND BRACES ---------------------------------------------------
        
        
        # if we have a '(' sign (go to state 24)
        elif character == "(": 
            
            # add '(' to current_token
            # set current_state = state 24
            current_token += character
            current_state = table[1][13]
            
        
        # if we have a ')' sign (go to state 25)
        elif character == ")": 
            
            # add ')' to current_token
            # set current_state = state 25
            current_token += character
            current_state = table[1][14]
           
        
        # if we have a '{' sign (go to state 26)
        elif character == "{": 
            
            # add '{' to current_token
            # set current_state = state 26
            current_token += character
            current_state = table[1][15]
            
            
        # if we have a '}' sign (go to state 27)
        elif character == "}": 
            
            # add '}' to current_token
            # set current_state = state 27
            current_token += character
            current_state = table[1][16]
            
        
        # COMMA AND SEMICOLON ------------------------------------------------------
        
        
        # if we have a ',' sign (go to state 28)
        elif character == ",": 
            
            # add ',' to current_token
            # set current_state = state 28
            current_token += character
            current_state = table[1][15]
            
            
        # if we have a ';' sign (go to state 29)
        elif character == ";": 
            
            # add ';' to current_token
            # set current_state = state 29
            current_token += character
            current_state = table[1][16]
        
            
        # SPACE AND UNIDENTIFIED SYMBOLS -------------------------------------------
            
            
        # if we have whitespace (go to state 0)
        elif character == " " or character == "\n":
            
            # set current_state = state 0
            current_state = table[1][1]
            
            
        # otherwise we have an unidentified symbol (go to state 1)
        else:
            
            # set current_state = state 1
            print(character)
            current_state = table[1][2]
            
            
        # CASE STATEMENTS FOR current_state ---------------------------------------
    
    
        # we check current_state and proceed accordingly
        match current_state:

            
            # case 0
            case "0":
                current_token = ""

                
            # case 1
            case "1":
                print("Illegal character")
                break

                
            # case 2 
            case "2":
                pass

                
            # case 3 ( [a-zA-Z] )
            case "3":
                if current_token != "\n":
                    token_list.append(current_token)
                
                current_token = ""
                current_state = "0"

                
            # case 4
            case "4":
                pass

                
            # case 5 ( [0-9] )
            case "5":
                if current_token != "\n":
                    token_list.append(current_token)
                    
                current_token = ""
                current_state = "0"

                
            # case 6 ( + )
            case "6":
                token_list.append(current_token)
                current_token = ""
                current_state = "0"
                
            
            # case 7 ( - )
            case "7":
                token_list.append(current_token)
                current_token = ""
                current_state = "0"
                
            
            # case 8 ( * )
            case "8":
                token_list.append(current_token)
                current_token = ""
                current_state = "0"
                
            
            # case 9 
            case "9":
                pass
                
            
            # case 10 ( / )
            case "10":
                if current_token != " ":
                    token_list.append(current_token)
                    
                current_token = ""
                current_state = "0"
                

            # case 11 ( /* )
            case "11":
                comment_flag = True
                current_token = ""
                current_state = "11"
                
                
            # case 12 ( */ )
            case "12":
                if current_token == "*/":
                    current_token = ""
                    current_state = "0"
                    comment_flag = False
                    
                else:
                    current_state = "11"
                    
                    
            # case 13
            case "13":
                pass

            
            # case 14 ( = )
            case "14":
                if current_token != " ":
                    token_list.append(current_token)
                    
                current_token = ""
                current_state = "0"
                    
            
            # case 15 ( == )
            case "15":
                token_list.append(current_token)
                current_token = ""
                current_state = "0"
                
                               
            # case 16
            case "16":
                pass

            
            # case 17 ( < )
            case "17":
                if current_token != " ":
                    token_list.append(current_token)
                    
                current_token = ""
                current_state = "0"
                    
            
            # case 18 ( <= )
            case "18":
                token_list.append(current_token)
                current_token = ""
                current_state = "0"
                
                
            # case 19
            case "19":
                pass


            # case 20 ( > )
            case "20":
                if current_token != " ":
                    token_list.append(current_token)
                    
                current_token = ""
                current_state = "0"
                    
            
            # case 21 ( >= )
            case "21":
                token_list.append(current_token)
                current_token = ""
                current_state = "0"
                
            
            # case 22
            case "22":
                pass

                
            # case 23 ( != )
            case "23":
                token_list.append(current_token)
                current_token = ""
                current_state = "0"
                
            
            # case 24 ( ( )
            case "24":
                token_list.append(current_token)
                current_token = ""
                current_state = "0"
                
            
            # case 25 ( ) )
            case "25":
                token_list.append(current_token)
                current_token = ""
                current_state = "0"
                
                
            # case 26 ( { )
            case "26":
                token_list.append(current_token)
                current_token = ""
                current_state = "0"
                
            
            # case 27 ( } )
            case "27":
                token_list.append(current_token)
                current_token = ""
                current_state = "0"
                
                
            # case 28 ( , )
            case "28":
                token_list.append(current_token)
                current_token = ""
                current_state = "0"
                
            
            # case 29 ( ; )
            case "29":
                token_list.append(current_token)
                current_token = ""
                current_state = "0"
                
                
            # unidentified case
            case unknown_command:
                print("Invalid input.")
            
    
        # END OF CASE STATEMENTS FOR current_state -------------------------------
    
    # return the token list
    return token_list


def token_classification_table(token_list: list) -> list:
    
    # variables to help get the token_classification_list
    token_clasification_list: list = []
    program_name_flag: bool = False
    constant_type_flag: bool = False
    
    # get the dictionaries of reserved words and symbols
    reserved: list = get_dictionary("Reserved_Words.csv")
    symbols: list = get_dictionary("Reserved_Symbols.csv")
    
    
    # we go through each token 
    for token in token_list:
        
        
        # first we check if the token is a reserved word
        if token in reserved:
            
            # if so we add it to the token_classification_list along with the classification
            token_clasification_list.append((token, reserved[token]))
            
            # the token is 'class' we turn on program_name_flag
            if token == "class":
                program_name_flag = True
                
            # the token is 'const' we turn on constant_type_flag
            if token == "const":
                constant_type_flag = True
            
        
        # if program_name_flag is on we add the token and the clasification to token_classification_list
        # and turn off program_name_flag
        elif program_name_flag:
            token_clasification_list.append((token, "<program name>"))
            program_name_flag = False
    
        
        # we check that constant_type_flag is on and that the token is not a digit or symbol
        # and we add the token and the clasification to token_classification_list
        elif (constant_type_flag and token not in symbols and not token.isdigit()):
            token_clasification_list.append((token, "<constant identifier>"))
            
        
        # if the token is a digit add the token and the clasification to token_classification_list
        elif token.isdigit():
            token_clasification_list.append((token, "<numeric literal>"))
            
            
        # if the token has letters and digits add the token and the clasification to token_classification_list
        elif token.isalnum():
            token_clasification_list.append((token, "<variable identifier>"))
            
            
        # if the token is a reserved symbol
        elif token in symbols:
            
            # if the token is a semicolon we turn off the constant_type_flag
            if token == ";":
                constant_type_flag = False
            
            # we add the token and the clasification to token_classification_list
            token_clasification_list.append((token, symbols[token]))
            
        # otherwise print that the token has no classification 
        else:
            print("No classification for:", token)

    
    # return the token classification list
    return token_clasification_list


def write_to_csv(token_clasification_list: list) -> list:
    
    # create the CSV file
    with open('Token_Classification_Table.csv', 'w', newline='') as csv_file:
            
        # get the header
        header = ["Token", "Classification"]
        
        # set up our writer object
        writer = csv.writer(csv_file)
        
        # write the header to the CSV file
        writer.writerow(header)
        
        # we write each token along with its classification in the CSV file
        for token in token_clasification_list:
            writer.writerow([token[0], token[1]])


def token_symbol_table(token_classification_list: list) -> list:
    
    # some variables to help us
    row_number: int = 1
    temp_counter: int = 1
    address_counter: int = 0
    token_classifications: list = []
    symbol_table: list = []
    variable_list: list = []
    header: list = []
    
    # we get the classifications
    token_classifications = token_classification_list
        
    # we create the symbol table
    with open("Symbol_Table.csv", 'w', newline='') as csv_file:
            
        # we get the header
        header = [" ", "Symbol", "Classification", "Value", "Address", "Segment"]
        
        # we get our writer object
        writer = csv.writer(csv_file)
        
        
        # we get the data needed into the table ----------------------------------------------
        
        
        # we go through every token in the classification table
        for index, token in enumerate(token_classifications):
            
            
            # if the token is classified as the program name
            if token[1] == "<program name>":
                
                # we add the data to symbol_table
                symbol_table.append(list([row_number, token[0], token[1], "", "0", "CS"]))
                
            
            # if the token is a variable or constant identifier and the next token is a '='
            # and the token next to it is a digit
            if ((token[1] == "<variable identifier>" or token[1] == "<constant identifier>") and 
                  token_classifications[index + 1][0] == "=" and 
                  token_classifications[index + 2][0].isdigit()):

                # add the variable to the list
                variable_list.append(token[0])
                
                # we add the data to symbol_table
                symbol_table.append(
                    list([row_number, token[0], token[1], token_classifications[index + 2][0], "0", "DS"])
                )
                
                
            # if the token is a variable identifier and the token is not in variable_list
            elif token[1] == "<variable identifier>" and token[0] not in variable_list:
                variable_list.append(token[0])
                
                # we add the data to symbol_table
                symbol_table.append(list([row_number, token[0], token[1], "", "0", "DS"]))

            
            # if the token is a numeric literal and the token before it is not a '='
            if token[1] == "<numeric literal>" and token_classifications[index - 1][0] != "=":
                
                # we add the data to symbol_table
                symbol_table.append(list([row_number, token[0], token[1], token[0], "0", "DS"]))
                
                
            # if the token is an addition, subtraction, mupltiplication, or division operator
            if (token[1] == "<addition operator>" or 
                token[1] == "<multiplication operator>" or
                token[1] == "<subtraction operator>" or 
                token[1] == "<division operator>" or 
                token[1] == "<equality operator>" or
                token[1] == "<less than operator>" or 
                token[1] == "<greater than operator>" or
                token[1] == "<less than equals operator>" or
                token[1] == "<greater than equals operator>" or 
                token[1] == "<not equals operator>"):
                
                # we add the data to symbol_table
                symbol_table.append(list([row_number, "temp", "", "", "" ""]))

                
        # now we format the symbol table -------------------------------------------------
        
        
        # we check every row for the ones holding 'temp' in the symbol column
        for row in symbol_table:
            if "temp" in row[1]:
                
                # we move the row to the bottom of the list
                symbol_table.append(symbol_table.pop(symbol_table.index(row)))
                
        
        # if a row has 'temp' in the symbol column we modify them by adding numbers 
        # to them in ascending order
        for row in symbol_table:
            if "temp" in row[1]:
                row[1] += str(temp_counter)
                temp_counter += 1
                
                
        # we add the proper row number to each row
        for row in symbol_table:
            row[0] = row_number
            row_number += 1
            
            
        # we fix the address counter to each row
        for row in symbol_table[1:]:
            if row[4] == "0":
                row[4] = address_counter
                address_counter += 2
                
                
        # we insert the header at the top 
        symbol_table.insert(0, header)
        
        
        # finally we write the table to the CSV file
        for row in symbol_table:
            writer.writerow(row)


def lexical_analyzer(file_name: str) -> str:
    
    # we declare the variable for the token list and its classifications, and the symbol table
    token_list: list = []
    token_classifications: list = []
    symbol_table: list = []

    # we save the token list and its classifications to the respective variable 
    token_list = java_0_DFSM(read_file(file_name))
    token_classifications = token_classification_table(token_list)
    
    # we write the token classification and symbol table into a CSV file
    write_to_csv(token_classifications)
    symbol_table = token_symbol_table(token_classifications)
    
    return "Lexical analysis complete."



# SYNTAX ANALYZER -------------------------------------------------------------



def read_operator_table(file_name: str):
    
    table: list = []
    
    # open CSV file 
    with open(file_name, 'r') as csv_file:
        
        # set up reader
        csv_reader = csv.reader(csv_file)
            
        # go over the rows and add them to table
        for row in csv_reader:
            table.append(row)

        # return table
        return table


def read_symbol_table(file_name: str, column_name: str) -> list:

    # set up variables 
    columns: defaultdict = defaultdict(list)
    symbol_list: list = []

    # open CSV file 
    with open(file_name, 'r') as csv_file:

        # set up reader
        csv_reader = csv.DictReader(csv_file)

        # go over the rows
        for row in csv_reader: 
            
            # create a dict that has the row category as a key and the items
            # in the row category are placed in a list as the value
            for (key, value) in row.items(): 
                columns[key].append(value) 
    
    # make a list of the values
    symbol_list = columns[column_name]
    
    # return symbol_list
    return symbol_list


def read_token_list(file_name: str) -> list:
    
    # set up variables 
    columns: defaultdict = defaultdict(list)
    token_list: list = []

    # open CSV file 
    with open(file_name, 'r') as csv_file:

        # set up reader
        csv_reader = csv.DictReader(csv_file)

        # go over the rows
        for row in csv_reader: 
            
            # create a dict that has the row category as a key and the items
            # in the row category are placed in a list as the value
            for (key, value) in row.items(): 
                columns[key].append(value) 
        
    # make a list of the values
    token_list = columns["Token"]
    
    # return token_list
    return token_list


def push_down_automata(symbols_list: list) -> list: # symbols: list
    
    # quad variables
    quad: list = [0, 0, 0, 0]
    quad_list: list = []
    quad_flag: bool = True
    quad_counter: int = 2
        
    # PDA stack
    push_down_stack: list = ["^"]
        
    # terminals stacks
    symbol_terminals: list = []
    pda_terminals: list = []
        
    # symbols lists
    symbols: list = symbols_list
    symbols_initial: list = []
    symbols_initial = symbols.copy()
    
    # symbols current
    symbols_current_left: int = 0
        
    # operators
    current_operator: str = push_down_stack[0]
    previous_operator: str = push_down_stack[0]
        
    # indexes
    current_index: int = 0
    previous_index: int = 0
        
    # index counters
    index_counter_current: int = 0
    index_counter_previous: int = 0
        
    # index tracker
    print_index_tracker: int = 0
        
    # temporary tracking
    current_temporary: str = ""
    temp_counter: int = 1
    temp_string: str = "temp"
        
    # PDA handling
    pushing_down: bool = True
    break_flag: int = 0
    length_count: int = 0
    
    # fix-up stack and variables
    fix_up_list: list = []
    label_counter: int = 1
    label_string: str = "L"
    label_current: str = ""
        
    # left brace
    current_left_brace: str = ""
    left_brace_tracker: int = 0
        
    # class name
    class_name_tracker: int = 0
    class_name: str = ""
    
    # reserved
    reserved: list = list(get_dictionary("Reserved_Words.csv"))[1:]
    reserved_tracker: int = 0
        
    # current if and then
    symbols_current_if: int = 0
    symbols_current_then: int = 0
    pda_current_if: int = 0
    pda_current_then: int = 0
        
    # then flag
    then_flag: int = 0
        
    # precedence table
    precedence_table: list = read_operator_table("Operator_Precedence_Table.csv")
        
    # operators
    operator_list: list = precedence_table[0]

        
    # ------------------------------------------------------ START -------------------------------------------------

    
    while pushing_down:
        
        # we keep track index and character (symbol)
        for index, symbol in enumerate(symbols):
            
            # check if symbol is in operator list or not
            if symbol not in operator_list:

                push_down_stack.append(symbol)

            elif symbol in operator_list:

                previous_operator = current_operator
                current_operator = symbol
                
                push_down_stack.append(symbol)
                symbol_terminals.append(symbol)
                
                if symbol == "print":
                    print_index_tracker = symbol_terminals.index(symbol)
             
            # check to see if symbol is a special case
            if symbol == "class":
                class_name_tracker = 1
                
            if class_name_tracker:
                class_name = symbols[index + 1]
                class_name_tracker = 0
                
            if symbol == "{":
                current_left_brace = symbol
                left_brace_tracker = index
                
            if symbol in reserved:
                reserved_tracker = index
                
            if symbol == "if":
                symbols_current_if = index
                
            if symbol == "then":
                symbols_current_then = index
                
            # get current and precious index
            current_index = operator_list.index(current_operator)
            previous_index = operator_list.index(previous_operator)
            

            # ----------------------------------------- ( < ) -------------------------------------------------------
            
            # if we have '<' then we yield precedence
            if precedence_table[previous_index][current_index] == "<":
                pass

            # ----------------------------------------- ( = ) -------------------------------------------------------
                
            # if we have '=' then we have equal precedence so we continue
            elif precedence_table[previous_index][current_index] == "=":
                
                # pop parenthesis if no longer needed in Symbols
                if symbol_terminals[symbol_terminals.index(current_operator) - 1] == "(" and current_operator == ")":
                    break

            # ----------------------------------------- ( > ) -------------------------------------------------------
                    
            # if we have '>' then we take precedence
            elif precedence_table[previous_index][current_index] == ">":
                pda_terminals = symbol_terminals.copy()
                
                # setting index_counters
                index_counter_current = index
                index_counter_previous = index - 2
            
                # ------------------------------------ SYMBOLS ------------------------------------------------------
                
                # we go through the tokens in the range and move backwards to avoid index issues
                for item in reversed(range(index_counter_previous - 1, index)):
                    
                    symbols.pop(item)
                    index_counter_current -= 1
                    
                # we add the temp token to symbols
                symbols.insert(index_counter_current, temp_string + str(temp_counter))
                
                # we update current_temporary
                current_temporary = temp_string + str(temp_counter)
                
                # pop parenthesis if no longer needed in Symbols
                symbol_terminals.remove(previous_operator)
                if symbol_terminals[symbol_terminals.index(current_operator) - 1] == "(" and current_operator == ")":
                    symbols.pop(symbols.index(current_temporary) - 1)
                    symbols.pop(symbols.index(current_temporary) + 1) 
                
                # ----------------------------------------- PDA -------------------------------------------------------
                
                # setting index_counters
                index_counter_current = index
                index_counter_previous = index - 2
                
                # we go through the tokens in the range and move backwards to avoid index issues
                for item in reversed(range(index_counter_previous, index + 1)):
        
                    # if quad_flag is on then we create the flag by adjusting the counter
                    # to get the correct index for the quad list
                    if quad_flag:
                        quad[quad_counter] = push_down_stack[item]
                    
                        if quad_counter == 2:
                            quad_counter -= 2
                        
                        elif quad_counter == 0:
                            quad_counter += 1
                            
                        elif quad_counter == 1:
                            quad_counter += 2
                            
                        elif quad_counter == 3:
                            quad_flag = False      
                            
                    # pop item
                    push_down_stack.pop(item)
                    
                    # update current index counter
                    index_counter_current -= 1
                    
                # ------------------------------ COMPARISSON OPERATORS -----------------------------------------------
                
                # we update the quad assuming we have comparisson operators
                if "<" in quad:
                    quad[quad_counter] = '-'
                    temp_counter -= 1
                    
                elif ">" in quad:
                    quad[quad_counter] = '-'
                    temp_counter -= 1
                
                elif "=" not in quad:
                    quad[quad_counter] = temp_string + str(temp_counter)
                    
                else:
                    quad[quad_counter] = "-"
                
                # add temp to PDA
                push_down_stack.insert(index_counter_current + 1, temp_string + str(temp_counter))
                
                # pop parenthesis if no longer needed in PDA
                pda_terminals.remove(previous_operator)
                if pda_terminals[pda_terminals.index(current_operator) - 1] == "(" and current_operator == ")":
                    push_down_stack.pop(push_down_stack.index(current_temporary) - 1)
                    push_down_stack.pop(push_down_stack.index(current_temporary) + 1)            
                    
                # input quad rearrangement
                if quad[2] == 'input':
                    quad[0] = quad[2]
                    quad[2] = "-"
                    temp_counter -= 1
                
                # reset variables for next round
                quad_counter = 2
                temp_counter += 1
                quad_list.append(quad)
                quad = [0, 0, 0, 0]
                
                # -------------------------------- IF THEN statement is complete ----------------------------------------------------
    
                # REMOVE items between if then
                for if_index, item in enumerate(pda_terminals):
                
                    if item == "if":
                        pda_current_if = if_index
                        
                    elif item == "then":
                        pda_current_then = if_index
        
                # check PDA rweminals and remove items from symbols
                if len(pda_terminals) >= 3 and (pda_terminals[pda_current_if] == "if" and pda_terminals[pda_current_then] == "then"):

                    symbols_current_then -= 2
                
                    for item in reversed(range(symbols_current_if + 1, symbols_current_then)):
                        symbols.pop(item)
                        then_flag = 1
                    
                    # if we have a symbol 'then' we add the corresponding quad along with fix-up labels
                    if then_flag:
                        quad_list.append(["THEN", label_string + str(label_counter), previous_operator, "-"])
                        fix_up_list.append(label_string + str(label_counter))
                        label_current = label_string + str(label_counter)
                        label_counter += 1
                
                # ---------------------------------------- END current loop ---------------------------------------------------------
                break
                
                
            # if no operators remain inbetween the braces pop anything between them and themselves
            elif current_operator == "}" and current_left_brace:
                
                # pop if then from stack
                for if_index, item in enumerate(symbol_terminals):
                
                    if item == "if":
                        symbols_current_if = if_index
                        
                    elif item == "then":
                        symbols_current_then = if_index
                        
                    elif item == "{":
                        symbols_current_left = if_index
                
                # pop the print string
                if len(symbol_terminals) >= 4 and (symbol_terminals[print_index_tracker] == "print" and symbol_terminals[-2] == "{" and symbol_terminals[-1] == "}"):
                    
                    for item in range(left_brace_tracker + 1, index):
                        quad_list.append(["print", symbols[item], "-", "-"])
            
                # if then popped from the stack
                if fix_up_list and (symbol_terminals[symbols_current_if] == "if" and symbol_terminals[symbols_current_then] == "then"):
                    
                    quad_list.append([fix_up_list[-1], "-", "-", "-"])
                    fix_up_list.pop()
                
                # remove empty braces
                if current_operator == symbol_terminals[-1] and symbols_current_left:
                    
                    for item in reversed(range(left_brace_tracker, index + 1)):
                        symbols.pop(item)
                        
                    break
                    
                # remove final if then if it exists
                if symbol_terminals[symbols_current_left] == "{" and symbol_terminals[-1] == "}":
                    
                    for item in reversed(range(left_brace_tracker, index + 1)):
                        symbols.pop(item)
                    
                    
            # no conditions are met
            else:
                pass
                
            length_count = len(symbols)
            
        # -------------------------- End of for loop -------------------------------
        
        # if the length of symbols didn't change add 1 to break_flag
        if len(symbols) == length_count:
            break_flag += 1
            
        # reset variables for next round
        previous_operator = push_down_stack[0]
        current_operator = push_down_stack[0]
        push_down_stack = ["^"]
        symbol_terminals = []
        pda_terminals =[]
        current_temporary = ""
        current_left_brace = ""
        print_index_tracker = 0
        then_flag = 0
        symbols_current_if = 0
        symbols_current_then = 0
        symbols_current_left = 0
        
        # if length of symbols is 2 or less we have popped all the items
        if len(symbols) <= 2:
            pushing_down = False
        
        # a back-up measure to avoid infinite loops
        if break_flag == 10:
            break
            
    # ---------------------------------- End of while loop --------------------------
    
    # return the quads generated
    return quad_list


def assembly_code(quad_list: list) -> list:
    
    # set up variables needed
    assembly_list: list = []
    fix_up_list: list = []
    current_code: list = []
    string: str = ""

    # we run through all the quads and get the assembly equivalent
    for quad in quad_list:
        
        # we check the operator and only look at the first 3 items in the quad
        for operator in quad[:-3]:
            
            if operator[0] == "L":
                operator = "L"
            
            match operator:
                
                case "+":
                    
                    current_code.append("mov ax, [" + quad[1] + "]")
                    current_code.append("add ax, [" + quad[2] + "]")
                    current_code.append("mov [" + quad[3] + "], ax")
                    
                    assembly_list.append(current_code)
                
                case "-":
                    
                    current_code.append("mov ax, [" + quad[1] + "]")
                    current_code.append("sub ax, [" + quad[2] + "]")
                    current_code.append("mov [" + quad[3] + "], ax")
                    
                    assembly_list.append(current_code)
                    
                case "*":
                    
                    current_code.append("mov ax, [" + quad[1] + "]")
                    
                    if quad[2].isdigit():
                        current_code.append("imul ax, [" + quad[2] + "]")
                        
                    else:
                        current_code.append("mul byte [" + quad[2] + "]")
                        
                    current_code.append("mov [" + quad[3] + "], ax")
                    assembly_list.append(current_code)
                
                case "/":
                    
                    current_code.append("mov dx, 0")
                    current_code.append("mov ax, [" + quad[1] + "]")
                    current_code.append("mov bx, [" + quad[2] + "]")
                    current_code.append("div bx")
                    current_code.append("mov [" + quad[3] + "], ax")
                    
                    assembly_list.append(current_code)
                
                case "=":
                    current_code.append("mov ax, [" + quad[2] + "]")
                    current_code.append("mov [" + quad[1] + "], ax")
                    current_code.append("nop")
                    
                    assembly_list.append(current_code)
                
                case ">":
                    
                    current_code.append("mov ax, [" + quad[1] + "]")
                    current_code.append("cmp ax, [" + quad[2] + "]")
                    
                    assembly_list.append(current_code)
                
                case "<":
                    
                    current_code.append("mov ax, [" + quad[1] + "]")
                    current_code.append("cmp ax, [" + quad[2] + "]")
                    
                    assembly_list.append(current_code)
                
                case "<=":
                    
                    current_code.append("mov ax, [" + quad[1] + "]")
                    current_code.append("cmp ax, [" + quad[2] + "]")
                    
                    assembly_list.append(current_code)
                    
                case ">=":
                    
                    current_code.append("mov ax, [" + quad[1] + "]")
                    current_code.append("cmp ax, [" + quad[2] + "]")
                    
                    assembly_list.append(current_code)
                    
                case "==":
                    
                    current_code.append("mov ax, [" + quad[1] + "]")
                    current_code.append("cmp ax, [" + quad[2] + "]")
                    
                    assembly_list.append(current_code)
                    
                case "!=":
                    
                    current_code.append("mov ax, [" + quad[1] + "]")
                    current_code.append("cmp ax, [" + quad[2] + "]")
                    
                    assembly_list.append(current_code)
                
                case "THEN":
                    
                    if quad[2] == "<":
                        string = "JGE"
                        
                    elif quad[2] == ">":
                        string = "JLE"
                        
                    elif quad[2] == "<=":
                        string = "JG"
                        
                    elif quad[2] == ">=":
                        string = "JL"
                        
                    elif quad[2] == "==":
                        string = "JNE"
                        
                    elif quad[2] == "!=":
                        string = "JE"
                    
                    current_code.append(string + " " + quad[1])
                    
                    fix_up_list.append(quad[1])
                    assembly_list.append(current_code)
                    
                case "L":
                    print("LABEL")
                    current_code.append("nop")
                    assembly_list.append(current_code)
                    
                case "print":
                    current_code.append("mov ax, [" + quad[1] + "]")
                    current_code.append("mov [" + quad[1] + "], ax")
                    current_code.append("mov ax, [" + quad[1] + "]")
                    current_code.append("call ConvertIntegerToString")
                    current_code.append("mov ax, [" + quad[1] + "]")
                    current_code.append("mov eax, 4")
                    current_code.append("mov ebx, 1")
                    current_code.append("mov ecx, Result")
                    current_code.append("mov edx, ResultEnd")
                    current_code.append("int 80h")
                    
                    assembly_list.append(current_code)
                    
                case "input":
                    current_code.append("call PrintString")
                    current_code.append("call GetAnInteger")
                    current_code.append("mov ax, [ReadInt]")
                    current_code.append("mov ["+ quad[1] + "], ax")
                    
                    assembly_list.append(current_code)
                
                case unknown_command:
                    print("Invalid Input:", operator)
                    
        # reset variable for next round
        current_code = []
        
        # --------------------------------- End nested loop -----------------------------------
        
    return [assembly_list, fix_up_list]


def assembly_literals(assembly: list) -> list:
    
    
    # bracket variables
    left_bracket: str = "["
    right_bracket: str = "]"
    left_bracket_index: int = 0
    right_bracket_index: int = 0
    
    # str variables
    list_to_str: list = []
    str_replacement: str = ""
        
    # assembly variables
    assembly_list: list = []
    assembly_list.extend(assembly[0])
    assembly_counter: int = 0
        
    # fix up variables
    fix_up_counter: int = 0
    fix_up_list: list = []
        
    # jump variables
    jump_list: list = ["JG", "JL", "JGE", "JLE", "JNE", "JE"]
        
    # body variable
    body_list: list = []

    # if the list with the asm code includes also has a fix-up list then initialize it
    if len(assembly) > 1:
        fix_up_list = assembly[1]
    
    
    # we go through the list that contains all the lists
    for index_1, assembly in enumerate(assembly_list):
        
        # we go through each individual list
        for index_2, item in enumerate(assembly):
            
            # get the index for the left and right bracket
            try:
                left_bracket_index = item.index(left_bracket)
                right_bracket_index = item.index(right_bracket)
                
            # item doesn't have brackets
            except (IndexError, ValueError) as error:
                pass
            
            # we check if the asm code is greater than the left bracket index that an actual left bracket exists in item
            if len(item) > left_bracket_index and "[" in item:
                
                # we go through each character in the asm code
                for character in range(left_bracket_index + 1, right_bracket_index):
                    
                    # if we have a digit then we remove the brackets and end the loop
                    if item[character].isdigit():
            
                        list_to_str.extend(assembly_list[index_1][index_2])
                
                        list_to_str.remove(left_bracket)
                        list_to_str.remove(right_bracket)
                        str_replacement = "".join(list_to_str)
                        
                        assembly[index_2] = str_replacement
                        
                        break
                        
                    # otherwise we end the loop
                    else:
                        break
                        
                # we reset the variables for the next round
                list_to_str = []
                str_replacement = ""
                
            # otherwise we have a NOP operation
            else:
                pass
            
        # --------------------------------- End nested loop -----------------------------------

    # we go through all the lists in the assembly_list
    for assembly in assembly_list:
        
        # we go through each item in assembly
        for item in assembly:
            
            # if NOT nop add space to the code and make it it's own list
            if item != "nop":
                body_list.append(["    " + item])
                
            # if nop is the only asm code in assembly it means we have items in the fix-up list
            elif len(assembly) == 1 and item == "nop":
                body_list.append([fix_up_list[fix_up_counter][-2:] + ":", item])
                fix_up_counter += 1
            
            # otherwise add add space to the asm code
            else:
                body_list.append(["    " + item])
                
    # we go through body_list
    for index, item in enumerate(body_list):
        
        # if we have a label we hoin it with nop
        if item[0][0] == "L":
            body_list[index] = [" ".join(item)]
        
    # we return body_list
    return body_list


# ----------------------------- generate the asm file --------------------------------------------------------


def initialize_asm_file(file_name: str):
    
    with open(file_name, "w") as file:
        
        file.write("")


def write_asm_header(file_name: str):
    
    asm_keys: str = ""
    program_name: str = read_symbol_table("Symbol_Table.csv", "Symbol")[0]
    
    asm_keys = f"""; Program Name: {program_name}\n
sys_exit    equ 1
sys_read    equ 3
sys_write   equ 4
stdin       equ 0   ; default keyboard
stdout      equ 1   ; default terminal screen
stderr      equ 3
"""
    
    with open(file_name, "a") as file:
        
        file.write(asm_keys)


def write_asm_data(file_name: str):
    
    asm_keys: str = ""
    symbol_table_tokens: list = read_symbol_table("Symbol_Table.csv", "Symbol")[1:]
    symbol_table_values: list = read_symbol_table("Symbol_Table.csv", "Value")[1:]
    symbol_table_combo: list = []
        
    symbol_table_combo = list(zip(symbol_table_tokens,symbol_table_values))
    
    constant_header: str = """; -------------------------- declare constants ------------------------------------

section .data
    
"""
        
    constant: str = """    userMsg         db     'Input an integer: '
    lenUserMsg      equ    $-userMsg
    newline         db     0xA
    Ten             DW     10
    num times 6     db     'ABCDEF'
    numEnd          equ    $-num
    Result          db     'Output: '
    ResultValue     db     'aaaaa'
                    db     0xA
    ResultEnd       equ    $-Result
    
"""
    
    # we fill out the variables from the symbol table along with their values
    with open(file_name, "a") as file:

        file.write("\n")
        file.write(constant_header)
    
        for item in symbol_table_combo:

            if item[1] == "":
                file.write("    " + (item[0] + "\tdw\t00000\n"))
                
            elif item[0].isdigit():
                    pass
            
            else:
                file.write("    " + item[0] + "\tdw\t" + item[1] + "\n")

        file.write(constant)


def write_asm_bss(file_name: str):
    
    variables: str = """; -------------------------- uninitiated variables ---------------------------------

section .bss 

    TempChar        RESB    1
    testchar        RESB    1
    ReadInt         RESW    1              
    tempint         RESW    1             
    negflag         RESB    1 
    
"""
    
    with open(file_name, "a") as file:
        
        file.write(variables)


def write_asm_start(file_name: str):
    
    main_program: str = """; -------------------------- Main program -----------------------------------------

global _start   

section .text

_start:
    
"""
        
    with open(file_name, "a") as file:
        
        file.write(main_program)


def write_asm_body(file_name: str):
    
    quads: list = push_down_automata(read_token_list("Token_Classification_Table.csv"))
    assembly_list: list = assembly_code(quads)
    body: list = assembly_literals(assembly_list)
    
    with open(file_name, "a") as file:
        
        for line in body:
        
            for item in line:
                    
                file.write(item + "\n")


def write_asm_end(file_name: str):
    
    end_program: str = """; -------------------------- End Main program -------------------------------------

fini:

    mov eax,sys_exit
    xor ebx,ebx
    int 80h
    
"""
    with open(file_name, "a") as file:
        
        file.write(end_program)


def write_asm_functions(file_name: str):
    
    functions: str = """; ------------------------------ functions ----------------------------------------

PrintString:

    push    ax
    push    dx

    ; prompt user

    mov eax, 4
    mov ebx, 1
    mov ecx, userMsg
    mov edx, lenUserMsg
    int 80h
    pop     dx 
    pop     ax
    ret

;End PrintString


GetAnInteger:

    mov eax, 3
    mov ebx, 2
    mov ecx, num
    mov edx, 6
    int 0x80


;End GetAnInteger


ConvertStringToInteger:

    mov ax, 0
    mov [ReadInt], ax 
    mov ecx, num
    mov bx,0
    mov bl, byte [ecx]

Next:

    sub bl,'0'
    mov ax, [ReadInt]
    mov dx, 10
    mul dx
    add ax, bx
    mov [ReadInt], ax
    mov bx, 0
    add ecx, 1
    mov bl, byte[ecx]
    cmp bl,0xA
    jne Next
    ret

;End GetAnInteger


ConvertIntegerToString:

    mov ebx, ResultValue + 4

ConvertLoop:

    sub dx,dx
    mov cx,10
    div cx
    add dl,'0'
    mov [ebx], dl
    dec ebx
    cmp ebx, ResultValue
    jge ConvertLoop

    ret

; End ConvertIntegerToString
"""
        
    with open(file_name, "a") as file:
        
        file.write(functions)


# ----------------------------- asm file complete -------------------------------------------------


def write_asm_file(file_name: str):
    
    # run all the functions to create the asm file
    initialize_asm_file(file_name)
    write_asm_header(file_name)
    write_asm_data(file_name)
    write_asm_bss(file_name)
    write_asm_start(file_name)
    write_asm_body(file_name)
    write_asm_end(file_name)
    write_asm_functions(file_name)
    
    print(f".asm file created. File name is: {file_name}")


def syntax_analyzer(file_name: str) -> str:

    # run all the functions to get the output of the suntax analyzer
    quads = push_down_automata(read_token_list("Token_Classification_Table.csv"))
    assembly_list = assembly_code(quads)
    
    write_asm_file(file_name)
    
    return "Syntax Analysis Complete."


if __name__ == "__main__":
    lexical_analyzer("java_0_code_text_file.txt")
    syntax_analyzer("asm_file.txt")