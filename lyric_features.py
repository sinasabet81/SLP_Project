import re
from sklearn.feature_extraction.text import CountVectorizer

def setFeaturesBoW(splitData):
    # bag of words featurizer

    cv = CountVectorizer(strip_accents="ascii", tokenizer=tokenizer)
    # fit and transform the train data lyrics
    train_lyrics = getLyricsFromData(splitData["train"])
    train_features = cv.fit_transform(train_lyrics)
    for i in range(len(splitData["train"])):
        splitData["train"][i]["features"] = train_features[i]
    # transform test and validation data groups
    test_lyrics = getLyricsFromData(splitData["test"])
    test_features = cv.fit_transform(test_lyrics)
    for i in range(len(splitData["test"])):
        splitData["test"][i]["features"] = test_features[i]
    validation_lyrics = getLyricsFromData(splitData["validation"])
    validation_features = cv.fit_transform(validation_lyrics)
    for i in range(len(splitData["validation"])):
        splitData["validation"][i]["features"] = validation_features[i]
    splitData["cv"] = cv
    return {
        "cv": cv,
        "train": train_features,
        "test": test_features,
        "validation": validation_features
    }

def tokenizer(doc):
    delims = "[ \n\[\]:]" # regex of our delimiters; \n, sp, and some puncts.
    return [token for token in re.split(delims, doc)
        if token is not ''
    ]

def getLyricsFromData(data):
    return [song['lyrics'] for song in data]