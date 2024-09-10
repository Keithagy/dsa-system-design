from typing import List, Optional


class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        bookings = []

        def startAfter(i1: List[int], i2: Optional[List[int]]) -> bool:
            return i1[0] > i2[1] if i2 else True

        def endBefore(i1: List[int], i2: List[int]) -> bool:
            return i1[1] < i2[0]

        def ableToSlotIn(interval: List[int], room: List[List[int]]) -> bool:
            for idx, existing in enumerate(room):
                if endBefore(interval, existing) and startAfter(
                    interval, room[idx - 1] if idx >= 1 else None
                ):
                    room.insert(idx, interval)
                    return True
            return False

        for interval in intervals:
            if not bookings:
                bookings.append([interval])
            else:
                for room in bookings:
                    if ableToSlotIn(interval, room):
                        break
                bookings.append([interval])

        return len(bookings)
