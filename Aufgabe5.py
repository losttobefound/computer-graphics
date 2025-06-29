def v2_substract(v1, v2) :
    return [v1[0] - v2[0], v1[1] - v2[1]]

def determinant(m) :
    return m[0] * m[3] - m[1] * m[2]

#raster coordinates 
a = [1, 7]
b = [2, 3]
c = [7, 6]

# Zu testender Rasterpunkt
p = [4, 5]

#triangle edges
v_edge_ab = v2_substract(b, a)
v_edge_bc = v2_substract(c, b)
v_edge_ca = v2_substract(a, c)

#from triangle point to pixel
v_ap = v2_substract(p, a)
v_bp = v2_substract(p, b)
v_cp = v2_substract(p, c)

m2_edge1= [
    v_edge_ab[0], v_edge_ab[1],
    v_ap[0], v_ap[1]
]

m2_edge2= [
    v_edge_bc[0], v_edge_bc[1],
    v_bp[0], v_bp[1]
]

m2_edge3= [
    v_edge_ca[0], v_edge_ca[1],
    v_cp[0], v_cp[1]
]

det1 = determinant(m2_edge1)
det2 = determinant(m2_edge2)
det3 = determinant(m2_edge3)

print("Determinanten: ", det1, det2, det3)

if det1 >=0 and det2 >= 0 and det3 >= 0:
    print("Pixel", p, "is inside the triangle")
else:
    print("Pixel", p, "is not inside the triangle")