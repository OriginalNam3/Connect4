class ConnectFour():
    def __init__(self, h=6, w=7):
        self.h = h
        self.w = w
        self.grid = [[0] * h for _ in range(w)]
        self.state = True
        self.p = 1

    def check(self, x, p):
        if not self.grid[x][0]:
            for y in range(self.h):
                if self.grid[x][y]:
                    break
        else:
            y = 0
        for r in [range(i, i+4) for i in range(-3, 1)]:
            if 0 <= x + r[0] and x + r[3] < self.w and sum([self.grid[x + dx][y] for dx in r]) == p*4:
                return True
            if 0 <= y + r[0] and y + r[3] < self.h and sum([self.grid[x][y + dy] for dy in r]) == p*4:
                return True
            if y + r[0] >= 0 <= x + r[0] and x + r[3] < self.w and y + r[3] < self.h and sum([self.grid[x + d][y + d] for d in r]) == p*4:
                return True
            if self.h > y - r[0] >= 0 <= x + r[0] < self.w and 0 <= x + r[3] < self.w and 0 <= y - r[3] < self.h and sum([self.grid[x + d][y - d] for d in r]) == p*4:
                return True
        return False

    def full(self): return sum(sum(map(abs, col)) for col in self.grid) == self.h * self.w

    def drop(self, col):
        self.p *= -1
        if not self.grid[col][self.h-1]:
            self.grid[col][self.h-1] = self.p
        elif not self.grid[col][0]:
            for i in range(1, self.h):
                if self.grid[col][i]:
                    self.grid[col][i-1] = self.p
                    break
        self.state = not self.check(col, self.p)
        return self.check(col, self.p)

    def simdrop(self, col, p, grid):
        ogrid = [col[:] for col in self.grid]
        self.grid[:] = [col[:] for col in grid]
        op = self.p
        self.p = -p
        self.drop(col)
        b = self.check(col, p)
        ngrid = [col[:] for col in self.grid]
        self.grid[:] = [col[:] for col in ogrid]
        self.p = op
        return ngrid, b

    def valid(self, col): return 0 <= int(col) < self.w and not self.grid[int(col)][0]

    def restart(self):
        self.state = True
        self.grid = self.grid = [[0] * self.h for _ in range(self.w)]

    def gridcopy(self):
        return [col[:] for col in self.grid]

