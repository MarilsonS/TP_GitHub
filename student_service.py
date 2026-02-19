"""Service layer for student management operations."""

import csv
import json

from student import Student


class StudentService:
    """Handles in-memory student operations.

    This class exposes methods used by the CLI to list, add, remove, and
    export students.
    """

    def __init__(self) -> None:
        """Initializes an empty in-memory student list."""
        self._students: list[Student] = []

    def print_list(self) -> None:
        """Prints all students to stdout.

        Returns:
            None.
        """

    def add_student(self, student_id: str, name: str) -> bool:
        """Adds a student if the id is unique.

        Args:
            student_id: Unique identifier for the student.
            name: Student display name.

        Returns:
            True if the student was added, False if the id already exists.
        """

    def remove_student(self, student_id: str) -> bool:
        """Removes a student by id.

        Args:
            student_id: Id of the student to remove.

        Returns:
            True if the student was found and removed, False otherwise.
        """

    def _find_by_id(self, student_id: str) -> Student | None:
        """Finds a student by id.

        Args:
            student_id: Id to search for.

        Returns:
            The matching Student if found, otherwise None.
        """
