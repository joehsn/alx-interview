#!/usr/bin/python3

def canUnlockAll(boxes):
    """
        Checks if all boxes can be opened
    """
    unlocked = set([0])  # Box 0 is always unlocked
    keys = [0]  # Start with the keys from box 0

    while keys:
        current_box = keys.pop()

        for key in boxes[current_box]:
            if key not in unlocked and key < len(boxes):
                unlocked.add(key)
                keys.append(key)

    # Check if all boxes are unlocked
    return len(unlocked) == len(boxes)
