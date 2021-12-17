p2 = 0
ans = 0
for DX in range(400):
    for DY in range(-300, 1000):
        ok = False
        max_y = 0
        x = 0
        y = 0
        dx = DX
        dy = DY
        for t in range(1000):
            x += dx
            y += dy
            max_y = max(max_y, y)
            if dx > 0:
                dx -= 1
            elif dx < 0:
                dx += 1
            dy -= 1
            if 277<=x<=318 and -92<=y<=-53:
                ok = True
        if ok:
            p2 += 1
            if max_y > ans:
                ans = max_y
                print(DX,DY,ans)
print("part 1: ",ans)
print("part 2: ",p2)