#!/usr/bin/env python
# coding: utf-8

# <table> <tr>
#         <td  style="background-color:#ffffff;">
#             <a href="http://qworld.lu.lv" target="_blank"><img src="..\images\qworld.jpg" width="25%" align="left"> </a></td>
#         <td style="background-color:#ffffff;vertical-align:bottom;text-align:right;">
#             prepared by <a href="http://abu.lu.lv" target="_blank">Abuzer Yakaryilmaz</a> (<a href="http://qworld.lu.lv/index.php/qlatvia/" target="_blank">QLatvia</a>)
#         </td>        
# </tr></table>

# <table width="100%"><tr><td style="color:#bbbbbb;background-color:#ffffff;font-size:11px;font-style:italic;text-align:right;">This cell contains some macros. If there is a problem with displaying mathematical formulas, please run this cell to load these macros. </td></tr></table>
# $ \newcommand{\bra}[1]{\langle #1|} $
# $ \newcommand{\ket}[1]{|#1\rangle} $
# $ \newcommand{\braket}[2]{\langle #1|#2\rangle} $
# $ \newcommand{\dot}[2]{ #1 \cdot #2} $
# $ \newcommand{\biginner}[2]{\left\langle #1,#2\right\rangle} $
# $ \newcommand{\mymatrix}[2]{\left( \begin{array}{#1} #2\end{array} \right)} $
# $ \newcommand{\myvector}[1]{\mymatrix{c}{#1}} $
# $ \newcommand{\myrvector}[1]{\mymatrix{r}{#1}} $
# $ \newcommand{\mypar}[1]{\left( #1 \right)} $
# $ \newcommand{\mybigpar}[1]{ \Big( #1 \Big)} $
# $ \newcommand{\sqrttwo}{\frac{1}{\sqrt{2}}} $
# $ \newcommand{\dsqrttwo}{\dfrac{1}{\sqrt{2}}} $
# $ \newcommand{\onehalf}{\frac{1}{2}} $
# $ \newcommand{\donehalf}{\dfrac{1}{2}} $
# $ \newcommand{\hadamard}{ \mymatrix{rr}{ \sqrttwo & \sqrttwo \\ \sqrttwo & -\sqrttwo }} $
# $ \newcommand{\vzero}{\myvector{1\\0}} $
# $ \newcommand{\vone}{\myvector{0\\1}} $
# $ \newcommand{\vhadamardzero}{\myvector{ \sqrttwo \\  \sqrttwo } } $
# $ \newcommand{\vhadamardone}{ \myrvector{ \sqrttwo \\ -\sqrttwo } } $
# $ \newcommand{\myarray}[2]{ \begin{array}{#1}#2\end{array}} $
# $ \newcommand{\X}{ \mymatrix{cc}{0 & 1 \\ 1 & 0}  } $
# $ \newcommand{\Z}{ \mymatrix{rr}{1 & 0 \\ 0 & -1}  } $
# $ \newcommand{\Htwo}{ \mymatrix{rrrr}{ \frac{1}{2} & \frac{1}{2} & \frac{1}{2} & \frac{1}{2} \\ \frac{1}{2} & -\frac{1}{2} & \frac{1}{2} & -\frac{1}{2} \\ \frac{1}{2} & \frac{1}{2} & -\frac{1}{2} & -\frac{1}{2} \\ \frac{1}{2} & -\frac{1}{2} & -\frac{1}{2} & \frac{1}{2} } } $
# $ \newcommand{\CNOT}{ \mymatrix{cccc}{1 & 0 & 0 & 0 \\ 0 & 1 & 0 & 0 \\ 0 & 0 & 0 & 1 \\ 0 & 0 & 1 & 0} } $
# $ \newcommand{\norm}[1]{ \left\lVert #1 \right\rVert } $
# $ \newcommand{\pstate}[1]{ \lceil \mspace{-1mu} #1 \mspace{-1.5mu} \rfloor } $

# <h2>Visualization of a (Real-Valued) Qubit</h2>
# 
# [Watch Lecture](https://youtu.be/p4HjmbAmUh8)

# _We use certain tools from python library "<b>matplotlib.pyplot</b>" for drawing. Check the notebook [Python: Drawing](../python/Python06_Drawing.ipynb) for the list of these tools._

