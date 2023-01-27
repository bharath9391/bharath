def multi(m):
    def multy(n):
        result=m*n
        return result
    return multy
multi3times=multi(3)
multi5times=multi(5)
result_3=multi3times(4)
result_5=multi5times(4)
print(result_3,result_5)
