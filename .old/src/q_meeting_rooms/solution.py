from typing import List, Tuple


def meeting_rooms(times: List[Tuple[int, int]]) -> bool:
    sorted_meetings = sorted(times, key=lambda x: x[0])
    for i in range(1, len(sorted_meetings)):
        cur = sorted_meetings[i]
        prev = sorted_meetings[i - 1]
        if cur[0] < prev[1]:
            return False
    return True
