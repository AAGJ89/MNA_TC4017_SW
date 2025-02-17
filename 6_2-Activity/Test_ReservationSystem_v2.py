"""
Programming exercises
Arturo Alfonso Gallardo Jasso
A01795510
Test_ReservationSystem_v2.py
"""
# pylint: disable=invalid-name

import unittest
import sys
from io import StringIO
from ReservationSystem_v2 import ReservationSystem


class TestReservationSystem(unittest.TestCase):
    """Unit tests for ReservationSystem"""
    @classmethod
    def setUpClass(cls):
        cls.test_file = "TestStoredData.json"
        cls.system = ReservationSystem(cls.test_file)

    def test_create_hotel(self):
        """Test creating a hotel"""
        self.system.create_hotel(
            hotel_id="10", name="Test Hotel", description="Test hotel for unit test",
            location="Test Location", telephone="123-456-7890",
            amenities="WiFi, Pool", pet_allowance="Yes", rate="150"
        )
        added_hotel = next(
            (hotel for hotel in self.system.data["hotels"]
             if hotel["id"] == "10"),
            None
        )
        self.assertIsNotNone(added_hotel)
        self.assertEqual(added_hotel["name"], "Test Hotel")
        self.assertEqual(added_hotel["rate"], "150")

    def test_display_hotels(self):
        """Test displaying all hotels"""
        self.system.create_hotel("11", "Another Hotel", "Another test desc",
                                 "Another Location", "123-456-0000",
                                 "WiFi, Gym", "No", "200"
                                 )
        captured_output = StringIO()
        sys.stdout = captured_output
        self.system.display_hotels()
        sys.stdout = sys.__stdout__
        self.assertIn("Another Hotel", captured_output.getvalue())

    def test_display_hotel_details(self):
        """Test displaying detailed hotel information"""
        self.system.create_hotel("15", "Detailed Hotel", "Description test",
                                 "Detail Location", "555-123-4567",
                                 "Spa, WiFi", "Yes", "250"
                                 )
        captured_output = StringIO()
        sys.stdout = captured_output
        self.system.display_hotel_details("15")
        sys.stdout = sys.__stdout__
        self.assertIn("Detailed Hotel", captured_output.getvalue())
        self.assertIn("Description test", captured_output.getvalue())

    def test_delete_hotel(self):
        """Test deleting a hotel"""
        self.system.create_hotel("12", "Deletable Hotel", "To be deleted",
                                 "Delete Location", "000-000-0000",
                                 "None", "Yes", "100"
                                 )
        self.system.delete_hotel("12")
        deleted_hotel = next(
            (hotel for hotel in self.system.data["hotels"]
             if hotel["id"] == "12"),
            None
        )
        self.assertEqual(deleted_hotel["status"], "Deleted")

    def test_modify_hotel(self):
        """Test modifying a hotel"""
        self.system.create_hotel("13", "Modifiable Hotel", "To be modified",
                                 "Modify Location", "555-555-5555",
                                 "WiFi", "No", "300"
                                 )
        self.system.modify_hotel("13", "rate", "350")
        modified_hotel = next(
            (hotel for hotel in self.system.data["hotels"]
             if hotel["id"] == "13"),
            None
        )
        self.assertEqual(modified_hotel["rate"], "350")

    def test_modify_non_existent_hotel(self):
        """Test modifying a non-existing hotel"""
        result = self.system.modify_hotel("999", "rate", "500")
        self.assertFalse(result)

    def test_create_customer(self):
        """Test creating a customer"""
        self.system.create_customer(
            customer_id="20", name="John Doe", country="USA", age="30",
            gender="Male", document="Passport"
        )
        added_customer = next(
            (customer for customer in self.system.data["customers"]
             if customer["id"] == "20"),
            None
        )
        self.assertIsNotNone(added_customer)
        self.assertEqual(added_customer["name"], "John Doe")
        self.assertEqual(added_customer["country"], "USA")

    def test_display_customers(self):
        """Test displaying customers"""
        self.system.create_customer("21", "Jane Doe", "Canada",
                                    "28", "Female", "ID Card"
                                    )
        customer_ids = [
            customer["id"] for customer in self.system.data["customers"]
        ]
        self.assertIn("21", customer_ids)

    def test_delete_customer(self):
        """Test deleting a customer"""
        self.system.create_customer("22", "Mark Smith",
                                    "UK", "40", "Male", "Driver License"
                                    )
        self.system.delete_customer("22")
        deleted_customer = next(
            (customer for customer in self.system.data["customers"]
             if customer["id"] == "22"),
            None
        )
        self.assertEqual(deleted_customer["status"], "Deleted")

    def test_modify_customer(self):
        """Test modifying a customer"""
        self.system.create_customer("23", "Emily Johnson",
                                    "France", "32", "Female", "Passport"
                                    )
        self.system.modify_customer("23", "age", "33")
        modified_customer = next(
            (customer for customer in self.system.data["customers"]
             if customer["id"] == "23"),
            None
        )
        self.assertEqual(modified_customer["age"], "33")

    def test_modify_non_existent_customer(self):
        """Test modifying a non-existing customer"""
        result = self.system.modify_customer("100", "age", "40")
        self.assertFalse(result)

    def test_create_reservation(self):
        """Test creating a reservation"""
        self.system.create_reservation(
            hotel_id="10", customer_id="20", num_people=2,
            check_in="2025-03-01", check_out="2025-03-05", total_price=600
        )
        added_reservation = next(
            (res for res in self.system.data["reservations"]
             if res["hotel_id"] == "10" and res["customer_id"] == "20"),
            None
        )
        self.assertIsNotNone(added_reservation)
        self.assertEqual(added_reservation["num_people"], 2)
        self.assertEqual(added_reservation["total_price"], 600)

    def test_cancel_reservation(self):
        """Test canceling a reservation"""
        self.system.create_reservation("10", "20", 1,
                                       "2025-04-01", "2025-04-03", 300
                                       )
        self.system.cancel_reservation("10", "20")
        canceled_reservation = next(
            (res for res in self.system.data["reservations"]
             if res["hotel_id"] == "10" and res["customer_id"] == "20"),
            None
        )
        self.assertEqual(canceled_reservation["status"], "Cancelled")

    def test_cancel_non_existent_reservation(self):
        """Test canceling a non-existing reservation"""
        result = self.system.cancel_reservation("100", "888")
        self.assertFalse(result)

    def test_load_data_with_corrupted_json(self):
        """Test corrupted JSON file"""
        with open(self.test_file, "w", encoding="utf-8") as file:
            file.write("{invalid_json}")
        system = ReservationSystem(self.test_file)
        self.assertEqual(system.data, {"hotels": [],
                                       "customers": [],
                                       "reservations": []})


if __name__ == "__main__":
    unittest.main()
