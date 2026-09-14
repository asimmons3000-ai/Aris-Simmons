from product_data import products
# TODO: Step 1 - Print out the products to see the data that you are working with.
print(products[:3])  # Print the first 3 products to get an idea of the data structure


# TODO: Step 2 - Create a list called customer_preferences and store the user preference in this list.

customer_preferences = ["gaming", "computer", "music"]

response = ""
while response != "N":
    print("Input a preference:")
    preference = input()
    # Add the customer preference to the list
    customer_preferences.append(preference)

    response = input("Do you want to add another preference? (Y/N): ").upper()
  

# TODO: Step 3 - Convert customer_preferences list to set to eliminate duplicates.
customer_preferences = set(customer_preferences)


# TODO: Step 4 - Convert the product tags to sets in order to allow for faster comparisons.
converted_products = []
for product in products:
    product_copy = product.copy()  # Create a copy of the product dictionary
    product_copy['tags'] = set(product_copy['tags'])  # Convert tags to a set
    converted_products.append(product_copy)  # Add the modified product to the new list



# TODO: Step 5 - Write a function to calculate the number of matching tags
def count_matches(product_tags, customer_tags):
    '''
    Args:
        product_tags (set): A set of tags associated with a product.
        customer_tags (set): A set of tags associated with the customer.
    Returns:
        int: The number of matching tags between the product and customer.
    '''
    return len(product_tags & customer_tags)




# TODO: Step 6 - Write a function that loops over all products and returns a sorted list of matches
def recommend_products(products, customer_tags):
    '''
    Args:
        products (list): A list of product dictionaries.
        customer_tags (set): A set of tags associated with the customer.
    Returns:
        list: A list of products containing product names and their match counts.
    '''
    recommendations = []
    for product in products:
        match_count = count_matches(product['tags'], customer_tags)

        if match_count > 0:
            recommendations.append({'name': product['name'], 'match_count': match_count})
    recommendations.sort(key=lambda product: product["match_count"], reverse=True)
    return recommendations



# TODO: Step 7 - Call your function and print the results
recommendations = recommend_products(converted_products, customer_preferences)
print("\nRecommended Products:")
for product in recommendations:
    print(f"- {product['name']} (Matches: {product['match_count']})")
    


# DESIGN MEMO (write below in a comment):
# 1. What core operations did you use (e.g., intersections, loops)? Why?
# 2. I used loops to go through the products and collect customer preferences.
# 3. I used sets and intersections to compare the product tags with the customer's preferences. Sets make it easier and faster to find matching tags.
# 4. How might this code change if you had 1000+ products?
# 5. If there were 1000+ products, I would make the code more efficient.
# 6. I could use a database or organize the products differently so the program does not have to check every product each time.# 1. What core operations did you use (e.g., intersections, loops)? Why?
# 7. How might this code change if you had 1000+ products?

git add .
git commit -m "Debugged final output issues"
git push