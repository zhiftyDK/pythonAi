import json
import torch.nn as nn
from gensim.test.utils import common_texts
from gensim.models import Word2Vec

def word2vec(input):
    with open("data/intents.json", "r") as f:
        filedata = json.load(f)
        allPatterns = []
        for intent in filedata["intents"]:
            for pattern in intent["patterns"]:
                words = []
                for word in pattern.split(" "):
                    words.append(word.lower().replace("!", "").replace("?", "").replace(".", "").replace(",", ""))
                allPatterns.append(words)
        model = Word2Vec(sentences=allPatterns, vector_size=100, window=5, min_count=1, workers=4)
        model.save("data/models/w2vWithIntents.model")
        vector = model.wv[input]
        return vector

class FeedForwardModel(nn.Module):
    def __init__(self, inputDimensions, outputDimensions):
        super(FeedForwardModel, self).__init__()

        self.layer1 = nn.Linear(inputDimensions, 8)
        self.sigmoid = nn.Sigmoid()
        self.layer2 = nn.Linear(8, outputDimensions)
    
    def forward(self, x):
        output = self.layer1(x)
        output = self.sigmoid(output)
        output = self.layer2(output)
        return output
    
FeedForwardModel()