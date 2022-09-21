def ticket(lines):
    columns = 5
    ticket_1 = [[] * lines for i in range(columns)]
    ticket_1[0].append('Ф.И.О.: ')
    ticket_1[1].append("Дата рождения: ")
    ticket_1[2].append("Возраст: ")
    ticket_1[3].append("Дата консультации: ")
    ticket_1[4].append("Диагноз: ")
    return ticket_1
    
t = ticket(1)

print(t)