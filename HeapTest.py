# CS2302
# Elijah Pele
# Lab 5
#
# Instructor: Diego Aguirre
# TA: Manoj Pravaka Saha
# Last Modified: 11/29/2018
#
# The purpose of this lab is to familiarize ourselves with
# the Heap data structure. We were asked to complete and test
# the methods for the given Heap class.
from MinHeap import Heap  
heap = Heap()
heap.insert(20)
heap.insert(12)
heap.insert(15)
heap.insert(17)
heap.insert(43)
heap.insert(14)
heap.insert(0)
print(heap.heap_array)