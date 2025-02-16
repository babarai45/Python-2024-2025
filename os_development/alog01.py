class Process:
    def __init__(self, pid, arrival_time, burst_time):
        self.pid = pid
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.completion_time = 0
        self.waiting_time = 0
        self.turnaround_time = 0

def fifo_scheduling(processes):
    processes.sort(key=lambda x: x.arrival_time)    
    current_time = 0

    for process in processes:
        # If the CPU is idle, move to the next arrival time
        if current_time < process.arrival_time:
            current_time = process.arrival_time
        process.completion_time = current_time + process.burst_time
        process.turnaround_time = process.completion_time - process.arrival_time
        process.waiting_time = process.turnaround_time - process.burst_time
        current_time += process.burst_time

    return processes

# Example usage:
process_list = [
    Process(pid=1, arrival_time=0, burst_time=5),
    Process(pid=2, arrival_time=1, burst_time=3),
    Process(pid=3, arrival_time=2, burst_time=8),
    Process(pid=4, arrival_time=3, burst_time=6),
]

scheduled_processes = fifo_scheduling(process_list)

# Output the process details
print("PID\tArrival\tBurst\tCompletion\tWaiting\tTurnaround")
for p in scheduled_processes:
    print(f"{p.pid}\t{p.arrival_time}\t{p.burst_time}\t{p.completion_time}\t\t{p.waiting_time}\t{p.turnaround_time}")
