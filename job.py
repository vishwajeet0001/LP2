n = int(input("Enter number of jobs: "))
jobs = []
print("Enter Id deadline and profit respectively for each job:")
for i in range(n):
    while True:
        job = input("Job " + str(i+1) + ": ").split()
        if len(job)<3:
            print("job must contain 3 elements")
            continue
        break
    jobs.append(job)

sorter = lambda job: int(job[2]) 
jobs = sorted(jobs, key=sorter, reverse=True)

scheduled = []
time = 0

for i in jobs:
    scheduled.append(i[0])
    time += 1

print("Jobs are scheduled as: ")
print(scheduled)