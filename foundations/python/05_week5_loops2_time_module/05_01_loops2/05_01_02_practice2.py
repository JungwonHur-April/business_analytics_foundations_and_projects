for i in range(4, 9):
    print(i, "th score (0~100):")
    score = int(input())
    if score < 0 or score > 100:
        print("error")
        break
