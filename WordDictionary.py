def get_word_dictionary():
    # read all word from dictionary file
    with open("noun.dat", "r") as f:
        nouns = [word.replace("\n", "") for word in f.readlines()]
        
    with open("preposition.dat", "r") as f:
        preps = [word.replace("\n", "") for word in f.readlines()]
        
    with open("verb.dat", "r") as f:
        verbs = [word.replace("\n", "") for word in f.readlines()]
        
    with open("adjective.dat", "r") as f:
        adjs = [word.replace("\n", "") for word in f.readlines()]
        
    with open("determinant.dat", "r") as f:
        det = [word.replace("\n", "") for word in f.readlines()]
    #end read dictionary
    return adjs, nouns, verbs, det, preps