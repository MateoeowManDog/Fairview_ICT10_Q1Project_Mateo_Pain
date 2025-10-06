from pyscript import document

menuItems = {
    "Espresso": 50,
    "Latte": 80,
    "Cappuccino": 70,
    "Mocha": 90,
    "Americano": 60
}

def create_order(event=None):
    name = document.getElementById("name").value.strip()
    address = document.getElementById("address").value.strip()
    contact = document.getElementById("contact").value.strip()

    if not name or not address or not contact:
        document.getElementById("output").innerText = "⚠️ Please fill in all fields."
        return

    menu = []
    total = 0
    checked = [el for el in document.querySelectorAll('input[name="menu"]:checked')]
    for c in checked:
        item = c.value
        price = menuItems[item]
        menu.append(f"• {item} (₱{price})")
        total += price

    message = f"""
🧾 Order Summary
-----------------------
Name   : {name}
Address: {address}
Contact: {contact}

Items:
{chr(10).join(menu)}

-----------------------
Total: ₱{total}
Thank you for ordering from La Casa de Mateo!
    """.strip()

    output = document.getElementById("output")
    output.innerText = message
