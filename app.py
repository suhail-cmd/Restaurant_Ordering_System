import streamlit as st
from menu_item import MainCourse, Drink, Dessert
from order import Order
from customer import Customer
import json
import requests

# ===== Menu Setup =====
menu = {
    "Paneer Butter Masala": MainCourse("Paneer Butter Masala", 180),
    "Veg Biryani": MainCourse("Veg Biryani", 150),
    "Coke": Drink("Coke", 60),
    "Cold Coffee": Drink("Cold Coffee", 120),
    "Chocolate Cake": Dessert("Chocolate Cake", 250),
    "Ice Cream": Dessert("Ice Cream", 100)
}

st.title("🍽️ Guddu's Restaurant Ordering System")

# ===== User Info =====
st.header("🧑‍💼 Customer Details")
name = st.text_input("Enter your name:")
phone = st.text_input("Enter your mobile number (without +91):")

# ===== Order Section =====
st.header("📜 Menu")
selected_items = st.multiselect("Select items from the menu:", menu.keys())

quantities = {}
for item in selected_items:
    quantities[item] = st.number_input(f"Enter quantity for {item}:", 1, 10, 1)

# ===== Bill Button =====
if st.button("🧾 Generate Bill"):
    if not name or not phone:
        st.warning("Please enter your name and mobile number.")
    elif not selected_items:
        st.warning("Please select at least one item.")
    else:
        customer = Customer(name, phone)
        order = Order(customer.name)

        for item in selected_items:
            order.add_item(menu[item], quantities[item])

        # ===== Bill Summary =====
        st.success("✅ Order Placed Successfully!")
        st.subheader("🧾 Bill Summary")

        total_bill = 0
        for item, qty in order.items:
            subtotal = item.calculate_total(qty)
            st.write(f"{item.get_name()} × {qty} = ₹{subtotal:.2f}")
            total_bill += subtotal

        st.write(f"**💰 Total Amount: ₹{total_bill:.2f}**")

        # ===== Save Order =====
        order_data = {
            "customer": name,
            "phone": phone,
            "items": [
                {"name": item.get_name(), "qty": qty, "price": item.get_price()}
                for item, qty in order.items
            ],
            "total": total_bill,
        }

        with open("order_history.json", "a") as f:
            json.dump(order_data, f)
            f.write("\n")

        # ===== Send WhatsApp Message =====
        try:
            msg = f"""
🍴 *Guddu's Restaurant* 🍴
Customer: {name}
--------------------------
"""
            for item, qty in order.items:
                subtotal = item.calculate_total(qty)
                msg += f"{item.get_name()} x{qty} - ₹{subtotal}\n"
            msg += "--------------------------\n"
            msg += f"💰 Total: ₹{total_bill:.2f}\n"
            msg += "Thank you! Visit again 😋"

            # Generate WhatsApp link
            whatsapp_url = f"https://api.whatsapp.com/send?phone=91{phone}&text={requests.utils.quote(msg)}"

            st.markdown("### 💬 Send Bill on WhatsApp:")
            st.markdown(f"[👉 Click here to open WhatsApp and send the bill]({whatsapp_url})", unsafe_allow_html=True)
            st.info("📱 Click the link above — it will open WhatsApp Web or App with the bill pre-filled!")

        except Exception as e:
            st.error(f"Failed to prepare WhatsApp message: {e}")
