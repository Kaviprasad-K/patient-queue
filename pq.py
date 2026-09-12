"""
Hospital Patient Priority Queue
--------------------------------
Priority 1 = Emergency, 2 = Urgent, 3 = Routine.
Lowest priority number is treated first. Among patients with the same
priority, whoever arrived earlier is treated first (FIFO tie-break).

Implemented using Python's heapq (a min-heap).
"""

import heapq
import itertools


class HospitalQueue:
    def __init__(self):
        self._heap = []
        # counter breaks ties by arrival order, since heapq compares
        # tuples element by element and can't compare strings directly
        self._counter = itertools.count()

    def add_patient(self, name: str, priority: int) -> None:
        """Add a patient with a given priority (1=Emergency, 2=Urgent, 3=Routine)."""
        count = next(self._counter)
        heapq.heappush(self._heap, (priority, count, name))
        print(f"Added: {name} (priority {priority})")

    def treat_next_patient(self):
        """Remove and return the patient who should be treated next."""
        if not self._heap:
            print("No patients waiting.")
            return None
        priority, _, name = heapq.heappop(self._heap)
        print(f"Treating next: {name} (priority {priority})")
        return name


def run_tests():
    q = HospitalQueue()

    print("\n--- Step 3: Adding patients P1-P6 ---")
    patients = [("P1", 3), ("P2", 1), ("P3", 2),
                ("P4", 1), ("P5", 3), ("P6", 2)]
    for name, priority in patients:
        q.add_patient(name, priority)

    print("\n--- Treating 2 patients first ---")
    q.treat_next_patient()   # expect P2 (priority 1)
    q.treat_next_patient()   # expect P4 (priority 1)

    print("\n--- New Emergency patient (P7, priority 1) arrives ---")
    q.add_patient("P7", 1)

    print("\n--- Treating everyone else in order ---")
    while True:
        result = q.treat_next_patient()
        if result is None:
            break


if __name__ == "__main__":
    run_tests()
