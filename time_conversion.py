# Given a time in -hour AM/PM format, convert it to military (24-hour) time.

# Note: - 12:00:00AM on a 12-hour clock is 00:00:00 on a 24-hour clock.
# - 12:00:00PM on a 12-hour clock is 12:00:00 on a 24-hour clock.

def timeConversion(s):
    # Write your code here
    am_or_pm = s[-2:]
    time_splits = s[:-2].split(':')
    hrs = int(time_splits[0])
    mins = time_splits[1]
    secs = time_splits[2]
    
    if am_or_pm == "PM" and hrs != 12:
        hrs += 12
    elif am_or_pm == 'AM' and hrs == 12:
        hrs = 0
    
    return '{:02d}:{:s}:{:s}'.format(hrs,mins,secs)