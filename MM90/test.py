from RollingBalls import RollingBalls as RB

start = ("#00......#",\
		 "...##...#.",\
		 "....#...#.",\
		 "..........",\
		 "#.#...#0..",\
		 "..#......#",\
		 ".0#.....#.",\
		 ".#.0..##..",\
		 "#..#....#.",\
		 "#....#....")
target = ("#........#",\
		  "...##...#.",\
		  ".0..#0..#.",\
		  ".00.......",\
		  "#.#...#...",\
		  "..#......#",\
		  "..#.0...#.",\
		  ".#....##..",\
		  "#..#....#.",\
		  "#....#....")

ans = RB.restorePattern(0, start, target)
print(len(ans))
for e in ans:
	print(e)