def powerset(array):
    # Write your code here.
    subset=[[]]
    for ele in array:
        for i in range(len(subset)):
            current_subset=subset[i]
            subset.append(current_subset +[ele] )
    return subset
    
print powerset([1,2,5])
