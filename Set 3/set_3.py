'''Programming Set 3

This assignment will develop your ability to manipulate data.
'''

def relationship_status(from_member, to_member, social_graph):
    '''Relationship Status.

    Let us pretend that you are building a new app.
    Your app supports social media functionality, which means that users can have
    relationships with other users.

    There are two guidelines for describing relationships on this social media app:
    1. Any user can follow any other user.
    2. If two users follow each other, they are considered friends.

    This function describes the relationship that two users have with each other.

    Please see "assignment-4-sample-data.py" for sample data. The social graph
    will adhere to the same pattern.

    Parameters
    ----------
    from_member: str
        the subject member
    to_member: str
        the object member
    social_graph: dict
        the relationship data

    Returns
    -------
    str
        "follower" if fromMember follows toMember,
        "followed by" if fromMember is followed by toMember,
        "friends" if fromMember and toMember follow each other,
        "no relationship" if neither fromMember nor toMember follow each other.
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    if to_member in social_graph[from_member]["following"]:
        if from_member in social_graph[to_member]["following"]: 
            return "friends"
        else:
            return "follower"

    elif from_member in social_graph[to_member]["following"]:
       return "followed by"
    else:
       return "no relationship"

def tic_tac_toe(board):
    '''Tic Tac Toe.

    Tic Tac Toe is a common paper-and-pencil game.
    Players must attempt to successfully draw a straight line of their symbol across a grid.
    The player that does this first is considered the winner.

    This function evaluates a tic tac toe board and returns the winner.

    Please see "assignment-4-sample-data.py" for sample data. The board will adhere
    to the same pattern. The board may by 3x3, 4x4, 5x5, or 6x6. The board will never
    have more than one winner. The board will only ever have 2 unique symbols at the same time.

    Parameters
    ----------
    board: list
        the representation of the tic-tac-toe board as a square list of lists

    Returns
    -------
    str
        the symbol of the winner or "NO WINNER" if there is no winner
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    something_happened = 0
    # all possible horizontal wins
    for i in range(0,len(board)):
        # for j in range(0,len(board)-2):
            # if board[i][j] == board[i][j+1] == board[i][j+2] != '':
                # something_happened += 1
                # return board[i][j]
        counter = 0
        for j in range(0,len(board)-1):
            if board[i][j] == board[i][j+1] != '':
                counter += 1
            if counter == len(board)-1:
                something_happened += 1
                return board[i][0]

    # all possible vertical wins
    for i in range(0,len(board)): #
        # for j in range(0,len(board)-2):
            # if board[j][i] == board[j+1][i] == board[j+2][i] != '':
                # something_happened += 1
                # return board[j][i]
        counter = 0
        for j in range(0,len(board)-1):
            if board[j][i] == board[j+1][i] != '':
                counter += 1
            if counter == len(board)-1:
                something_happened += 1
                return board[0][i]

    # all possible diagonal wins top to bottom, left to right
    # for i in range(0,len(board)-2):
        # for j in range(0,len(board)-2):
            # if board[i][j] == board[i+1][j+1] == board[i+2][j+2] != '':
                # something_happened += 1
                # return board[i][j]
    counter = 0
    for j in range(0,len(board)-1):
        if board[j][j] == board[j+1][j+1] != '':
            counter += 1
        if counter == len(board)-1:
            something_happened += 1
            return board[0][0]

    # all possible diagonal wins top to bottom, right to left
    # for i in range(0,len(board)-2):
        # for j in range(0,len(board)-2):
            # if board[i][j+2] == board[i+1][j+1] == board[i+2][j] != '':
                # something_happened += 1
                # return board[i][j+2]
                
    counter = 0
    for j in range(1,len(board)):
        if board[j-1][-j] == board[j][-j-1] != '':
            counter += 1
        if counter == len(board)-1:
            something_happened += 1
            return board[0][-1]
                
    if something_happened == 0:
        return "NO WINNER"

def eta(first_stop, second_stop, route_map):
    '''ETA.

    A shuttle van service is tasked to travel along a predefined circlar route.
    This route is divided into several legs between stops.
    The route is one-way only, and it is fully connected to itself.

    This function returns how long it will take the shuttle to arrive at a stop
    after leaving another stop.

    Please see "mod-4-ipa-1-sample-data.py" for sample data. The route map will
    adhere to the same pattern. The route map may contain more legs and more stops,
    but it will always be one-way and fully enclosed.

    Parameters
    ----------
    first_stop: str
        the stop that the shuttle will leave
    second_stop: str
        the stop that the shuttle will arrive at
    route_map: dict
        the data describing the routes

    Returns
    -------
    int
        the time it will take the shuttle to travel from first_stop to second_stop
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    route_line = []
    for i in route_map.keys():
        route_line.append(i[0])
    route_line.append(list(route_map.keys())[0][0])

    total_travel = 0

    if route_line.index(second_stop) >= route_line.index(first_stop):
        for j in range(route_line.index(first_stop),route_line.index(second_stop)):
            total_travel += route_map[route_line[j],route_line[j+1]]["travel_time_mins"]
    
        return total_travel

    elif route_line.index(second_stop) < route_line.index(first_stop):
        for j in range(route_line.index(first_stop),len(route_line)-1):
            total_travel += route_map[route_line[j],route_line[j+1]]["travel_time_mins"]
        for p in range(0,route_line.index(second_stop)):
            total_travel += route_map[route_line[p],route_line[p+1]]["travel_time_mins"]

        return total_travel