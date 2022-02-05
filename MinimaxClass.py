import heapq

class Minimax():
    def __init__(self, p, game):
        self.p = p
        self.game = game
        self.history = []

    def count(self, p, grid):
        points = {0: 10000, 1: 100, 2: 40, 3: 20, 4: 5}
        poss = [0, 0, 0, 0]
        r = [0, 1, 2, 3]
        # for i in range(self.game.w):
        #     print(grid[col][i] for col in grid)
        for x in range(self.game.w-3):
            for y in range(self.game.h):
                f = [grid[x+dx][y] for dx in r]
                if (-p in f and p not in f) or (-p not in f and p in f) and 0 not in grid[x][y+1:]+grid[x+1][y+1:]+grid[x+2][y+1:]+grid[x+3][y+1:]:
                    poss[4-abs(sum([grid[x+dx][y] for dx in r]))] += 1
        for x in range(self.game.w):
            for y in range(self.game.h-3):
                if -p in grid[x][y:y+4] and p not in grid[x][y:y+4]:
                    poss[4-abs(sum(grid[x][y:y+4]))] += 1
        for x in range(self.game.w-3):
            for y in range(self.game.h-3):
                if -p in [grid[x+d][y+d] for d in r] and p not in [grid[x+d][y+d] for d in r] and 0 not in grid[x][y+1:]+grid[x+1][y+2:]+grid[x+2][y+3:]+grid[x+3][y+4:]:
                    poss[4-(abs(sum([grid[x+d][y+d] for d in r])))] += 1
        for x in range(self.game.w-3):
            for y in range(3, self.game.h):
                if -p in [grid[x+d][y-d] for d in r] and p not in [grid[x+d][y-d] for d in r] and 0 not in grid[x][y+1:]+grid[x+1][y:]+grid[x+2][y-1:]+grid[x+3][y-2:]:
                    poss[4-abs(sum([grid[x + d][y - d] for d in r]))] += 1
        t = 0
        print(poss)
        for i in range(len(poss)):
            t += points[i] * poss[i]
        return t

    def move(self, n, grid, n_=0):
        c = []
        for i in range(self.game.w):
            nc = []
            if grid[i][0]: continue
            ngrid, win = self.game.simdrop(i, self.p, grid)
            if win: return [0, i]
            for j in range(self.game.w):
                if grid[j][0]: continue
                ngrid_, win = self.game.simdrop(j, -self.p, ngrid)
                if win: heapq.heappush(nc, 1000000)
                if n_ < n and ngrid_ not in self.history:
                    heapq.heappush(nc, -self.move(n, ngrid_, n_+1)[0])
                    self.history.append(ngrid_)
                print(ngrid_)
                heapq.heappush(nc, -(self.count(self.p, ngrid_)-self.count(-self.p, ngrid)))
            heapq.heappush(c, [-heapq.heappop(nc), i])
        print(n, n_)
        print(c)
        if n_ == 0: self.history[:] = []
        if c: return heapq.heappop(c)
        else: return [10000000, 0]


