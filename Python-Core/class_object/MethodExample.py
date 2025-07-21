def total(*args):
    return sum(args)

def show_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")


print(total(1,2,3,4,5,6,7))
show_info(name="Alice", age=25, country="USA")