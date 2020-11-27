class Node:
  # creating a node instance
  def __init__(self,data):
    self.data=data
    self.next=None

class LinkedList:
   # creating a LinkedList instance
  def __init__(self):
    self.head=None
  # adds elements to beginning of LinkedList
  def push(self,new_data):
    new_node = Node(new_data)
    new_node.next=self.head
    self.head=new_node

  def addTwoLists(self,first,second):
    prev=None
    carry = 0
    # stopping condition ensures that all numbers are summed even if length isn't the same
    # carry initilized to zero as we haven't done any calculation
    while (first is not None or second is not None):
      # ensures that uneven LinkedList are summed properly
      fdata = 0 if first is None else first.data
      sdata = 0 if second is None else second.data
      total = carry + fdata + sdata
      # similar to normal addition where we carry the extra term
      carry = 1 if total >= 10 else 0
      # result left after we carry
      total = total%10
      # node with results
      temp=Node(total)
      # this head is from the results instance not to be confused with first and second heads
      if self.head is None:
        self.head =  temp
      else:
        prev.next = temp
      prev = temp
      # continue updating first and second
      if first is not None:
        first = first.next
      if second is not None:
        second = second.next
    # if carry had a term, it's appended to end of LinkedList
    if carry !=0:
      temp.next=Node(carry)
# Driver code
first = LinkedList()
second = LinkedList()
 
# Create first list
first.push(3)
first.push(1)
first.push(5)

print("First List is ")
first.printList()
 
# Create second list
second.push(5)
second.push(9)
second.push(2)
print ("\nSecond List is ")
second.printList()
 
# Add the two lists and see result
res = LinkedList()
res.addTwoLists(first.head, second.head)
print("\nResultant list is ")
res.printList()