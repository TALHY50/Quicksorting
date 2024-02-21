# Defining Quick Sort for sorting chocolates by weight
def quick_sort_by_weight(chocolates):
    if len(chocolates) <= 1:
        return chocolates
    else:
        pivot = chocolates[0].weight
        less = [choc for choc in chocolates[1:] if choc.weight <= pivot]
        greater = [choc for choc in chocolates[1:] if choc.weight > pivot]
        return quick_sort_by_weight(less) + [chocolates[0]] + quick_sort_by_weight(greater)

# Defining Merge Sort for sorting chocolates by price
def merge_sort_by_price(chocolates):
    if len(chocolates) <= 1:
        return chocolates
    
    middle = len(chocolates) // 2
    left = merge_sort_by_price(chocolates[:middle])
    right = merge_sort_by_price(chocolates[middle:])
    
    return merge(left, right)

def merge(left, right):
    result = []
    left_index_type = right_index_type = 0
    
    while left_index_type < len(left) and right_index_type < len(right):
        if left[left_index_type].price <= right[right_index_type].price:
            result.append(left[left_index_type])
            left_index_type += 1
        else:
            result.append(right[right_index_type])
            right_index_type += 1
    
    result += left[left_index_type:]
    result += right[right_index_type:]
    return result

# Test cases for sorting
    chocolates = [
        Chocolate(5, 2, 'Almond', '002'),
        Chocolate(7, 4, 'Peanut Butter', '005'),
        Chocolate(3, 3, 'Milk', '003'),
        Chocolate(6, 1, 'Dark', '004')
    ]

    sorted_by_weight = quick_sort_by_weight(chocolates)
    sorted_by_price = merge_sort_by_price(chocolates)

    print("Sorted by Weight:")
    for chocolate in sorted_by_weight:
        print(chocolate)

    print("\nSorted by Price:")
    for chocolate in sorted_by_price:
        print(chocolate)