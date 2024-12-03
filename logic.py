from math import ceil

def calculate_points(receipt):
    points = 0

    # Rule 1: One point for every alphanumeric character in the retailer name
    retailer = receipt["retailer"]
    points += sum(c.isalnum() for c in retailer)

    # Rule 2: 50 points if the total is a round dollar amount
    total = float(receipt["total"])
    if total.is_integer():
        points += 50

    # Rule 3: 25 points if the total is a multiple of 0.25
    if total % 0.25 == 0:
        points += 25

    # Rule 4: 5 points for every two items
    items = receipt["items"]
    points += (len(items) // 2) * 5

    # Rule 5: Points based on item description length multiple of 3
    for item in items:
        description = item["shortDescription"].strip()
        if len(description) % 3 == 0:
            price = float(item["price"])
            points += ceil(price * 0.2)

    # Rule 6: 6 points if the purchase day is odd
    day = int(receipt["purchaseDate"].split('-')[2])
    if day % 2 != 0:
        points += 6

    # Rule 7: 10 points if the time is between 2:00 PM and 4:00 PM
    hour, minute = map(int, receipt["purchaseTime"].split(':'))
    if 14 <= hour < 16:
        points += 10

    return points