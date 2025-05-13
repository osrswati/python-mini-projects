#To Do List with While Loops
import inflect

p = inflect.engine()
total_tasks = int(input("How many tasks would you like want to input? ")) - 1 #index start with 0
to_do = []
task_i = p.ordinal(1) #start with 1st task

while len(to_do) <= total_tasks:
  
  task = input(f"Enter your {task_i} task: ")
  # task = task.capitalize() #constrains user input
  task = task.title() #constrains user input
  
  to_do.append(task)
  task_i = p.ordinal(len(to_do) + 1)

print("Your to-do list:")
print(to_do)