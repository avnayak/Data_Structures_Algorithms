class Solution:
#Using two-pointer approach
#leetcode 141
    def hasCycle(self,head):
        slow, fast = head,head
        while fast and fast.next:
            fast=fast.next.next
            slow=slow.next
        if fast == slow:
		return True 
	return False
