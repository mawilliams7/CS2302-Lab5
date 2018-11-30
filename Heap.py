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
#  the methods for the given Heap class.
# (mawilliams7) Consider writing function docstrings to make method purpose more clear
class Heap:
    def __init__(self):
        self.heap_array = []
        
    def insert(self, k):
        self.heap_array.append(k)
        self.min_heap_sort()
        
    def extract_min(self):
        if self.is_empty():
            return None
        min_elem = self.heap_array[0]
        i = 0
        left = 2*i+1
        right = 2*i+2
        # (mawilliams7) I would separate this logic into another method as extract min should only be doing one task (extracting min)
        # The while loop will make sure
        # all valid postiions in the heap are populated
        # after extracting the minimum from the root.
        while(right < len(self.heap_array)):
            if(self.heap_array[left] > self.heap_array[right]):
                new_min = self.heap_array[right]
                index = right
            else:
                new_min = left
                index = left
            self.heap_arrayarray[i] = new_min
            i = index
            right = 2*i+1
            left = 2*i+2           
        return min_elem
    
    def is_empty(self):
        return len(self.heap_array) == 0
    
    def min_heap_sort(self):
        if(self.is_empty == 0):
            return       
        # Will check every elment starting from the end of the array to the ith index.
        # (mawilliams7) This logic could be implemented in a single while loop. Unnecessary comparisons made in this implementation
        for i in range(len(self.heap_array)):
            k = len(self.heap_array) -1
            while(k >= i): 
                # If an elements child is smaller than itself, they swap postions.
                if(self.heap_array[k-1//2] < self.heap_array[i]):
                    temp = self.heap_array[k-1//2]
                    self.heap_array[k-1//2] = self.heap_array[i]
                    self.heap_array[i] = temp  
                k-=1
        return
