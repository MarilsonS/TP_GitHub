import shlex

from student_service import StudentService


def print_help() -> None:
    print("Commands:")
    print("  help")
    print("  list")
    print("  add <id> <name>")
    print("  remove <id>")
    print("  quit")


def main() -> None:
    service: StudentService = StudentService()

    print("Student Manager")
    print("Type 'help' to see commands.")

    while True:
        raw_command: str = input("> ").strip()
        if not raw_command:
            continue

        parts: list[str] = shlex.split(raw_command)
        command: str = parts[0].lower()

        if command in {"quit", "exit"}:
            print("Goodbye.")
            break

        if command == "help":
            print_help()

        elif command == "list":
            service.print_list()

        elif command == "add":
            if len(parts) < 3:
                print("Usage: add <id> <name>")
                continue

            student_id: str = parts[1]
            name: str = " ".join(parts[2:])

            if service.add_student(student_id, name):
                print(f"Added '{name}'.")
            else:
                print(f"Id '{student_id}' is already used.")

        elif command == "remove":
            if len(parts) != 2:
                print("Usage: remove <id>")
                continue

            student_id: str = parts[1]
            if service.remove_student(student_id):
                print(f"Removed student '{student_id}'.")
            else:
                print(f"No student with id '{student_id}'.")
                

        else:
            print("Unknown command.")
            print_help()


if __name__ == "__main__":
    main()
