def split(astring, splitter):
    """Split astring by splitter and return list of splits.

    This should work like that built-in Python .split() method [*].
    YOU MAY NOT USE the .split() method in your solution!
    YOU MAY NOT USE regular expressions in your solution!

    >>> split("i love balloonicorn", " ")
    ['i', 'love', 'balloonicorn']

    >>> split("that is which is that which is that", " that ")
    ['that is which is', 'which is that']

    >>> split("that is which is that which is that", "that")
    ['', ' is which is ', ' which is ', '']

    >>> split("hello world", "nope")
    ['hello world']

    * Note: the actual Python split method has special behavior
      when it is not passed anything for the splitter -- you do
      not need to implemented that.
    """

    index = 0
    out = []

    while index <= len(astring):
        current_index = index
        index = astring.find(splitter, index)
        if index != -1:
            out.append(astring[current_index:index])
            index += len(splitter)
        else:
            out.append(astring[current_index:])
            break

    return out


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. FINE SPLITTING!\n"

