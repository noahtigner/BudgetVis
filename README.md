# BudgetFlow

A tool for visualizing your budget.

Constructs Sankey flow diagrams.
                        
Available as a standalone web page or a full-stack web app (supports saving, security, etc.)

![BudgetVis](budgetvis.png)

## Use

Add nodes and their colors in the Nodes Table.

Add links between nodes and their respective value in the Links Table.

Rows can be added and removed from the table by clicking the '+' or '-' buttons on the right sides.

The graph will be redrawn when a new valid node or link is inserted, or an existing node or link is changed or removed.


Standalone Version:
- visit: [http://ix.cs.uoregon.edu/~nzt/sankey](http://ix.cs.uoregon.edu/~nzt/sankey)

Full Stack Version:
- use: flask run
- visit: [localhost:5000](localhost:5000)


## Development

Dependencies: 
- Flask 
- D3.js 
- JQuery 

## Author

Noah Tigner

nzt@cs.uoregon.edu

References: Jarret Meyer's D3.js code for advanced D3 sankey graphs
