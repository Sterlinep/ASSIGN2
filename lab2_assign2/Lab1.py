Name=(input("who are we calculating grade for? "))
labs=int(input('Enter the Lab grades? '))
labExams=int(input('Enter the EXAMS grade? '))
attendance=int(input('Enter the Attendance grade? '))
wg=labs*0.7+labExams*0.2+attendance*0.1
g=''
if wg>=90 and wg<=100:
    g='A'
elif wg>=80 and wg<90:
    g='B'
elif wg>=70 and wg<80:
    g='C'
elif wg>=60 and wg<70:
    g='D'
elif wg>=0 and wg<60:
    grade='F'
print(Name, 'has the letter grade of',g) 
