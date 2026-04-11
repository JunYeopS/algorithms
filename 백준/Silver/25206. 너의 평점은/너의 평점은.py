import sys

input = sys.stdin.readline

grades = ["A+","A0","B+","B0","C+","C0","D+","D0"," ","F"]

def trans_module_grade(grade):
    for i in range(10):
        if grade == grades[i]:
            grade = 4.5 - (i*0.5)
    return float(grade)

overall = 0 
total = 0

for _ in range(20):
    tmp = list(input().strip().split(" "))
    
    if tmp[2] == "P":
        continue
    # 학점 x 과목 평점 / 학점 총합 
    overall += float(tmp[1]) * trans_module_grade(tmp[2])
    total += float(tmp[1])
    
print(overall / total)