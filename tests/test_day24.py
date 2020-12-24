from day24 import part1, part2

def test_find_tile_coords():
    assert part1.find_tile_coords("eeee") == (4,0)
    assert part1.find_tile_coords("wwwwne") != (-3, -2)

def test_flip_one_tile():
    grid = {(3,5): 1}
    coords1 = (4, 5)
    coords2 = (3, 5)
    assert part2.flip_one_tile(grid, coords2) == {(3,5): 0}
    assert part2.flip_one_tile(grid, coords1) == {(4,5): 1, (3,5): 0}
