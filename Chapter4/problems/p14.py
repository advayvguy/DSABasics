#i am trash at solving problems, i over complicated this


def cannibal_transport(onshore, offshore):
    if onshore[0] == 2:
        return
    if offshore[0] == offshore[1]:
        offshore[0] = offshore[0] + 1
        onshore[0] = onshore[0] - 1
        print(f'{"M(onshore) -> M,C(boat) -> M(offshore)":<42} onshore- ( {onshore[0]} , {onshore[1]} )    offshore- ( {offshore[0]} , {offshore[1]} )')
    elif offshore[0] > offshore[1]:
        offshore[1] = offshore[1] + 1
        onshore[1] = onshore[1] - 1
        print(f'{"M(onshore) -> M,C(boat) -> M(offshore)":<42} onshore- ( {onshore[0]} , {onshore[1]} )    offshore- ( {offshore[0]} , {offshore[1]} )')
    cannibal_transport(onshore, offshore)


def missionary_transport(onshore, offshore):
    if onshore[1] == 1:
        return
    offshore[1] = offshore[1] + 1
    onshore[1] = onshore[1] - 1
    print(f'{"C(onshore) -> M,C(boat) -> C(offshore)":<42} onshore- ( {onshore[0]} , {onshore[1]} )    offshore- ( {offshore[0]} , {offshore[1]} )')
    missionary_transport(onshore, offshore)
    

def main():
    onshore = [3,3]
    offshore = [0,0]
    print("C gets on boat")
    onshore[1] = onshore[1] - 1
    cannibal_transport(onshore, offshore)
    print("C gets off boat and two M get on boat")
    onshore[1] = onshore[1] + 1
    onshore[0] = onshore[0] - 2
    offshore[0] = offshore[0] + 1
    print(f'{"M,M(boat) -> M(offshore)":<42} onshore- ( {onshore[0]} , {onshore[1]} )    offshore- ( {offshore[0]} , {offshore[1]} )')
    missionary_transport(onshore, offshore)
    print("M and C get on the boat and deboard offshore")
    offshore[1], offshore[0] = offshore[1] + 1, offshore[0] + 1
    onshore[1] = onshore[1] - 1
    print(f'{"M,C(boat) -> M,C(offshore)":<42} onshore- ( {onshore[0]} , {onshore[1]} )    offshore- ( {offshore[0]} , {offshore[1]} )')


main()