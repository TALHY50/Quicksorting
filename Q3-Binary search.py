# Binary search algorithm to find chocolate by weight or price
def binary_search_chocolates(chocolates, key, search_by='weight'):
    low = 0
    high = len(chocolates) - 1
    
    while low <= high:
        mid = (low + high) // 2
        if search_by == 'weight':
            if chocolates[mid].weight == key:
                return chocolates[mid]
            elif chocolates[mid].weight < key:
                low = mid + 1
            else:
                high = mid - 1
        elif search_by == 'price':
            if chocolates[mid].price == key:
                return chocolates[mid]
            elif chocolates[mid].price < key:
                low = mid + 1
            else:
                high = mid - 1
    return None

    # Test cases for searching
    search_weight = 6  # Searching for a chocolate with weight 6g
    search_price = 2  # Searching for a chocolate with price 2 AED

    found_by_weight = binary_search_chocolates(sorted_by_weight, search_weight)
    found_by_price = binary_search_chocolates(sorted_by_price, search_price, search_by='price')

    print("Found by Weight:", found_by_weight)
    print("Found by Price:", found_by_price)