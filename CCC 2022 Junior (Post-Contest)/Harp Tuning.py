string = input()
current_instruction = ""
string += " "
for char in string:
    if char.isdigit() and string[string.index(char) + 1].isupper():
        current_instruction += char
        print(current_instruction.replace("+", " tighten ").replace("-", " loosen "))
        current_instruction = ""
    
    else:
        current_instruction += char

if current_instruction:
    print(current_instruction.replace("+", " tighten ").replace("-", " loosen "))