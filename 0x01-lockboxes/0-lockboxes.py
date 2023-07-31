def canUnlockAll(boxes):
    """
    Function that checks if all the boxes can be unlocked.

    Args:
    boxes (list of lists): Each element is a list representing a box
                           containing keys to other boxes.

    Returns:
    bool: True if all boxes can be unlocked, False otherwise.
    """
    if not isinstance(boxes, list) or len(boxes) == 0:
        return False

    num_boxes = len(boxes)
    unlocked_boxes = [False] * num_boxes
    unlocked_boxes[0] = True  # The first box is initially unlocked.
    stack = [0]  # Start with the first box.

    while stack:
        current_box = stack.pop()

        # Check the keys in the current box.
        for key in boxes[current_box]:
            if 0 <= key < num_boxes and not unlocked_boxes[key]:
                unlocked_boxes[key] = True
                stack.append(key)

    # If any box is still locked, return False, otherwise, True.
    return all(unlocked_boxes)
