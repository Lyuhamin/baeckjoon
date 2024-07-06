num1, num2, num3 = map(int, input().split())

def price(num1, num2, num3):
    if num1 == num2 == num3:
        return 10000 + num1 * 1000
    elif num1 == num2 or num1 == num3:
        return 1000 + num1 * 100
    elif num2 == num3:
        return 1000 + num2 * 100
    else:
        return max(num1, num2, num3) * 100
    
final = price(num1, num2, num3)
print(final)
    