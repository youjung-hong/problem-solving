# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 링크드리스트 iterate
        prev = None
        cur = head
        node_index_map = set()
        while cur: 
          # 이미 방문했으면 인덱스를 반환 
          if cur in node_index_map:
            return cur
          # 노드와 인덱스를 맵
          node_index_map.add(cur)
          prev = cur
          cur = cur.next
        
        # 사이클이 없으면 -1
        return None