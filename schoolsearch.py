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
    #query_lname("STERBACK")
    #query_lname_bus("STERBACK")
    #query_teacher("HAMER")
    #query_bus("52")
    query_grade("3")
    query_grade_averageGPA("3")
    query_grade_highestGPA("3")

def search(entryPosition, entry):
    indices = []
    l_index = 0
    with open(f_name, 'r') as file:
        for line in file:
            # Process each line here
            l = line.strip().split(',') # Split by comma and remove whitespace
            if l[entryPosition] == entry:
                indices.append(l_index)
            l_index += 1
    return indices

def return_line(line):
    with open(f_name, 'r') as file:
        lines = file.readlines()
        if 0 <= line < len(lines):
            return lines[line].strip().split(',')
        else:
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
        if len(indices) > 1:
            s += return_entry(index, s_first_name) + " "
        s += last_name + ": Grade(" + return_entry(index, grade) + ") Classroom(" + return_entry(index, classroom) + ") Teacher(" + return_entry(index, t_first_name) + " " + return_entry(index, t_last_name) + ")"
        results.append(s)
    for result in results:
        print(result)

def query_lname_bus(last_name):
    indices = search(s_last_name, last_name)
    results = []
    for index in indices:
        s = "  "
        if len(indices) > 1:
            s += return_entry(index, s_first_name) + " "
        s += last_name + ": Bus(" + return_entry(index, bus) + ")"
        results.append(s)
    for result in results:
        print(result)

def query_teacher(t_lname):
    indices = search(t_last_name, t_lname)
    results = []
    for index in indices:
        s = "  "
        s += return_entry(index, s_first_name) + " " + return_entry(index, s_last_name)
        results.append(s)
    for result in results:
        print(result)

def query_bus(bus_route):
    indices = search(bus, bus_route)
    results = []
    for index in indices:
        s = "  "
        s += return_entry(index, s_first_name) + " " + return_entry(index, s_last_name)
        results.append(s)
    for result in results:
        print(result)

def query_grade(grade_level):
    indices = search(grade, grade_level)
    results = []
    for index in indices:
        s = "  "
        s += return_entry(index, s_first_name) + " " + return_entry(index, s_last_name)
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
        gpa = float(return_entry(index, gpa))
        if gpa > max:
            max = gpa
            max_index = index
    if max_index > 0:
        print("  Grade " + grade_level + " Highest GPA: " + return_entry(max_index, s_first_name) + " " + return_entry(max_index, s_last_name) + " ({:.2f})".format(max))

#main entry point
main()