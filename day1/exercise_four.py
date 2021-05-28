principle = 25000
annual_rate = 12
term_length = 12

print("Input Data")
print(principle, annual_rate, term_length)

monthly_rate = (annual_rate / 12) / 100 + 1
total = principle

for x in range(term_length):
    total = (total * monthly_rate)

monthly_payment = total / term_length

print(round(monthly_payment))
