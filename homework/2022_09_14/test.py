from hotel import Hotel
from registration import RegistrationError

hotel = Hotel("Ramada")
dmitry_booking = hotel.book_room("Dmitry", "Maksakov", "King Suite")
denis_booking = hotel.book_room("Denis", "Korobitsin", "Penthouse")
print(hotel.all_bookings())
hotel.cancel_booking(denis_booking)
print(hotel.all_bookings())
dmitry_registration = hotel.registration("Dmitry", "Maksakov", "741234123")
try:
    denis_registration = hotel.registration("Denis", "Korobitsin", "6512312341")
except RegistrationError:
    print("You shell not pass, Denis!")
print(dmitry_registration)