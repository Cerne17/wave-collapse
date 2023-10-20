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

# PSEUDOCODE:
```
function WaveFunctionCollapse(inputImage, outputSize):
    Initialize an output image of size outputSize
    Initialize a wave (a set of all possible states at each position in the output image)

    while wave is not empty:
        Choose a cell from the wave
        Collapse the cell to a single state based on the constraints and inputImage
        Remove the cell from the wave

        Propagate the changes to neighboring cells based on the propagation rules

    return the final output image

function CollapseCell(cell, wave, inputImage):
    Compute the entropy of the cell based on the wave and inputImage
    Select a state for the cell with the minimum entropy
    Update the output image with the selected state
    Update the wave with the selected state
    Remove all other states for the cell from the wave

function PropagateChanges(cell, wave, inputImage):
    for each neighboring cell of cell:
        Update the wave based on the constraints and the states of neighboring cells
```
