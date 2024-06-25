numbers = [1, 2, 3]


# Collecion of Items

def do_something(pramod_list):
    pramod_list.append(100)
    pramod_list[0] = 123
    return pramod_list

def shanti():
    print("dasda")

l = do_something(pramod_list=numbers)
print(l)

###########

number1 = [2, 4, 6, 8]

def add1(two_table):
    two_table.append(10)
    two_table[0] = 2*10
    return two_table

t = add1(two_table=number1)
print(t)