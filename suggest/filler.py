from places.models import Attribute
from django.core.cache import get_cache

class AutoSuggestFiller():
    def __init__(self):
        self.r = get_cache('autosuggest')

    def setup(self): 
        """
        Set up the data store
        """
        #sentences = [ "Take out the trash", "Talk to the school bus driver" ]
        for attr in Attribute.objects.all():
            index = int(attr.osm_id)
            sentence = "%s : %s : %s : %s" % (attr.name, attr.suburb, attr.city, attr.state)
            sentence = sentence.lower()
            print 'Adding %s' % sentence
            self.addSentence(sentence,index)
            self.addWordPrefix(sentence,index)

    def addSentence(self, sentence, hashes):
        """
        Add the complete sentence in the hashes
        """
        self.r._client.hset('task',hashes, sentence)

    def addWordPrefix(self, sentence, hashes):
        """
        Adding the prefixes in the sorted set
        """
        for word in sentence.split(' '):
            for index,letter in enumerate(word.strip()):
                # Deletermin the prefix
                prefix = word[:index+1]
                # Add the prefix to the set along with the sentence hashes
                print 'Adding task:%s' % prefix
                self.r._client.zadd('task:%s'%prefix, hashes, 0)

a = AutoSuggestFiller()
a.setup()
