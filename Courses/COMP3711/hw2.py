k = 114
n = 514
A = []
G = []
def INIT(G):
	pass
def COMPARE(a,b):
	pass
def INCREASE(a,b):
	pass


INIT(G)
chunk_len = n//k
for j in range(k): # from 0 to k-1, both inclusive
	count(j*chunk_len+1,(j+1)*chunk_len if j<k-1 else n) # sepertate to k chunks, last chunk contain all remaining elements

def count(start, end):
	# base case
	if end<start :
		return
	
	# notation // means floor devision
	mid = (start+end)//2
	
    # base case for last element
	if mid==n: 
		INCREASE(mid,mid)

	# if A[mid] and A[mid+1] is not in same group
	if not COMPARE(mid,mid+1):
		# codes here execute for k-1 times
		INCREASE(mid,mid)
		INCREASE(mid+1,-mid)
		
    start = start

    if start==end:
	count(start,mid)
	count(mid+1,end)
