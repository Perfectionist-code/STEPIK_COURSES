A, C = 45, 43
for B in range(1, 100):
    if (not (A == B)) and ((A > B) <= (B > C)) and ((B > A) <= (C > B)):
        print(B)
