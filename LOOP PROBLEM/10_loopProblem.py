# exponential backoff :that doubles the wait time between retries, starting from 1sec , but stops after 5sec
import time
wait_time=1
max_retries=5
attempts=0

while attempts< max_retries:
    print("attempt ",attempts+1 , "- wait time", wait_time)
    time.sleep(wait_time)
    wait_time*=2
    attempts+=1