import psutil
import sys
#import requests
#import multiprocessing as mp
#import time


def get_ram_usage():
    try:
        #while not stop_signal.is_set():
        #get script arguments from javascript
        script_first_value = sys.argv[1]
        BENCHMARK_VALUE = sys.argv[2]
                
        # # Get process object
        application_process_ID = int(script_first_value)
        
        operation = psutil.Process(application_process_ID)

        # # Get memory usage
        info_mem = operation.memory_info()
        usage_mem_mb = info_mem.rss / 1024 / 1024

        #ram_usage_list.append(usage_mem_mb)
        #print(stop_signal.is_set())


        #return ram_usage_list
        
        if usage_mem_mb > BENCHMARK_VALUE:
            raise ValueError(f"Application ram usage exceeded benchmark.")
        else:
            return usage_mem_mb
        

    except Exception as e:
        raise ValueError(f"Process has discontinued.")
    
# def make_request(url, requestbody, headers, method):
#     if method == "POST":
#         requests.post(url=url, json=requestbody, headers=headers)


    
if __name__ == "__main__":
    # tasks = mp.Queue()
    # # Start monitoring RAM usage in a separate process
    # stop_signal = mp.Event()
    # p = mp.Process(target=get_ram_usage, args=(stop_signal,))
    # p.start()
    # time.sleep(20)
    # # Make your request or do other operations here
    # # Example:
    # requestsbody ={
    #     "fullname" : "john",
    #     "nickname" : "johne",
    #     "age": 67
    # }
    
    # url = "http://127.0.0.1:8000/api/v1/programmers/"

    # headers = {
    #      'Content-Type': 'application/json'

    # }
    # method = 'POST'


    # make_request(url, requestsbody, headers, method)


    # # Signal the RAM monitoring process to stop
    # stop_signal.set()
    # print(f'process1 stop signal {stop_signal}')
    # p.join()  # Wait for the RAM monitoring process to finish

    # # Retrieve RAM usage data
    # print(ram_usage_list)

    ram_usage = get_ram_usage()
    print(ram_usage)



