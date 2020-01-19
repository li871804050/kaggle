class Solution:
    def robot(self, command: str, obstacles: [[int]], x: int, y: int) -> bool:
        pos = [0, 0]
        road = []
        road.append(pos.copy())

        for c in command:
            if c == 'U':
                pos[1] = pos[1] + 1
            elif c == 'R':
                pos[0] = pos[0] + 1
            if pos == [x, y]:
                return True
            elif pos[0] > x or pos[1] > y:
                return False
            if pos in obstacles:
                return False
            road.append(pos.copy())
        for ob in obstacles:
            if ob[0] > x or ob[1] > y:
                continue
            if self.robot_obst(road, ob):
                return False
        if self.robot_obst(road, [x, y]):
            return True
        return False

    def robot_obst(self,road, pos):
        x = road[-1][0]
        y = road[-1][1]
        t = min(pos[0]//x, pos[1]//y)
        pos = [pos[0] - t*x, pos[1] - t*y]
        if pos in road:
            return True
        else:
            return False



if __name__ == '__main__':
    s = Solution()
    command = "URR"

    obstacles = [[4, 2]]
    x = 3
    y = 2
    print(s.robot(command, obstacles, x, y))