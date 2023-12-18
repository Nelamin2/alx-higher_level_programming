def safe_print_list(my_list=[], x=0):
    try:
        count = 0
        for i in range(x):
            print(my_list[i], end=' ')
            count += 1
    except IndexError:
        pass  # Handle the case when x is greater than the length of my_list
    finally:
        print()  # Print a new line after printing the elements
        return count
