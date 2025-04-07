# POS for Best Buy Retail Store

# Product Management
class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity


# Define a list of products
products = [
    Product("Rice", 150.00, 50),
    Product("Sugar", 200.00, 60),
    Product("Salt", 250.00, 70),
    Product("Mackerl", 200.00, 50),
    Product("Cornedbeef", 500.00, 80),
    Product("Water", 400.00, 50),
    Product("Egg", 500.00, 100),
    Product("Bread", 950.00, 120),
    Product("Cheese", 70.00, 80),
    Product("Dish Soap", 85.00, 50),
    Product("Floor Mop", 100.00, 50),
    Product("Bleach", 150.00, 55),
    Product("Bucket", 200.00, 35),
]


# Shopping Cart

class ShoppingCart:
    # Initialize empty shopping cart
    def __init__(self):
        self.items = {}

    # Add Items to Cart
    def add_item(self, product, quantity):
        # Check for sufficient stock
        if product.quantity >= quantity:
            if product.name in self.items:
                self.items[product.name]["quantity"] += quantity
            else:
                self.items[product.name] = {"price": product.price, "quantity": quantity}
            product.quantity -= quantity
        else:
            # Display error message for insufficient stock
            print()
            print("Not enough stock!")
            print()

    # Remove Items from Cart
    def remove_item(self, product_name, quantity):
        if product_name in self.items:
            if self.items[product_name]["quantity"] >= quantity:
                self.items[product_name]["quantity"] -= quantity
                for product in products:
                    if product.name == product_name:
                        product.quantity += quantity
            else:
                print("Not enough items in cart!")
        else:
            print("Item not found in cart!")

    # Display cart content
    def view_cart(self):

        print("-------------------------------------------------")
        print("================= Shopping Cart =================")
        print("-------------------------------------------------")
        print()
        for item, values in self.items.items():
            print(
                f"{item}: {values['quantity']} x ${values['price']:.2f} = ${values['quantity'] * values['price']:.2f}")
            print("-------------------------------------------------")
            print()
    # Checkout


def checkout(cart):
    subtotal = sum(values["quantity"] * values["price"] for values in cart.items.values())
    discount = 0

    # Calculating Discount
    if subtotal > 5000:
        discount = subtotal * 0.05

    tax = (subtotal - discount) * 0.10
    total = subtotal - discount + tax

    print(f"Subtotal: ${subtotal:.2f}")
    if discount > 0:
        print(f"Discount (5%): ${discount:.2f}")
    print(f"Tax (10%): ${tax:.2f}")
    print(f"Total: ${total:.2f}")

    # Varify that payment is sufficient
    while True:
        try:
            payment = float(input("Enter payment amount: $"))
            if payment < total:
                print()
                print("Insufficient payment! Please enter a valid amount.")
                print()
                
                # Option to remove items from cart if payment is insufficient
                remove_choice = input("Would you like to remove an item from your cart? (yes/no): ")
                if remove_choice.lower() == "yes":
                    print("\nItems in cart:")
                    for i, item in enumerate(cart.items.items()):
                        print(f"{i + 1}. {item[0]}: {item[1]['quantity']} x ${item[1]['price']:.2f}")
                        print()
                    item_choice = int(input("Enter item number to remove: ")) - 1
                    print()
                    quantity = int(input("Enter quantity to remove: "))
                    cart.remove_item(list(cart.items.keys())[item_choice], quantity)
                    subtotal = sum(values["quantity"] * values["price"] for values in cart.items.values())
                    discount = 0
                    if subtotal > 5000:
                        discount = subtotal * 0.05
                    tax = (subtotal - discount) * 0.10
                    total = subtotal - discount + tax
                    print(f"Subtotal: ${subtotal:.2f}")
                    if discount > 0:
                        print(f"Discount (5%): ${discount:.2f}")
                    print(f"Tax (10%): ${tax:.2f}")
                    print(f"Total: ${total:.2f}")
                else:
                    print()
                    print("Please enter a valid payment amount.")
                    print()
            else:
                break
        except ValueError:
            print()
            print("Invalid input! Please enter a valid amount.")

    change = payment - total
    print(f"Change: ${change:.2f}")
    print_receipt(cart, subtotal, tax, discount, total, payment, change)
    # Clare the cart after printing receipt
    cart.items.clear()

    # Generate Receipt
