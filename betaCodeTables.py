# The file includes three conversion tables.
# - betacodeTranslit: one-to-one unconventional
# - translitLOC:      Library of Congress Romanization of Arabic
# - translitSearch:   simplified transliteration for search and alphabetization purposes
#### To add
# - translitArabic:   conversion to Arabic script (also requires a different function with Arabic orthography rules)
# - possibly other transliteration flavors: Brill, French, German and Spanish tranliteration system differ from LOC

# One-to-one transliteration for computational research
# - main principle: one Arabic character = one Latin character
# - understandable for Arabists, but has some unconventional symbols
betacodeTranslit = {
# Alphabet letters
    '_a' : 'ā', # alif
    'b'  : 'b', # bā’
    't'  : 't', # tā’
    '_t' : 'ṯ', # thā’
    '^g' : 'ǧ', # jīm
    'j'  : 'ǧ', # jīm
    '^c' : 'č', # chīm / Persian
    '*h' : 'ḥ', # ḥā’
    '.h' : 'ḥ', # ḥā’
    '_h' : 'ḫ', # khā’
    'd'  : 'd', # dāl
    '_d' : 'ḏ', # dhāl
    'r'  : 'r', # rā’
    'z'  : 'z', # zayn
    's'  : 's', # sīn
    '^s' : 'š', # shīn
    '*s' : 'ṣ', # ṣād
    '.s' : 'ṣ', # ṣād
    '*d' : 'ḍ', # ḍād
    '.d' : 'ḍ', # ḍād
    '*t' : 'ṭ', # ṭā’
    '.t' : 'ṭ', # ṭā’
    '*z' : 'ẓ', # ẓā’
    '.z' : 'ẓ', # ẓā’
    '`'  : 'ʿ', # ‘ayn
    '*g' : 'ġ', # ghayn
    '.g' : 'ġ', # ghayn
    'f'  : 'f', # fā’
    '*k' : 'ḳ', # qāf
    '.k' : 'ḳ', # qāf
    'q'  : 'ḳ', # qāf
    'k'  : 'k', # kāf
    'g'  : 'g', # gāf / Persian
    'l'  : 'l', # lām
    'm'  : 'm', # mīm
    'n'  : 'n', # nūn
    'h'  : 'h', # hā’
    'w'  : 'w', # wāw
    '_u' : 'ū', # wāw
    'y'  : 'y', # yā’
    '_i' : 'ī', # yā’
# Non-alphabetic letters
    '\'' : 'ʾ', # hamzaŧ
    '/a' : 'á', # alif maqṣūraŧ
    ':t' : 'ŧ', # tā’ marbūṭaŧ, add +, it in idafa (`_amma:t+ ba.gd_ad)
# Vowels
    '~a' : 'ã', # dagger alif
    'a'  : 'a', # fatḥaŧ
    'u'  : 'u', # ḍammaŧ
    'i'  : 'i', # kasraŧ

    '^n' : 'ȵ',  # n of tanwīn
    '.n' : 'ȵ',  # n of tanwīn
    '_n' : 'ȵ',  # n of tanwīn
    '*n' : 'ȵ'   # n of tanwīn
    }

# conventional US/LOC transliteration
translitLOC = {
# Alphabet letters
    'ā' : 'ā',  # alif
    'b' : 'b',  # bā’
    't' : 't',  # tā’
    'ṯ' : 'th', # thā’
    'ǧ' : 'j',  # jīm
    'č' : 'ch', # chīm / Persian
    'ḥ' : 'ḥ',  # ḥā’
    'ḫ' : 'kh', # khā’
    'd' : 'd',  # dāl
    'ḏ' : 'dh', # dhāl
    'r' : 'r',  # rā’
    'z' : 'z',  # zayn
    's' : 's',  # sīn
    'š' : 'sh', # shīn
    'ṣ' : 'ṣ',  # ṣād
    'ḍ' : 'ḍ',  # ḍād
    'ṭ' : 'ṭ',  # ṭā’
    'ẓ' : 'ẓ',  # ẓā’
    'ʿ' : 'ʿ',   # ‘ayn
    'ġ' : 'gh', # ghayn
    'f' : 'f',  # fā’
    'ḳ' : 'q',  # qāf
    'k' : 'k',  # kāf
    'g' : 'g',  # gāf / Persian
    'l' : 'l',  # lām
    'm' : 'm',  # mīm
    'n' : 'n',  # nūn
    'h' : 'h',  # hā’
    'w' : 'w',  # wāw
    'ū' : 'u',  # wāw
    'y' : 'y',  # yā’
    'ī' : 'i',  # yā’
# Non-alphabetic letters
    'ʾ' : 'ʾ',   # hamzaŧ
    'á' : 'ā',  # alif maqṣūraŧ
    'ŧ' : 'h',  # tā’ marbūṭaŧ
# Vowels
    'ã' : 'ā',  # dagger alif
    'a' : 'a',  # fatḥaŧ
    'u' : 'u',  # ḍammaŧ
    'i' : 'i',  # kasraŧ
    'aȵ' : '',  # tanwīn fatḥ
    'uȵ' : '',  # tanwīn ḍamm
    'iȵ' : '',  # tanwīn kasr
    }

