import psutil
import sys


def get_ram_usage():
    try:
        
        application_process_ID = sys.argv[1]
        BENCHMARK_VALUE = sys.argv[2]
                
        # print(f"Django Process PID: {django_pid}")
        # # Get process object
        operation = psutil.Process(application_process_ID)

        # # Get memory usage
        info_mem = operation.memory_info()
        usage_mem_mb = info_mem.rss / 1024 / 1024
        
        return usage_mem_mb
        # if usage_mem_mb > benchmarkValue:
        #     raise ValueError(f"Analysis failed.")
        # else:
        #     return usage_mem_mb
        

    except Exception as e:
        raise ValueError(f"Process has discontinued.")
    
if __name__ == "__main__":
    ram_usage = get_ram_usage()
    print(ram_usage)



