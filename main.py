from manager import TaskManager

manager = TaskManager()

PRIORITY_COLORS = {
    "high":   "\033[91m",  # red
    "medium": "\033[93m",  # yellow
    "low":    "\033[92m",  # green
}
RESET = "\033[0m"
BOLD  = "\033[1m"


def print_header():
    print(f"\n{BOLD}{'─' * 50}")
    print("        ✅  CLI Task Manager + AI")
    print(f"{'─' * 50}{RESET}")


def print_menu():
    print(f"""
{BOLD}What would you like to do?{RESET}
  1. Add a task
  2. View all tasks
  3. View pending tasks
  4. View completed tasks
  5. Complete a task
  6. Delete a task
  7. Filter by priority
  0. Exit
""")


def print_tasks(tasks: list):
    if not tasks:
        print("  No tasks found.")
        return

    print(f"\n  {'─' * 44}")
    for task in tasks:
        color = PRIORITY_COLORS.get(task.priority, RESET)
        status_icon = "✅" if task.status == "completed" else "⏳"
        print(f"  {status_icon} {BOLD}{task.title}{RESET}")
        print(f"     ID:       {task.task_id[:8]}")
        print(f"     Priority: {color}{task.priority.upper()}{RESET}")
        print(f"     Time:     {task.estimated_time or 'not set'}")
        print(f"     Status:   {task.status}")
        if task.description:
            print(f"     Note:     {task.description}")
        print(f"  {'─' * 44}")


def handle_add():
    print(f"\n{BOLD}New Task{RESET}")
    title = input("  Title: ").strip()
    if not title:
        print("  Title cannot be empty.")
        return

    description = input("  Description (optional): ").strip()
    use_ai = input("  Use AI to suggest priority? (y/n): ").strip().lower() != "n"

    print()
    task = manager.add_task(title, description, use_ai=use_ai)
    print(f"\n  Task '{task.title}' added successfully.")


def handle_complete():
    tasks = manager.get_by_status("pending")
    print_tasks(tasks)
    if not tasks:
        return
    task_id = input("\n  Enter task ID (first 8 chars): ").strip()
    task = manager.complete_task(task_id)
    if task:
        print(f"\n  ✅ '{task.title}' marked as completed.")


def handle_delete():
    print_tasks(manager.get_all_tasks())
    task_id = input("\n  Enter task ID (first 8 chars) to delete: ").strip()
    deleted = manager.delete_task(task_id)
    if deleted:
        print(f"\n  🗑  Task deleted successfully.")


def handle_priority_filter():
    priority = input("\n  Filter by priority (low/medium/high): ").strip().lower()
    tasks = manager.get_by_priority(priority)
    print_tasks(tasks)


def main():
    print_header()
    while True:
        print_menu()
        choice = input("  Enter choice: ").strip()
        print()

        if choice == "1":
            handle_add()
        elif choice == "2":
            print_tasks(manager.get_all_tasks())
        elif choice == "3":
            print_tasks(manager.get_by_status("pending"))
        elif choice == "4":
            print_tasks(manager.get_by_status("completed"))
        elif choice == "5":
            handle_complete()
        elif choice == "6":
            handle_delete()
        elif choice == "7":
            handle_priority_filter()
        elif choice == "0":
            print("  Goodbye. 👋")
            break
        else:
            print("  Invalid choice. Try again.")


if __name__ == "__main__":
    main()