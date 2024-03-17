class Solution:
    def countPair(self, head1, head2, n1, n2, x):
        '''
        head1:  head of linkedList 1
        head2:  head of linkedList 2
        n1:  len of  linkedList 1
        n2:  len of linkedList 1
        x:   given sum
        '''
        count = 0;    
        us = set() 
      
        # add all the elements of 1st list
        # in the hash table(unordered_set 'us')
        while (head1 != None):   
            us.add(head1.data);    
          
            # move to next node    
            head1 = head1.next;
      
        # for each element of 2nd list
        while (head2 != None):  
     
            # find (x - head2.data) in 'us'
            if ((x - head2.data) in us):
                count += 1
          
            # move to next node
            head2 = head2.next;    
     
        # required count of pairs     
        return count;