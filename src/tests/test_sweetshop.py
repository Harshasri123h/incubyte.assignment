import unittest
from src.sweetshop import SweetShop

class TestSweetShop(unittest.TestCase):
    def test_add_sweet(self):
        shop = SweetShop()
        shop.add_sweet("Ladoo", 10, 50)
        self.assertEqual(shop.inventory["Ladoo"]["price"], 10)
        self.assertEqual(shop.inventory["Ladoo"]["quantity"], 50)

    def test_purchase_sweet(self):
        shop = SweetShop()
        shop.add_sweet("Barfi", 20, 30)
        bill = shop.purchase_sweet("Barfi", 5)
        self.assertEqual(bill, 100)
        self.assertEqual(shop.inventory["Barfi"]["quantity"], 25)

    def test_purchase_invalid_sweet(self):
        shop = SweetShop()
        with self.assertRaises(ValueError):
            shop.purchase_sweet("Jalebi", 2)

    def test_purchase_out_of_stock(self):
        shop = SweetShop()
        shop.add_sweet("Rasgulla", 15, 3)
        with self.assertRaises(ValueError):
            shop.purchase_sweet("Rasgulla", 5)

    def test_low_stock_report(self):
        shop = SweetShop()
        shop.add_sweet("Kaju Katli", 50, 2)
        shop.add_sweet("Ladoo", 10, 20)
        low_stock = shop.low_stock_report(threshold=5)
        self.assertEqual(low_stock, ["Kaju Katli"])

    def test_sales_tracking(self):
        shop = SweetShop()
        shop.add_sweet("Barfi", 20, 10)
        shop.purchase_sweet("Barfi", 2)
        shop.purchase_sweet("Barfi", 3)
        self.assertEqual(shop.total_sales, 100)

if __name__ == '__main__':
    unittest.main()
