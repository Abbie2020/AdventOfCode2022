with open("Documents/Code/AdventOfCode2022/aoc1input.txt",'r') as data_file:
    
    ### PART 1 ###
    
    elves = []
    total = 0    
    for x in data_file:
        cals = x.split("\n")
        if len(cals[0]) > 0:
                total += int(cals[0])
        else:
            elves.append(total)
            total = 0
    print("PART 1\nHighest calories: " + str(max(elves)))
    
    ### PART 2 ###
    
    top3_list = sorted(elves, reverse=True)[:3]
    total_top3 = 0
    for x in top3_list:
        total_top3 += x
    print("PART 2\nTotal of top 3 calories: " + str(total_top3))
