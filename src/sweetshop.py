class SweetShop:
    def __init__(self):
        self.inventory = {}
        self.total_sales = 0

    def add_sweet(self, name, price, quantity):
        self.inventory[name] = {"price": price, "quantity": quantity}

    def purchase_sweet(self, name, qty):
        if name not in self.inventory:
            raise ValueError("Sweet not found")
        if self.inventory[name]["quantity"] < qty:
            raise ValueError("Not enough stock")
        self.inventory[name]["quantity"] -= qty
        bill = self.inventory[name]["price"] * qty
        self.total_sales += bill
        return bill

    def low_stock_report(self, threshold=5):
        return [name for name, details in self.inventory.items() if details["quantity"] <= threshold]
