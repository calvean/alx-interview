# 0x01-lockboxes

This program takes a list of boxes as its parameter and returns a Boolean value indicating whether all the boxes in the list can be unlocked.

# Usage

import function and call it with a list of boxes.
```
from 0-lockboxes import canUnlockAll

boxes = [[1], [2], [3], []]
print(canUnlockAll(boxes)) # prints True
```
# Examples
## Example 1

```
boxes = [[1], [2], [3], []]
canUnlockAll(boxes) # True
```
#### Explanation:
All boxes can be unlocked since the first box (`boxes[0]`) is unlocked by default and contains the key to the second box (`boxes[1]`). The second box contains the key to the third box (`boxes[2]`), and the third box contains the key to the fourth box (`boxes[3]`). The fourth box is empty and can be opened without a key.

## Example 2

```
boxes = [[1, 2], [3, 4], [5], [], [6], [7], []]
canUnlockAll(boxes) # False
```

#### Explanation:
The first box (`boxes[0]`) contains the keys to the second (`boxes[1]`) and third (`boxes[2]`) boxes. The second box contains the keys to the fourth (`boxes[3]`) and fifth (`boxes[4]`) boxes. The third box contains the key to the sixth box (`boxes[5]`). The sixth box contains the key to the seventh box (`boxes[6]`). However, the fifth box does not contain a key to any other box, so it cannot be unlocked. Therefore, not all boxes can be unlocked, and the function returns False.

## Author

Calvin Sharara - [Github](https://github.com/calvean)

## License
Public Domain. No copy write protection. 
