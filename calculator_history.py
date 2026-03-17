History_file = "history.txt"

def show_history():
    try:
        with open(History_file, 'r') as file:
            lines = file.readlines()
            if len(lines) == 0:
                print("No history found!")
            else:
                for line in reversed(lines):
                    print(line.strip())
    except FileNotFoundError:
        print("No history found!")

def clear_history():
    open(History_file, 'w').close()
    print("History cleared.")

def save_to_history(equation, result):
    with open(History_file, 'a') as file:
        file.write(equation + " = " + str(result) + "\n")

def calculate(user_input):
    # Remove spaces to allow both "8+8" and "8 + 8"
    user_input = user_input.replace(" ", "")
    
    # Find operator position
    for op in "+-*/":
        if op in user_input:
            parts = user_input.split(op)
            if len(parts) != 2:
                print("Invalid input. Use format: number operator number (e.g., 8+8)")
                return
            try:
                num1 = float(parts[0])
                num2 = float(parts[1])
            except ValueError:
                print("Invalid numbers entered!")
                return
            
            if op == "+":
                result = num1 + num2
            elif op == "-":
                result = num1 - num2
            elif op == "*":
                result = num1 * num2
            elif op == "/":
                if num2 == 0:
                    print("Cannot divide by zero!")
                    return
                result = num1 / num2
            
            # Convert to int if no decimal
            if result == int(result):
                result = int(result)
            
            print("Result:", result)
            save_to_history(user_input, result)
            return
    
    print("Invalid operator. Use only +, -, *, /.")

def main():
    print("------- Simple Calculator (type history, clear, or exit) -------")
    while True:
        user_input = input("Enter calculation (+ - * /) or command (history, clear, exit): ").strip()
        if user_input.lower() == "exit":
            print("Goodbye!")
            break
        elif user_input.lower() == "history":
            show_history()
        elif user_input.lower() == "clear":
            clear_history()
        else:
            calculate(user_input)

main()

    
