# Data-Structure Project

## This project's menu is in console, the main focus is on the algorithms.

## This project is for restaurant administraition for following matarials 
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
 * "$" is used as kitchen .
 * "#" shows the obstacles in waitress way to deliver food.
 Other testcases for map can be find here { https://github.com/Mitraaaaa/Restaurant/tree/main/Maps }.
      
### Deliver Fucntions 
  **Finding the shortest path (Bfs is used for the calculating the following function).
  **Finding the shortest path crossing all the nodes (Travel’s salesman problem) --> (Dynamic Programming and Recursive algorithm is used for this part).
  **Finding the shortets path between to two desired table.

<img src="Guide/4.png" width="600">

* Maps entery :
<img src="Guide/5.png" width="600">


* Shortest path from kitchen to any optional table you desire : 
<img src="Guide/6.png" width="600">


* Shortest path length passing all the tables :
<img src="Guide/7.png" width="600">
 
 
* Shortest path between two desired tables :
<img src="Guide/8.png" width="600">

## 3. Kitchen 
* Algorithms of this part are Graph algorithms including BFS and Topilogical Sort 
    Sample format of foods can be seen here {https://github.com/Mitraaaaa/Restaurant/tree/main/Food%20Recipes }
    
    **Kitchen Menu
    <img src="Guide/9.png" width="600">
     
    **This part gives the abilities to :
    * 1.Enter foods'name and it's prerequisites (The Format is written in each option),also you may print the Topoligical sort( sort by number of           prerequisites).
   
     <img src="Guide/10.png" width="600">
     <img src="Guide/11.png" width="600">
     
     
    * 2. Add a relation to a food you desire :
    <img src="Guide/14.png" width="600">
    
     
