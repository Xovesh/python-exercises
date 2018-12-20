package landmines;

import java.util.Iterator;
import java.util.LinkedList;


public class PathInLandMines {
	static int lenghtShortPath = Integer.MAX_VALUE;
	// row and column allow access to the adjacent to a cell
	static int row[] = { -1, 0, 0, 1 };
	static int col[] = { 0, -1, 1, 0 };
	static int max = 0;
	public static class Cell {
		public final int row;
		public final int col;
		public Cell parent;

		public Cell(int row, int column, Cell parent) {
			this.row = row;
			this.col = column;
			this.parent = parent;
		}
	}

	// find the shortest path using BFS using the parent to make it more easier
	private static void findShortestPath(int[][] land) {
		LinkedList<Cell> a = new LinkedList<Cell>();
		for(int i=0; i<land.length;i++) {
			if(land[i][0]==1) {
				a.add(new Cell(i,0, null));
			}
		}
		
		Cell result = null;
		while(!a.isEmpty()) {
			Cell x = a.remove();
			
			if(x.col == 9) {
				result = x;
				break;
			}else{
				for(int i= 0;i<4;i++) {
					if(validposition(land, x.row+row[i], x.col+col[i])) {
						if(land[x.row+row[i]][x.col+col[i]]==1) {
							a.add(new Cell(x.row+row[i], x.col+col[i], x));
						}
					}
				}
			}
			
		}
		
		System.out.println("Path to follow");
		while(result.parent != null) {
			System.out.println("Row: " + result.row + " Column: " + result.col );
			land[result.row][result.col] = 3;
			result = result.parent;
		}
		System.out.println("Row: " + result.row + " Column: " + result.col );
		land[result.row][result.col] = 3;
	}
	
	// prints all the paths
	private static void findAllPaths(int[][] land) {
		LinkedList<LinkedList<Cell>> Results = new LinkedList<LinkedList<Cell>>();
		// for each element in the first column call to helperallpaths
		for(int i=0; i<land.length; i++) {
			if(land[i][0] == 1) {
				LinkedList<Cell> s = new LinkedList<Cell>();
				s.add(new Cell(i,0,null));
				helperallpaths(land, i, 0, Results, s);
			}
		}
		Iterator<LinkedList<Cell>> b = Results.iterator();
		while(b.hasNext()) {
			Iterator<Cell> r = b.next().iterator();
			System.out.println("\nPath\n");
			while(r.hasNext()) {
				Cell p = r.next();
				System.out.println("Row: " + p.row + " Column: " + p.col );
			}
		}
		System.out.println("Number of paths found");
		System.out.println(Results.size());
	}
	
	// using skiena methodology
	private static void helperallpaths(int[][] land, int i, int column, LinkedList<LinkedList<Cell>> Results, LinkedList<Cell> path) {
		//if we reach to the last column add the path to the list
		if(column == 9) {
			Results.add(new LinkedList<Cell>());
			Results.getLast().addAll(path);
		}else{
			Cell[] c = new Cell[4];
			int a = buildcandidates(land, i, column, c);
			// mark as visited
			land[i][column] = 6;
			for(int l = 0; l<a;l++) {
				path.add(c[l]);
				helperallpaths(land, c[l].row, c[l].col, Results, path);
				path.removeLast();
			}
			// unmark
			land[i][column] = 1;
		}
	}
	
	
	
	// creates the candidates given a position
	private static int buildcandidates(int[][] land, int i, int j, Cell[] c) {
		int count = 0;
		for(int s= 0;s<4;s++) {
			if(validposition(land, i+row[s], j+col[s])) {
				if(land[i+row[s]][j+col[s]]==1) {
					c[count] = new Cell(i+row[s],j+col[s], null);
					count ++;
				}
			}
		}
		return count;
	}
	
	// prints the longest path
	private static void longestpath(int[][] land) {
		LinkedList<Cell> Results = new LinkedList<Cell>();
		// for each element in the first column call to helperlongestpath
		for(int i=0; i<land.length; i++) {
			if(land[i][0] == 1) {
				LinkedList<Cell> s = new LinkedList<Cell>();
				s.add(new Cell(i,0,null));
				helperlongestpath(land, i, 0, Results, s, 0);
			}
		}
		
		//print the solution
		System.out.println("Longest Path");
		Iterator<Cell> b = Results.iterator();
		while(b.hasNext()) {
				Cell p = b.next();
				System.out.println("Row: " + p.row + " Column: " + p.col );
				land[p.row][p.col] = 9;
			}
		}
	
