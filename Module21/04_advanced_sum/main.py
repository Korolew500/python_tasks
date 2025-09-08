def sum(u_list):
    summ = 0
    for i in u_list:
        if (isinstance(i, int) or
                isinstance(i, float)):
            summ += i
        elif (isinstance(i, list) or
              isinstance(i, tuple) or
              isinstance(i, set)):
            summ += sum(i)
        elif isinstance(i, dict):
            summ += sum(i.items())
    return summ

# j = [1, 2, (1, 2, [1, {2}, [1, -2.976, {1: 1, 3: 100}]])]; print(sum(j))
