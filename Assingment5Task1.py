

st_name = input ("Enter the student's name: ")
my_dict = {"Suraj":50, "Alice":85, "Shripad":49, "Teema":55}

result = my_dict.get(st_name)

if result is not None:
    print(st_name + "'s marks: ", result)

else:
    print("Student not found")