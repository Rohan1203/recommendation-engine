# app/data/fake_data.py

products = [
    {"id": 1, "name": "iPhone", "tags": ["mobile", "apple", "electronics"]},
    {"id": 2, "name": "MacBook", "tags": ["laptop", "apple", "electronics"]},
    {"id": 3, "name": "Nike Shoes", "tags": ["shoes", "sports"]},
    {"id": 4, "name": "Adidas T-shirt", "tags": ["clothing", "sports"]},
    {"id": 4, "name": "motorola phone", "tags": ["electronics"]},
]

# simulate user interest (clicked tags)
user_interest = {
    1: ["apple", "electronics"],
    2: ["sports"]
}