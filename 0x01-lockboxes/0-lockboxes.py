#!/usr/bin/python3
"""
Mock Interview

Lockboxes
"""


def canUnlockAll(boxes):
    """Checks if all boxes can be
    unlocked.

    Args:
        boxes (list[list]): List of boxes to unlock
    """
    total_boxes = len(boxes)
    keys_set = [0]
    counter = 0
    index = 0

    while index < len(keys_set):
        key_set = keys_set[index]
        for key in boxes[key_set]:
            if 0 < key < total_boxes and key not in keys_set:
                keys_set.append(key)
                counter += 1
        index += 1

    return counter == total_boxes - 1
