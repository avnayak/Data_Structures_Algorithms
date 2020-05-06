def spiralMatrix(A):
    m,n = len(A),len(A[0])
    count =0 
    sr,sc=0,0
    ans=[]
    er,ec=m-1,n-1
    while sr <= er and sc<= ec:
            for i in range(sc,ec+1):
                ans.append(A[sr][i])
                count +=1
            sr+=1
            if count == m*n:
                return ans
            for i in range(sr,er+1):
                ans.append(A[i][ec])
                count+=1
            ec-=1
            if count == m*n:
                return ans
            for i in range(ec,sc-1,-1):
                ans.append(A[er][i])
                count +=1
            if count == m*n:
                return ans
            er -=1
            for i in range(er,sr-1,-1):
                ans.append(A[i][sc])
                count+=1
            if count == m*n:
                return ans
            sc +=1
    return ans

A=[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ],
[10,11,12]
]

print spiralMatrix(A)
