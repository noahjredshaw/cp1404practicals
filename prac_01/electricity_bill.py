# print("Electricity bill estimator")
# cents_per_kwh = int(input("Enter cents per kWh: "))
# daily_kwh_use = float(input("Enter daily use in kWh: "))
# number_of_billing_days = int(input("Enter number of billing days: "))
# estimated_bill = (cents_per_kwh * 0.01) * daily_kwh_use * number_of_billing_days
# print(f"Estimated bill: ${estimated_bill:.2f}")

TARIFF_11 = 0.244618
TARIFF_31 = 0.136928
print("Electricity bill estimator 2.0")
tariff_type = input("Which tariff? 11 or 31: ")
while tariff_type != "11" or tariff_type != "31":
    print("Invalid tariff type. Please input either 11 or 31.")
    tariff_type = input("Which tariff? 11 or 31: ")
if tariff_type == "11":
    tariff_type = TARIFF_11
else:
    tariff_type = TARIFF_31
daily_kwh_use = float(input("Enter daily use in kWh: "))
number_of_billing_days = int(input("Enter number of billing days: "))
estimated_bill = tariff_type * daily_kwh_use * number_of_billing_days
print(f"Estimated bill: ${estimated_bill:.2f}")
