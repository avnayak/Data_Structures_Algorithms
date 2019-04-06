class Solution:
#Using two-pointer approach
#leetcode 876
    def middleNode(self,head):
        slow, fast = head,head
        while fast and fast.next:
            fast=fast.next.next
            slow=slow.next
        return slow
