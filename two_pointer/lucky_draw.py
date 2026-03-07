def lucky_draw(chocolates, choices):
    left = 0
    right = len(chocolates) - 1
    red_count = 0

    for c in choices:
        if left > right:   # no chocolates left
            break

        if c == 'F':
            if chocolates[left] == 'R':
                red_count += 1
            left += 1

        elif c == 'L':
            if chocolates[right] == 'R':
                red_count += 1
            right -= 1

    return red_count

chocolates = "RGRGRGRG"
choices = "FLFL"

print(lucky_draw(chocolates, choices))