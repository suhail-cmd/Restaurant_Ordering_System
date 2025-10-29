# 🍽️ Restaurant Ordering System

A simple and interactive restaurant ordering web app built using **Python, Streamlit, and Object-Oriented Programming (OOPs)** concepts.

## 🧩 Features
- Add menu items, take customer orders, and generate a bill.
- Uses OOPs principles:
  - **Inheritance** – Common menu item class extended by MainCourse, Drink, Dessert.
  - **Encapsulation** – Class variables and methods manage internal data.
  - **Polymorphism** – Overridden methods to calculate total prices.
  - **Abstraction** – Hides internal logic and provides clean interfaces.
- Built with **Streamlit** for a clean and responsive UI.
- Saves all order data in a JSON file (`order_history.json`).
- Future scope: Send bill via WhatsApp / SMS and connect to an SQL database.

## ⚙️ Tech Stack
- **Python 3**
- **Streamlit**
- **OOP Concepts**
- **JSON for data storage**

## 🚀 How to Run Locally
```bash
git clone https://github.com/suhail-cmd/Restaurant_Ordering_System.git
cd Restaurant_Ordering_System
pip install -r requirements.txt
streamlit run app.py
