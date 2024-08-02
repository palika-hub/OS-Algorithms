import threading

buffer = [0] * 5  

def producer():
    global buffer
    item = input("Enter the item to produce: ")
    if 0 in buffer: 
        index = buffer.index(0)  
        buffer[index] = 1 
        print(f"Produced: {item}")
    else:
        print("Buffer is full. Cannot produce.")
    print("Buffer:", buffer)  

def consumer():
    global buffer
    if 1 in buffer:  
        index = buffer.index(1) 
        item = buffer[index] 
        buffer[index] = 0 
        print(f"Consumed: {item}")
    else:
        print("Buffer is empty. Nothing to consume.")
    print("Buffer:", buffer) 

while True:
    user_choice = input("Enter 'P' to produce, 'C' to consume, or 'Q' to quit: ")
    if user_choice.upper() == 'P':
        producer()
    elif user_choice.upper() == 'C':
        consumer()
    elif user_choice.upper() == 'Q':
        break
    else:
        print("Invalid choice. Please enter 'P', 'C', or 'Q.")

for thread in threading.enumerate():
    if thread != threading.current_thread():
        thread.join()

print("Program terminated.")
