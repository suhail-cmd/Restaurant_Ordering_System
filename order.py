# order.py

class Order:
    def __init__(self, customer_name):
        self.customer_name = customer_name
        self.items = []  # list of tuples: (item_object, quantity)

    def add_item(self, item, quantity):
        self.items.append((item, quantity))
        print(f"✅ Added {quantity} × {item.get_name()} to your order.")

    def display_order(self):
        print(f"\n🧾 Order Summary for {self.customer_name}")
        print("-" * 40)
        total_bill = 0
        for item, qty in self.items:
            subtotal = item.calculate_total(qty)
            total_bill += subtotal
            print(f"{item.get_name():20} x{qty}  →  ₹{subtotal:.2f}")
        print("-" * 40)
        print(f"💰 Total Bill: ₹{total_bill:.2f}")
        print("Thank you! Enjoy your meal 😋")
