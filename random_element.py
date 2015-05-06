import random

def random_element(stream, k = 1):
   selected_elements = {}

   key_counter = 0
   for elem in stream:
       if len(selected_elements) < k:
           selected_elements[key_counter] = elem
       else:
           sample_random = random.randrange(0,key_counter)
           if sample_random in selected_elements:
               selected_elements.pop(sample_random, None)
               selected_elements[key_counter] = elem
       key_counter += 1
   return [v for k, v in selected_elements.iteritems()]

print random_element(xrange(500000), 2)