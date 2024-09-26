from abc import ABC, abstractmethod


class InterviewPreprocessingCorpusRepository(ABC):

    @abstractmethod
    def loadMecab(self):
        pass

    @abstractmethod
    def posTagging(self, mecab, text):
        pass

    @abstractmethod
    def filterWord(self, posTagging):
        pass

    @abstractmethod
    def loadSentenceTransformer(self):
        pass

    @abstractmethod
    def calculateCosineSimilarityWithSentenceTransformer(
            self, sentenceTransformer, answerList, questionList):
        pass

    @abstractmethod
    def downloadNltkData(self, nltkDataPath):
        pass

    @abstractmethod
    def loadVectorizer(self):
        pass

    @abstractmethod
    def calculateCosineSimilarityWithNltk(self, vectorizer, answerStringList, questionStringList):
        pass

    @abstractmethod
    def countWantToData(self, keyword, interviewDataPath):
        pass