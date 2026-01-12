# Default parameters
import sys

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

    # app params
    continue_l = True

    print("School Search Application")
    prompt()

    while continue_l:

        input_u = input("Press Enter to run queries or type 'q' to quit: ")
        input_u = input_u.split(' ')
        input_u[0] = input_u[0].lower()
        if len(input_u) >= 3:
            input_u[2] = input_u[2].lower()

        if input_u[0] == 'q' or input_u[0] == 'quit':
            continue_l = False
            break
        elif input_u[0] == 's' or input_u[0] == 'student':
            if len(input_u) >= 3 and (input_u[2] == 'b'  or input_u[2] == 'bus'):
                query_lname_bus(input_u[1])
            else:
                if len(input_u) < 2:
                    print("Invalid input")
                    continue
                else:
                    query_lname(input_u[1])
        elif input_u[0] == 't' or input_u[0] == 'teacher':
            if len(input_u) < 2:
                    print("Invalid input")
                    continue
            else:
                query_teacher(input_u[1])
        elif input_u[0] == 'b' or input_u[0] == 'bus':
            if len(input_u) < 2:
                    print("Invalid input")
                    continue
            else:
                query_bus(input_u[1])
        elif input_u[0] == 'g' or input_u[0] == 'grade':
            if len(input_u) >= 3:
                if input_u[2] == 'h' or input_u[2] == 'high':
                    query_grade_highestGPA(input_u[1])
                elif input_u[2] == 'l' or input_u[2] == 'low':
                    query_grade_lowestGPA(input_u[1])
                else:
                    print("Invalid input")
                    continue
            else:
                if len(input_u) < 2:
                    print("Invalid input")
                    continue
                else:
                    query_grade(input_u[1])
        elif input_u[0] == 'a' or input_u[0] == 'average':
            if len(input_u) < 2:
                    print("Invalid input")
                    continue
            else:
                query_grade_averageGPA(input_u[1])
        elif input_u[0] == 'i' or input_u[0] == 'info':
            query_info()
        else:
            print("Invalid input")
            continue

#general functions
def prompt():
    print("Available commands:")
    print("• S[tudent] <lastname> [B[us]]")
    print("• T[eacher] <lastname>")
    print("• B[us] <number>")
    print("• G[rade] <number> [H[igh]|L[ow]]")
    print("• A[verage] <number>")
    print("• I[nfo]")
    print("• Q[uit]")

# Search functionality
def search(entryPosition, entry):
    indices = []
    l_index = 0

    try:
        with open(f_name, 'r') as file:
            for line in file:
                l = line.strip().split(',')
                if entryPosition < len(l) and l[entryPosition].lower() == entry.lower():
                    indices.append(l_index)
                l_index += 1
    except FileNotFoundError:
        print(f"Error: file '{f_name}' not found.")
        sys.exit(1)
    except OSError as e:
        print(f"I/O error while reading '{f_name}': {e}")
        sys.exit(1)

    return indices

def return_line(line):
    try:
        with open(f_name, 'r') as file:
            lines = file.readlines()
    except FileNotFoundError:
        print(f"Error: file '{f_name}' not found.")
        sys.exit(1)   # non-zero exit code indicates failure

    if 0 <= line < len(lines):
        return lines[line].strip().split(',')
    return None

        
def return_entry(line, entryPosition):
    l = return_line(line)
    if l is not None:
        return l[entryPosition]
    else:
        return None
    
# Search queries
def query_lname(last_name):
    indices = search(s_last_name, last_name)
    results = []
    for index in indices:
        s = "  "
        s += last_name + " " + return_entry(index, s_first_name) + ": Grade(" + return_entry(index, grade) + ") Classroom(" + return_entry(index, classroom) + ") Teacher(" + return_entry(index, t_last_name) + " " + return_entry(index, t_first_name) + ")"
        results.append(s)
    for result in results:
        print(result)

def query_lname_bus(last_name):
    indices = search(s_last_name, last_name)
    results = []
    for index in indices:
        s = "  "
        s += last_name + " " + return_entry(index, s_first_name) + ": Bus(" + return_entry(index, bus) + ")"
        results.append(s)
    for result in results:
        print(result)

def query_teacher(t_lname):
    indices = search(t_last_name, t_lname)
    results = []
    for index in indices:
        s = "  "
        s += return_entry(index, s_last_name) + " " + return_entry(index, s_first_name)
        results.append(s)
    for result in results:
        print(result)

def query_bus(bus_route):
    indices = search(bus, bus_route)
    results = []
    for index in indices:
        s = "  "
        s += return_entry(index, s_last_name) + " " + return_entry(index, s_first_name) + ": Grade(" + return_entry(index, grade) + ") Classroom(" + return_entry(index, classroom) + ")"
        results.append(s)
    for result in results:
        print(result)

def query_grade(grade_level):
    indices = search(grade, grade_level)
    results = []
    for index in indices:
        s = "  "
        s += return_entry(index, s_last_name) + " " + return_entry(index, s_first_name)
        results.append(s)
    for result in results:
        print(result)

def query_grade_averageGPA(grade_level):
    indices = search(grade, grade_level)
    result = 0
    for index in indices:
        result += float(return_entry(index, gpa))
    if len(indices) > 0:
        average = result / len(indices)
        print("  Grade " + grade_level + " Average GPA: " + "{:.2f}".format(average))

def query_grade_highestGPA(grade_level):
    indices = search(grade, grade_level)
    max = 0
    max_index = -1
    for index in indices:
        s_gpa = float(return_entry(index, gpa))
        if s_gpa > max:
            max = s_gpa
            max_index = index
    if max_index > 0:
        s = "  " + return_entry(max_index, s_last_name) + " " + return_entry(max_index, s_first_name) + ": GPA(" + return_entry(max_index, gpa) + ") Teacher(" + return_entry(max_index, t_last_name) + " " + return_entry(max_index, t_first_name) + ") Bus(" + return_entry(max_index, bus) + ")"
        print(s)

def query_grade_lowestGPA(grade_level):
    indices = search(grade, grade_level)
    min = 1000.0
    min_index = -1
    for index in indices:
        s_gpa = float(return_entry(index, gpa))
        if s_gpa < min:
            min = s_gpa
            min_index = index
    if min_index > 0:
        s = "  " + return_entry(min_index, s_last_name) + " " + return_entry(min_index, s_first_name) + ": GPA(" + return_entry(min_index, gpa) + ") Teacher(" + return_entry(min_index, t_last_name) + " " + return_entry(min_index, t_first_name) + ") Bus(" + return_entry(min_index, bus) + ")"
        print(s)

def query_info():
    for i in range(6):
        grade_level = str(i+1)
        indices = search(grade, grade_level)
        print(f"  Grade {grade_level}: {len(indices)} students")

#main entry point
main()