from random import randint

class Shop:
    def __init__(self, name, shopkeeper):
        self.name = name
        self.shopkeeper = shopkeeper
        self.products = []

    #List of items in shop
    def list_items(self):
        return [product.name for product in self.products]

    #Selling items to shop
    def sell_items(self, product):
        self.products.append(product)

    #Buying items from shop
    def buy_items(self, product, player_inventory):
        if product in player_inventory:
            self.products.append(product)
            player_inventory.remove(product)
            print(f"Product: {product.name} is added to shop and removed from player's inventory")
        else:
            print("Product is not in player's inventory")

    #Gamble feature
    def gamble_feature(self, player_inventory, desired_product):
        if desired_product not in self.products:
            print("Desired product is not available in the shop")
            return

        random_number = randint(1, 10)
        if random_number >= 5:
            if player_inventory:
                random_item = player_inventory.pop(randint(0, len(player_inventory) - 1))
                self.products.append(random_item)
                self.products.remove(desired_product)
                player_inventory.append(desired_product)
                print(f"Gamble successful! {random_item.name} is added to shop and {desired_product.name} is added to player's inventory")
            else:
                print("Player's inventory is empty")
        else:
            print("Gamble failed! No items exchanged")