from typing import Optional

class Node:

  def __init__(self, data: int, next: Optional['Node']=None):
    self.data = data
    self.next = next

class Head:

  def __init__(self):
    self.head = None

  def print(self):
    p = self.head
    print("\n[', end='")
    while p:
      print(f'{p.data} ', end='')
      p = p.next
    print(']')

  def insert(self, data: int):
    lk = Node(data)
    lk.next = self.head
    self.head = lk

if __name__ == '__main__':
  pointer = Head()
  pointer.insert(1)
  pointer.insert(2)
  pointer.insert(3)
  pointer.insert(4)
  pointer.insert(5)
  pointer.print()
















