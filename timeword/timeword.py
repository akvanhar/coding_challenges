HOURS = ["twelve", "one", "two", "three", "four", "five", "six",
             "seven", "eight", "nine", "ten", "eleven"]

ONES = ["", "one", "two", "three", "four", "five", "six",
            "seven", "eight", "nine", "ten", "eleven", "twelve",
            "thirteen", "fourteen", "fifteen", "sixteen", "seventeen",
            "eighteen", "nineteen"]

TENS = ["", "", "twenty", "thirty", "forty", "fifty"]

def time_word(time):
    """
    convert time from digits to words

    Handle noon and midnight specially:

        >>> time_word("00:00")
        'midnight'

        >>> time_word("12:00")
        'noon'

    Otherwise, covert times to text:

        >>> time_word("01:00")
        "one o'clock am"

        >>> time_word("06:01")
        'six oh one am'

        >>> time_word("06:10")
        'six ten am'

        >>> time_word("06:18")
        'six eighteen am'

        >>> time_word("06:30")
        'six thirty am'

        >>> time_word("10:34")
        'ten thirty four am'

    Don't forget to handle early morning properly:

        >>> time_word("00:12")
        'twelve twelve am'

    For times after noon, add 'pm':

        >>> time_word("12:09")
        'twelve oh nine pm'

        >>> time_word("23:23")
        'eleven twenty three pm'

    """
    written_time = ""

    if time == "00:00":
        return 'midnight'

    if time == "12:00":
        return 'noon'

    hour, minutes = time.split(':')
    hour = int(hour)
    minutes = int(minutes)

    # add hour, use 'twelve' for 0
    written_time = HOURS[hour % 12] + " "
    
    # add minutes but check for 1 on 3 cases

    if minutes > 19:
        written_time += TENS[minutes / 10] + " " + ONES[minutes % 10]
    elif minutes > 9:
        written_time += ONES[minutes]
    elif minutes > 0:
        written_time += "oh " + ONES[minutes]
    else:
        written_time += "o'clock"

    written_time = written_time.rstrip()

    if hour > 11:
        written_time += " pm"
    else:
        written_time += " am"

    return written_time

if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TEST PASSED. YOU'RE A TIME WIZARD!\n"

