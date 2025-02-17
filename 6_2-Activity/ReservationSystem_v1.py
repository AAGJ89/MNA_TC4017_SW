import json
import os
from datetime import datetime

# JSON file name
#TEST_MODE = os.getenv("TEST_MODE", "false").lower() == "true"
DATA_FILE = "StoredData.json" #if TEST_MODE else "StoredData.json"

if os.path.exists(DATA_FILE) and os.path.getsize(DATA_FILE) > 0:
    with open(DATA_FILE, "r") as file:
        try:
            data = json.load(file)
        except json.JSONDecodeError:
            print("Corrupted JSON file detected. Initializing with empty data.")
            data = {"hotels": [], "customers": [], "reservations": []}
else:
    data = {"hotels": [], "customers": [], "reservations": []}

while True:
    print("\nReservation System")
    print("1. Hotel management")
    print("2. Customer management")
    print("3. Reservation")
    print("4. Exit application")
    
    option = input("\nPlease, select an option: ")
    
    if option == "1":
        while True:
            print("\nHotel Management Options")
            print("1. Create Hotel")
            print("2. Delete Hotel")
            print("3. Display Hotel Information")
            print("4. Modify Hotel Information")


            print("5. Return to Main Menu")
            
            sub_option = input("\nPlease, select an option: ")
            
            if sub_option == "1":
                hotel_id = input("Enter hotel ID: ")
                hotel_name = input("Enter hotel name: ")
                hotel_desc = input("Enter hotel description: ")
                hotel_rate = input("Enter hotel rate per night: ")
                hotel_location = input("Enter hotel location (Street, City, State, Country, Postal Code): ")
                hotel_telephone = input("Enter hotel telephone: ")
                hotel_amenities = input("Enter hotel amenities: ")
                hotel_pet_allowance = input("Is pet allowance available? (Yes/No): ")
                timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                data["hotels"].append({"id": hotel_id, "name": hotel_name, "description": hotel_desc, "location": hotel_location, "telephone": hotel_telephone, "amenities": hotel_amenities, "pet_allowance": hotel_pet_allowance, "rate": hotel_rate, "status": "Active", "created_at": timestamp, "updated_at": timestamp})
                with open(DATA_FILE, "w") as file:
                    json.dump(data, file, indent=4)
                print("Hotel successfully added.")
            
            elif sub_option == "2":
                print("\nAvailable Hotels:")
                for hotel in data["hotels"]:
                    print(f"{'ID:'} {hotel['id']:<10} {'Name:'} {hotel['name']:<50} {'Status:'} {hotel['status']} since {hotel['updated_at']}")
                    #print(f"ID: {hotel['id']}, Name: {hotel['name']}, Status: {hotel['status']} since {hotel['updated_at']}")
                hotel_id = input("\nEnter the ID of the hotel to delete or press any letter to cancel: ")
                if hotel_id not in [hotel['id'] for hotel in data['hotels']]:
                    print("Item not found. Operation cancelled.")
                    continue
                if not hotel_id.isdigit():
                    print("Operation cancelled.")
                    continue
                for hotel in data["hotels"]:
                    if hotel["id"] == hotel_id:
                        if hotel["status"] == "Deleted":
                            print("This ID has already been deleted.")
                        else:
                            hotel["status"] = "Deleted"
                            hotel["updated_at"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                            with open(DATA_FILE, "w") as file:
                                json.dump(data, file, indent=4)
                            print("Hotel status updated to Deleted and saved.")
                        break
            
            elif sub_option == "3":
                for hotel in data["hotels"]:
                    print(f"{'ID:'} {hotel['id']:<10} {'Name:'} {hotel['name']:<50} {'Status:'} {hotel['status']} since {hotel['updated_at']}")
                hotel_id = input("\nEnter the ID of the hotel you want to review information or press any letter to cancel: ")
                    #hotel_desc = hotel.get("description", "No description available")
                    #print(f"ID: {hotel['id']}, Name: {hotel['name']}, Status: {hotel['status']}, Created: {hotel['created_at']}, Updated: {hotel['updated_at']}, Description: {hotel.get('description', 'No description available')}, Amenities: {hotel.get('amenities', 'Not specified')}, Parking: {hotel.get('parking', 'Not specified')}, Pet Allowance: {hotel.get('pet_allowance', 'Not specified')}, Rate: {hotel.get('rate', 'Not specified')}")
                if hotel_id not in [hotel['id'] for hotel in data['hotels']]:
                    print("Item not found. Operation cancelled.")
                    continue
                if not hotel_id.isdigit():
                    print("Operation cancelled.")
                    continue
                selected_hotel = next((hotel for hotel in data["hotels"] if hotel['id'] == hotel_id), None)
                print("\nHotel Details:")
                print(f"ID: {selected_hotel['id']}")
                print(f"Name: {selected_hotel['name']}")
                print(f"Description: {selected_hotel.get('description', 'No description available')}")
                print(f"Rate per night: {selected_hotel.get('rate', 'Not specified')}")
                print(f"Location: {selected_hotel.get('location', 'Not specified')}")
                print(f"Telephone: {selected_hotel.get('telephone', 'Not specified')}")
                print(f"Amenities: {selected_hotel.get('amenities', 'Not specified')}")
                print(f"Pet Allowance: {selected_hotel.get('pet_allowance', 'Not specified')}")
                print(f"Status: {selected_hotel['status']}")
                print(f"Created: {selected_hotel['created_at']}")
                print(f"Updated: {selected_hotel['updated_at']}")
            
            elif sub_option == "4":
                for hotel in data["hotels"]:
                    print(f"{'ID:'} {hotel['id']:<10} {'Name:'} {hotel['name']:<50} {'Status:'} {hotel['status']} since {hotel['updated_at']}")
                hotel_id = input("\nEnter the ID of the hotel you want to modify or press any letter to cancel: ")
                
                if not hotel_id.isdigit():
                    print("Operation cancelled.")
                    continue
                
                selected_hotel = next((hotel for hotel in data["hotels"] if hotel['id'] == hotel_id), None)
                
                if not selected_hotel:
                    print("Item not found. Operation cancelled.")
                    continue
                
                while True:
                    print("\nHotel Details:")
                    print(f"1. Name: {selected_hotel['name']}")
                    print(f"2. Description: {selected_hotel.get('description', 'No description available')}")
                    print(f"3. Rate per night: {selected_hotel.get('rate', 'Not specified')}")
                    print(f"4. Location: {selected_hotel.get('location', 'Not specified')}")
                    print(f"5. Telephone: {selected_hotel.get('telephone', 'Not specified')}")
                    print(f"6. Amenities: {selected_hotel.get('amenities', 'Not specified')}")
                    print(f"7. Pet Allowance: {selected_hotel.get('pet_allowance', 'Not specified')}")
                    print("Press any letter to return to menu.")
                    
                    option = input("Select the number of the field you want to modify: ")
                    
                    if option == "1":
                        selected_hotel["name"] = input("New name: ")
                    elif option == "2":
                        selected_hotel["description"] = input("New description: ")
                    elif option == "3":
                        selected_hotel["rate"] = input("New rate per night: ")
                    elif option == "4":
                        selected_hotel["location"] = input("New location: ")
                    elif option == "5":
                        selected_hotel["telephone"] = input("New telephone: ")
                    elif option == "6":
                        selected_hotel["amenities"] = input("New amenities: ")
                    elif option == "7":
                        selected_hotel["pet_allowance"] = input("New pet allowance status (Yes/No): ")
                    else:
                        print("Returning to menu.")
                        break
                    
                    selected_hotel["updated_at"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    with open(DATA_FILE, "w") as file:
                                json.dump(data, file, indent=4)
                    print("\nHotel information successfully modified.")
                        
            elif sub_option == "5":
                break
            else:
                print("Invalid option.")
    
    if option == "2":
        while True:
            print("\nCustomer Management Options")
            print("1. Create Customer")
            print("2. Delete Customer")
            print("3. Display Customer Information")
            print("4. Modify Customer Information")
            print("5. Return to Main Menu")
        
            sub_option = input("\nPlease, select an option: ")
        
            if sub_option == "1":
                customer_id = input("Enter customer ID: ")
                customer_name = input("Enter customer name: ")
                customer_country = input("Enter nationality: ")
                customer_age = input("Enter customer age: ")
                customer_gender = input("Enter customer gender (Female, Male, Other): ")
                customer_document = input("Enter customer ID presented (ID, Passport, Driver License, School badge): ")
                timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                data["customers"].append({"id": customer_id, "name": customer_name, "country": customer_country, "age": customer_age, "gender": customer_gender, "document": customer_document, "status": "Active", "created_at": timestamp, "updated_at": timestamp})
                with open(DATA_FILE, "w") as file:
                    json.dump(data, file, indent=4)
                print("Customer successfully added.")
        
            elif sub_option == "2":
                print("\nAvailable Customers:")
                for customer in data["customers"]:
                    print(f"{'ID:'} {customer['id']:<10} {'Name:'} {customer['name']:<50} {'Status:'} {customer['status']} since {customer['updated_at']}")
                customer_id = input("\nEnter the ID of the customer to delete or press any letter to cancel: ")
                if customer_id not in [customer['id'] for customer in data['customers']]:
                    print("Item not found. Operation cancelled.")
                    continue
                if not customer_id.isdigit():
                    print("Operation cancelled.")
                    continue
                for customer in data["customers"]:
                    if customer["id"] == customer_id:
                        if customer["status"] == "Deleted":
                            print("This ID has already been deleted.")
                        else:
                            customer["status"] = "Deleted"
                            customer["updated_at"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                            with open(DATA_FILE, "w") as file:
                                json.dump(data, file, indent=4)
                            print("Customer status updated to Deleted and saved.")
                        break
        
            elif sub_option == "3":
                for customer in data["customers"]:
                    print(f"{'ID:'} {customer['id']:<10} {'Name:'} {customer['name']:<50} {'Status:'} {customer['status']} since {customer['updated_at']}")
                customer_id = input("\nEnter the ID of the customer you want to review information or press any letter to cancel: ")
                if customer_id not in [customer['id'] for customer in data['customers']]:
                    print("Item not found. Operation cancelled.")
                    continue
                if not customer_id.isdigit():
                    print("Operation cancelled.")
                    continue
                selected_customer = next((customer for customer in data["customers"] if customer['id'] == customer_id), None)
                print("\nCustomer Details:")
                print(f"ID: {selected_customer['id']}")
                print(f"Name: {selected_customer['name']}")
                print(f"Nationality: {selected_customer.get('country', 'Not specified')}")
                print(f"Age: {selected_customer.get('age', 'Not specified')}")
                print(f"Gender: {selected_customer.get('gender', 'Not specified')}")
                print(f"Document: {selected_customer.get('document', 'Not specified')}")
                print(f"Status: {selected_customer['status']}")
                print(f"Created: {selected_customer['created_at']}")
                print(f"Updated: {selected_customer['updated_at']}")
        
            elif sub_option == "4":
                for customer in data["customers"]:
                    print(f"{'ID:'} {customer['id']:<10} {'Name:'} {customer['name']:<50} {'Status:'} {customer['status']} since {customer['updated_at']}")
                customer_id = input("\nEnter the ID of the customer you want to modify or press any letter to cancel: ")
            
                if not customer_id.isdigit():
                    print("Operation cancelled.")
                    continue
            
                selected_customer = next((customer for customer in data["customers"] if customer['id'] == customer_id), None)
            
                if not selected_customer:
                    print("Item not found. Operation cancelled.")
                    continue
            
                while True:
                    print("\nCustomer Details:")
                    print(f"1. Name: {selected_customer['name']}")
                    print(f"2. Nationality: {selected_customer.get('country', 'Not specified')}")
                    print(f"3. Age: {selected_customer.get('age', 'Not specified')}")
                    print(f"4. Gender: {selected_customer.get('gender', 'Not specified')}")
                    print(f"5. Document: {selected_customer.get('document', 'Not specified')}")
                    print("Press any letter to return to menu.")
                
                    option = input("Select the number of the field you want to modify: ")
                
                    if option == "1":
                        selected_customer["name"] = input("New name: ")
                    elif option == "2":
                        selected_customer["country"] = input("New nationality: ")
                    elif option == "3":
                        selected_customer["age"] = input("New age: ")
                    elif option == "4":
                        selected_customer["gender"] = input("New gender: ")
                    elif option == "5":
                        selected_customer["document"] = input("New document type: ")
                    else:
                        print("Returning to menu.")
                        break
                
                    selected_customer["updated_at"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    with open(DATA_FILE, "w") as file:
                        json.dump(data, file, indent=4)
                    print("\nCustomer information successfully modified.")
                    
            elif sub_option == "5":
                break
            else:
                print("Invalid option.")

    if option == "3":
        while True:
            print("\nReservation Management Options")
            print("1. Create Reservation")
            print("2. Cancel Reservation")
            print("3. Return to Main Menu")
            
            reservation_option = input("\nPlease, select an option: ")
            
            if reservation_option == "1":
                print("\nAvailable Hotels:")
                for hotel in data["hotels"]:
                    print(f"ID: {hotel['id']}, Name: {hotel['name']}, Rate: {hotel['rate']}")
                hotel_id = input("Enter the hotel ID for the reservation (if not available, press any letter to cancel): ")
                
                if hotel_id not in [hotel['id'] for hotel in data['hotels']]:
                    print("Item not found. Operation cancelled.")
                    continue
                
                print("Available Customers:")
                for customer in data["customers"]:
                    print(f"ID: {customer['id']}, Name: {customer['name']}")
                customer_id = input("Enter the customer ID for the reservation (if not available, press any letter to cancel): ")

                if customer_id not in [customer['id'] for customer in data['customers']]:
                    print("Item not found. Operation cancelled.")
                    continue

                selected_customer = next((customer for customer in data["customers"] if customer['id'] == customer_id), None)
                customer_name = selected_customer['name']
                num_people = int(input("Enter number of people in the reservation: "))
                check_in = input("Enter check-in date (YYYY-MM-DD): ")
                check_out = input("Enter check-out date (YYYY-MM-DD): ")
                
                selected_hotel = next((hotel for hotel in data["hotels"] if hotel['id'] == hotel_id), None)
                nights = (datetime.strptime(check_out, "%Y-%m-%d") - datetime.strptime(check_in, "%Y-%m-%d")).days
                hotel_rate = float(selected_hotel['rate'].replace('$', '').replace(',', ''))
                total_price = nights * hotel_rate * (1 + (0.2 * num_people))
                
                print(f"The total price for {nights} nights will be: ${total_price:.2f}")
                print("To proceed, a credit card must be provided.")
                print("Cancellation Policy: Free cancellation if done more than 24 hours before check-in.")
                
                credit_card = input("Enter credit card number to confirm the reservation: ")
                
                timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                data["reservations"].append({
                    "hotel_id": hotel_id,
                    "customer_name": customer_name,
                    "num_people": num_people,
                    "check_in": check_in,
                    "check_out": check_out,
                    "total_price": total_price,
                    "status": "Confirmed",
                    "created_at": timestamp,
                    "updated_at": timestamp
                })
                
                with open(DATA_FILE, "w") as file:
                    json.dump(data, file, indent=4)
                
                print("Reservation successfully created.")
            
            elif reservation_option == "2":
                print("\nExisting Reservations:")
                for reservation in data["reservations"]:
                    print(f"Hotel ID: {reservation['hotel_id']}, Customer: {reservation['customer_name']}, Check-in: {reservation['check_in']}, Status: {reservation['status']}")
                
                hotel_id = input("Enter the hotel ID of the reservation to cancel: ")
                customer_name = input("Enter the customer name associated with the reservation: ")
                
                selected_reservation = next((reservation for reservation in data["reservations"] if reservation['hotel_id'] == hotel_id and reservation['customer_name'] == customer_name), None)
                
                if not selected_reservation:
                    print("Reservation not found. Operation cancelled.")
                    continue
                
                cancel_time = datetime.now()
                check_in_time = datetime.strptime(selected_reservation['check_in'], "%Y-%m-%d")
                
                if (check_in_time - cancel_time).days >= 1:
                    selected_reservation["status"] = "Cancelled"
                    selected_reservation["updated_at"] = cancel_time.strftime("%Y-%m-%d %H:%M:%S")
                    with open(DATA_FILE, "w") as file:
                        json.dump(data, file, indent=4)
                    print("Reservation successfully cancelled.")
                else:
                    print("Cancellation is not free within 24 hours before check-in.")
            
            elif reservation_option == "3":
                break
            else:
                print("Invalid option.")