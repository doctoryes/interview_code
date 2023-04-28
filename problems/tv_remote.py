"""
Given:
- a particular width for a TV's alphabetic display
- a cursor controlled by a remote that can:
    - move the cursor up, down, left, or right (U, D, L, R)
    - click on a letter on which the cursor is placed (*)
return the sequence of U/D/L/R/* instructions needed to spell the title.

For example, a width of 5 would yield this alphabetic display:

A B C D E
F G H I J
K L M N O
P Q R S T
U V W X Y
Z

while a width of 7 would yield this:

A B C D E F G
H I J K L M N
O P Q R S T U
V W X Y Z

The instructions must *not* attempt to move the cursor outside the bounds
of the alphabetic display.

Assume that the cursor begins on 'A'.
"""


def tv_remote(width, title):
    curr_pos = [0,0]
    directions = []
    for c in title:
        alpha_pos = ord(c) - ord('a')
        target_pos = [alpha_pos // width, alpha_pos % width]
        diff = [target_pos[0] - curr_pos[0], target_pos[1] - curr_pos[1]]
        # U & L instructions are always safe for all widths - so do first.
        # D & R instructions always follow.
        # No instructions are added for 0 or negative values.
        directions += \
            ['U' * -diff[0]] + \
            ['L' * -diff[1]] + \
            ['D' * diff[0]] + \
            ['R' * diff[1]] + \
            ['*']
        curr_pos = target_pos
    return ''.join(directions)
