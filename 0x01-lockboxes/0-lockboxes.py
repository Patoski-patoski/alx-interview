#!/usr/bin/python3
"""Lockboxes Module
"""
from typing import List


def canUnlockAll(boxes: List[List[int]]) -> bool:
    """
    Function to determine if all boxes can be unlocked.

    Args:
    boxes (List[List[int]]): A list of lists, where each inner list represents
    a box and contains integers representing keys to other boxes.

    Returns:
    bool: True if all boxes can be unlocked, False otherwise.
    """

    # Initialize a list with the key to the first box
    keys = [0]

    # Get the total number of boxes
    number_of_boxes = len(boxes)

    # Iterate over the keys we have
    for key in keys:

        # Iterate over the keys in the box that the current key opens
        for box_number in boxes[key]:

            # If the key is unique and can open a box, add it to our keys list
            if box_number not in keys and box_number < number_of_boxes:
                keys.append(box_number)

    # If the number of unique keys is equal to the number of boxes, return
    # True. Otherwise, return False.
    return len(boxes) == len(keys)
