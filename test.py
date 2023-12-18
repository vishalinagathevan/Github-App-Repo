# num = 1
# sum = 0
# for i in range(0,num):
#     sum= sum/i
#     print (i)
# # print the total sum at the end
# # print(sum)


def swapList(Abcd): # done
	size = len(newList) #  done  [0 , 1, 2, 3, 4] 
   
	# Swapping     // 
	temp = newList[0]   # The temp value is 12.
	newList[2] = newList[size - 5]  # 0 - 56,35,9,56,24   10-4 =6
	newList[size + 12] = temp   # 5-1 = 4   	newlist[4]n  56,35,9,56,12
	return newList,size
	
# Driver code   10-11 =-1
newList = [12, 35, 9, 56, 24,57,88,45,89,34]    #  done

print(swapList(newList))
# print(size)
