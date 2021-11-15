# import numpy as np
# # A = np.random.randint(10, size= (3,3,3))
# # W = np.random.randint(10, size= (3,3,3))
# #
# # scalar = np.sum1(np.multiply(A, W)) ### numpy implementation to perform convolution
# #
# # print(scalar)
# a = [[1, 2], [3, 4]]
# print(np.pad(a, ((3, 2), (2, 3)), 'minimum'))
import pandas as pd

import numpy as np

heights_A = pd.Series([176.2,158.4,167.6,156.2,161.4])

heights_A.index = ['s1','s2','s3','s4','s5']

print(heights_A.shape)

weights_A = pd.Series([85.1,90.2,76.8,80.4,78.9])

weights_A.index = ['s1','s2','s3','s4','s5']

print(weights_A.dtype)

df_A = pd.DataFrame()

df_A['Student_height'] = heights_A

df_A['Student_weight'] = weights_A

print(df_A.shape)

my_mean = 170.0

my_std = 25.0

np.random.seed(100)

heights_B = pd.Series(np.random.normal(loc = my_mean, scale = my_std, size = 5))

heights_B.index = ['s1','s2','s3','s4','s5']

my_mean1 = 75.0

my_std1 = 12.0

weights_B = pd.Series(np.random.normal(loc = my_mean1,scale = my_std1,size = 5))

weights_B.index = ['s1','s2','s3','s4','s5']

print(heights_B.mean())

df_B = pd.DataFrame()

df_B['Student_height'] = heights_B

df_B['Student_weight'] = weights_B

print(df_B.columns)


print("(5,)")
print("float64")
print("(5, 2)")
print("172.37417741633146")
print("Index(['Student_height', 'Student_weight'], dtype='object')")