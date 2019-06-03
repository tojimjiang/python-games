break_out = 0
while break_out == 0:
    name_cleaned = ''
    name_input = input('Name: ')
    name_lower = name_input.lower()
    name_lower_len = len(name_lower)
    for bit in range (0,name_lower_len):
        if name_lower[bit].isalpha():
            name_cleaned += name_lower[bit]
    print("Your 'cleaned up' name is:", name_cleaned)
    name_cleaned_len = len(name_cleaned)
    print("Your 'cleaned up' name reduces to:")
    num_sum = 0
    for let in range (0, name_cleaned_len):
        print(ord(name_cleaned[let])-96, end=' ')
        num_sum += (ord(name_cleaned[let])-96)
        if let == name_cleaned_len-1:
            print('=', end=' ')
        else:
            print('+', end=' ')
    print(num_sum)
    num_sum_str = str(num_sum)
    while len(num_sum_str) != 1:
        num_sum = 0
        for red in range (0, len(num_sum_str)):
            num_sum += ord(num_sum_str[red])-48
        print('Further Reduction:', num_sum)
        num_sum_str = str(num_sum)
    print('This name means ...', end='')
    if num_sum == 0:
        print('emptiness, nothingness, blank')
    elif num_sum == 1:
        print('independence, loneliness, creativity, originality, dominance, leadership, impatienc')
    elif num_sum == 2:
        print('quiet, passive, diplomatic, co-operation, comforting, soothing, intuitive, compromising, patient')
    elif num_sum == 3:
        print('charming, outgoing, self expressive, extroverted, abundance, active, energetic, proud')
    elif num_sum == 4:
        print('harmony, truth, justice, order discipline, practicality')
    elif num_sum == 5:
        print('new directions, excitement, change, adventure')
    elif num_sum == 6:
        print('love, harmony, perfection, marriage, tolerance, public service')
    elif num_sum == 7:
        print('spirituality, completeness, isolation, introspection')
    elif num_sum == 8:
        print('organization, business, commerce, new beginnings')
    elif num_sum == 9:
        print('romatic, rebellious, determined, passionate, compassionate')
