# ex3-1 - constellation_mapper
# attempt: try8.py
# (signature pre-filled from the .en; write your solution below)

def constellation_mapper(stars: list[tuple[int, int]], size: int) -> list[str]:
    grid_outer = []
    for _ in range(size):
        inner_ls = []
        for _ in range(size):
            inner_ls.append(".")
        grid_outer.append(inner_ls)
    
    for (row,col) in stars:
        if 0<= row <=size and 0 <= col <= size:
            grid_outer[row][col] = "*"
    
    grid_completed = []
    for item in grid_outer:
        grid_completed.append("".join(item))

    return grid_completed

