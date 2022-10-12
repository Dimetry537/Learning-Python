import os
from doctor import Doctor
from ticket import Ticket


filename_doctor = f'{os.path.dirname(os.path.realpath(__file__))}/doctor.txt'


filename = f'{os.path.dirname(os.path.realpath(__file__))}/ticket.txt'

doctor_restored = Doctor.read_from_file(filename_doctor)
ticket_restored = Ticket.read_from_file(filename, doctor_restored)

print(ticket_restored) # call to method __repr__

print(ticket_restored.doctor.specialization)