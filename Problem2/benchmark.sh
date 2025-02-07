#!/bin/bash

if [ $# -ne 2 ]; then
    echo "Usage: $0 <python_script> <server_type>"
    exit 1
fi

PYTHON_SCRIPT=$1
SERVER_TYPE=$2
RESULTS_FILE="benchmark_results_${SERVER_TYPE}.txt"

echo "Benchmarking $SERVER_TYPE Server..."
echo "Clients,Execution Time" > $RESULTS_FILE  # CSV Header

for clients in {10..100..10}; do
    echo "Running $clients clients..."
    
    START_TIME=$(date +%s.%N)
    
    for ((i=1; i<=clients; i++)); do
        python3 "$PYTHON_SCRIPT" &  # Run clients concurrently
    done
    
    wait  # Wait for all clients to finish

    END_TIME=$(date +%s.%N)
    # EXEC_TIME=$(echo "$END_TIME - $START_TIME" | bc)
    EXEC_TIME=$(awk -v start="$START_TIME" -v end="$END_TIME" 'BEGIN {print end - start}')

    # Calculate total execution time using awk
    # EXEC_TIME=$(awk "BEGIN {print $END_TIME - $START_TIME}")

    echo "$clients,$EXEC_TIME" >> $RESULTS_FILE  # Save results
    echo "Completed $clients clients: $EXEC_TIME seconds"
done

echo "Benchmark complete. Data saved in $RESULTS_FILE."

# Call Python script to plot results
python3 plot_graph.py "$RESULTS_FILE" "$SERVER_TYPE"
