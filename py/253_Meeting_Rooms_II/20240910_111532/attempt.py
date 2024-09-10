from typing import List


class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        start_times = sorted([i[0] for i in intervals])
        end_times = sorted([i[1] for i in intervals])

        max_rooms = 0
        start_ptr = 0
        end_ptr = 0
        rooms = 0

        while start_ptr < len(intervals):
            if start_times[start_ptr] < end_times[end_ptr]:
                start_ptr += 1
                rooms += 1  # a new meeting is starting, so you need one more room
            else:
                end_ptr += 1
                rooms -= 1  # some meeting is ending, so you need one less
            max_rooms = max(max_rooms, rooms)
        return max_rooms
