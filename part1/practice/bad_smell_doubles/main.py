# Как то вечером три разработчика написали 
# три метода класса `SomeClass`, каждый под себя. 
# Методы по сути своей почти одинаковые.
#
# Напишите свой метод `sorted_func`, 
# учитывая особенности всех представленных методов


class SomeClass:
    def __init__(self, lst):
        self.lst = lst

    def sorting(self, reverse=False):
        return sorted(self.lst, reverse=reverse)


if __name__ == "__main__":
    lst = [3, 2, 1, 4, 2, 1]
    sort = SomeClass(lst)

    print(sort.sorting())
    print(sort.sorting(True))