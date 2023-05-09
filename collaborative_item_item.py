from collections import defaultdict

# Define the Cart class
class Cart:
    def __init__(self, cart_id, items):
        self.cart_id = cart_id
        self.items = items

# Create some sample carts
cart1 = Cart(1, ["item1", "item2", "item3"])
cart2 = Cart(2, ["item1", "item3", "item4"])
cart3 = Cart(3, ["item2", "item3", "item4"])
cart4 = Cart(4, ["item1", "item2", "item4"])
cart5 = Cart(5, ["item1", "item3", "item4"])

# Put the carts in a list
shopping_carts = [cart1, cart2, cart3, cart4, cart5]

# Create a dictionary to store the co-occurrence counts
item_counts = defaultdict(lambda: defaultdict(int))

# Iterate over the shopping carts and increment the co-occurrence counts
for cart in shopping_carts:
    items = cart.items
    for i in range(len(items)):
        for j in range(i+1, len(items)):
            item_counts[items[i]][items[j]] += 1
            item_counts[items[j]][items[i]] += 1

# Normalize the co-occurrence counts to get the item-item similarity scores
item_similarities = defaultdict(lambda: defaultdict(int))
for item1, related_items in item_counts.items():
    for item2, count in related_items.items():
        item_similarities[item1][item2] = count 

# Get the top 5 items that are most likely to be in a cart with "item1"
item1_similarities = item_similarities["item1"]
top_items = sorted(item1_similarities, key=item1_similarities.get, reverse=True)[:5]
print("Top 5 items that are most likely to be in a cart with item1:", top_items)
