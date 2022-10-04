# A function to reverse an input
# 2022-09-27
# Jackson Blackman

def reverse(x):
    list = []
    for i in x:
        list.append(i)
    list.reverse()
    print(list)


number = input('number:')
reverse(number)
