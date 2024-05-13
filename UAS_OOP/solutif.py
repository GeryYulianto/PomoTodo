data = [
    {"name": "John", "state": "California"},
    {"name": "Emily", "state": "New York"},
    {"name": "Michael", "state": "Texas"},
    {"name": "Sarah", "state": "Florida"},
    {"name": "David", "state": "Washington"},
    {"name": "Emma", "state": "Illinois"},
    {"name": "James", "state": "Georgia"},
    {"name": "Olivia", "state": "Pennsylvania"},
    {"name": "Daniel", "state": "Ohio"},
    {"name": "Sophia", "state": "Michigan"}
]

#Ohio, california

for profile in data:
    if profile["state"] == "California" or profile["state"] == "Ohio":
        print(profile["name"])