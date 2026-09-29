import random

# 1.
result = random.choice([True, False])
print(f"The result is: {result}")


# 2.
result = bool(random.randint(0,1))
print(f"The result is: {result}")


# 3.
result = random.random() < 0.5
print(f"The result is: {result}")