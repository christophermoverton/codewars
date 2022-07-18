# codewars
navigatingforest.py is Kata 1 challenge problem known as Tip Toe through circles.

This is a circle boundary path optimization problem from start to target destination.

In this case I've tested through most unit tests (should pass) at the moment.

May need some added optizimation tweaks for larger unit tests not publicly furnished.
Application layout is as follows:

*Providing custom vector class

*Graph class for formatting graph data for Dykstra's algorithm method

*Utility functions: 

  1. circle to cirlce intersection 
  
  2. line of sight intersection tests 
  
  3. external/internal bitangent
  
  4. arc line of sight intersection testing that is for determining open arc node to node path (if any)
  
  5. arc length for node to node path (based upon results of the previous)
  
For an excellent summary of this problem see 
[Circular Obstacle path finding](https://redblobgames.github.io/circular-obstacle-pathfinding/)

This application works by constructing all external and internal bitangents (if exists), 

and then checks to see if any open path from start and target nodes to all such nodes.

Then computes any line of sight open tangent nodes to all circles in problem set,

then checks to see if start and target node is open (no line of sight obstruction),

then computes arc line of sight open or closed paths and min max paths for all arc tangent nodes computed above,

once compiling this, handing graph (dictionary) object to Graph class for formatting 

and completing processing with Dykstra's method.
