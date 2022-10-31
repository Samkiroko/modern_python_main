"""
Variable Scope:
---------------

Scopes can be `Global` or `Local`
"""
# is a scode any one in the module can use it
num = 10


def print_global_num():
    # Global declaration not required as there is no operation
    # on the varible
    print(f"Global num is: {num}")


def print_num():
    num = 20  # Function or local scope
    print(f"Local varible: {num}")


def inc_num():
    # Explicit global declaration
    global num
    num += 2


def inc_local_num():
    new_num = num + 10
    print(new_num)


inc_num()
print_global_num()
print_num()
print(num)
inc_local_num()
