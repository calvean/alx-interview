# UTF-8 Validation

This code contains a method `validUTF8` that determines if a given data set represents a valid UTF-8 encoding. The method checks whether the data set is a valid UTF-8 encoding by examining a list of integers, where each integer represents 1 byte of data.

## Usage

To use the method, follow these steps:

*    Import the validUTF8 function from the 0-validate_utf8 module.

        `from 0-validate_utf8 import validUTF8`

*    Provide the data set as a list of integers, where each integer represents a byte of data.
*    Call the validUTF8 function with the data set as the argument.

### Example

```
from 0-validate_utf8 import validUTF8

data = [0x41]
print(validUTF8(data))
```

Approach

Here's a summary of the approach:

*    Iterate through each byte in the data set.
*    Check if the byte is the start of a UTF-8 character by examining the high-order bits.
*    If the byte indicates a character that is 1, 2, 3, or 4 bytes long, update the num_bytes counter accordingly.
*    For continuation bytes, verify that the high-order bits match the UTF-8 specification.
*    If any byte fails the UTF-8 encoding rules, return False.
*    After iterating through all bytes, check if there are any incomplete characters by verifying that num_bytes is zero.
*    If there are no incomplete characters, return True; otherwise, return False.


## Author

Calvin Sharara - [Github](https://github.com/calvean)

## License
Public Domain. No copy write protection. 
