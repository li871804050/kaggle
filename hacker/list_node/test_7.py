class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeKLists(self, lists) -> ListNode:
        min = lists[0].val
        head = None
        listPos = [lists[x] for x in range(len(lists))]
        while True:
            for i in range(len(listPos)):
                if listPos[i] == None:
                    listPos.pop(i)
                elif listPos[i].val <= min:
                    min = listPos[i].val
            if len(listPos) == 0:
                break
            if head == None:
                head = ListNode(min)
                listPos[i] = listPos[i].next
        return head

def isMatch(s: str, p: str) -> bool:
   m = [[0 for x in range(len(s) + 1)] for y in range(len(p) + 1)]
   m[0][0] = 1
   for i in range(len(p)):
       if p[i] == '*':
           for k in range(len(s) + 1):
               if m[i][k] == 1:
                    m[i + 1][k] = 1
           for k in range(len(s) + 1):
               if m[i + 1][k] == 1:
                   for j in range(k, len(s)):
                       if p[i - 1] == s[j] or p[i - 1] == '.':
                           m[i + 1][j + 1] = 1
                       else:
                           break
           if i - 1 >= 0:
               for k in range(len(s) + 1):
                   if m[i - 1][k] == 1:
                       m[i + 1][k] = 1
       else:
           for j in range(len(s)):
               if m[i][j] == 1:
                   if p[i] == '.' or p[i] == s[j]:
                       m[i + 1][j + 1] = 1

   if m[len(p)][len(s)] == 1:
       return True
   else:
       return False

def isMatch2(s: str, p: str) -> bool:
   m = [[0 for x in range(len(s) + 1)] for y in range(len(p) + 1)]
   m[0][0] = 1
   for i in range(1, len(p)):
       if p[i] == '*':
           for k in range(len(s) + 1):
               if p[i][k - 1] == 1:
                   p[i][k] = 1



       else:
           for j in range(len(s)):
               if m[i][j] == 1:
                   if p[i] == '?' or p[i] == s[j]:
                       m[i + 1][j + 1] = 1

   if m[len(p)][len(s)] == 1:
       return True
   else:
       return False


if __name__ == '__main__':
    a = "mississippi"
    b = "mis*is*p*."
    # a =  "aab"
    # b =  "c*a*b"
    print(isMatch(a, b))