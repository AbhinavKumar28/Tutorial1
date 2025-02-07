# import sys
# import matplotlib.pyplot as plt

# def plot_results(file_name, server_type):
#     clients = []
#     times = []

#     # Read results from file
#     with open(file_name, 'r') as file:
#         next(file)  # Skip header
#         for line in file:
#             num_clients, exec_time = line.strip().split(',')
#             clients.append(int(num_clients))
#             times.append(float(exec_time))

    # # Plot the results
    # plt.figure(figsize=(10, 5))
    # plt.plot(clients, times, marker='o', linestyle='-', color='b', label=server_type)

    # plt.xlabel("Number of Clients")
    # plt.ylabel("Execution Time (Seconds)")
    # plt.title(f"Performance of {server_type} Server")
    # plt.legend()
    # plt.grid(True)

    # # Save and show graph
    # plt.savefig(f"benchmark_{server_type}.png")
    # plt.show()

# if __name__ == "__main__":
#     if len(sys.argv) != 3:
#         print("Usage: python3 plot_graph.py <results_file> <server_type>")
#         sys.exit(1)

#     plot_results(sys.argv[1], sys.argv[2])
import matplotlib.pyplot as plt

# Clients=[10,20,30,40,50,60,70,80,90,100]
# ExecutionTime=[30.8486,60.3437,90.8817,120.592,150.569,180.632,210.829,240.588,270.62,300.859]
# Clients=[10,20,30,40,50,60,70,80,90,100]
# ExecutionTime=[3.75896,4.35428,4.85407,7.28887,10.5937,11.7671,8.41519,12.3042,12.2696,12.6693]
Clients=[10,20,30,40,50,60,70,80,90,100]
ExecutionTime=[3.51008,3.66445,3.93652,4.23052,4.9072,4.73364,5.10582,6.67058,5.91779,6.09829]
# Plot the results
plt.figure(figsize=(10, 5))
plt.plot(Clients, ExecutionTime, marker='o', linestyle='-', color='b', label="Multi-Threaded Server")
plt.xlabel("Number of Clients")
plt.ylabel("Execution Time (Seconds)")
plt.title(f"Performance of Multi-Threaded Server")
plt.legend()
plt.grid(True)

# Save and show graph
plt.savefig(f"benchmark_Multi-Threaded-Server.png")
plt.show()