import threading

counter = 0

counter_lock = threading.Lock()

def increment_counter(times):
    global counter
    for _ in range(times):
        with counter_lock:
            counter += 1

def main():
    num_threads = 5
    increments_per_thread = 100000
    threads = []

    for i in range(num_threads):
        thread = threading.Thread(target=increment_counter, args=(increments_per_thread,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    print(f"Final counter value: {counter}")
    print(f"Expected value: {num_threads * increments_per_thread}")

if __name__ == "__main__":
    main()
