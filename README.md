Hospital Patient Priority Queue


A min-heap based priority queue that decides which patient gets treated next.
Priority 1 = Emergency, 2 = Urgent, 3 = Routine. Lowest number goes first,
regardless of arrival order.
Functions
add_patient(name, priority) — adds a patient to the queue.
treat_next_patient() — removes and shows the patient to be treated next.
Run
Code:
     hpriority.py
Test result (Step 3)
Patients added in order: P1(3), P2(1), P3(2), P4(1), P5(3), P6(2)
Treatment order:
P2 (1)
P4 (1)
P7 (1) — new Emergency added after treating P2 & P4
P3 (2)
P6 (2)
P1 (3)
P5 (3)
