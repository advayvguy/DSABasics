from GraphADT import Graph

def get_moves(row, col, boardsize):
    valid_boxes = []
    move_offset = [
        (1,2),
        (-1,2),
        (1,-2),
        (-1,-2),
        (2,1),
        (2,-1),
        (-2,1),
        (-2,-1)
    ]
    for row_off, col_off in move_offset:
        row2 = row + row_off
        col2 = col + col_off
        if 0 <= row2 < boardsize and 0 <= col2 < boardsize:
            valid_boxes.append(row2*boardsize + col2)
    
    return valid_boxes

def knight_graph(boardsize):
    kt_graph = Graph()
    for row in range(boardsize):
        for col in range(boardsize):
            block_id = row*boardsize + col
            squares = get_moves(row, col, boardsize)
            for square in squares:
                kt_graph.add_edge(block_id,square)
    return kt_graph

def knight_tour(depth, path, u, limit):
    u.color = "grey"
    path.append(u)
    if depth == limit:
        return True
    if depth < limit:
        neighbors = order_by_avail(u)
        i = 0
        done = False
        while i < len(neighbors) and not done:
            if neighbors[i].color == 'white':
                done = knight_tour(depth+1, path, neighbors[i], limit)
            i += 1
        if not done:
            path.pop()
            u.color = "white"
        else:
            done = True
        return done

def order_by_avail(u):
    res_list = []
    for v in u.get_neighbors():
        if v.color == 'white':
            c = 0

           #to count how many unvisited neighbors v has
            for w in v.get_neighbors():
                if w.color == 'white':
                    c += 1
        
            res_list.append((c,v))
    res_list.sort(key=lambda x:x[0]) #sort according to the least number of neighbors 

    return [x[1] for x in res_list]

def printpath(init_pos, boardsize):
    kt_graph = knight_graph(boardsize)
    start_square = (ord(init_pos[0])-ord('a'))*boardsize + int(init_pos[1]) - 1
    path = []
    limit = boardsize**2
    knight_tour(1, path, kt_graph.get_vertex(start_square), limit)
    for square in path:
        col = (square.key)%boardsize + 1
        row = chr(square.key//boardsize + ord('a'))
        print(f"{row}{col}")

start = input("")
printpath(start, 8)