words = ['ate','bat','tab','race','care','eat']

similar_words = []

new_words= []
for i in range(len(words)):
    for j in range(i+1,len(words)):
        if sorted(words[i],key=None,reverse=False) == sorted(words[j],key=None,reverse=False):
            new_words.append(words[i])
            new_words.append(words[j])
            i += 1

    if new_words:
        similar_words.append(new_words)
    new_words = []    
print(similar_words)