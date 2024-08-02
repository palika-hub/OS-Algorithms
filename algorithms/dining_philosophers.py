import threading

NUM_PHILOSOPHERS = 5

forks = [threading.Lock() for _ in range(NUM_PHILOSOPHERS)]

eating = [False] * NUM_PHILOSOPHERS

fork_status = [False] * NUM_PHILOSOPHERS

def acquire_forks(index):
    left_fork = forks[index]
    right_fork = forks[(index + 1) % NUM_PHILOSOPHERS]

    with left_fork, right_fork:
        if not eating[index] and not eating[(index + 1) % NUM_PHILOSOPHERS]:
            eating[index] = True
            eating[(index + 1) % NUM_PHILOSOPHERS] = True
            fork_status[index] = True
            fork_status[(index + 1) % NUM_PHILOSOPHERS] = True
            print(f'Philosopher {index} acquired forks and is eating.')
        else:
            print(f'Philosopher {index} cannot acquire forks at the moment.')

def release_forks(index):
    left_fork = forks[index]
    right_fork = forks[(index + 1) % NUM_PHILOSOPHERS]

    with left_fork, right_fork:
        eating[index] = False
        eating[(index + 1) % NUM_PHILOSOPHERS] = False
        fork_status[index] = False
        fork_status[(index + 1) % NUM_PHILOSOPHERS] = False
        print(f'Philosopher {index} released forks and is thinking.')

def print_fork_status():
    status = ['1' if status else '0' for status in fork_status]
    print(f'Fork status: {" ".join(status)}')

def user_input():
    while True:
        choice = input("Enter 'A' to acquire forks, 'R' to release forks, or 'Q' to quit: ").upper()
        if choice == 'Q':
            break
        elif choice == 'A':
            philosopher_index = int(input("Enter the philosopher's index (0 to 4): "))
            acquire_forks(philosopher_index)
        elif choice == 'R':
            philosopher_index = int(input("Enter the philosopher's index (0 to 4): "))
            release_forks(philosopher_index)
        else:
            print("Invalid choice. Please enter 'A', 'R', or 'Q.")
        print_fork_status()

philosophers = []

user_thread = threading.Thread(target=user_input)
user_thread.start()

user_thread.join()

print("Program terminated.")
