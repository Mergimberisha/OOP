# 1 Make the list with some duplicates
initial_list = ["Apple", "Banana", "Grapes", "Apple", "Mango", "Peach", "Grapes"]
check_list = []
duplicates = []

# 2 Loop through initial list
for item in initial_list:

    # 3 check if that item is already in the check list
    if item in check_list:

        # 4 if it does exist in the check list already then we append it to the duplicates list
        duplicates.append(item)

    # 5 if it is not a duplicate then we add it to the check list to see if it pops up again later
    check_list.append(item)
print("These are the duplicates")

# 6 loop through duplicates array to show which items were duplicates
for duplicate in duplicates:
    print(duplicate)