def all_variants(text):
    for size in range(len(text)):
        for j in range(len(text)-size):
            yield text[j:j+size+1]


a = all_variants("abc")
for i in a:
    print(i)
