"""ספרייה של פונקציות אלגוריתמיות נוצרה על ידי תלמיד א ותלמיד ב"""

def welcome():
    """פונקציה לברכה"""
    print("ברוכים הבאים לספרייה של פונקציות אלגוריתמיות!")
def factorial(n):
    """פונקציה רקורסיבית לחישוב פקטוריאל"""
    if n < 0:
        return "אין פקטוריאל למספרים שליליים"
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)
if __name__ == "__main__":
    welcome()
number = int(input("הכנס מספר שלם כדי לחשב את הפקטוריאל שלו: "))
result = factorial(number)
print(f"הפקטוריאל של {number} הוא: {result}")
