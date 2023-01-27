from faker import Faker
import json

fake = Faker()
data = {}

for _ in range(10):
    data[fake.name()] = {"address": fake.address(), "job": fake.job()}

print(json.dumps(data, indent=4))