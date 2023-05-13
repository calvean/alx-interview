# 0x00-pascal_triangle

This script generates a Pascal's triangle of a given number of rows.
Usage

To use this script, run the following command:

`./0-pascal_triangle.py`

By default, this will generate a Pascal's triangle of 0 rows. To generate a triangle with a different number of rows, pass the number as an argument to the script:

`./0-pascal_triangle.py 5`

This will generate a Pascal's triangle of 5 rows.

## Functionality

The script defines a single function, pascal_triangle(n), that takes in a single argument n, which is the number of rows to generate. The function returns a list of lists representing the Pascal's triangle.

If the input n is less than or equal to 0, an empty list is returned.

## Examples

To generate a Pascal's triangle with 5 rows, run the following command:

`./0-pascal_triangle.py 5`

This will produce the following output:

`[[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]`

To generate a Pascal's triangle with 0 rows, run the following command:

`./0-pascal_triangle.py`

This will produce the following output:

`[]`

## Author

Calvin Sharara - [Github](https://github.com/calvean)

## License
Public Domain. No copy write protection. 
