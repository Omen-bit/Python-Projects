def calculate_love_score(name1, name2):
    name1=name1.lower()
    name2=name2.lower()
    count1=0
    count2=0
    word1=["t","r","u","e"]
    word2=["l","o","v","e"]
    length=len(word1)
    for i in range(4):
        if word1[i] in name1:
            count1 += name1.count(word1[i])
        if word1[i] in name2:
            count1 += name2.count(word1[i])

    for i in range(4):
        if word2[i] in name1:
            count2 += name1.count(word2[i])
        if word2[i] in name2:
            count2 += name2.count(word2[i])

    print(f"{count1}{count2}")

calculate_love_score("Catherine Elizabeth Middleton", "William Arthur Philip Louis")