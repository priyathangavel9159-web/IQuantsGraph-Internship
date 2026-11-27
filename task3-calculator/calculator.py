
from datetime import datetime, timedelta


def get_positive_number(message):
    while True:
        try:
            value = float(input(message))

            if value <= 0:
                print("Error: Please enter a number greater than zero.")
            else:
                return value

        except ValueError:
            print("Error: Please enter a valid number.")


def get_positive_days():
    while True:
        try:
            days = int(input("Enter number of working days: "))

            if days <= 0:
                print("Error: Days must be greater than zero.")
            else:
                return days

        except ValueError:
            print("Error: Please enter a positive whole number.")


def get_start_date():
    while True:
        date_text = input("Enter start date (dd/mm/yyyy): ")

        try:
            return datetime.strptime(date_text, "%d/%m/%Y").date()

        except ValueError:
            print("Error: Enter a valid date in dd/mm/yyyy format.")


def collect_inputs():
    print("===== OFFICE COMMUTE CALCULATOR =====")

    name = input("Enter your name: ").strip()

    while not name:
        print("Error: Name cannot be empty.")
        name = input("Enter your name: ").strip()

    card = get_positive_number("Enter available card balance: ")
    wallet = get_positive_number("Enter available wallet cash: ")
    meals = get_positive_number("Enter cost of one meal: ")
    travel = get_positive_number("Enter one-way travel cost: ")
    days = get_positive_days()
    start_date = get_start_date()

    return name, card, wallet, meals, travel, days, start_date


def calculate_results(inputs):
    name, card, wallet, meals, travel, days, start_date = inputs

    total_travel = travel * days
    total_meals = meals * days

    remaining_card = card - total_travel
    remaining_wallet = wallet - total_meals

    end_date = start_date + timedelta(days=days - 1)

    return {
        "name": name,
        "card": card,
        "wallet": wallet,
        "meals": meals,
        "travel": travel,
        "days": days,
        "total_travel": total_travel,
        "total_meals": total_meals,
        "remaining_card": remaining_card,
        "remaining_wallet": remaining_wallet,
        "start_date": start_date,
        "end_date": end_date
    }


def display_results(result):
    print("\n========== COMMUTE SUMMARY ==========")

    print("Name:", result["name"])
    print("Working days:", result["days"])

    print("\nDaily Costs:")
    print(f"Daily travel cost: Rs. {result['travel']:.2f}")
    print(f"Daily meal cost: Rs. {result['meals']:.2f}")

    print("\nTotal Costs:")
    print(f"Total travel cost: Rs. {result['total_travel']:.2f}")
    print(f"Total meal cost: Rs. {result['total_meals']:.2f}")

    print("\nRemaining Balances:")
    print(f"Card balance: Rs. {result['remaining_card']:.2f}")
    print(f"Wallet balance: Rs. {result['remaining_wallet']:.2f}")

    if result["remaining_card"] < 0:
        print(
            f"Insufficient card balance by Rs. "
            f"{abs(result['remaining_card']):.2f}"
        )
    else:
        print("Card balance is sufficient.")

    if result["remaining_wallet"] < 0:
        print(
            f"Insufficient wallet cash by Rs. "
            f"{abs(result['remaining_wallet']):.2f}"
        )
    else:
        print("Wallet cash is sufficient.")

    print("\nOffice Schedule:")
    print("Start date:", result["start_date"].strftime("%d/%m/%Y"))
    print("End date:", result["end_date"].strftime("%d/%m/%Y"))

    print("\n=====================================")


def main():
    try:
        inputs = collect_inputs()
        result = calculate_results(inputs)
        display_results(result)

    except (KeyboardInterrupt, EOFError):
        print("\nProgram cancelled by user.")


if __name__ == "__main__":
    main()
