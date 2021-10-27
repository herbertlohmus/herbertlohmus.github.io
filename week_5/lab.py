'''
Lab instructions: 
Complete each function below so that all doctests pass.
You can run the doctests with the command
$ python3 -m doctest --verbose lab.py
Once all doctests pass, upload the output of the above command to sakai.
'''


from typing import Container


def rot13(text):
    '''
    [ROT13](https://en.wikipedia.org/wiki/ROT13) stands for "ROTate characters by 13".
    It is a commonly used encryption scheme where each character is replaced by the character 13 positions above/below it.
    For example, the letter 'a' gets replaced by 'n',
    and 'n' gets replaced by 'a'.
    This is of course not a very good encryption scheme because it's easy for anyone to decrypt,
    but it's useful for hiding information from the muggles who can't program.
    It's basically like the [pig latin](https://en.wikipedia.org/wiki/Pig_Latin) of programming.
    NOTE:
    Your function only has to work for lower case English text.
    HINT:
    Use the `ord` function to convert each character to a number;
    do your math on that number;
    then use `chr` to convert back to a string.
    >>> rot13('python is awesome')
    'clguba vf njrfbzr'
    >>> rot13('clguba vf njrfbzr')
    'python is awesome'
    >>> rot13('PYTHON')
    'CLGUBA'
    >>> rot13(rot13('python is awesome!!'))
    'python is awesome!!'
    >>> rot13('Crescit cum commercio civitas.')
    'Perfpvg phz pbzzrepvb pvivgnf.'
    >>> rot13('Pynerzbag ZpXraan Pbyyrtr’f zvffvba vf "gb rqhpngr vgf fghqragf sbe gubhtugshy naq cebqhpgvir yvirf naq erfcbafvoyr yrnqrefuvc va ohfvarff, tbireazrag, naq gur cebsrffvbaf, naq gb fhccbeg snphygl naq fghqrag fpubynefuvc gung pbagevohgr gb vagryyrpghny ivgnyvgl naq gur haqrefgnaqvat bs choyvp cbyvpl vffhrf."')
    'Claremont McKenna College’s mission is "to educate its students for thoughtful and productive lives and responsible leadership in business, government, and the professions, and to support faculty and student scholarship that contribute to intellectual vitality and the understanding of public policy issues."'

    NOTE:
    HINT:
    Use the accumulator pattern.
    Loop over each character in the string, and if it is not a letter, then just add it to the accumulator.
    If it is a letter, then do a ROT13 transformation using the `ord` and `chr` functions and some simple math.
    You know something is a capital letter because it is >= 'A' and <= 'Z';
    similarly, you know something is a lowercase letter because it is >= 'a' and <= 'z'.
    '''
    result = ""
    # Loop over characters.
    for v in text:
        # Convert to number with ord.
        c = ord(v)

        # Shift number back or forward.
        if c >= ord('a') and c <= ord('z'):
            if c > ord('m'):
                c -= 13
            else:
                c += 13
        elif c >= ord('A') and c <= ord('Z'):
            if c > ord('M'):
                c -= 13
            else:
                c += 13

        # Append to result.
        result += chr(c)

    # Return transformation.
    return result


def greekify(text):
    '''
    Transliterating is the process of converting between two different alphabets at a character-by-character level.
    Unlike translation, transliterating does not take into account the semantic meaning of words.
    This function transliterates between the Greek and Latin alphabets.
    >>> greekify('python is awesome')
    'πψτηον ισ αωεσομε'
    >>> greekify('PyThoN Is AwEsOmE!!!')
    'ΠψΤηοΝ Ισ ΑωΕσΟμΕ!!!'
    >>> greekify('ΠψΤηοΝ Ισ ΑωΕσΟμΕ!!!')
    'PyThoN Is AwEsOmE!!!'
    >>> greekify('CSCI040')
    'CΣCΙ040'
    >>> greekify('Crescit cum commercio civitas.')
    'Cρεσcιτ cυμ cομμερcιο cιvιτασ.'
    >>> greekify('Claremont McKenna College’s mission is "to educate its students for thoughtful and productive lives and responsible leadership in business, government, and the professions, and to support faculty and student scholarship that contribute to intellectual vitality and the understanding of public policy issues."')
    'Cλαρεμοντ ΜcΚεννα Cολλεγε’σ μισσιον ισ "το εδυcατε ιτσ στυδεντσ φορ τηουγητφυλ ανδ προδυcτιvε λιvεσ ανδ ρεσπονσιβλε λεαδερσηιπ ιν βυσινεσσ, γοvερνμεντ, ανδ τηε προφεσσιονσ, ανδ το συππορτ φαcυλτψ ανδ στυδεντ σcηολαρσηιπ τηατ cοντριβυτε το ιντελλεcτυαλ vιταλιτψ ανδ τηε υνδερστανδινγ οφ πυβλιc πολιcψ ισσυεσ."'

    NOTE:
    The `greek_alphabet` and `latin_alphabet` variables provide a mapping between the greek and latin alphabets.
    For example, we know that 'Δ' corresponds to 'D' because the occur at the same position in both strings.
    HINT:
    You should loop over the input text using the accumulator pattern.
    If the next character is at position i in `greek_alphabet`,
    then add the character at position i in the `latin_alphabet` to the accumulator (and vice versa).
    If the character is not in either string,
    then just add that character to the accumulator.
    '''
    greek_alphabet = 'ΑαΒβΓγΔδΕεΖζΗηΘθΙιΚκΛλΜμΝνΞξΟοΠπΡρΣσςΤτΥυΦφΧχΨψΩω'
    latin_alphabet = 'AaBbGgDdEeZzHhJjIiKkLlMmNnXxOoPpRrSssTtUuFfQqYyWw'
    text_accumulator = ''
    for i in range(len(text)):
        x = text[i]
        l = latin_alphabet.find(x)
        g = greek_alphabet.find(x)

        if l == -1 and g == -1:
            text_accumulator += x
        elif l == -1 and g >= 0:
            l = latin_alphabet[g]
            text_accumulator += l
        else:
            g = greek_alphabet[l]
            text_accumulator += g

    return text_accumulator


def character_equality(x, y):
    '''
    >>> character_equality('A', 'a')
    False
    >>> character_equality('A', 'A')
    True
    >>> character_equality('A', 'Α')
    False
    >>> character_equality('Á', 'A\u0301')
    True
    >>> character_equality('Á', 'Á')
    False
    >>> 'Á' == 'Á'
    False
    >>> character_equality('lập trình máy tính là tốt nhất !!!', 'lập trình máy tính là tốt nhất !!!')
    False
    '''

    if x == y:
        return True
    else:
        return False


def grapheme_equality(x, y):
    '''
    >>> grapheme_equality('A', 'a')
    False
    >>> grapheme_equality('A', 'A')
    True
    >>> grapheme_equality('A', 'Α')
    False
    >>> grapheme_equality('Á', 'A\u0301')
    True
    >>> grapheme_equality('Á', 'Á')
    True
    >>> 'Á' == 'Á'
    False
    >>> grapheme_equality('lập trình máy tính là tốt nhất !!!', 'lập trình máy tính là tốt nhất !!!')
    True
    '''
    import unicodedata

    z = unicodedata.normalize('NFC', x)
    v = unicodedata.normalize('NFC', y)
    if z == v:
        return True
    else:
        return False
