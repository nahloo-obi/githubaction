import psutil
import sys


# def get_ram_usage():
#     try:
#         # for process in psutil.process_iter(['pid', 'name']):
            
#         # # Check if the process name matches 'python' and 'manage.py'
#         #     if 'python' in process.info['name'] and 'manage.py' in process.info['name']:
#         #         # Get the PID of the Django process
#         #         django_pid = process.info['pid']
        
#         input_value = sys.argv[1]
#         #benchmarkValue = sys.argv[2]

#         # if input_value == django_pid:
#         #     print("same process id")
#         #     return input_value
#         # else:
#         #     return benchmarkValue
#         # print('here in python')
#         # print(input_value)
#         return input_value

#         # print(f"Django Process PID: {django_pid}")
#         # # Get process object
#         # operation = psutil.Process(django_pid)

#         # # Get memory usage
#         # info_mem = operation.memory_info()
#         # usage_mem_mb = info_mem.rss / 1024 / 1024

#         # if usage_mem_mb > benchmarkValue:
#         #     raise ValueError(f"Analysis failed.")
#         # else:
#         #     return usage_mem_mb
        

#     except Exception as e:
#         raise ValueError(f"Process has discontinued.")
#     # except psutil.NoSuchOperation:
#     #     raise ValueError(f"Process has discontinued.")
    
# if __name__ == "__main__":
#     ram_usage = get_ram_usage()
#     #print(ram_usage)


import sys

def main():
    # Check if an argument was provided
    if len(sys.argv) < 2:
        print("Usage: python script.py <input>")
        sys.exit(1)
    
    # Get the input argument
    input_value = sys.argv[1]

    # Your script logic goes here
    result = your_script_logic(input_value)

    # Print the result
    print(result)

def your_script_logic(input_value):
    # Your script logic here
    # This is just an example; replace it with your actual script logic
    return f"The input value is: {input_value}"

if __name__ == "__main__":
    main()
