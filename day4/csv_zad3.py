import pandas
#  pip install pandas

data = pandas.read_csv('records_discount.csv', delimiter=";")
print(data)
#    sku  exp_date  price
# 0    1     today    200
# 1    2     today    100
# 2    3  tomorrow    500
# 3    4     today   2000
# 4    5     today   1200
# 5    6  tomorrow    700

print(data.columns)
# Index(['sku', 'exp_date', 'price'], dtype='str')

print(data.values)
# [[1 'today' 200]
#  [2 'today' 100]
#  [3 'tomorrow' 500]
#  [4 'today' 2000]
#  [5 'today' 1200]
#  [6 'tomorrow' 700]]