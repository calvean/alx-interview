# 0x02-minimum_operations

We initialize 'num_ops' to '0', which will keep track of the number of operations performed.
We then initialize current_h and clipboard to 1 and 0, respectively. current_h = current number of 'H' characters in the file,
 and clipboard_h = number of 'H' characters in the clipboard.
We loop until 'H' characters in the file is equal to n.
In each iteration, contents of the clipboard is pasted into the file if posible and number of 'H' characters in the file and the number of operations performed are update. If imposible, contents of the file is copied to the clipboard and number of operations performed updated

At the end of the loop, we return the number of operations performed.

## Usage

To use this module, import it into your Python script, and call the minOperations function with an integer argument n. For example:

```
from 0-minoperations import minOperations

result = minOperations(9)
print(result) # This will print 6
```

## Author

Calvin Sharara - [Github](https://github.com/calvean)

## License
Public Domain. No copy write protection. 
