def route_ticket(ticket):
    priority = ticket["priority"].strip().lower()

    if priority == "critical":
        return "escalations"
    elif priority == "high":
        return "priority-support"

    return "general-support"


if __name__ == "__main__":
    test_tickets = [
        {"id": 1001, "priority": "critical"},
        {"id": 1002, "priority": "HIGH"},
        {"id": 1003, "priority": "High"},
        {"id": 1004, "priority": "normal"},
    ]

    for ticket in test_tickets:
        print(
            f"Ticket {ticket['id']}: "
            f"{route_ticket(ticket)}"
        )