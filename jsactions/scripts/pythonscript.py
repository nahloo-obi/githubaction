import psutil
import sys


def get_ram_usage():
    try:
        django_pid = None

        for process in psutil.process_iter(['pid', 'name']):
            print("Process info:", process.info)

        # Check if the process name matches 'python' and 'manage.py'
            if 'python' in process.info['name'] and 'manage.py' in process.info['name']:
                # Get the PID of the Django process
                django_pid = process.info['pid']
        
        input_value = sys.argv[1]
        input_value2 = sys.argv[2]
        # if input_value == django_pid:
        #     print("same process id")
        #     return input_value
        # else:
        #     return benchmarkValue
        # print('here in python')
        print(input_value)
        print(input_value2)

        if django_pid:
            return django_pid
        else:
            return input_value2
                
        # print(f"Django Process PID: {django_pid}")
        # # Get process object
        # operation = psutil.Process(django_pid)

        # # Get memory usage
        # info_mem = operation.memory_info()
        # usage_mem_mb = info_mem.rss / 1024 / 1024

        # if usage_mem_mb > benchmarkValue:
        #     raise ValueError(f"Analysis failed.")
        # else:
        #     return usage_mem_mb
        

    except Exception as e:
        raise ValueError(f"Process has discontinued.")
    # except psutil.NoSuchOperation:
    #     raise ValueError(f"Process has discontinued.")
    
if __name__ == "__main__":
    ram_usage = get_ram_usage()
    print(ram_usage)



