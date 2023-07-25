import sys
from heapq import *

Row_Count = 0
Col_Count = 0
Query_Count = 0
Table = []
Query_Dict = {}
Query_Results = []
Shortest_Paths = []
Visited = []


def readInput():
    global Row_Count, Col_Count, Query_Count, Table, Query_Dict, Query_Results, Shortest_Paths, Visited
    
    Row_Count, Col_Count = map(int, input().split())
    for i in range(Row_Count):
        row = []
        entry_list = input().split()
        for j in range(Col_Count):
            row.append(int(entry_list[j]))
        Table.append(row)

    Shortest_Paths = [[sys.maxsize for j in range(Col_Count)] for i in range(Row_Count)]
    Visited = [[False for j in range(Col_Count)] for i in range(Row_Count)]  
    
    Query_Count = int(input())
    for i in range(Query_Count):
        Query_Results.append(sys.maxsize)
        query = list(map(int, input().split()))
        if query[1] > query[3]:
            query = (query[2], query[3], query[0], query[1])
        else:
            query = (query[0], query[1], query[2], query[3])
        
        if query not in Query_Dict:
            Query_Dict[query] = []
        Query_Dict[query].append(i)
    
    
def isValidSquare(row, col, left_bound, right_bound):
    return row >= 0 and row < Row_Count and col >= left_bound and col <= right_bound

    
def processSingleSquare(start_row, start_col, left_bound, right_bound):
    global Shortest_Paths, Visited
    
    for i in range(Row_Count):
        for j in range(left_bound, right_bound + 1):
            Shortest_Paths[i][j] = sys.maxsize
            Visited[i][j] = False  
    
    bfs_heap = []
    Shortest_Paths[start_row][start_col] = Table[start_row][start_col]
    heappush(bfs_heap, (Table[start_row][start_col], start_row, start_col))
    
    while bfs_heap:
        weight, row, col = heappop(bfs_heap)
        if Visited[row][col]:
            continue         
            
        Visited[row][col] = True
        
        if isValidSquare(row - 1, col, left_bound, right_bound) and not Visited[row - 1][col]:
            if weight + Table[row - 1][col] < Shortest_Paths[row - 1][col]:
                Shortest_Paths[row - 1][col] = weight + Table[row - 1][col]
                heappush(bfs_heap, (weight + Table[row - 1][col], row - 1, col))
        if isValidSquare(row + 1, col, left_bound, right_bound) and not Visited[row + 1][col]:
            if weight + Table[row + 1][col] < Shortest_Paths[row + 1][col]:
                Shortest_Paths[row + 1][col] = weight + Table[row + 1][col]
                heappush(bfs_heap, (weight + Table[row + 1][col], row + 1, col))
        if isValidSquare(row, col - 1, left_bound, right_bound) and not Visited[row][col - 1]:
            if weight + Table[row][col - 1] < Shortest_Paths[row][col - 1]:
                Shortest_Paths[row][col - 1] = weight + Table[row][col - 1]
                heappush(bfs_heap, (weight + Table[row][col - 1], row, col - 1))               
        if isValidSquare(row, col + 1, left_bound, right_bound) and not Visited[row][col + 1]:
            if weight + Table[row][col + 1] < Shortest_Paths[row][col + 1]:
                Shortest_Paths[row][col + 1] = weight + Table[row][col + 1]
                heappush(bfs_heap, (weight + Table[row][col + 1], row, col + 1))
                        

def processOnlyOneColumn(start_row, col_index):
    shortest_paths = [sys.maxsize for i in range(Row_Count)]
    shortest_paths[start_row] = Table[start_row][col_index]
    
    weight = Table[start_row][col_index]
    for i in reversed(range(0, start_row)):
        weight = weight + Table[i][col_index]
        shortest_paths[i] = weight
    
    weight = Table[start_row][col_index]
    for i in range(start_row + 1, Row_Count):
        weight = weight + Table[i][col_index]
        shortest_paths[i] = weight
        
    return shortest_paths
    
    
def processQueriesByColumn(left_col, right_col, whole_queries):
    global Query_Results
        
    if not whole_queries:
        return

    if left_col >= right_col:
        for query in whole_queries:
            query_indexes = whole_queries[query]
            paths = processOnlyOneColumn(query[0], left_col)
            new_min = min(Query_Results[query_indexes[0]], paths[query[2]])
            for q_index in query_indexes:
                Query_Results[q_index] = new_min
        return
    
    paths = []
    middle_col = (left_col + right_col) // 2
    for i in range(Row_Count):
        processSingleSquare(i, middle_col, left_col, right_col)
        for query in whole_queries:
            query_indexes = whole_queries[query]
            tmp_w = Shortest_Paths[query[0]][query[1]] + Shortest_Paths[query[2]][query[3]] - Table[i][middle_col]
            if tmp_w < Query_Results[query_indexes[0]]:
                for q_index in query_indexes:
                    Query_Results[q_index] = tmp_w
    
    queries_on_left = {}
    queries_on_right = {}
    for query in whole_queries:
        query_indexes = whole_queries[query]
        if query[3] < middle_col:
            queries_on_left[query] = query_indexes
        if query[1] > middle_col:
            queries_on_right[query] = query_indexes
                            
    processQueriesByColumn(left_col, middle_col - 1, queries_on_left)
    processQueriesByColumn(middle_col + 1, right_col, queries_on_right)
        
        
def printQueryResults():
    for q_result in Query_Results:
        print(q_result)
    
    
if __name__ == '__main__':
    readInput()
    processQueriesByColumn(0, Col_Count - 1, Query_Dict)
    printQueryResults()