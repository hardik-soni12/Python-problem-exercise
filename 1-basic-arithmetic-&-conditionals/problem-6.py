'''
6) Read marks and print grade (A/B/C/Fail) based on ranges.
'''

def check_grade(marks):

    if marks >= 75 and marks <= 100:
        return "You Got 'A' Grade Congrats!"
    elif marks >= 60 and marks < 75:
        return "You Got 'B' Grade Congrats!"
    elif marks >= 40 and marks < 60:
        return "You Got 'C' Grade Congrats!"
    elif marks >= 0 and marks < 40:
        return "You 'Failed', sorry!"
    else:
        return f"{marks}, Please enter valid marks, in between 0 to 100."
    
marks = 88
print(check_grade(marks))