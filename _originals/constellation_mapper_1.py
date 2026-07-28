
#def constellation_mapper(stars: list[tuple[int, int]], size: int) -> list[str]:

#	grid = [["."] * size for x in range(size)]

#	for row, col in stars:
#		if 0 <= row < size and 0 <= col < size:
#			grid[row][col] = "*"
	
#	return ["".join(r) for r in grid]



#def constellation_mapper(stars: list[tuple[int, int]], size: int) -> list[str]:
#    s = set(stars)
#    return ["".join('*' if (r, c) in s else '.' for c in range(size)) for r in range(size)]



def constellation_mapper(stars: list[tuple[int, int]], size: int) -> list[str]:
    result = []
    
    for r in range(size):        # çdo rresht
        row = ""
        for c in range(size):    # çdo kolonë
            if (r, c) in stars:
                row += "*"
            else:
                row += "."
        result.append(row)
    
    return result
	

    result = []
    for r in range(size)
        row = ""
        for c in range(size):
            if (r, c) in stars:
                row += "*"
            else:
                row += "."
        result.append(row)
    return result

    result = []

    for r in range(size):
        row = ""
        for c in range(size):
            if(r, c) in stars:
                row += "*"
            else:
                row += "."
        result.append(row)
    return result

    for r in range(size):
        row = ""
        for c in range(size):
            if (r, c) in stars:
                row += "*"
            else:
                row += "."
        result.append(row)
    return result

    result = []
    
    for r in range(size):
        row += ""
        for c in range(size):
            if (r, c) in stars:
                row += "*"
            else:
                row += "."
        result.append(row)
    return result

print(constellation_mapper([(0, 0), (1, 1), (2, 2)], 3))
# ['*..', '.*.', '..*']

print(constellation_mapper([(1, 1), (0, 1), (2, 1), (1, 0), (1, 2)], 3))
# ['.*.', '***', '.*.']

print(constellation_mapper([], 2))
# ['..', '..']

print(constellation_mapper([(0, 1), (1, 1), (2, 1)], 3))
# ['.*.', '.*.', '.*.']

print(constellation_mapper([(0, 0), (5, 5)], 3))
# ['*..', '...', '...']

print(constellation_mapper([(0, 1), (1, 1), (2, 1)], 3))
# ['.*.', '.*.', '.*.']