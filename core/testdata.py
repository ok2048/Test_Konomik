class TestData:
    username_negative = [
        ('short', 'too short'),
        ('too_long_012345678901234567890123', 'too long'),
        ('кириллица', 'cyrillic'),
        ('UPPER', 'capital letters'),
        ('1qwerty', 'starts with digit')
    ]

    email_negative = [
        ('somewhere.com', 'without name'),
        ('sombodysomewhere.com', 'without @'),
        ('somebody@somewhere', 'without zone'),
        ('кир@илли.ца', 'cyrillic')
    ]

    password_nagative = [
        ('short67', 'too short'),
        ('too_long_01234567890123456789012345678901234567890123456789012345', 'too long'),
        ('withoutcapitals1', 'without capital letters'),
        ('Withoutdigits', 'without digits')
    ]