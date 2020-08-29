import string


# students saved as (student_name, list of lists)
def class_input(Units, Unit_name):
    # Units saved as [[Class name(WS1 1), day, time], [Class name (WS2 1), day, time]]
    row_num = 0
    file = open(str(Units), "r", encoding="UTF-8-sig")
    for line in file:
        line = line.split(',')
        if line[0] != str(Unit_name):
            row_num += 1
        else:
            break
    skip_line = 0
    full_class_list = []
    single_class_list = []
    single_class_list_counter = 0
    for word in line:
        if word == '':
            break
        if skip_line == 0:
            skip_line += 1
            continue
        if single_class_list_counter == 3:
            full_class_list.append(single_class_list)
            single_class_list_counter = 0
            single_class_list = []
        # strips punctuation and \n
        single_class_list.append(word.translate(str.maketrans('', '', string.punctuation)).strip())
        single_class_list_counter += 1
    full_class_list.append(single_class_list)
    file.close()
    return full_class_list

def student_input(Students):
    # turn student input into python readable list of lists
    student_table = []
    single_student_hour = []
    single_student_table = []
    student_names = []
    file = open(str(Students), "r", encoding="UTF-8-sig")
  
    for line in file:
        line = line.split(',')
        for word in line:
            try:
                int(word)
            except ValueError:
                if len(single_student_table) > 0:
                    student_table.append(single_student_table)
                    single_student_table = []
                student_names.append(word)

                break
                    
                    # run new function

            if int(word) == 0:
                single_student_hour.append(None)
            else:
                single_student_hour.append(word.strip())
        if (len(single_student_hour) == 5):
            single_student_table.append(single_student_hour)
            single_student_hour = []
    student_table.append(single_student_table)
    file.close()
    return student_table


print(class_input('Class input.csv', 'FIT2014'))
print(student_input('test student.csv'))






