'''
Created on May 6, 2014

@author: greensalad
'''
wordstwo = {}
words = {
      'anent':'concerning',
      'citoyen':'citizen',
      'refugee':'a person fleeing from danger',
      'plebeian':'member of the common party',
      'epistle':'a letter',
      'enigmatic':'puzzle-like',
      'convent':'a girl school run by nuns',
      'inane':'not smart',
      'coterie':'a small group with a common interest',
      'debut':'first appearance',
      'inanities':'foolish catchphrases',
      'flippant':'not respectful',
      'inadvertently':'not focusing on the matter',
      'soupcon':'small amount',
      'ennui':'bored',
      'envoy':'delegate from another country',
      'billet doux':'love note',
      'enigma':'something unclear',
      'sobriquet':'nickname',
      'au revoir':'until we meet again',
      'palatial':'palace-like',
      'raiment':'clothes',
      'alacrity':'speed',
      'abate':'to put an end to',
      'waylay':'to attack',
      'dilapidated':'fallen to ruin',
      'sordid':'dirty',
      'quandry':'difficult situation',
      'bourgeois':'middle-class',
      'lacquey':'servant',
      'squalid':'filthy',
      'urbane':'polite',
      'nil':'none',
      'prejudice':'bias',
      'league':'3 miles'}
for word in words:
    print "What is the definition of %s?" %word
    answer = raw_input().lower()
    if answer==words[word]:
        print "You are correct! On to the next one."
    else:
        print "The correct answer was %s. I will re-test you at the end."%words[word]
        wordstwo[word]=words[word]
        
for word in wordstwo:
    print "What is the definition of %s?" %word
    answer = raw_input().lower()
    if answer==wordstwo[word]:
        print "You are correct!"
    else:
        print "The correct answer was %s. You need to review and re-run the program."%wordstwo[word]




