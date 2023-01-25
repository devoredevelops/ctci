class Stack(list):
	def peak(self):
		return self[-1]
	def push(self, item):
		self.append(item)
	def empty(self):
		return len(self) == 0

	def sort_stack(self):
		r = Stack()
		while not self.empty():		
			tmp = self.pop()
			while not r.empty() and r.peak() > tmp:
				self.push(r.pop())
			r.push(tmp)
			while not self.empty() and self.peak() >= r.peak():
				#warning, >= here
				r.push(self.pop())
		return r

#testing
from random import randrange
test_items = [randrange(20) for x in xrange(20)]
print test_items
S = Stack()
for item in test_items:
	S.push(item)
S = Stack.sort_stack(S)
for i, item in enumerate(sorted(test_items)):
	print "item", item, S[i]
