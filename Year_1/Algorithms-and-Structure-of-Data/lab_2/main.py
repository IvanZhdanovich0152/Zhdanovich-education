import SortManager as SM
import random
import string


def random_int(min, max):
    return random.randint(min, max)


def random_float(min, max):
    return random.uniform(min, max)


def random_char():
    return random.choice(string.ascii_letters)



def input_data():
    array = []
    n = int(input("Введите кол-во элементов массива >>> "))
    data_type = input("Введите тип данных в массиве [int/real/char] >>> ")

    match data_type:
        case "int":
            for _ in range(n):
                array.append(int(random_int(1, 100)))
        case "real":
            for _ in range(n):
                array.append(float(random_float(1, 100)))
        case "char":
            for _ in range(n):
                array.append(random_char())
        case _:
            print("Invalid input")
            exit(0)

    return array


def print_stats(name, array, comp, swap, time_taken = 0):
    print("=" * 60)
    print(name, "sort")
    print(f"Sorted array: {array}")
    print(f"Comparisons: {comp}")
    print(f"Swaps: {swap}")
    print(f"Time taken: {time_taken :.8f} seconds")
    print("=" * 60)


my_array = input_data()
print(my_array)



arr, *stats = SM.quick_sort_stat(my_array)
print_stats("quick", arr, *stats)

arr, *stats= SM.insertion_sort(my_array)
print_stats("insertion", arr, *stats)

arr, *stats= SM.selection_sort(my_array)
print_stats("selection", arr, *stats)

arr, *stats= SM.cocktail_sort(my_array)
print_stats("cocktail", arr,*stats)

arr, *stats= SM.heap_sort(my_array)
print_stats("heap", arr, *stats)