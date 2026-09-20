import math


def main():
    T = int(input())
    if T == 1:
        print("I love Luogu!")
    elif T == 2:
        print(2 + 4, 10 - 2 - 4)
    elif T == 3:
        print(14 // 4)
        print(14 - (14 % 4))
        print(14 % 4)
        pass
    elif T == 4:
        t4 = 500/3
        print(f"{t4:.6g}")
        pass
    elif T == 5:
        for n in range(20):
            if n * 12 + n * 20 == 220 + 260:
                print(int(n))
                break
        pass
    elif T == 6:
        t = math.sqrt(9**2+6**2)
        print(f"{t:.6g}")
        pass
    elif T == 7:
        a = 100+10
        b = a-20
        c = 0
        print(f"{a}\n{b}\n{c}")
        pass
    elif T == 8:
        Pi=3.141593
        r = 5
        l = 2*Pi*r
        s = Pi*r**2
        q = (4/3)*Pi*r**3
        print(f"{l:.6g}\n{s:.6g}\n{q:.6g}")
        pass
    elif T == 9:
        t4 = 1
        t3 = (t4+1)*2
        t2 = (t3 + 1) * 2
        t1 = (t2 + 1) * 2
        print(t1)
        pass
    elif T == 10:
        x = (8*30-60)/24
        y = 8*30-30*x
        n = (y+10*x)/10
        print(int(n))
        pass
    elif T == 11:
        n = 100/3
        print(f"{n:.6g}")
        pass
    elif T == 12:
        idx = ord("M") - ord("A") + 1
        c_18 = chr(ord("A") + 18 - 1)
        print(f"{idx}\n{c_18}")
        pass
    elif T == 13:
        Pi = 3.141593
        r1 = 4
        r2 = 10
        v1 = 4/3 * Pi * r1**3
        v2 = 4 / 3 * Pi * r2 ** 3
        v=v1+v2
        l = v**(1/3)
        print(int(l))
        pass
    elif T == 14:
        #a=1,b=-100,c=2400
        p1 = (100+math.sqrt(100**2 - 4*1*2400))/2*1
        p2 = (100 - math.sqrt(100 ** 2 - 4 * 1 * 2400)) / 2 * 1
        p1 = 110 - p1
        p2 = 110 - p2
        p = min(p1,p2)
        print(int(p))
        pass

if __name__ == "__main__":
    main()
