class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        
        for i in range(len(image)):
            temp=image[i][::-1]
            for j in range(len(temp)):
                if temp[j]==1:
                    temp[j]=0
                else:
                    temp[j]=1
            image[i]=temp
        return image


        