To compare the TDMA function with an LU decomposition we first put both functions in one code to be ran at the same time. For the LU decomposition we decided to use _lu_factor_ and _lu_decompose_ from the _scipy.linalg_ library. The execution time was counted with _clock()_ from the _time_ library in Python. The counting  started at the start of the recursive algorithm, and were stopped immediately after.

The code is available in _Project-1/Code/Python/tdma_compare_lu.py_ in our github repository.

|          |      TDMA      |LU decomposition |
|----------|-------------:|------:|
| $n=  10$  |  $0.000045s$ | $0.000151s$ |
| $n= 100$  |    $0.002442s$   |  $0.002045s$ |
| $n= 1000$ | $0.026847s$ |    $0.131573s$|

The table is a bit confusing since for $n=100$ the LU decomposition is faster than the TDMA method, but the general trend is that the TDMA method is wildly superior.

If the LU decomposition is run with a $10^5\times 10^5$ matrix, we quickly run out of RAM. This is because every matrix element takes up 8Bytes, which in our case adds up to 80Gigabytes.
