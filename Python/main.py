# disctories 
student ={
    "name":"kunal",
    "Compnay":"Autoliter EnterPrice",
    "Phone":"8155901304",
    "Email":"kgs2002107@gmail.com",
    "password":"kgs2002107", 
    "Position":"Full Stack Developer", 
    "Teachnologies":["ReactJs", "NodeJs", "Django", "MySql", "Rest Api", "Ai-Ml Integration"]
}
"""
for key,value in student.items():
    text = "{}={}"
    print(text.format(key, value))
"""
""" 
listStudent = list(student.keys())
listStudent.sort()
newstudent={i:student[i] for i in listStudent}
print(newstudent, "listStudent")
"""
"""
n = int(input().strip())
if(n % 2 !=0):
    print("Weird")
elif (n%2 == 0  and 2<= n <=5):
    print("Weird")
elif (n%2 == 0  and 6<= n <=20):
    print("Weird")
elif (n%2 == 0  and n>20):
    print("Not Weird")
else :
    print("not weight")
"""
