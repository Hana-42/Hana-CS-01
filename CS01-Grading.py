score = int(input('input you score :'))
mid = int(input('input you mid score :'))
final = int(input('input you final score :'))
A = (score+mid+final)
if (80 <= A <= 100):
    print("เกรดที่คุณได้คือ A")
elif (75 <= A < 80):
    print("เกรดที่คุณได้คือ B+")
elif (70 <= A < 75):
    print("เกรดที่คุณได้คือ B")
elif (65 <= A < 70):
    print("เกรดที่คุณได้คือ C+")
elif (60 <= A < 65):
    print("เกรดที่คุณได้คือ C")
elif (55 <= A < 60):
    print("เกรดที่คุณได้คือ D+")
elif (50 <= A < 55):
    print("เกรดที่คุณได้คือ D")
elif (0 <= A < 50):
    print("เกรดที่คุณได้คือ F")