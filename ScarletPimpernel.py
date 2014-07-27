'''
Created on May 6, 2014

@author: greensalad
'''
wordstwo = {}
words = {
      'sallow' : 'of a sickly, yellowish color',
      'ruddy' : 'reddish',
      'pock-marked' : 'marked with small pits and scars',
      'glibness' : 'state of ease and ready fluency',
      'reverent' : 'deeply restpectful, worshipful',
      'peruse' : 'to read through, survey, or examine in detail',
      'gruff' : 'hoarse, harsh, rough',
      'amiable': 'affable, friendly, sociable',
      'propaganda' : 'deliberate spreading of rumors to harm a group or person',
      'conceited' : 'vain, farfetchedly compared',
      'abscond' : 'withdraw, decamp',
      'slovenly' : 'dirtily, untidily',
      'alfresco' : 'in the open air',
      'aerate' : 'expose to or mix with air',
      'chastise' : 'inflict punishment on, scold',
      'ostracize' : 'exclude from society, exile',
      'precocious' : 'matured to an abnormal level',
      'peripatetic' : 'walking',
      'opulent' : 'wealthy'}
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




