def read_file_content(filename):
    count_words = {}
    with open(filename, "r") as openfile:
        read_file = openfile.read()
        words = read_file.split()
      
        for word in words:
            if word in count_words:
                count_words[word] +=1
            else:
                count_words[word] = 1
    return count_words


     
print (read_file_content("./story.txt"))