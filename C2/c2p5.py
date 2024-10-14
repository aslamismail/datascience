print("23mca022")
print("Aslam Ismail")
print("29-07-24")
import numpy as np
even_numbers=np.arange(2,31,2)
slice_result=even_numbers[2:9:2]
last_3_elements=even_numbers[-3:]
alternate_elements=even_numbers[::2]
last_3_alternate_elements=alternate_elements[-3:]
print("Original Array: ",even_numbers)
print("Elements from index 2 to 8 with step2: ",slice_result)
print("Last 3 elements of array using negative index: ",last_3_elements)
print("Alternate elements of array:",alternate_elements)
print("Last 3 alternate elements: ",last_3_alternate_elements)

