# Data-Structure Project

This project's menu is in console, the main focus is on the algorithms.

This project is for restaurant administraition for following matarials 
 * storing customer's data 
 * storing foods and their requirments 
 * geting service and finding the shortes path to deliver the food
 * finding the shortest path among all the tables
 * asigning turns to each customer that enters & taking their services by their priority 


## Welcome page 
* This welcome will be shown for 4 seconds then the main menu will apear.

<img src="Guide/1.png" width="600">

# Main menu 
* This program contains 4 different part each one will be expalined later 

<img src="Guide/2.png" width="600">


## 1. Customer Acceptance 

* In this part you may add customer's information saud as follow 

<img src="Guide/3.png" width="600">

## 2. Delivery

* In order to use all functions in this part first you may enter the restaurant 's map , if you don't do so you'll be warned.
    Map's enteries should have the following format with opetional number of size and characters place :
      #+#+$++++#
      +#++#+###+
      a+###++#++
      +#++#+b+#+
      #+c+#+++##
      ++#+##++++
      ##+#+##+++
      ++++#e#+##
      ++#++##+#+
      d####+++#+
      * English characters(a,b,..c) are presented as tables.
      * $ is used as kitchen .
      * # shows the obstacles in waitress way to deliver food.
      Other testcases for map can be find here {https://github.com/Mitraaaaa/Restaurant/tree/main/Maps}.
      
### Deliver Fucntions 
  * 1. Finding the shortest path (Bfs is used for the calculating the following function).
  * 2. Finding the shortest path crossing all the nodes (Travel’s salesman problem) --> (Dynamic Programming and Recursive algorithm is used for this part.)
  * 3. Finding the shortets path between to tables.

<img src="Guide/4.png" width="600">
        
