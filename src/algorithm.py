def close_with_zero(x: list) -> list:
    closest = x[0]
    for num in x:
        if abs(num) < abs(closest) or (abs(num) == abs(closest) and num > closest):
            closest = num
    return closest


print(close_with_zero([1, 2, 3,-1,5]))
