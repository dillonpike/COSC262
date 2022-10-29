def print_shows(show_list):
    shows = show_list[:]
    shows.sort(key=lambda x: x[1] + x[2])
    time = 0
    for title, start_time, duration in shows:
        if start_time >= time:
            time = start_time + duration
            print(title, start_time, time)

def time_to_mins(time):
    """Converts string of time to minutes since midnight.
       Time format: hh:mm (24 hour time)
    """
    time = time.split(':')
    mins = int(time[0]) * 60 + int(time[1])
    return mins

# The example from the lecture notes
print_shows([
    ('a', 0, 6),
    ('b', 1, 3),
    ('c', 3, 2),
    ('d', 3, 5),
    ('e', 4, 3),
    ('f', 5, 4),
    ('g', 6, 4), 
    ('h', 8, 3)])

print_shows([
    (19, time_to_mins('9:20'), 10),
    (3, time_to_mins('9:11'), 25),
    (16, time_to_mins('9:31'), 15),
    (103, time_to_mins('11:02'), 20),
    (81, time_to_mins('10:29'), 54),
    (27, time_to_mins('11:15'), 17),
    (100, time_to_mins('10:29'), time_to_mins('01:17')), 
    (11, time_to_mins('11:18'), 44),
    (92, time_to_mins('11:58'), 31),
    (93, time_to_mins('12:04'), 32),
    (205, time_to_mins('12:42'), 7),
    (6, time_to_mins('13:24'), 6),
    (24, time_to_mins('12:42'), time_to_mins('01:50')),
    (159, time_to_mins('14:40'), 16),
    (15, time_to_mins('14:50'), 23), 
    (1, time_to_mins('14:51'), 22),
    (99, time_to_mins('14:36'), 43),
    (77, time_to_mins('15:15'), 9),
    (5, time_to_mins('15:34'), 20),
])