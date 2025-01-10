from random import randint, choice

class MakeMaze:
    def __init__(self,width,height):
        """
        width and height must be Odd numbers for a balanced maze generation
        """
        self.width,self.height=width,height
        self.grid=[[1 for _ in range(width)] for __ in range(height)]
    def notout(self,nx,ny):
        return nx<self.width-1 and nx>=0 and ny<self.height-1 and ny >=0
    def getneighbours(self,nx,ny,k=2):
        n=[]
        if self.notout(nx+k,ny): n.append([nx+k,ny])
        if self.notout(nx-k,ny): n.append([nx-k,ny])
        if self.notout(nx,ny+k): n.append([nx,ny+k])
        if self.notout(nx,ny-k): n.append([nx,ny-k])
        return n
    def generate(self,target=None):
        stack=[[1,1]]
        place=1
        while stack:
            cur=stack[-1]
            self.grid[cur[1]][cur[0]]=0
            unvisited=[i for i in self.getneighbours(cur[0],cur[1]) if self.grid[i[1]][i[0]] == 1]
            if unvisited:
                ncur=choice(unvisited)
                stack.append(ncur)
                midx=(cur[0]+ncur[0])//2
                midy=(cur[1]+ncur[1])//2
                self.grid[midy][midx]=0
                self.grid[ncur[1]][ncur[0]]=0
            else:
                if target and place==1:
                    self.grid[cur[1]][cur[0]]=target
                    place*=-1
                stack.pop()


m=MakeMaze(13,13)
m.generate(2)
for n in m.grid:
    print(n)