def print_receipt(cart, subtotal, discount, tax, total, payment, change):
    print("\nReceipt")
    print("-----------------------------------------------")
    print(" ============ Best Buy Retail Store ===========")
    print("-----------------------------------------------")
    print("================== RECEIPT ====================")
    print("-----------------------------------------------")
    print()
    for item, values in cart.items.items():
        print(f"{item}: {values['quantity']} x ${values['price']:.2f} = ${values['quantity'] * values['price']:.2f}")
    print(f"Subtotal: ${subtotal:.2f}")
    if discount > 0:
        print("------------------------------------------------")
        print(f"Discount (5%): ${discount:.2f}")
    print(f"Tax (10%): ${tax:.2f}")
    print(f"Total: ${total:.2f}")
    print(f"Payment: ${payment:.2f}")
    print(f"Change: ${change:.2f}")
    print("------------------------------------------------")
    print("======= Thank you for shopping with us! ========")
    print("------------------------------------------------")
    print()
    print()


def main():
    cart = ShoppingCart()
    # Display Menu for User
    while True:
        print("====================================")
        print("======= Best Buy Retail Store ======")
        print("====================================")
        print("\n1. Add item to cart")
        print("2. Remove item from cart")
        print("3. View cart")
        print("4. Checkout")
        print("5. Exit")
        print("------------------------------------")
        print("------------------------------------")
        # Collecting User Input
        choice = input("Enter your choice: ")
        print()
        if choice == "1":
            print("======= WELCOME TO PRODUCT MENU =======")
            print("\nAvailable products:")
            print()
            for i, product in enumerate(products):
                print(f"{i + 1}. {product.name}: ${product.price:.2f} ({product.quantity} in stock)")

                # Checking Stock to notify when stock is low
                if product.quantity < 5:
                    print()
                    print("==== Low stock alert! ====")
                    print()
            while True:
                try:
                    print()
                    print("--------------------------------------")
                    print()
                    product_choice = int(input(" Enter product number: "))

                    # Validate user input for Product Choice
                    if 1 <= product_choice <= len(products):
                        product_choice -= 1
                        break
                    else:
                        print("INVALID OPTION. Please choose a valid product number.")
                        print()
                except ValueError:
                    print()
                    print("INVALID OPTION. Please enter a number.")
                    print("--------------------------------------")
                    print()
            while True:
                try:
                    # Collect quantity from user
                    print("--------------------------------------")
                    quantity = int(input(f"Enter quantity for {products[product_choice].name}: "))
                    print("--------------------------------------")

                    # Validate user input
                    if quantity > 0:
                        break
                    else:
                        print()
                        print("INVALID OPTION. Please enter a positive quantity.")
                except ValueError:
                    print()
                    print("INVALID OPTION. Please enter a number.")
            cart.add_item(products[product_choice], quantity)

        # View Cart
        elif choice == "2":
            if not cart.items:
                print("-------------------------------")
                print("======== Cart is empty.========")
                print("-------------------------------")
            else:
                print("\nItems in cart:")
                for i, item in enumerate(cart.items.items()):
                    print(f"{i + 1}. {item[0]}: {item[1]['quantity']} x ${item[1]['price']:.2f}")
                item_choice = int(input("Enter item number to remove: ")) - 1
                print()
                quantity = int(input("Enter quantity to remove: "))
                cart.remove_item(list(cart.items.keys())[item_choice], quantity)
        elif choice == "3":
            cart.view_cart()
        elif choice == "4":
            checkout(cart)
        elif choice == "5":
            print("Exiting program. Goodbye!")
            break
        else:
            print()
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()