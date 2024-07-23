def translate(bn_sentences, en_sentences):
    translations = []
    for bn, en in zip(bn_sentences, en_sentences):
        translation = f"Translated: {bn} -> {en}"
        translations.append(translation)
    return translations