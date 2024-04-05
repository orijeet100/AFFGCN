import numpy as np

# Load the npz file
# data = np.load('data/PEMS04/weather.npz')
data = np.load('data/PEMS04/pems04.npz')

# List all the keys (names) of arrays stored in the npz file
# keys = data.files
#
# # Print the keys
# print("Keys in the npz file:", keys)
# #
# # # Access and print the arrays using their keys
# for key in keys:
#     print("Array", key, ":")
#     print(data[key])

# print(data['arr_0'].shape)
print(data['data'])
print(data['data'].shape)

