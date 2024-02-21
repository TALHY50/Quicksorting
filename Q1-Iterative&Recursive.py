# Defining a Class of Chocolate to encapsulate the properties of a chocolate
class Chocolate:
    def __init__(self, weight, price, type, id):
        self.weight = weight
        self.price = price
        self.type = type
        self.id = id

    def __repr__(self):
        return f"Chocolate(weight={self.weight}, price={self.price}, type='{self.type}', id={self.id})"

# Defining the iterative function of chocolates to students
def chocolates_iteratively(chocolates, students):
    distribution = {}
    for student in students:
        if chocolates:
            distribution[student] = chocolates.pop(0)
        else:
            distribution[student] = None
    return distribution

# Defining the recursive function of chocolates to students
def chocolates_recursively(chocolates, students, distribution=None, index=0):
    if distribution is None:
        distribution = {}
    
    if index < len(students):
        student = students[index]
        if chocolates:
            distribution[student] = chocolates.pop(0)
            return chocolates_recursively(chocolates, students, distribution, index + 1)
        else:
            distribution[student] = None
            return chocolates_recursively(chocolates, students, distribution, index + 1)
    else:
        return distribution

# Example test cases
chocolates = [Chocolate(5, 2, 'Almond', '002'), Chocolate(7, 4, 'Peanut Butter', '005')]
students = ['Alice', 'Bob', 'Charlie', 'David']

iterative_distribution = chocolates_iteratively(chocolates[:], students)
recursive_distribution = chocolates_recursively(chocolates[:], students)

print("Iterative Distribution:")
for student, chocolate in iterative_distribution.items():
    print(f"{student}: {chocolate}")

print("\nRecursive Distribution:")
for student, chocolate in recursive_distribution.items():
    print(f"{student}: {chocolate}")