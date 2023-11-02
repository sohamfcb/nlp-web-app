import paralleldots

paralleldots.set_api_key('TwRCu9dsQcTRQmSM7EJly8IORzGhcSIoSxQ7csQkNQI')

def ner(text):

    ner=paralleldots.ner(text)
    return ner

def sentiment_analysis(text):

    sentiment=paralleldots.sentiment(text)
    return sentiment

def abuse_detection(text):

    abuse=paralleldots.abuse(text)
    return abuse