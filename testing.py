import timeit
cy = timeit.timeit('example.test(5)',setup = 'import example',number=10000)
py = timeit.timeit('example1.test(5)',setup = 'import example1',number=10000)

print(cy,py)
print(py/cy)