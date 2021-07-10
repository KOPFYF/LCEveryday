'''
Let chopper help explain.

Starting at the origin and face north (0,1),
after one sequence of instructions,

if chopper return to the origin, he is obvious in an circle.
if chopper finishes with face not towards north,
it will get back to the initial status in another one or three sequences.

'''

class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        x, y, dr = 0, 0, 0
        dirs = ((0, 1), (1, 0), (0, -1), (-1, 0))
        for ins in instructions:
            if ins == 'R':
                dr = (dr + 1) % 4
            elif ins == 'L':
                dr = (dr + 3) % 4
            else:
                x += dirs[dr][0]
                y += dirs[dr][1]
        return (x == 0 and y == 0) or dr > 0 # not facing north