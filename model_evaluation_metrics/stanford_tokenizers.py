import stanfordnlp

stanford_nlp = stanfordnlp.Pipeline(processors='tokenize', lang='en')


def stanford_tokenizer(text):
    text = text.replace(' .', '.')
    doc = stanford_nlp(text)
    sentences = []
    for i, sentence in enumerate(doc.sentences):
        sent = [word.text for word in sentence.words]
        sentences.append(sent)

    return sentences


def sent_tokenizer(text):
    if type(text) == list:
        return text

    text = text.replace(' .', '.')
    doc = stanford_nlp(text)
    sentences = []
    for i, sentence in enumerate(doc.sentences):
        sent = ' '.join([word.text for word in sentence.words])
        sentences.append(sent)

    return sentences


def word_tokenizer(text):
    text = text.replace(' .', '.')
    doc = stanford_nlp(text)
    words = []
    for i, sentence in enumerate(doc.sentences):
        words += [word.text for word in sentence.words]

    return words




