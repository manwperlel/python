ingredients = ["milk", "bread", "eggs", "cheese", "butter"]

item_to_remove = input("Enter an ingredient to remove: ").lower()

if item_to_remove in ingredients:
    ingredients.remove(item_to_remove)
    print(f"'{item_to_remove}' was removed successfully.")
else:
    print(f"'{item_to_remove}' was not found in the list.")

print(f"Updated list: {ingredients}")