#include <bits/stdc++.h>
using namespace std;
#define V 4

void printSolution(int color[]);

bool isSafe(int v, bool graph[V][V], int color[], int c)
{
	for (int i = 0; i < V; i++)
		if (graph[v][i] && c == color[i])
			return false;

	return true;
}

bool graphColoringUtil(bool graph[V][V], int m, int color[],int v){
	/* base case: If all vertices areassigned a color then return true */
	if (v == V)
		return true;
	/* Consider this vertex v andtry different colors */
	for (int c = 1; c <= m; c++) {
		/* Check if assignment of color c to v is fine*/
		if (isSafe(v, graph, color, c)) {
			color[v] = c;
			
			if (graphColoringUtil(graph, m, color, v + 1) == true)   /* recur to assign colors to rest of the vertices */
				return true;
			color[v] = 0;   /* If assigning color c doesn't	lead to a solution then remove it */
		}
	}
	return false; /* If no color can be assigned tot his vertex then return false */
}

bool graphColoring(bool graph[V][V], int m)
{
	int color[V];
	for (int i = 0; i < V; i++)
		color[i] = 0;

	// Call graphColoringUtil() for vertex 0
	if (graphColoringUtil(graph, m, color, 0) == false) {
		cout << "Solution does not exist";
		return false;
	}

	// Print the solution
	printSolution(color);
	return true;
}

void printSolution(int color[])
{
	cout << "Solution Exists:"
		<< " Following are the assigned colors"
		<< "\n";
	for (int i = 0; i < V; i++)
		cout << " " << color[i] << " ";
	cout << "\n";
}

int main()
{

	/* Create following graph and test
	whether it is 3 colorable
	(3)---(2)
	|    / |
	|   /  |
	| /    |
	(0)---(1)
	*/
	bool graph[V][V] = {                                   
		{ 0, 1, 1, 1 },
		{ 1, 0, 1, 0 },
		{ 1, 1, 0, 1 },
		{ 1, 0, 1, 0 },
	};

	// Number of colors
	int m = 3;

	// Function call
	graphColoring(graph, m);
	return 0;
}
