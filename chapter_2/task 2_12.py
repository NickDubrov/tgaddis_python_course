# Вправа по програмуванню 2-12
# Програма розрахунку купівлі-продажу акцій

# Іменовані константи.
NUM_SHARES = 2000
PURCHASE_PRICE = 40.00
SELLING_PRICE = 42.75
COMMISSION_RATE = 0.03

# Розрахунок суми, яку було сплачено при купівлі акцій, не включаючи комісію.
purchase_sum = NUM_SHARES * PURCHASE_PRICE

# Розрахунок комісії, яку було сплачено брокеру при купівлі акцій.
purchase_rate = purchase_sum * COMMISSION_RATE

# Розрахунок загальної суми, яку було сплачено при купівлі акцій.
total_purchase = purchase_sum + purchase_rate

# Розрахунок загальної суми, яку отримали при продажу акцій.
selling_sum = NUM_SHARES * SELLING_PRICE

# Розрахунок комісії, яку було сплачено брокеру при продажу акцій.
selling_rate = selling_sum * COMMISSION_RATE

# Розрахунок суми, яка залишилася після сплати послуг брокера.
total_selling = selling_sum - selling_rate

# Розрахунок суми прибутку або збитку.
income = total_selling - total_purchase

# Виводимо на екран результати розрахунків.
print(f"Сума, сплачена за акції: {purchase_sum:,.2f}")
print(f"Комісія, сплачена брокеру при купівлі акцій: {purchase_rate:,.2f}")
print(f"Сума, отримана при продажі акцій: {selling_sum:,.2f}")
print(f"Комісія, сплачена брокеру при продажу акцій: {selling_rate:,.2f}")
print(f"Сума прибутку: {income:,.2f}")
