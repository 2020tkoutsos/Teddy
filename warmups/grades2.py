arr = [60,70,80,90,100]

def grade(letter_grade):
    letter_grade = []

        for num in arr:

            if num >= 90:
                letter_grade.append("A")
            elif num =< 60:
                letter_grade.append("F")
            elif 70 <= num <= 80:
                letter_grade.append("C")
            elif 80 <= num <= 90:
                letter_grade.append("B")
        print(letter_grade)
grade(arr)
