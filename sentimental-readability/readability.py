import re

def word_count(text):
    return len(text.split())


def letter_count(text):
    return len(re.findall(r'[a-zA-Z]', text))

def sentence_count(text):
    return len(re.findall(r'[.!?]', text))

def calcGrade(text):
    words = word_count(text)
    letters = letter_count(text)
    sentences = sentence_count(text)
    L = 100 * letters / words
    S = 100 * sentences / words
    grade = 0.0588 * L - 0.296 * S - 15.8
    return grade

text = input("Text: ")

grade = calcGrade(text)
rounded_grade = round(grade)

if grade >= 16:
    print("Grade 16+")
elif grade < 1:
    print("Before Grade 1")
else:
    print(f"Grade {rounded_grade}")

