words = {"one":"1","two":"2","three":"3","four":"4","five":"5","six":"6","seven":"7","eight":"8","nine":"9"}
total = 0
part_2 = True
with open('day1.txt', 'r') as file:
    i=0
    while True:
        i+=1
        line = file.readline().replace('\n', '')
        if not line:
            break
                 
        matches = []       
        for i, char in enumerate(line):
            if char.isdigit():
                matches.append([i, int(char)])
                
        if part_2:
            for word, value in words.items():
                if word in line:
                    index = line.find(word)
                    while True:
                        matches.append([index, int(value)])
                        index = line.find(word, index+1)
                        if index == -1:
                            break
                        
        matches = sorted(matches, key=lambda x: x[0])
        total += matches[-1][1]+matches[0][1]*10

    print(total) 
                