# Suppose that we have a single qubit. 
# 
# Each possible (real-valued) quantum state of this qubit is a point on 2-dimensional space.
# 
# It can also be represented as a vector from origin to that point.
# 
# We start with the visual representation of the following quantum states: 
# 
# $$ \ket{0} =  \myvector{1\\0}, ~~ \ket{1} = \myvector{0\\1} , ~~ -\ket{0} = \myrvector{-1\\0}, ~~\mbox{and}~~ -\ket{1} = \myrvector{0\\-1}. $$

# We draw these quantum states as points.
# 
# We use one of our predefined functions for drawing axes: "draw_axes()". We include our predefined functions with the following line of code:
# 
#     %run qlatvia.py

# In[19]:




# import the drawing methods
from matplotlib.pyplot import plot, figure, show

# draw a figure
figure(figsize=(6,6), dpi=80)

# include our predefined functions
get_ipython().run_line_magic('run', 'qlatvia.py')
get_ipython().run_line_magic('run', 'include_drawing.py')
# draw the axes
draw_axes()

# draw the origin
plot(0,0,'ro') # a point in red color

# draw these quantum states as points (in blue, green, yellow, and cyan colors)
plot(1,0,'bo') 
plot(0,1,'go')
plot(-1,0,'yo')
plot(0,-1,'co')

show()


# In[ ]:





# Now, we draw the quantum states as arrows (vectors):

# In[21]:


# import the drawing methods
from matplotlib.pyplot import figure, arrow, show

# draw a figure
figure(figsize=(6,6), dpi=80)

# include our predefined functions
get_ipython().run_line_magic('run', 'qlatvia.py')
get_ipython().run_line_magic('run', 'include_drawing.py')
# draw the axes
draw_axes()

# draw the quantum states as vectors (in red, blue, green, and yellow colors)
arrow(0,0,0.92,0,head_width=0.04, head_length=0.08, color="r")
arrow(0,0,0,0.92,head_width=0.04, head_length=0.08, color="b")
arrow(0,0,-0.92,0,head_width=0.04, head_length=0.08, color="g")
arrow(0,0,0,-0.92,head_width=0.04, head_length=0.08, color="y")

show()


# <h3> Task 1 </h3>
# 
# Write a function that returns a randomly created 2-dimensional (real-valued) quantum state.
# 
# _You can use your code written for [a task given in notebook "Quantum State](B28_Quantum_State.ipynb#task2)._
# 
# Create 100 random quantum states by using your function and then draw all of them as points.
# 
# Create 1000 random quantum states by using your function and then draw all of them as points.
# 
# The different colors can be used when drawing the points ([matplotlib.colors](https://matplotlib.org/2.0.2/api/colors_api.html)).

# In[29]:


def random_quantum_state():
    
    a = randrange(-100, 101)
    b = randrange(-100, 101)
    l_square= a**2 + b**2
    while l_square==0:
         a = randrange(-100, 101)
         b = randrange(-100, 101)
         l_square= (a**2)+(b**2)       
         
    a= a/l_square**0.5
    b= b/l_square**0.5
    return [a,b]


# In[33]:


# import the drawing methods
from matplotlib.pyplot import plot, figure

# draw a figure
figure(figsize=(6,6), dpi=60) 

# draw the origin
plot(0,0,'ro') 

from random import randrange
colors = ['ro','bo','go','yo','co','mo','ko']

#
# your solution is here
#
for i in range(500):
    new_quantum_state=random_quantum_state();
    x=new_quantum_state[0];
    y=new_quantum_state[1];
    plot(x,y,colors[randrange(len(colors))]) 
 # this above one calls in random colors from the list of colors
show()


# <a href="B30_Visualization_of_a_Qubit_Solutions.ipynb#task1">click for our solution</a>

# <h3> Task 2 </h3>
# 
# Repeat the previous task by drawing the quantum states as vectors (arrows) instead of points.
# 
# The different colors can be used when drawing the points ([matplotlib.colors](https://matplotlib.org/2.0.2/api/colors_api.html)).
# 
# _Please keep the codes below for drawing axes for getting a better visual focus._

# In[41]:


# import the drawing methods
from matplotlib.pyplot import plot, figure, arrow

# draw a figure
figure(figsize=(6,6), dpi=60) 

# include our predefined functions
get_ipython().run_line_magic('run', 'qlatvia.py')
get_ipython().run_line_magic('run', 'include_drawing.py')
# draw the axes
draw_axes()

# draw the origin
plot(0,0,'ro') 

from random import randrange
colors = ['r','b','g','y','b','c','m']

