import sys

in_file = sys.argv[1] if len(sys.argv) > 1 else "input"
with open(in_file, 'r') as f:
    data = f.read().splitlines()
    
nb = [[x for x in l] for l in data]

s = 0
for r in range(len(nb)):
    for c in range(len(nb[r])):
        n = nb[r][c]
        
        all_vis = False
        vis = all(nb[x][c] < n for x in range(r))
        all_vis = all_vis or vis
        
        if not all_vis:
            vis = all(nb[x][c] < n for x in range(r+1, len(nb)))
            all_vis = all_vis or vis
        
        if not all_vis:
            vis = all(nb[r][x] < n for x in range(c))
            all_vis = all_vis or vis
                    
        if not all_vis:
            vis = all(nb[r][x] < n for x in range(c+1, len(nb[r])))
            all_vis = all_vis or vis
                
        s += int(all_vis)
print(s)


mx = 0
for r in range(1, len(nb)-1):
    for c in range(1, len(nb[r])-1):
        n = nb[r][c]
        a, b, c_, d = 0, 0, 0, 0
        
        for r2 in range(r-1, -1, -1):
            a += 1
            if nb[r2][c] >= n:
                break
        
        for r2 in range(r+1, len(nb)):
            b += 1
            if nb[r2][c] >= n:
                break
            
        for c2 in range(c-1, -1, -1):
            c_ += 1
            if nb[r][c2] >= n:
                break
            
        for c2 in range(c+1, len(nb[r])):
            d += 1
            if nb[r][c2] >= n:
                break
        mx = max(mx, a*b*c_*d)
print(mx)