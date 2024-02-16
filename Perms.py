perm =[]

for i in range(0,10):
    for j in range(0,10):
        if i != j :
            for q in range(0,10):
                 if q != i and q != j:
                     for t in range(0,10):
                        if t != i and t != j and t!=q:
                            for v in range(0,10):
                                 if v != i and v!= j and v != q and v != t:
                                    for b in range(0,10):
                                        if b != i and b != j and b != q and b !=v and b != t:
                                            for p in range(0,10):
                                                 if p != i and p != j and p != q and p != v and p != t and p != b:
                                                     for o in range(0,10):
                                                        if o != i and o != j and o != q and o != v and o != t and o != b and o != p:
                                                            for l in range(0,10):
                                                                  if l != i and l != j and l != q and l != v and l != t and l != b and l != o and l !=p:
                                                                      for z in range(0,10):
                                                                          if z != i and z != j and z != q and z != v and z != t and z != b and z != o and z != p and z != l:
                                                                                perm.append(1000000000*i + 100000000*j + 10000000*q + 1000000*t + 100000*v + 10000*b + 1000*p + 100*o + 10*l + z)

perm.sort()

print(perm[999999])