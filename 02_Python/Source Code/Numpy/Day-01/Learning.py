# import numpy as np
#
# # 1D array
# a = np.array([10,20,30,40,50])
# # print(a)
#
# # 2D array
# b = np.array([[1,2,3],
#               [4,5,6],
#               [7,8,9]])
# # print(b)
#
# # 3D array
#
# c = np.array([[[1,2], [3,4]],[[5,6],[7,8]]])
# # print(c)
# # print(c.ndim)
#
# # Force a specific data type
#
# d = np.array([1.5, 2.7, 3.3], dtype=int)
# # print(d)

# z = np.zeros((3,3), dtype=int)
# print(z)

# o = np.ones((3,3), dtype=int)
# print(o)

# f = np.full((3,3),5)
# print(f)

# I = np.eye(4)
# print(I)

# print(np.arange(1, 10))
# print(np.arange(1, 20, 2))
# print(np.arange(10, 1, -1))
# print(np.arange(0.0, 1.0, 0.2))

# x = np.linspace(0,1,5)
# print(x)

# theta = np.linspace(0, 0.2 * np.pi, 100)
# # print(theta)
# print(np.sin(theta))

# print(np.random.rand(3, 4))
# print(np.random.randn(3, 4))
# print(np.random.randint(1, 101, size=(5, 5)))

# np.random.seed(42)
# print(np.random.rand(3, 3))

# a = np.array([1,2,3,4,5], dtype = np.float32)
# print(a.dtype)

# b = a.astype(np.int32)
# print(b.dtype)

# big_float64 = np.ones((1000, 1000), dtype = np.float64)
# big_float32 = np.ones((1000, 1000), dtype = np.float32)

# print(big_float64.nbytes)
# print(big_float32.nbytes)

# a = np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12]])
#
# print(a.ndim)
# print(a.shape)
# print(a.size)
# print(a.itemsize)
# print(a.dtype)
# print(a.nbytes)


# a = np.array([82, 95, 45, 80, 76, 69, 49, 46, 60, 56])
#
# print(a >= 50)
# print(a[a >= 50])
# print(a[a < 50])

# a = np.array([[1,2,3,4],
#               [5,6,7,8],
#               [9,10,11,12]])

# print(a[0,0])
# print(a[:,0])
# # This both works same
# print(a[2,:])
# print(a[2])

# print(a[-1,-1])
# print(a[0:3, 0:2])


# original = np.array([1,2,3,4,5, 6, 7, 8])
# view = original[1:4]
# clone = original.copy()
#
# view[0] = 69
# print(view)
# print(clone)

# a = np.array([5,6,7,8])
# b = np.array([1,2,3,4])

# print(a+b)
# print(a-b)
# print(a*b)
# print(a/b)
# print(a//b)
# print(a%b)
# print(a**b)
# print(a**2)
# print(b**2)
# print(a**a)
# print(b**b)
# print(np.sqrt(a))
# print(np.sqrt(b))
# print(np.cbrt(8))
# print(np.exp(2))

# marks = np.array([72, 85, 91, 60, 78, 95, 55, 88])
#
# print(np.sum(marks))
# print(np.min(marks))
# print(np.max(marks))
# print(np.mean(marks))
# print(np.median(marks))
# print(np.std(marks))
# print(np.var(marks))
# print(np.argmax(marks))
# print(np.argmin(marks))
# print(np.sort(marks))

# sales = np.array([[100,200,150],
#                   [250, 180, 220],
#                   [300, 275, 190]])
#
# print(np.sum(sales ,axis=1)) # Columns
# print(np.sum(sales ,axis=0)) # Rows
# print(np.mean(sales ,axis=0)) # Rows

# prices = np.array([100, 250, 399, 599])
#
# discounted = prices * 0.90 # 10% discount
# print(discounted)
#
# with_gst = prices * 1.18
# print(with_gst)

# a = np.arange(1,13)

# m = a.reshape(3,4)
# # print(m)
#
# m2 = a.reshape(2, -1)
# # print(m2)
#
# m3 = a.reshape(-1,3)
# # print(m3)
#
# flat = m.flatten()
# # print(flat)
#
# rav = m.ravel()
# # print(rav)
#
# t = m.T
# print(t.shape)
# print(t)

# arr = np.array([[[1,2], [3,4]],[[5,6],[7,8]]])
#
# arr2 = np.array([[[np.arange(1,5)], [np.arange(5,9)]],
#                  [[np.arange(9,13)], [np.arange(13,17)]]], dtype=np.int32)
# # print(arr)
# # print(arr2)
# # print(arr2.dtype)
# print(arr2.nbytes)

