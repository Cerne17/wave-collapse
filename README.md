# ALGORITHM EXPLANATION:
* The wfc (Wafe Function Collapse) is a genarator.

* The goal is to fill every empty space in the screen, mantaining cohesion.

# RULES:
* Create a boolean array for each cell representing the domain of that variable. The domain has one entry per tile (all initially true). A tile is in the domain if it's set to true.
* While there are still any cells with multiple possible states:
    * Pick a random cell with the least 'entropy';
    * Pick a random cell from that cells domain and remove all other tiles from the domain;
    * Update the domain of other cells based on this new information - for example - cell propagation.

# A MORE IN DEPTH EXPLANATION:
https://www.boristhebrave.com/2020/04/13/wave-function-collapse-explained/
