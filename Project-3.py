import sys

def get_user_input():
    try:
        weight = float(input("Enter your weight: "))
        height = float(input("Enter your height: "))
        return weight, height
    except ValueError:
        print("Invalid input. Please enter numeric values.")
        sys.exit()

def calculate_bmi(weight, height, unit_system):
    if unit_system == "metric":
        bmi = weight / (height ** 2)
    elif unit_system == "imperial":
        bmi = (weight / (height ** 2)) * 703
    else:
        print("Invalid unit system. Please choose 'metric' or 'imperial'.")
        sys.exit()
    return bmi

def categorize_health(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obesity"

def display_results(bmi, health_category):
    print(f"\nYour BMI is: {bmi:.2f}")
    print(f"Health Category: {health_category}")

def main():
    print("Welcome to the Command Line BMI Calculator in Python!\n")

    unit_system = input("Choose unit system (metric/imperial): ").lower()

    weight, height = get_user_input()

    bmi = calculate_bmi(weight, height, unit_system)

    health_category = categorize_health(bmi)

    display_results(bmi, health_category)

if __name__ == "__main__":
    main()
