# Sum of List Elements Using List Comprenhension

list_elements = []
size_of_list_elements = int(input("Enter number of List Elements: "))

for ele in range(0, size_of_list_elements):
    element = int(input())
    list_elements.append(element)
    list_elem = [item for item in list_elements]

print(list_elem)
print(sum(list_elem))



