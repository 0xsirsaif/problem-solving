# pascal's traingle
def pascale_traingle(n):
    if n == 1:
        return [1,1]
    else:
        tuple = pascale_traingle(n-1)
        new = []
        for i in range(len(tuple)-1):
            num = tuple[i] + tuple[i+1]
            new.append(num)
        new.insert(0,1)
        new.append(1)
        return new
print(pascale_traingle(6))

