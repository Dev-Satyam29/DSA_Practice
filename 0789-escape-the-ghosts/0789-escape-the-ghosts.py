class Solution:
    def escapeGhosts(self, ghosts: list[list[int]], target: list[int]) -> bool:
        player_dis=abs(target[0])+abs(target[1])
        for i in ghosts:
            ghost_dis=abs(i[0]-target[0])+abs(i[1]-target[1])
            if ghost_dis<=player_dis:
                return False
        return True