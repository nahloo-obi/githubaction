import sys

def main():
    
    # Get the input argument
    input_value = sys.argv[1]

    # Your script logic goes here
    result = your_script_logic(input_value)

    # Print the result
    print(result)
    return result

def your_script_logic(input_value):
    # Your script logic here
    # This is just an example; replace it with your actual script logic
    return f"The input value must be: {input_value}"

if __name__ == "__main__":
    main()
