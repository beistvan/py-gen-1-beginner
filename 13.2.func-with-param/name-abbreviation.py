# function declaration
def print_fio(name, surname, patronymic):
    print(surname[0].upper() + name[0].upper() +  patronymic[0].upper())

# read data
name, surname, patronymic = input(), input(), input()

# function call
print_fio(name, surname, patronymic)
