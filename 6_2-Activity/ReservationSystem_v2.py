"""
Programming exercises
Arturo Alfonso Gallardo Jasso
A01795510
ReservationSystem_v2.py
"""
# pylint: disable=invalid-name, too-many-arguments, disable=too-many-positional-arguments

import json
import os
from datetime import datetime


class ReservationSystem:
    """Main code for ReservationSystem"""
    def __init__(self, data_file="StoredData.json"):
        self.data_file = data_file
        self.data = self.load_data()

    def load_data(self):
        """Load data from StoredData or create new file if empty or corrupt"""
        file_exists = os.path.exists(self.data_file)
        file_not_empty = os.path.getsize(self.data_file) > 0
        if file_exists and file_not_empty:
            with open(self.data_file, "r", encoding="utf-8") as file:
                try:
                    return json.load(file)
                except json.JSONDecodeError:
                    print("Corrupted JSON file detected. Starting empty file.")
        return {"hotels": [], "customers": [], "reservations": []}

    def save_data(self):
        """Save data to StoredData"""
        with open(self.data_file, "w", encoding="utf-8") as file:
            json.dump(self.data, file, indent=4)

    def create_hotel(self, hotel_id, name, description,
                     location, telephone, amenities,
                     pet_allowance, rate):
        """Create new hotel and save in StoredData"""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.data["hotels"].append({
             "id": hotel_id, "name": name, "description": description,
             "location": location, "telephone": telephone,
             "amenities": amenities, "pet_allowance": pet_allowance,
             "rate": rate, "status": "Active", "created_at": timestamp,
             "updated_at": timestamp
        })
        self.save_data()

    def delete_hotel(self, hotel_id):
        """Modify hotel status as eliminated in StoredData."""
        for hotel in self.data["hotels"]:
            if hotel["id"] == hotel_id:
                hotel["status"] = "Deleted"
                current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                hotel["updated_at"] = current_time
                self.save_data()
                return True
        return False

    def display_hotels(self):
        """Display all high level information from StoredData"""
        for hotel in self.data["hotels"]:
            print(f"{hotel['id']:<10}{hotel['name']:<50}"
                  f"{hotel['status']:<10}{hotel['updated_at']}")

    def display_hotel_details(self, hotel_id):
        """Display the detailed information from StoredData"""
        selected_hotel = next(
            (hotel for hotel in self.data["hotels"]
             if hotel['id'] == hotel_id),
            None
        )
        if selected_hotel:
            print("\nHotel Details:")
            print(f"ID: {selected_hotel['id']}")
            print(f"Name: {selected_hotel['name']}")
            print(f"Description: {selected_hotel.get('description', 'No d')}")
            print(f"Rate per night: {selected_hotel.get('rate', 'Not speci')}")
            print(f"Location: {selected_hotel.get('location', 'Not specif')}")
            print(f"Telephone: {selected_hotel.get('telephone', 'Not speci')}")
            print(f"Amenities: {selected_hotel.get('amenities', 'Not speci')}")
            print(f"Pet Allowance: {selected_hotel.get('pet_allowance', 'N')}")
            print(f"Status: {selected_hotel['status']}")
            print(f"Created: {selected_hotel['created_at']}")
            print(f"Updated: {selected_hotel['updated_at']}")
        else:
            print("Hotel not found.")

    def modify_hotel(self, hotel_id, field, new_value):
        """Modify a specific hotel"""
        selected_hotel = next(
            (hotel for hotel in self.data["hotels"]
             if hotel['id'] == hotel_id),
            None
        )
        if selected_hotel:
            selected_hotel[field] = new_value
            selected_hotel["updated_at"] = datetime.now().strftime(
                "%Y-%m-%d %H:%M:%S")
            self.save_data()
            return True
        return False

# Customer Management

    def create_customer(self, customer_id, name,
                        country, age, gender, document):
        """Create customer"""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.data["customers"].append({
            "id": customer_id, "name": name, "country": country,
            "age": age, "gender": gender,
            "document": document, "status": "Active",
            "created_at": timestamp, "updated_at": timestamp
        })
        self.save_data()

    def delete_customer(self, customer_id):
        """Delete customer"""
        for customer in self.data["customers"]:
            if customer["id"] == customer_id:
                customer["status"] = "Deleted"
                customer["updated_at"] = datetime.now().strftime(
                    "%Y-%m-%d %H:%M:%S")
                self.save_data()
                return True
        return False

    def display_customers(self):
        """Display all customers"""
        for customer in self.data["customers"]:
            print(f"{customer['id']:<10}{customer['name']:<50}"
                  f"{customer['status']:<10}{customer['updated_at']}")

    def display_customer_details(self, customer_id):
        """Display specific customer"""
        selected_customer = next(
            (customer for customer in self.data["customers"]
             if customer['id'] == customer_id),
            None
        )
        if selected_customer:
            print("\nCustomer Details:")
            for key, value in selected_customer.items():
                print(f"{key.capitalize()}: {value}")
        else:
            print("Customer not found.")

    def modify_customer(self, customer_id, field, new_value):
        """Modify a customer"""
        selected_customer = next(
            (customer for customer in self.data["customers"]
             if customer['id'] == customer_id),
            None
        )
        if selected_customer:
            selected_customer[field] = new_value
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            selected_customer["updated_at"] = timestamp
            self.save_data()
            return True
        return False

# Reservation Management

    def create_reservation(self, hotel_id, customer_id, num_people,
                           check_in, check_out, total_price):
        """Create reservation"""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.data["reservations"].append({
            "hotel_id": hotel_id, "customer_id": customer_id,
            "num_people": num_people, "check_in": check_in,
            "check_out": check_out, "total_price": total_price,
            "status": "Confirmed", "created_at": timestamp,
            "updated_at": timestamp
        })
        self.save_data()

    def cancel_reservation(self, hotel_id, customer_id):
        """Cancel reservation"""
        selected_reservation = next(
            (res for res in self.data["reservations"]
             if res['hotel_id'] == hotel_id
             and res['customer_id'] == customer_id),
            None
        )
        if selected_reservation:
            selected_reservation["status"] = "Cancelled"
            selected_reservation["updated_at"] = datetime.now().strftime(
                "%Y-%m-%d %H:%M:%S")
            self.save_data()
            return True
        return False


if __name__ == "__main__":
    system = ReservationSystem()
    print("Hotel Management System Loaded.")
