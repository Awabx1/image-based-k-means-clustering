# image-based-k-means-clustering
Define color-based clusters using K-means on any image


K=2
![image](https://github.com/Awabx1/image-based-k-means-clustering/assets/103901752/1a60c81c-c19b-4ebe-ae0a-32e153e621f3)


K=3
![image](https://github.com/Awabx1/image-based-k-means-clustering/assets/103901752/b489814f-ed95-4585-8bf3-02188c77f02e)


K=5
![image](https://github.com/Awabx1/image-based-k-means-clustering/assets/103901752/0306ebe5-7e81-4420-9db9-d49349cb3d13)

 
K=10
![image](https://github.com/Awabx1/image-based-k-means-clustering/assets/103901752/d9f0e39c-22c0-428c-b13e-fccf974adff0)


K=15
![image](https://github.com/Awabx1/image-based-k-means-clustering/assets/103901752/ca2df2f7-2d0b-44f9-b9b8-3b669db1e8bb)


K=20
![image](https://github.com/Awabx1/image-based-k-means-clustering/assets/103901752/17d13358-a8aa-445d-b234-7bc90b3fc892)


Notes:
We can see that with the increasing number of clusters (k), the image gets better and better to look at. However, with k just being equal to 2, it hard to depict almost anything on the face, k=3 is much better suited given the low execution time as well. However, if we were to use this for some face recognition program, k=10 could give us ideal results and we would not need to go any further. We can even achieve facial landmark information then. 
I have set the number of iterations to 10 as it provided almost the same results.
 
I tested with iterations=10 3 times to get execution times of this. We can see that the difference between k=2 and k=20 is almost 9 times. So it is safe to say that we the increase in time is directly proportional to the number of clusters. Also, with an image of a bigger size, the times would scale up.
![image](https://github.com/Awabx1/image-based-k-means-clustering/assets/103901752/dd0575f3-e499-4e6d-b682-e1957834ce59)

Limitation:
In some cases, since the clusters are being initialized randomly, the clusters end up with no points assigned to them and we get a broken output. To fix this, we can add an additional check to either force clustering or choose such clusters which have at least one point near them.
