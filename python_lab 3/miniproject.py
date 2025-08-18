def add_task(task_list, task_name):
    task_list.append({"name": task_name, "completed": False})
    return task_list

def list_pending(task_list):
    return list(filter(lambda t: not t["completed"], task_list))

def mark_all_completed(task_list):
    return list(map(lambda t: {"name": t["name"], "completed": True}, task_list))

def search_tasks(task_list, keyword):
    return list(filter(lambda t: keyword.lower() in t["name"].lower(), task_list))

# Sample Workflow
tasks = []
tasks = add_task(tasks, "Buy groceries")
tasks = add_task(tasks, "Finish assignment")
tasks = add_task(tasks, "Call friend")

print("Pending Tasks:", list_pending(tasks))

# Mark all as completed
tasks = mark_all_completed(tasks)
print("All Tasks After Completion:", tasks)

# Search for a task
print("Search 'friend':", search_tasks(tasks, "friend"))
