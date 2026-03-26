tasks = {}
executionorder = []
completedtasks = set()

num_tasks = int(input("Enter number of tasks: "))

for i in range(num_tasks):
    task_name = input("Enter task name: ")
    dep_count = int(input("How many dependencies for " + task_name + "? "))

    dependecies = []
    for j in range(dep_count):
        depen = input("Enter dependency: ")
        dependecies.append(depen)

    tasks[task_name] = dependecies

print("TASK STRUCTURE:")
for task, depens in tasks.items():
    print(task, "-->", depens)

print("INITIAL TASKS   (no dependencies):")
inital_tasks = []

for task, depens in tasks.items():
    if len(depens) == 0:
        inital_tasks.append(task)

if len(inital_tasks) == 0:
    print("None")
else:
    for task in inital_tasks:
        print(task)

print("EXECUTION ORDER:")
step = 1

while len(completedtasks) < len(tasks):
    prog = False

    for task, deps in tasks.items():
        if task not in completedtasks:
            tf = True

            for dep in deps:
                if dep not in completedtasks:
                    tf = False
                    break

            if tf:
                executionorder.append(task)
                completedtasks.add(task)
                print("Step", step, ":", task)
                step += 1
                prog = True

    if not prog:
        if len(completedtasks) == 0:
            print("No task can be started.")
        break

if len(completedtasks) == len(tasks):
    print("ALL TASKS COMPLETED SUCCESSFULLY")
else:
    print("ERROR: Circular dependency detected!")
    print("These tasks could not be completed:")
    for task in tasks:
        if task not in completedtasks:
            print(task)