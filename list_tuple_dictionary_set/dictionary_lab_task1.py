# student_data={
#     "divya":[100+50+75],
#     "jay":[75+100+80],
#     "shivam":[85+70+50]
# }
# # total=0
# for k,v in student_data.items():
#     print(k, '--->' ,v)


student_data={
    "divya@gmail.com":["divya","data scince",[100,50,75]],
    "jay@gmail.com":["jay","data analytics",[75,100,80]],
    "shivam@gmail.com":["shivam","python",[80,70,65]]
}

total=0
for k,v in student_data.items():
    print(k,'--->',v)
    if type(v)==list:
        for i in v:
            marks=v[2]
            total=sum(marks)
        print(total)
# student_data["total_marks"]=total
# print(student_data)


# student_data={
#     "divya@gmail.com":["divya","data scince",(100,50,75)],
#     "jay@gmail.com":["jay","data analytics",(75,100,80)],
#     "shivam@gmail.com":["shivam","python",(80,70,65)]
# }
# total=0
# for k,v in student_data.items():
#     for i in (v[2]):
#         total+=1
#     print(total)
        