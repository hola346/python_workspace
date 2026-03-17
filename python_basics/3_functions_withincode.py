def while_func_sum(limit):
    print("Summing numbers from 1 to inserted limit: ", limit)
    h = 0
    for i in range(limit + 1):
        h = h + i
    return h


limit = int(input("Insert limit:"))

suma = while_func_sum(limit)

print(suma)

# limit=int(input("insert limit"))
