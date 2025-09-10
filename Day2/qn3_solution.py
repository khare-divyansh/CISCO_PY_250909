def question3():
    
    sentence = input("Enter a sentence: ")
    words_list = sentence.split()
    words_tuple = tuple(word.upper() for word in words_list)

 
    with open("sentence_data.txt", "w") as f:
        f.write("List: " + str(words_list) + "\n")
        f.write("Tuple: " + str(words_tuple) + "\n")


    print("\nData read from file:")
    with open("sentence_data.txt", "r") as f:
        content = f.read()
        print(content)


question3()