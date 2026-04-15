student_data={

    "name" : "nandini",
    "c_no":12345,
    "marks":[120,20,30]
}
total=0
for k,v in student_data.items():
    print(k,'--->',v)
    if type(v)==list:
        for i in v:
            total+=i
        print(total)

student_data["total_marks"]=total
print(student_data)