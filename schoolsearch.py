# Default parameters

# Column indices
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
    print(search(s_last_name, "STERBACK"))

# file format: StLastName, StFirstName, Grade, Classroom, Bus, GPA, TLastName, TFirstName
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

#main entry point
main();