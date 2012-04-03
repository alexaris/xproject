# -*- coding: utf-8 -*
from collections import deque

class History():
	maxlen = 5
	def __init__(self):
		self.queue = deque()

	def size(self):
		return len(self.queue)

	def add(self, astring):
		if astring == '': return
		if astring in self.queue: return
		if len(self.queue) >= History.maxlen:
			self.queue.popleft()
		self.queue.append(astring)


