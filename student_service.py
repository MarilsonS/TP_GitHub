import json

from student import Student


class StudentService:

    def __init__(self) -> None:
        self._students: list[Student] = []

    def print_list(self) -> None:
        if not self._students:
            print("No students found.")
            return

        print("Students:")
        for student in self._students:
            print(f"- {student.student_id}: {student.name}")

    def add_student(self, student_id: str, name: str) -> bool:
        if self._find_by_id(student_id) is not None:
            return False

        self._students.append(Student(student_id=student_id, name=name))
        return True

    def remove_student(self, student_id: str) -> bool:
        student: Student | None = self._find_by_id(student_id)
        if student is None:
            return False

        self._students.remove(student)
        return True

    def _find_by_id(self, student_id: str) -> Student | None:
        for student in self._students:
            if student.student_id == student_id:
                return student
        return None
    
    def export_students_json(self, file_path: str) -> None:
        data: list[dict[str, str]] = [
            {"id": student.student_id, "name": student.name}
            for student in self._students
        ]

        with open(file_path, "w", encoding="utf-8") as json_file:
            json.dump(data, json_file, indent=2, ensure_ascii=False)
