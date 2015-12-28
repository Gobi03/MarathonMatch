# 0 ~ 9 : ball or goal
# . : plane field
# # : object
# Returns: String[]
# column = x, row = y
import random

class RollingBalls:
	def restorePattern(self, start, target):
		## initial process
		#
		W = len(start[0])
		H = len(start)
		start = list(start)
		target = list(target)
		
		# make outrange wall
		start.append("#" * W)
		target.append("#" * W)
		start = list(map(lambda s: s + '#', start))
		target = list(map(lambda s: s + '#', target))

		# functions
		def searchGoal():
			res = []
			for y in range(H):
				for x in range(W):
					now = target[y][x]
					if(ord(now) >= ord('0') and ord(now) <= ord('9')):
						res.append((x, y))
			return res

		def isBall(c):
			res = False if c == '.' or c == '#' else True
			return res

		def isDirection(x_mv, y_mv):
			if x_mv == 1:
				return 0
			elif y_mv == -1:
				return 1
			elif x_mv == -1:
				return 2
			elif y_mv == 1:
				return 3
			else:
				return -1

		def isBallCommand(x, y, x_mv, y_mv, res):
			rest = '.'
			while rest == '.':
				x += x_mv
				y += y_mv
				rest = start[y][x]
				
			if isBall(start[y][x]):
				# str 書き換え
				tmp2 = list(start[y])
				tmp2[x] = '.'
				start[y] = "".join(tmp2)

				tmp2 = list(target[y])
				tmp2[x] = '.'
				target[y] = "".join(tmp2)
				#
				return [str(y) + " " + str(x) + " " + str(isDirection(x_mv, y_mv))]
			else:
				return res
		
		## functions2
	    # return list has stopable from-directions(0: <-, 1: shita)
		def searchStopableDirection(x, y):
			ans = []

			if start[y][x+1] != '.':
				ans.append(0)
			if start[y-1][x] != '.':
				ans.append(1)
			if start[y][x-1] != '.':
				ans.append(2)
			if start[y+1][x] != '.':
				ans.append(3)

			return ans
	
		## function3
		#
		def initialize(goals):
			ans = []
			for e in goals:
				nx = e[0]
				ny = e[1]

				if isBall(start[ny][nx]):
					# str 書き換え
					tmp2 = list(start[ny])
					tmp2[nx] = '#'
					start[ny] = "".join(tmp2)

					tmp2 = list(target[ny])
					tmp2[nx] = '#'
					target[ny] = "".join(tmp2)
					#					
				else:
					ans.append(e)
			return ans

		
		## function4
		#
		def isXYmove(vec):
			if vec == 0:
				return (-1, 0)
			elif vec == 1:
				return (0, 1)
			elif vec == 2:
				return (1, 0)
			else:
				return (0, -1)

		def searchStartBall():
			res = []
			for y in range(H):
				for x in range(W):
					now = start[y][x]
					if(ord(now) >= ord('0') and ord(now) <= ord('9')):
						res.append((x, y))
			return res

		def rewritePreWallPoint(x, y, x_mv, y_mv):
			rest = '.'
			while rest == '.':
				x += x_mv
				y += y_mv
				rest = start[y][x]
			
			x -= x_mv
			y -= y_mv
			# str 書き換え
			tmp2 = list(start[y])
			tmp2[x] = '0'
			start[y] = "".join(tmp2)
			#				
			

		def rollBalls(x, y, vec):
			# str 書き換え
			tmp2 = list(start[y])
			tmp2[x] = '.'
			start[y] = "".join(tmp2)
			#
			move = isXYmove(vector)
			rewritePreWallPoint(x, y, move[0], move[1])
			
			return [str(y) + " " + str(x) + " " + str(vector)]

		## main statement
		# search goal
		goals = searchGoal()
		number_of_ball = len(goals)
		max_turn = number_of_ball * 20

		goals = initialize(goals)
		ans = []
		

		# kurikaeshi
		cnt = 1000
		vector = 0
		while len(ans) < max_turn and cnt > 0:
			# one block O(10^5)
			flag = True
			while flag:
				flag = False
				goals = searchGoal()

				# for loop o
				for i in range(len(goals)): # O(10^3)
					nx = goals[i][0]
					ny = goals[i][1]

					dirlist = searchStopableDirection(nx, ny)

					tmp = []
					for e in dirlist: # O(10^2)
						if tmp == []:
							if e == 0:
								tmp = isBallCommand(nx, ny, -1, 0, tmp)
							elif e == 1:
								tmp = isBallCommand(nx, ny, 0, 1, tmp)
							elif e == 2:
								tmp = isBallCommand(nx, ny, 1, 0, tmp)
							elif e == 3:
								tmp = isBallCommand(nx, ny, 0, -1, tmp)

					if tmp != []:
						# str 書き換え
						tmp2 = list(start[ny])
						tmp2[nx] = '#'
						start[ny] = "".join(tmp2)

						tmp2 = list(target[ny])
						tmp2[nx] = '#'
						target[ny] = "".join(tmp2)
						#		

					if tmp != []:
						flag = True
					ans += tmp
				# for loop c
			# one block
			cnt -= 1
			begins = searchStartBall()

			for e in begins:
				nx = e[0]
				ny = e[1]

				tmp3 = []
				muki = isXYmove(vector)
				if start[ny + muki[1]][nx + muki[0]] == '.':
					tmp3 = rollBalls(nx, ny, vector)
				ans += tmp3

			flag3 = True
			while flag3:
				ransu = random.randint(0,3)
				if(ransu != vector):
					vector = ransu
					flag3 = False
		#kurikaeshi toji

		if len(ans) > max_turn:
			ans2 = [""]*max_turn
			for i in range(max_turn):
				ans2[i] = ans[i]
			return tuple(ans2)
		else:
			return tuple(ans)
