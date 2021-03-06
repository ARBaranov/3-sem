# + a
# + ab
# - b
# - ba
REGEXP_1 = r'a'

# + aab
# + abb
# + acb
# - ab
# - aabc
REGEXP_2 = r'\w{3}$'

# + sofia.mp3
# + sofia.mp4
# - sofia.mp7
# - sofia.mp34
REGEXP_3 = r'\D*[34]$'


# + taverna
# + versus
# + vera
# + zveri
# - zver
REGEXP_4 = r'(?!zver$)'

# - a
# - aa
# + aaa
# - aaaa
# - b
# - bb
# + bbb
# - bbbb
# - ccc
REGEXP_5 = r'[ab]{3}$'
REGEXP_5 = r'[^c]{3}$'

# - Ok
# - OkOk
# + OkOkOk
# - OkOkOkOk
# - ab
# - abab
# + ababab
# - abababab
REGEXP_6 = r'\w{2}{3}$'
REGEXP_6 = r'(Ok|ab){3}$'

# - aaa
# - aaa aaa
# + aaa Aaa aaa
# + aaa aaa Aaa
# + Aaa aaa aaa
# - A
# - aaa A aaa
REGEXP_7 = r'.* \w{3} '

# + abc
# + abc03
# + a-b-c-3
# + a.b.c.0
# - Aabc
# - abc1
# - #abc
REGEXP_8 = r'(?!.{4}$)'  # Negative Lookahead!
REGEXP_8 = '^a[^1]+$'