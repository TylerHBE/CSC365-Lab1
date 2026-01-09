# Default parameters

# Column indices
# file format: StLastName, StFirstName, Grade, Classroom, Bus, GPA, TLastName, TFirstName
s_last_name = 0
s_first_name = 1
grade = 2
classroom = 3
bus = 4
gpa = 5
t_last_name = 6
t_first_name = 7

# file params
f_name = 'students.txt'

def main():
    print(return_line(search(s_last_name, "STERBACK")))

def search(entryPosition, entry):
    l_index = 0
    with open(f_name, 'r') as file:
        for line in file:
            # Process each line here
            l = line.strip().split(',') # Split by comma and remove whitespace
            if l[entryPosition] == entry:
                return l_index
            l_index += 1
    return -1

def return_line(line):
    with open(f_name, 'r') as file:
        lines = file.readlines()
        if 0 <= line < len(lines):
            return lines[line].strip().split(',')
        else:
            return None

#main entry point
main();