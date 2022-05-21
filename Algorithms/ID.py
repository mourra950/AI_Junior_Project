import networkx as nx
def DLS(G,src,target,maxDepth):
  
        if src == target : return True
  
        # If reached the maximum depth, stop recursing.
        if maxDepth <= 0 : return False
  
        # Recur for all the vertices adjacent to this vertex
        for i in G[src]:
                if DLS(i,target,maxDepth-1):
                    return True
        return False

  
    # IDDFS to search if target is reachable from v.
    # It uses recursive DLS()
def IDDFS(G,src, target, maxDepth=None ):
  
        # Repeatedly depth-limit search till the
        # maximum depth
        if maxDepth is None:
            maxDepth = nx.len(G)
        
        for i in range(maxDepth):
            if (DLS(src, target, i)):
                
                return True
        return False



