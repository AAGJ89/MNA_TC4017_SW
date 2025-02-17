import unittest
from ReservationSystem_v2 import ReservationSystem

class TestReservationSystem(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.test_file = "TestStoredData.json"
        cls.system = ReservationSystem(cls.test_file)

    def test_create_hotel(self):
        self.system.create_hotel(
            id="10", name="Test Hotel", description="A test hotel for unit testing",
            location="Test Location", telephone="123-456-7890", amenities="WiFi, Pool",
            pet_allowance="Yes", rate="150"
        )
        
        added_hotel = next((hotel for hotel in self.system.data["hotels"] if hotel["id"] == "10"), None)
        self.assertIsNotNone(added_hotel)
        self.assertEqual(added_hotel["name"], "Test Hotel")
        self.assertEqual(added_hotel["rate"], "150")
    
    def test_create_customer(self):
        self.system.create_customer(
            id="20", name="John Doe", country="USA", age="30", gender="Male", document="Passport"
        )
        
        # Verify the customer was added
        added_customer = next((customer for customer in self.system.data["customers"] if customer["id"] == "20"), None)
        self.assertIsNotNone(added_customer)
        self.assertEqual(added_customer["name"], "John Doe")
        self.assertEqual(added_customer["country"], "USA")
    
    def test_create_reservation(self):
        self.system.create_reservation(
            hotel_id="10", customer_id="20", num_people=2,
            check_in="2025-03-01", check_out="2025-03-05", total_price=600
        )
        
        # Verify the reservation was added
        added_reservation = next((res for res in self.system.data["reservations"] if res["hotel_id"] == "10" and res["customer_id"] == "20"), None)
        self.assertIsNotNone(added_reservation)
        self.assertEqual(added_reservation["num_people"], 2)
        self.assertEqual(added_reservation["total_price"], 600)

    def test_display_hotels(self):
        self.system.create_hotel("11", "Another Hotel", "Another test description", "Another Location", "123-456-0000", "WiFi, Gym", "No", "200")
        self.assertIn("11", [hotel["id"] for hotel in self.system.data["hotels"]])
    
    def test_display_customers(self):
        self.system.create_customer("21", "Jane Doe", "Canada", "28", "Female", "ID Card")
        self.assertIn("21", [customer["id"] for customer in self.system.data["customers"]])
 
    def test_delete_hotel(self):
        self.system.create_hotel("12", "Deletable Hotel", "To be deleted", "Delete Location", "000-000-0000", "None", "Yes", "100")
        self.system.delete_hotel("12")
        deleted_hotel = next((hotel for hotel in self.system.data["hotels"] if hotel["id"] == "12"), None)
        self.assertEqual(deleted_hotel["status"], "Deleted")
    
    def test_delete_customer(self):
        self.system.create_customer("22", "Mark Smith", "UK", "40", "Male", "Driver License")
        self.system.delete_customer("22")
        deleted_customer = next((customer for customer in self.system.data["customers"] if customer["id"] == "22"), None)
        self.assertEqual(deleted_customer["status"], "Deleted")
    
    def test_modify_hotel(self):
        self.system.create_hotel("13", "Modifiable Hotel", "To be modified", "Modify Location", "555-555-5555", "WiFi", "No", "300")
        self.system.modify_hotel("13", "rate", "350")
        modified_hotel = next((hotel for hotel in self.system.data["hotels"] if hotel["id"] == "13"), None)
        self.assertEqual(modified_hotel["rate"], "350")
    
    def test_modify_customer(self):
        self.system.create_customer("23", "Emily Johnson", "France", "32", "Female", "Passport")
        self.system.modify_customer("23", "age", "33")
        modified_customer = next((customer for customer in self.system.data["customers"] if customer["id"] == "23"), None)
        self.assertEqual(modified_customer["age"], "33")
    
    def test_cancel_reservation(self):
        self.system.create_reservation("10", "20", 1, "2025-04-01", "2025-04-03", 300)
        self.system.cancel_reservation("10", "20")
        canceled_reservation = next((res for res in self.system.data["reservations"] if res["hotel_id"] == "10" and res["customer_id"] == "20"), None)
        self.assertEqual(canceled_reservation["status"], "Cancelled")

if __name__ == "__main__":
    unittest.main()