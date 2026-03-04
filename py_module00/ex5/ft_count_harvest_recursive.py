
def ft_count_harvest_recursive():
    days = int(input("Days until harvest: "))

    def harvest_helper(current):
        if current > days:
            print("Harvest time!")
            return
        print("Day", current)
        harvest_helper(current + 1)

    harvest_helper(1)
