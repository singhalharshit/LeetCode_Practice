"""
    Create a Exponential Backoff strategy that doubles the wait time between retries, starting from 1 second, but stop after 5 retries
"""
import time


wait_time= 1
max_retries=5
attempts=0

while attempts<max_retries:
    time.sleep(wait_time)
    wait_time*=2
    attempts+=1
    