	// using skiena methodology
	private static void helperlongestpath(int[][] land, int i, int column, LinkedList<Cell> results, LinkedList<Cell> path, int distance) {
		//if we are in the column 9 check if the actual path is bigger than the one that we have
		if(column == 9) {
			if(distance>max) {
				results.clear();
				results.addAll(path);
				max = distance;
			}
		}else{
			Cell[] c = new Cell[4];
			int a = buildcandidates(land, i, column, c);
			// mark as visited
			land[i][column] = 6;
			for(int l = 0; l<a;l++) {
				path.add(c[l]);
				helperlongestpath(land, c[l].row, c[l].col, results, path, distance+1);
				path.removeLast();
			}
			// unmark
			land[i][column] = 1;
		}
	}
	
	
	// helper method to remove the impossible moves
	public static void unsafeareas(int[][] landmines) {
		for(int i=0; i<landmines.length;i++) {
			for(int j=0; j<landmines[0].length;j++) {
				if(landmines[i][j]==0) {
					for(int z= 0;z<4;z++) {
						if(validposition(landmines, i+row[z], j+col[z])) {
							
							landmines[i+row[z]][j+col[z]] = 2;
						}
					}
				}
			}
		}
	}
	
	// returns a boolean if the positions given is inside the matrix
	private static boolean validposition(int[][] landmines, int i, int j) {
		if(j<landmines[0].length && j>=0 && i<landmines.length && i>=0) {
			return true;
		}else {
			return false;
		}
	}
	public static void main(String[] args) {
		int[][] landmines = {
				{ 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 },
				{ 1, 0, 1, 1, 1, 1, 1, 1, 1, 1 },
				{ 1, 1, 1, 0, 1, 1, 1, 1, 1, 1 },
				{ 1, 1, 1, 1, 0, 1, 1, 1, 1, 1 },
				{ 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 },
				{ 1, 1, 1, 1, 1, 0, 1, 1, 1, 1 },
				{ 1, 0, 1, 1, 1, 1, 1, 1, 0, 1 },
				{ 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 },
				{ 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 },
				{ 0, 1, 1, 1, 1, 0, 1, 1, 1, 1 },
				{ 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 },
				{ 1, 1, 1, 0, 1, 1, 1, 1, 1, 1 } };
		
		int[][] landmines2 = {
				{ 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 },
				{ 1, 0, 1, 1, 1, 1, 1, 1, 1, 1 },
				{ 1, 1, 1, 0, 1, 1, 1, 1, 1, 1 },
				{ 1, 1, 1, 1, 0, 1, 1, 1, 1, 1 },
				{ 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 },
				{ 1, 1, 1, 1, 1, 0, 1, 1, 1, 1 },
				{ 1, 0, 1, 1, 1, 1, 1, 1, 0, 1 },
				{ 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 },
				{ 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 },
				{ 0, 1, 1, 1, 1, 0, 1, 1, 1, 1 },
				{ 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 },
				{ 1, 1, 1, 0, 1, 1, 1, 1, 1, 1 } };
		
		int[][] landmines3 = {
				{ 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 },
				{ 1, 0, 1, 1, 1, 1, 1, 1, 1, 1 },
				{ 1, 1, 1, 0, 1, 1, 1, 1, 1, 1 },
				{ 1, 1, 1, 1, 0, 1, 1, 1, 1, 1 },
				{ 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 },
				{ 1, 1, 1, 1, 1, 0, 1, 1, 1, 1 },
				{ 1, 0, 1, 1, 1, 1, 1, 1, 0, 1 },
				{ 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 },
				{ 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 },
				{ 0, 1, 1, 1, 1, 0, 1, 1, 1, 1 },
				{ 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 },
				{ 1, 1, 1, 0, 1, 1, 1, 1, 1, 1 } };
		
		unsafeareas(landmines);
		System.out.println("\nShortest path \n");
		print(landmines);
		findShortestPath(landmines);
		print(landmines);
		
		
		
		
		unsafeareas(landmines2);
		System.out.println("\nLongest paths \n");
		print(landmines2);
		longestpath(landmines2);
		print(landmines2);
		
		
		
		
		//unsafeareas(landmines3);
		//System.out.println("\nAll paths \n");
		//findAllPaths(landmines2);
		
		
		
	}
	public static void print(int[][] landmines) {
		String s = "";
		for(int i=0; i<landmines.length;i++) {
			for(int j=0; j<landmines[0].length;j++) {
				s = s +landmines[i][j];
			}
			System.out.println(s);
			s= "";
			}
	}
}

