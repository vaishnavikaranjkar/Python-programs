my_dict={}
grades={"Ana":"B","John":"A","Katy":"B"}
print(grades)

#add an entry
grades["Mary"]="A"
print(grades)

#test if a key in dict
isThere="John" in grades
print(isThere)

#delete a key
del(grades["Ana"])
print(grades)

#get all the keys - need to be unique and immutable
keys=grades.keys()
print(keys)

#get all the values
values=grades.values()
print(values)

#func to get input for dict
def get_grade(student, name_list, grade_list, course_list):
    i=name_list.index(student)
    grade=grade_list[i]
    course=course_list[i]
    return (course, grade) 