#
# your solution is here
#
for i in range(500):
    new_quantum_state=random_quantum_state();
    x=new_quantum_state[0];
    y=new_quantum_state[1];
    x = 0.92 * x
    y = 0.92 * y
    arrow(0,0,x,y,head_width=0.04, head_length=0.08, color=colors[randrange(len(colors))])
# draw the quantum states as vectors (in red, blue, green, and yellow colors)
show()


# <a href="B30_Visualization_of_a_Qubit_Solutions.ipynb#task2">click for our solution</a>

# <h3> Unit circle </h3>
# 
# All quantum states of a qubit form the unit circle.
# 
# The length of each quantum state is 1.
# 
# All points that are 1 unit away from the origin form the circle with radius 1 unit.
# 
# We can draw the unit circle with python.
# 
# We have a predefined function for drawing the unit circle: "draw_unit_circle()".

# In[42]:


# import the drawing methods
from matplotlib.pyplot import figure

figure(figsize=(6,6), dpi=80) # size of the figure

# include our predefined functions
get_ipython().run_line_magic('run', 'qlatvia.py')
get_ipython().run_line_magic('run', 'include_drawing.py')
# draw axes
draw_axes()

# draw the unit circle
draw_unit_circle()


# <h3>Quantum state of a qubit</h3>

# Suppose that we have a single qubit. 
# 
# Each possible (real-valued) quantum state of this qubit is a point on 2-dimensional space.
# 
# It can also be represented as a vector from origin to that point.
# 
# We draw the quantum state $ \myvector{3/5 \\ 4/5} $ and its elements.

# <i style="font-size:10pt;">
# Our predefined function "draw_qubit()" draws a figure, the origin, the axes, the unit circle, and base quantum states.
# <br>
# Our predefined function "draw_quantum_state(x,y,name)" draws an arrow from (0,0) to (x,y) and associates it with <u>name</u>.
# <br>
# We include our predefined functions with the following line of code:
#     
#     %run qlatvia.py
# </i>   

# In[43]:


get_ipython().run_line_magic('run', 'qlatvia.py')
get_ipython().run_line_magic('run', 'include_drawing.py')

draw_qubit()

draw_quantum_state(3/5,4/5,"|v>")


# Now, we draw its angle with $ \ket{0} $-axis and its projections on both axes.
# 
# <i> For drawing the angle, we use the method "Arc" from library "matplotlib.patches". </i> 

# In[49]:


get_ipython().run_line_magic('run', 'qlatvia.py')
get_ipython().run_line_magic('run', 'include_drawing.py')
draw_qubit()

draw_quantum_state(3/5,4/5,"|v>")

from matplotlib.pyplot import arrow, text, gca

# the projection on |0>-axis
arrow(0,0,3/5,0,color="blue",linewidth=1.5)
arrow(0,4/5,3/5,0,color="blue",linestyle='dotted')
text(0.1,-0.1,"cos(a)=3/5")
# the numbers in the text tell you where you place the text 

# the projection on |1>-axis
arrow(0,0,0,4/5,color="blue",linewidth=1.5)
# this line starts at x=0, and stays there
arrow(3/5,0,0,4/5,color="blue",linestyle='dotted')
# this line starts at x=3/5, and stays there
text(-0.1,0.55,"sin(a)=4/5",rotation="90")

# drawing the angle with |0>-axis
from matplotlib.patches import Arc
gca().add_patch( Arc((0,0),0.4,0.4,angle=0,theta1=0,theta2=53) )
text(0.08,0.05,'.',fontsize=30)
text(0.21,0.09,'a')


# <b> Observations: </b>
# <ul>
#     <li> The angle of quantum state with state $ \ket{0} $ is $a$.</li>    
#     <li> The amplitude of state $ \ket{0} $ is $ \cos(a) = \frac{3}{5} $.</li>
#     <li> The probability of observing state $ \ket{0} $ is $ \cos^2(a) = \frac{9}{25} $.</li>
#     <li> The amplitude of state $ \ket{1} $ is $ \sin(a) = \frac{4}{5} $.</li>
#     <li> The probability of observing state $ \ket{1} $ is $ \sin^2(a) = \frac{16}{25} $.</li>
# </ul>

# <h3> The angle of a quantum state </h3>
# 
# The angle of a vector (in radians) on the unit circle is the length of arc in counter-clockwise direction that starts from $ (1,0) $ and with the points representing the vector.
# 
# We execute the following code a couple of times to see different examples, where the angle is picked randomly in each run.
# 
# You can also set the value of "myangle" manually for seeing a specific angle.

