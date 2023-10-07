def get_data(aTuple):
    num=()
    words=()
    for t in aTuple:
        num=num+(t[0],)
        if t[1] not in words:
            words=words+(t[1],)
    min_n=min(num)
    max_n=max(num)
    unique_words=len(words)
    return (min_n, max_n, unique_words)

tswift=((2014,"Katy"),
        (2014,"Harry"),
        (2012,"Jake"),
        (2010,"Taylor"),
        (2008,"Joe"))
(min_year,max_year,num_people) = get_data(tswift)
print("From", min_year,"to",max_year,"Taylor Swift wrote song about",num_people,"people")