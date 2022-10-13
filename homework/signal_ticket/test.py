import os
from pydoc import doc
from doctor import Doctor
from ticket import Ticket
from ambulance_operator import Ambulance_employee

doctor = Doctor('Maksakov M.D.', 'уролог')

ambulance_employee = Ambulance_employee('Сергеев А.В.', 'фельдшер', '52')

ticket = Ticket('Иванов И.И.', '01.01.1977', 'Пневмония', 'Поликлиника №1')

doctor_write_to_file = doctor.write_to_file

ambulance_employee_write_to_file = ambulance_employee.write_to_file

ticket_write_to_file = ticket.write_to_file

filename_doctor = f'{os.path.dirname(os.path.realpath(__file__))}/doctor.txt'

filename_ambulance_employee = f'{os.path.dirname(os.path.realpath(__file__))}/ambulance_employee.txt'

filename = f'{os.path.dirname(os.path.realpath(__file__))}/ticket.txt'

doctor_restored = Doctor.read_from_file(filename_doctor)

ambulance_employee_restored = Ambulance_employee.read_from_file(filename_ambulance_employee)

ticket_restored = Ticket.read_from_file(filename, doctor_restored)