def route_ticket(ticket):
    if ticket["priority"] == "critical":
        return "escalations"
    elif ticket["priority"] == "high":
        return "priority-support"
    return "general-support"


if __name__ == "__main__":
    ticket = {
        "id": 1001,
        "priority": "high",
        "customer": "Enterprise"
    }

    print(route_ticket(ticket))