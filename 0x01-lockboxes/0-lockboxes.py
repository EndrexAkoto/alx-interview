#!/usr/bin/python3

def canUnlockAll(boxes):
    """
    Determines if all the boxes can be opened.

    Args:
    - boxes (List[List[int]]): A list of lists where each inner list represents a box and contains keys to other boxes.

    Returns:
    - bool: True if all boxes can be opened, else False.
    """
    if not boxes:
        return False

    num_boxes = len(boxes)
    keys = {0}
    visited = set()

    while keys:
        current_key = keys.pop()
        visited.add(current_key)

        if current_key < num_boxes:
            keys.update(key for key in boxes[current_key] if key not in visited)

    return len(visited) == num_boxes

if __name__ == "__main__":
    boxes = [[1], [2], [3], [4], []]
    print(canUnlockAll(boxes))

    boxes = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
    print(canUnlockAll(boxes))

    boxes = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
    print(canUnlockAll(boxes))

