  #Write a function called linear_search_product that takes the list of products and a target product name as input. The function should perform a linear search to find the target product in the list and return a list of indices of all occurrences of the product if found, or an empty list if the product is not found.

def linear_search_product(products, target_product):
    indices = []
    for i in range(len(products)):
        if products[i] == target_product:
            indices.append(i)
    return indices
  
products = ["Apple", "Banana", "Orange", "Banana", "Mango"]
target_product = "Banana"
result = linear_search_product(products, target_product)
print(result)