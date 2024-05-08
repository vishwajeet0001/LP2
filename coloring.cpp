#include<iostream>
using namespace std;
#define V 4

bool issafe(bool graph[V][V],int v,int color[],int c)
{
	for(int i=0;i<V;i++)
	{
		if(graph[v][i] && c==color[i])    //graph[v][i]->checking edge with that vertex and checking color is not same 
		{
			return false;
		}
	}
	return true;
}

bool backtrack(bool graph[V][V],int m, int color[],int v)
{
	if(v==V)
	return true;

    for(int c=1;c<=m;c++)  //*************************
	{
	if(issafe(graph,v,color,c))
	{
         color[v]=c;
		 if(backtrack(graph,m,color,v+1))
		 {
			return true;
		 }
		 color[v]=0;
	}
	}
	return false;
}
int main()
{
	bool graph[V][V] = {                                   
		{ 0, 1, 1, 1 },
		{ 1, 0, 1, 0 },
		{ 1, 1, 0, 1 },
		{ 1, 0, 1, 0 },
	};

	int m=3;
    int color[V]={0};
	if(backtrack(graph,m,color,0))
	{
		cout << "Solution Exists:"<< " Following are the assigned colors"<< "\n";
		for (int i = 0; i < V; i++)
		cout << " " << color[i] << " \n";

	}

}