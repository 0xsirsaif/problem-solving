# pascal's traingle
def pascale_traingle(n):
    if n == 1:
        return [1,1]
    else:
        returned_list = pascale_traingle(n-1)
        inner_list = []
        for i in range(len(returned_list)-1):
            num = returned_list[i] + returned_list[i+1]
            inner_list.append(num)

        # adding 1 to the first and the last of inner list
        inner_list.insert(0,1)
        inner_list.append(1)
        last_list = inner_list
        return last_list

print(pascale_traingle(2))