# necessary for rendering searcheable lines
translitSearch = {
# Alphabet letters
    'ā' : 'a',  # alif
    'b' : 'b',  # bā’
    't' : 't',  # tā’
    'ṯ' : 'th', # thā’
    'ǧ' : 'j',  # jīm
    'č' : 'ch', # chīm / Persian
    'ḥ' : 'h',  # ḥā’
    'ḫ' : 'kh', # khā’
    'd' : 'd',  # dāl
    'ḏ' : 'dh', # dhāl
    'r' : 'r',  # rā’
    'z' : 'z',  # zayn
    's' : 's',  # sīn
    'š' : 'sh', # shīn
    'ṣ' : 's',  # ṣād
    'ḍ' : 'd',  # ḍād
    'ṭ' : 't',  # ṭā’
    'ẓ' : 'z',  # ẓā’
    'ʿ' : '',   # ‘ayn
    'ġ' : 'gh', # ghayn
    'f' : 'f',  # fā’
    'ḳ' : 'q',  # qāf
    'k' : 'k',  # kāf
    'g' : 'g',  # gāf / Persian
    'l' : 'l',  # lām
    'm' : 'm',  # mīm
    'n' : 'n',  # nūn
    'h' : 'h',  # hā’
    'w' : 'w',  # wāw
    'ū' : 'u',  # wāw
    'y' : 'y',  # yā’
    'ī' : 'i',  # yā’
# Non-alphabetic letters
    'ʾ' : '',   # hamzaŧ
    'á' : 'a',  # alif maqṣūraŧ
    'ŧ' : 'h',  # tā’ marbūṭaŧ
# Vowels
    'ã' : 'a',  # dagger alif
    'a' : 'a',  # fatḥaŧ
    'u' : 'u',  # ḍammaŧ
    'i' : 'i',  # kasraŧ
    'aȵ' : 'an',  # tanwīn fatḥ
    'uȵ' : '',  # tanwīn ḍamm
    'iȵ' : '',  # tanwīn kasr
    }

translitArabic = {
# Alphabet letters
    'ā' : ' ا ',  # alif
    'b' : ' ب ',  # bāʾ
    't' : ' ت ',  # tāʾ
    'ṯ' : ' ث ', # thāʾ
    'ǧ' : ' ج ',  # jīm
    'č' : ' چ ', # chīm / Persian
    'ḥ' : ' ح ',  # ḥāʾ
    'ḫ' : ' خ ', # khāʾ
    'd' : ' د ',  # dāl
    'ḏ' : ' ذ ', # dhāl
    'r' : ' ر ',  # rāʾ
    'z' : ' ز ',  # zayn
    's' : ' س ',  # sīn
    'š' : ' ش ', # shīn
    'ṣ' : ' ص ',  # ṣād
    'ḍ' : ' ض ',  # ḍād
    'ṭ' : ' ط ',  # ṭāʾ
    'ẓ' : ' ظ ',  # ẓāʾ
    'ʿ' : ' ع ',  # ʿayn
    'ġ' : ' غ ', # ghayn
    'f' : ' ف ',  # fā’
    'ḳ' : ' ق ',  # qāf
    'k' : ' ك ',  # kāf
    'g' : ' گ ',  # gāf / Persian
    'l' : ' ل ',  # lām
    'm' : ' م ',  # mīm
    'n' : ' ن ',  # nūn
    'h' : ' ه ',  # hāʾ
    'w' : ' و ',  # wāw
    'ū' : ' و ',  # wāw
    'y' : ' ي ',  # yāʾ
    'ī' : ' ي ',  # yāʾ
# Non-alphabetic letters
    'ʾ' : ' ء ',  # hamza
    'á' : ' ى ',  # alif maqṣūraŧ
    'ŧ' : ' ة ',  # tāʾ marbūṭaŧ
# Vowels
    'ã'  : ' ٰ ',  # dagger alif
    'a'  : ' َ ',  # fatḥaŧ
    'u'  : ' ُ ',  # ḍammaŧ
    'i'  : ' ِ ',  # kasraŧ
    'aȵ' : ' ً ',  # tanwīn fatḥ
    'uȵ' : ' ٌ ',  # tanwīn ḍamm
    'iȵ' : ' ٍ ',  # tanwīn kasr
    }
