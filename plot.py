import subprocess
import matplotlib.pyplot as plt

num_data_values = range(0, 10001, 500)
test_results = []

for num_data in num_data_values:
    subprocess.run(f"NUM_DATA={num_data} python3 ./demo/gendata.py > ./demo/input-large.xml", shell=True)
    
    result = subprocess.run(["bash", "./demo/run_use_command.sh"], stdout=subprocess.PIPE)
    
    elapsed_time = float(result.stdout.strip().split()[0])
    print(f"Elapsed time for {num_data} data: {elapsed_time} ms")
    test_results.append(elapsed_time)

plt.plot(num_data_values, test_results)
plt.title("Relation between data size and test results")
plt.xlabel("Data size")
plt.ylabel("Test results (ms)")
plt.savefig("test_results.png")