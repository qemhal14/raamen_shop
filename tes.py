from tabulate import tabulate

data = [
    ["Index", "Dish", "Category", "Stock", "Price"],
    ["Shoyu Ramen", "Raamen", 20, 15000],
    ["Shio Ramen", "Raamen", 18, 25000],
    ["Miso Ramen", "Raamen", 9, 30000],
    ["Tempura Udon", "Udon", 37, 5000],
    ["Kitsune Udon", "Udon", 28, 25000],
    ["Kake Soba", "Soba", 23, 10000],
    ["Gyoza", "Snack", 5, 20000],
    ["Ocha", "Drinks", 50, 5000],
    ["Coffee", "Drinks", 20, 10000]
]

# Function to sort and print data
def sort_and_print(data, sort_key, reverse=False):
    sorted_data = sorted(data[1:], key=lambda x: x[sort_key], reverse=reverse)
    sorted_data.insert(0, data[0])  # Re-insert headers
    print(tabulate(sorted_data, headers="firstrow"))

# Sort alphabetically by dish name
print("Sorted Alphabetically by Dish Name:")
sort_and_print(data, 1)

# Sort by category
print("\nSorted by Category:")
sort_and_print(data, 2)

# Sort by price, ascending
print("\nSorted by Price (Ascending):")
sort_and_print(data, 4)

# Sort by price, descending
print("\nSorted by Price (Descending):")
sort_and_print(data, 4, reverse=True)
