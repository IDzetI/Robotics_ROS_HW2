****Six-link manipulator Arkodim (6R)****

Robot has 6 revolute joints and 6 links.

![Image alt](https://github.com/IDzetI/Robotics_ROS_HW2/blob/master/pictures/arkodim1.jpg)
![Image alt](https://github.com/IDzetI/Robotics_ROS_HW2/blob/master/pictures/arkodim2.jpg)
![Image alt](https://github.com/IDzetI/Robotics_ROS_HW2/blob/master/pictures/arkodim3.jpg)
![Image alt](https://github.com/IDzetI/Robotics_ROS_HW2/blob/master/pictures/arkodim4.jpg) 

1st joint is rotating around z-axis with limit [-180; 180]\
2nd joint is rotating around y-axis with limit [-138; 64]\
3rd joint is rotating around y-axis with limit [-124; 124]\
4th joint is rotating around z-axis with limit [-180; 180]\
5th joint is rotating around y-axis with limit [-141; 141]\
6th joint is rotating around z-axis without limit 

Length of links show on pictures.


**Inverse kinematic**

Work in wolfram mathematica.

Set a translation matrices:
![Image alt](https://github.com/IDzetI/Robotics_ROS_HW2/blob/master/pictures/m1.PNG)
![Image alt](https://github.com/IDzetI/Robotics_ROS_HW2/blob/master/pictures/m2.PNG)
![Image alt](https://github.com/IDzetI/Robotics_ROS_HW2/blob/master/pictures/m3.PNG)
![Image alt](https://github.com/IDzetI/Robotics_ROS_HW2/blob/master/pictures/m4.PNG)
![Image alt](https://github.com/IDzetI/Robotics_ROS_HW2/blob/master/pictures/m5.PNG)

![Image alt](https://github.com/IDzetI/Robotics_ROS_HW2/blob/master/pictures/sol0.PNG)

solve for q1, q2 and q3 using fsolve function

![Image alt](https://github.com/IDzetI/Robotics_ROS_HW2/blob/master/pictures/sol1.PNG)

Find the Euler angles for q4, q5 and q6

![Image alt](https://github.com/IDzetI/Robotics_ROS_HW2/blob/master/pictures/sol2.PNG)




