# Test 1: idendificates a walking with regular time reading interval
# and uniform moviment and velocity that is solved as a walking
data1 = [[0,0],[5,10],[10,20],[15,30],[20,40],[25,50],
         [30,60],[35,70],[40,80],[45,90],[50,100],[55,110],[60,120]]
result1 = [1, 1]

# Test 2: when user is walking with speed less than necessary
data2 = [[0,0],[5,10],[10,20],[15,30],[20,40],[25,50],
         [30,60],[35,70],[40,80],[45,90],[50,100],[55,110],[60,118]]
result2 = [0, 0]

# Test 3: when user is walking with speed greater velocity
# than necessary
data3 = [[0,0],[5,9],[10,17],[15,29],[20,38],[25,47],
         [30,55],[35,68],[40,79],[45,81],[50,99],[55,109],[60,121]]
result3 = [1, 1]

# Test 4: when user is walking with speed greater than necessary
# but occurs a reset on the step counter
data4 = [[0,0],[5,9],[10,17],[15,29],[20,38],[25,47],
         [30,55],[35,68],[40,79],[45,81],[46,0],[50,18],[55,28],[60,39]]
result4 = [1, 1]

# Test 5: when user is walking with speed less than necessary
# but occurs a reset on the step counter
data5 = [[0,0],[5,9],[10,17],[15,29],[20,38],[25,47],
         [30,55],[35,68],[40,79],[45,81],[46,0],[50,18],[55,28],[60,38]]
result5 = [0, 0]

# Test 6: Proving that as a walking is incremented a new walking must
# be started
data6 = [[0,0],[5,10],[10,20],[15,30],[20,40],[25,50],
         [30,60],[35,70],[40,80],[45,90],[50,100],[55,110],[60,120],
         [65, 132]]
result6 = [1, 1]

# Test 7: Proving that 2 walkings can occours if the condition is satisfied
data7 = [[0,0],[20,40],[40,80],[60,120],[80,120],[100,120],
         [120,120],[140, 160],[160, 200], [180, 240]]
result7 = [2, 2]

# Test 8: Proving that 2 walkings can occours if the condition is satisfied
data8 = [[0,0],[20,40],[40,80],[60,120],[80,120],[100,120],
         [120,120],[140, 160],[160, 200], [180, 239]]
result8 = [1, 1]

# Test 9: Proving that if there's 3 walkings but the walking number 2 has
# speed less than necessary, then only 2 walking will be computed
data9 = [[0,0],[20,42],[40,84],[60,127],[80,0],[100,0],[120,0],[140,0],
         [160,40],[180,79],[200,115],[220,0],[240,0],[260,0],[280,45],
         [300,73],[320,122]]
result9 = [2, 2]

