import numpy as np

tensor = [[[1,2,3,4],[1,2,3,4],[1,2,3,4]],
            [[1,2,3,4],[1,2,3,4],[1,2,3,4]],
            [[1,2,3,4],[1,2,3,4],[1,2,3,4]]]
tensor=np.array(tensor, int)
print(tensor)
print(tensor.shape)#텐서의 모양 (z,y,x)
print(tensor.ndim)#텐서의 차원
print(tensor.size)#(x*y*z)