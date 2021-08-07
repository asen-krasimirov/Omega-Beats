from django.core.exceptions import ValidationError


def first_latter_capital(data):
    if data[0] != data[0].upper():
        raise ValidationError('First latter must be upper!')


def no_bad_words(data):
    data = data.split()

    for word in data:
        # if any(bad_word in word.lower() for bad_word in bad_words):
        for bad_word in bad_words:
            if bad_word in word.lower():
                raise ValidationError('Do not use offensive words!')


bad_words = ['arse',
             'ass',
             'asshole',
             'bastard',
             'bitch',
             'bollocks',
             'brotherfucker',
             'bugger',
             'bullshit',
             'child-fucker',
             'cocksucker',
             'crap',
             'cunt',
             'damn',
             'effing',
             'fatherfucker',
             'frigger',
             'fuck',
             'goddamn',
             'godsdamn',
             'holy shit',
             'horseshit',
             'motherfucker',
             'nigga',
             'piss',
             'prick',
             'shit',
             'shit ass',
             'shitass',
             'sisterfucker',
             'slut',
             'son of a bitch',
             'son of a whore',
             'sweet Jesus',
             'twat',
             ]
