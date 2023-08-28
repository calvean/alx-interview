#0x09-island_perimeter

This function calculates the perimeter of an island described in a grid.

##Description

The island_perimeter function takes a rectangular grid as input and returns the perimeter of the island represented by the grid. The grid is a list of lists of integers, where each cell represents either water (0) or land (1). The function assumes that the grid is completely surrounded by water and contains only one island (or nothing). The island doesn't have any "lakes," meaning there is no water inside the island that isn't connected to the water surrounding it.

The function iterates over each cell in the grid and calculates the perimeter based on the land cells and their adjacency. Each land cell contributes 4 sides to the perimeter, and for each adjacent land cell, 2 sides are subtracted to account for the shared sides.

##Usage


To use the function, pass a rectangular grid to the island_perimeter function. The grid should be a list of lists, where each inner list represents a row of the grid. Each cell in the grid should contain either 0 for water or 1 for land. The function will return an integer representing the perimeter of the island.

###Example

```
grid = [
    [0, 1, 0, 0],
    [1, 1, 1, 0],
    [0, 1, 0, 0],
    [1, 1, 0, 0]
]

perimeter = island_perimeter(grid)
print(perimeter)  # Output: 16
```

##Constraints

The following constraints should be observed when using the island_perimeter function:

*    The grid is rectangular, with its width and height not exceeding 100.
*    The grid is completely surrounded by water.
*    There is only one island (or nothing).
*    The island doesn’t have any "lakes" (water inside that isn’t connected to the water surrounding the island).

## Author

Calvin Sharara - [Github](https://github.com/calvean)

## License
Public Domain. No copy write protection. 
