def route_ticket(ticket):
    if ticket["priority"] == "critical":
        return "escalations"
    return "general-support"


if __name__ == "__main__":
    ticket = {
        "id": 1001,
        "priority": "critical",
        "customer": "Enterprise"
    }

    print(route_ticket(ticket))