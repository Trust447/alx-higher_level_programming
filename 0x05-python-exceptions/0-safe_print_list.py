#!/usr/bin/python3
def safe_print_li t(my_list=[], x=0):
    count = 0
    try:
        for item in my_list:
            if x <= count:
                break
            print(item, end="")
            count += 1
        print()
    except:
        pass
     return count



