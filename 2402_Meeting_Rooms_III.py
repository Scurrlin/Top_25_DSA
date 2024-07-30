class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        # sort based on the starting time
        meetings = sorted(meetings, key=lambda x: x[0])

        # rooms[i] :=  min heap fro storing index of available rooms
        rooms = [i for i in range(n)]

        # count[i] := count number of meeting allocated to room i
        count = [0] * n

        hpq = []    # min heap storing (finish time, index of room)

        for start, end in meetings:

            while hpq and hpq[0][0] <= start:
                _, ind = heappop(hpq)
                heappush(rooms, ind)

            if rooms:
                i = heappop(rooms)
                heappush(hpq, (end, i))
                count[i] += 1

            else:
                finish, i = heappop(hpq)
                delay = finish - start
                new_end = end + delay
                heappush(hpq, (new_end, i))
                count[i] += 1

        return count.index(max(count))