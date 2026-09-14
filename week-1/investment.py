# **Pseudocode**

# START

# Set principal = 1000
principal = 100

# Set annual_rate = 0.07
annual_rate = 0.07

# Set amount = principal
amount = principal

# FOR year = 1 TO 30
for year in range(1, 31):

#     Calculate amount = amount * (1 + annual_rate)
        amount = amount * ( 1 + annual_rate)

#     Display year and amount
        if year == 10 or year == 20 or year == 30:
            print(f"After {year} years: ${amount:.2f}")

# END FOR

# END
