```python
'''
Jiajun Li, A16635772
Academic Integrity Policy: Integrity of scholarship is essential for an academic
community. The University expects that both faculty and students will honor this
principle and in so doing protect the validity of University intellectual work. For
students, this means that all academic work will be done by the individual to
whom it is assigned, without unauthorized aid of any kind. By including this in
my report, I agree to abide by the Academic Integrity Policy.
'''
```
```python
from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all"
import numpy as np
```
```python
#Programming with Matrices
# i
# Create a matrix
A = np.array([[60,-15,12,22,68],
                   [-97, 28,91,-49,7],
                   [9,57,-91,91,-88],
                   [29,-92,42,38,99],
                   [-58,91,90,95,-62]])
B = np.array([[1,1,0,1,1],
                   [1, 0,1,1,0],
                   [1,0,0,1,0],
                   [1,1,0,0,1],
                   [0,0,1,0,0]])
```


```python
# ii
for row in range(len(A)):
    for col in range(len(A[row])):
        if A[row][col] < -70:
            print("val",A[row][col],"in row",row+1,"and col",col+1)


    val -97 in row 2 and col 1
    val -91 in row 3 and col 3
    val -88 in row 3 and col 5
    val -92 in row 4 and col 2
    

```
```python
# iii
C = np.multiply(A,B)
C

    array([[ 60, -15,   0,  22,  68],
           [-97,   0,  91, -49,   0],
           [  9,   0,   0,  91,   0],
           [ 29, -92,   0,   0,  99],
           [  0,   0,  90,   0,   0]])


```

```python
# iv
np.inner(C[:,2],C[4,:])

    0
```
```python
# v
C[:,3].max()
arr = C[:,3]
row_pos = np.where(arr == 91)[0][0]
print("val", C[:,3].max(), "in row", row_pos+1, "and col", 4)

    91

    val 91 in row 3 and col 4
    

```
```python
# vi
D = np.multiply(C[0,:],C)
D

    array([[ 3600,   225,     0,   484,  4624],
           [-5820,     0,     0, -1078,     0],
           [  540,     0,     0,  2002,     0],
           [ 1740,  1380,     0,     0,  6732],
           [    0,     0,     0,     0,     0]])


```

```python
# vii
np.inner(D[:,2],D[4,:])

    0

```
```python
# Robot Traversal
# i)
# - The loc keeps track of the position of the robot.
# - The robot should moves one step to south.
# - If a object is placed at [3,6], the path is blocked and 
#   the robot stays.
# - The robot would not be considered an intelligent system 
#   because it cannot acquire and apply knowledge. 


# ii)
# The robot is now more intelligent than part i because this time
# it can acquire information and take reactions to it.
```
![alt text](/2.2.png)
```python
# iii)
# 
```
![alt text](/2.3.png)
```python
# iv)
# 
```
![alt text](/2.4.png)

```python
# 3.1 i)
# Bug 1:
#       Upper bound = 150 + 1.5*(400+8*5) = 810
#       Lower bound = 150
# ii)
# Bug 2:
#       Upper bound = 150 + 0.5*(2*(400+8*5)) = 590
#       Lower bound = 150
```
```python
# 3.2 i)
# All three can reach the end point
# ii)
    # Bug 2 would result in the least distance traveled 
    # because if you connect the end and start point with 
    # a straight line, the only obstacle is Geisel library
    # which intersect the line twice. From upper bound calculation
    # for Bug 2 and 1, we can tell Bug 2 has lower upper bound
    # than Bug 1. If we use Bug 0, we would face 2 obstacles 
    # since Bug 0 wont follow the straight line that connect from 
    # start to end but walking in the direction which head toward 
    # the end while walking.
```

```python
# 3.3 i)
# All three can reach the end point
# ii)
# Bug 2 would result in least distance traveled because it will ahve
# lower upper bound than Bug 1 and following more straight line from 
# start to end than Bug 0.
# iii)
```

```python
# 3.4 i)
# Bug 0 cannot reach the end point
# ii )
# Bug 2 would result in least distance traveled because it will ahve
# lower upper bound than Bug 1.
```

```python
# iii )
```
![alt text](/3.2.1.png)
![alt text](/3.2.2.png)
![alt text](/3.2.3.png)
```python
# 4 
# 1) The expected value for number of correct predictions out of 100 is 50
# 2) - The first puzzle is showing one block with graphics on it but the other does not.
#    Also, the test image has different size and rotation angle.
#    - The second puzzle is showing square and triangle, and the test image is the same as
#    one of the image in the block.
#    - The third puzzle is showing only square in triangle in two blocks but the test image
#    has different size and position than the image in the block.
#    - The last puzzle is showing more different kinds of graphics such as pentagon and hexagon.
#    The test image also has different size and angle than the image given.
# 3) For the first puzzle, I find the pattern that one of the block is empty, therefore,
#    instead of testing the shape of block and test image, I test whether the block is
#    blank. If yes, my test image should be the same as the other one. For the second puzzle,
#    I found that one of the block is the exact same as the test image. Therefore, beside finding 
#    the shape of test image, I test whether one of the block is the same as the test image.
#    If yes, then that block is the corrent answer. For the last two puzzles, I cant find the 
#    pattern of blocks and test images. I used OpenCV to identify the shape of input and test 
#    image. If they are the same, then it's the answer for the puzzle. For OpenCV, it takes binary 
#    image in and find the number of contours of the image. The number of the contours will identify
#    the shape of the image.
# 4) For the first two puzzles, I dont think my code as an example of intelligent
#    system because it does not have the ability to acquire and apply knowledge.
#    But for the last two codes, I think they can be accounted as intelligent system
#    because it can take in different kinds of shapes and tell which one is it. Besides
#    figuring out the pattern of option and test image, it can now figure out which shape
#    the testing image is.
```
```python
# 5 
```
<p>A warehouse robot which is used to carry goods and help workers can now read human body language. Such robot is used in industry but I believe it can also be employed in public which maintained by household. For internal sensors, it may contains position sensor which knowing its own location. It should also have velocity sensor which should limit it to certain safe speed. For external sensors, I think the most important sensor is the vision sensor because it needs to avoid obstacles and people. Since it is a warehouse robot, it should have the ability to get to the target fast and safe. To fulfill these two requirements, the combination usage of position sensor and vision sensor is essential. It should also have a weight sensor since there must have a maximum of how heavy the robot can carry. If the load exceeds the maximum, it should warn the workers about the dangerous. Since the robot can read human’s body language, the vision sensor should be able to track the motion of human’s body and the face expression. However, it could be difficult because human body language is different from words. It may have much more meaning than sentences. Also, it has less reference for robot to figure out the meaning. Unlike words, which may specifically mean under one context, body language is much more difficult to interpret in binary world. I believe the robot will use the graph search algorithm as motion planning because such algorithm might be the most reliable. In the warehouse, there will be many obstacles on the ground such as ladder and boxes. It might be difficult to guarantee the robot to reach the goal if we use bug algorithm because bug algorithm cannot plan the route ahead. As I have mentioned, besides applying only in industry, I believe the robot can be used in household as well because not only in industries have a lot of heavy boxes, also in household will carry heavy furniture. I think this robot can reduce human labor and easier to operate because it has the ability to read human body language. It is also easy for people who do not have good technological skills. Some people may worry about the artificial intelligent because now they have the ability to decode human’s body language. This means human has less secrete to robot, which may bring panic to the public. It might be a step towards that robotics overcome human.
</p>