# In[45]:


# set the angle

from random import randrange
myangle = randrange(361)

################################################

from matplotlib.pyplot import figure,gca
from matplotlib.patches import Arc
from math import sin,cos,pi

# draw a figure
figure(figsize=(6,6), dpi=60)

get_ipython().run_line_magic('run', 'qlatvia.py')
get_ipython().run_line_magic('run', 'include_drawing.py')

draw_axes()

print("the selected angle is",myangle,"degrees")

ratio_of_arc = ((1000*myangle/360)//1)/1000

print("it is",ratio_of_arc,"of a full circle")

print("its length is",ratio_of_arc,"x 2\u03C0","=",ratio_of_arc*2*pi) 
#u03C0 this is how you call pi in string
myangle_in_radian = 2*pi*(myangle/360)

print("its radian value is",myangle_in_radian)

gca().add_patch( Arc((0,0),0.2,0.2,angle=0,theta1=0,theta2=myangle,color="red",linewidth=2) )
#smaller circle in the middle to show angle

gca().add_patch( Arc((0,0),2,2,angle=0,theta1=0,theta2=myangle,color="brown",linewidth=2) )
#larger circle on the outside
x = cos(myangle_in_radian)
y = sin(myangle_in_radian)

draw_quantum_state(x,y,"|v>")

# the projection on |0>-axis
arrow(0,0,x,0,color="blue",linewidth=1)
arrow(0,y,x,0,color="blue",linestyle='dashed')

# the projection on |1>-axis
arrow(0,0,0,y,color="blue",linewidth=1)
arrow(x,0,0,y,color="blue",linestyle='dashed')

print()
print("the amplitude of state |0> is",x)
print("the amplitude of state |1> is",y)
print()
print("the probability of observing state |0> is",x*x)
print("the probability of observing state |1> is",y*y)
print("the total probability is",round(x*x+y*y,6))


# <h3> Random quantum states </h3>
# 
# Any quantum state of a (real-valued) qubit is a point on the unit circle.
# 
# We use this fact to create random quantum states by picking a random point on the unit circle. 
# 
# For this purpose, we randomly pick an angle between zero and 360 degrees and then find the amplitudes of the quantum state by using the basic trigonometric functions.

# <a id="task3"></a>
# <h3> Task 3 </h3>
# 
# Define a function randomly creating a quantum state based on this idea.
# 
# Randomly create a quantum state by using this function.
# 
# Draw the quantum state on the unit circle.
# 
# Repeat the task for a few times.
# 
# Randomly create 100 quantum states and draw all of them.

# <i> You can save your function for using later: comment out the first command, give an appropriate file name, and then run the cell.</i>

# In[64]:


# %%writefile FILENAME.py 
# your function is here
from math import cos, sin, pi
from random import randrange
from matplotlib.pyplot import figure

get_ipython().run_line_magic('run', 'qlatvia.py')
get_ipython().run_line_magic('run', 'include_drawing.py')
figure(figsize=(6,6), dpi=80) 
draw_axes()
draw_unit_circle()
colors = ['r','b','g','y','c','m','k']
for i in range(100):
    ab=[]
    ab=random_quantum_state()
    x= ab[0]
    y= ab[1]
    arrow(0,0,x,y,head_width=0, head_length=0, color=colors[randrange(len(colors))])
show()


# <i style="font-size:10pt;">
# Our predefined function "draw_qubit()" draws a figure, the origin, the axes, the unit circle, and base quantum states.
# <br>
# Our predefined function "draw_quantum_state(x,y,name)" draws an arrow from (0,0) to (x,y) and associates it with <u>name</u>.
# <br>
# We include our predefined functions with the following line of code:
#     
#     %run qlatvia.py
# </i>  

# In[65]:


from math import cos, sin, pi
from random import randrange
from matplotlib.pyplot import figure

get_ipython().run_line_magic('run', 'qlatvia.py')
get_ipython().run_line_magic('run', 'include_drawing.py')
figure(figsize=(6,6), dpi=80) 
draw_axes()
draw_unit_circle()
colors = ['r','b','g','y','c','m','k']
for i in range(100):
    ab=[]
    ab=random_quantum_state()
    x= ab[0]
    y= ab[1]
    arrow(0,0,x,y,head_width=0, head_length=0, color=colors[randrange(len(colors))])
show()


# <a href="B30_Visualization_of_a_Qubit_Solutions.ipynb#task3">click for our solution</a>
