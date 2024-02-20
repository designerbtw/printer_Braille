def characters(i):
    if i == 'а':
        GPIO.output(0, GPIO.HIGH)
        time.sleep(0.7)
        GPIO.output(0, GPIO.LOW)
        time.sleep(0.7)
        right()
        time.sleep(0.2)

    # б 13
    elif i == 'б':
        GPIO.output(0, GPIO.HIGH)
        GPIO.output(2, GPIO.HIGH)
        time.sleep(0.7)
        GPIO.output(0, GPIO.LOW)
        GPIO.output(2, GPIO.LOW)
        time.sleep(0.7)
        right()
        time.sleep(0.2)

    # в 2345
    elif i == 'в':
        GPIO.output(1, GPIO.HIGH)
        GPIO.output(2, GPIO.HIGH)
        GPIO.output(3, GPIO.HIGH)
        GPIO.output(4, GPIO.HIGH)
        time.sleep(0.7)
        GPIO.output(1, GPIO.LOW)
        GPIO.output(2, GPIO.LOW)
        GPIO.output(3, GPIO.LOW)
        GPIO.output(4, GPIO.LOW)
        time.sleep(0.7)
        right()
        time.sleep(0.2)

    # г 1234
    elif i == 'г':
        GPIO.output(0, GPIO.HIGH)
        GPIO.output(1, GPIO.HIGH)
        GPIO.output(2, GPIO.HIGH)
        GPIO.output(3, GPIO.HIGH)
        time.sleep(0.7)
        GPIO.output(0, GPIO.LOW)
        GPIO.output(1, GPIO.LOW)
        GPIO.output(2, GPIO.LOW)
        GPIO.output(3, GPIO.LOW)
        time.sleep(0.7)
        right()
        time.sleep(0.2)

    # д 124
    elif i == 'д':
        GPIO.output(0, GPIO.HIGH)
        GPIO.output(1, GPIO.HIGH)
        GPIO.output(3, GPIO.HIGH)
        time.sleep(0.7)
        GPIO.output(0, GPIO.LOW)
        GPIO.output(1, GPIO.LOW)
        GPIO.output(3, GPIO.LOW)
        time.sleep(0.7)
        right()
        time.sleep(0.2)

    # е 14
    elif i == 'е':
        GPIO.output(0, GPIO.HIGH)
        GPIO.output(3, GPIO.HIGH)
        time.sleep(0.7)
        GPIO.output(0, GPIO.LOW)
        GPIO.output(3, GPIO.LOW)
        time.sleep(0.7)
        right()
        time.sleep(0.2)

    # ё 16
    elif i == 'ё':
        GPIO.output(0, GPIO.HIGH)
        GPIO.output(5, GPIO.HIGH)
        time.sleep(0.7)
        GPIO.output(0, GPIO.LOW)
        GPIO.output(5, GPIO.LOW)
        time.sleep(0.7)
        right()
        time.sleep(0.2)

    # ж 234
    elif i == 'ж':
        GPIO.output(1, GPIO.HIGH)
        GPIO.output(2, GPIO.HIGH)
        GPIO.output(3, GPIO.HIGH)
        time.sleep(0.7)
        GPIO.output(1, GPIO.LOW)
        GPIO.output(2, GPIO.LOW)
        GPIO.output(3, GPIO.LOW)
        time.sleep(0.7)
        right()
        time.sleep(0.2)

    # з 1456
    elif i == 'з':
        GPIO.output(0, GPIO.HIGH)
        GPIO.output(3, GPIO.HIGH)
        GPIO.output(4, GPIO.HIGH)
        GPIO.output(5, GPIO.HIGH)
        time.sleep(0.7)
        GPIO.output(0, GPIO.LOW)
        GPIO.output(3, GPIO.LOW)
        GPIO.output(4, GPIO.LOW)
        GPIO.output(5, GPIO.LOW)
        time.sleep(0.7)
        right()
        time.sleep(0.2)

    # и 23
    elif i == 'и':
        GPIO.output(1, GPIO.HIGH)
        GPIO.output(2, GPIO.HIGH)
        time.sleep(0.7)
        GPIO.output(1, GPIO.LOW)
        GPIO.output(2, GPIO.LOW)
        time.sleep(0.7)
        right()
        time.sleep(0.2)

    # й 12356
    elif i == 'й':
        GPIO.output(0, GPIO.HIGH)
        GPIO.output(1, GPIO.HIGH)
        GPIO.output(2, GPIO.HIGH)
        GPIO.output(4, GPIO.HIGH)
        GPIO.output(5, GPIO.HIGH)
        time.sleep(0.7)
        GPIO.output(0, GPIO.LOW)
        GPIO.output(1, GPIO.LOW)
        GPIO.output(2, GPIO.LOW)
        GPIO.output(4, GPIO.LOW)
        GPIO.output(5, GPIO.LOW)
        time.sleep(0.7)
        right()
        time.sleep(0.2)

    # к 15
    elif i == 'к':
        GPIO.output(0, GPIO.HIGH)
        GPIO.output(4, GPIO.HIGH)
        time.sleep(0.7)
        GPIO.output(0, GPIO.LOW)
        GPIO.output(4, GPIO.LOW)
        time.sleep(0.7)
        right()
        time.sleep(0.2)

    # л 135
    elif i == 'л':
        GPIO.output(0, GPIO.HIGH)
        GPIO.output(2, GPIO.HIGH)
        GPIO.output(4, GPIO.HIGH)
        time.sleep(0.7)
        GPIO.output(0, GPIO.LOW)
        GPIO.output(2, GPIO.LOW)
        GPIO.output(4, GPIO.LOW)
        time.sleep(0.7)
        right()
        time.sleep(0.2)

    # м 125
    elif i == 'м':
        GPIO.output(0, GPIO.HIGH)
        GPIO.output(1, GPIO.HIGH)
        GPIO.output(4, GPIO.HIGH)
        time.sleep(0.7)
        GPIO.output(0, GPIO.LOW)
        GPIO.output(1, GPIO.LOW)
        GPIO.output(4, GPIO.LOW)
        time.sleep(0.7)
        right()
        time.sleep(0.2)

    # н 1245
    elif i == 'н':
        GPIO.output(0, GPIO.HIGH)
        GPIO.output(1, GPIO.HIGH)
        GPIO.output(3, GPIO.HIGH)
        GPIO.output(4, GPIO.HIGH)
        time.sleep(0.7)
        GPIO.output(0, GPIO.LOW)
        GPIO.output(1, GPIO.LOW)
        GPIO.output(3, GPIO.LOW)
        GPIO.output(4, GPIO.LOW)
        time.sleep(0.7)
        right()
        time.sleep(0.2)

    # о 145
    elif i == 'о':
        GPIO.output(0, GPIO.HIGH)
        GPIO.output(3, GPIO.HIGH)
        GPIO.output(4, GPIO.HIGH)
        time.sleep(0.7)
        GPIO.output(0, GPIO.LOW)
        GPIO.output(3, GPIO.LOW)
        GPIO.output(4, GPIO.LOW)
        time.sleep(0.7)
        right()
        time.sleep(0.2)

    # п 1235
    elif i == 'п':
        GPIO.output(0, GPIO.HIGH)
        GPIO.output(1, GPIO.HIGH)
        GPIO.output(2, GPIO.HIGH)
        GPIO.output(4, GPIO.HIGH)
        time.sleep(0.7)
        GPIO.output(0, GPIO.LOW)
        GPIO.output(1, GPIO.LOW)
        GPIO.output(2, GPIO.LOW)
        GPIO.output(4, GPIO.LOW)
        time.sleep(0.7)
        right()
        time.sleep(0.2)


    # р 1345
    elif i == 'р':
        GPIO.output(0, GPIO.HIGH)
        GPIO.output(2, GPIO.HIGH)
        GPIO.output(3, GPIO.HIGH)
        GPIO.output(4, GPIO.HIGH)
        time.sleep(0.7)
        GPIO.output(0, GPIO.LOW)
        GPIO.output(2, GPIO.LOW)
        GPIO.output(3, GPIO.LOW)
        GPIO.output(4, GPIO.LOW)
        time.sleep(0.7)
        right()
        time.sleep(0.2)

    # c 235
    elif i == 'с':
        GPIO.output(1, GPIO.HIGH)
        GPIO.output(2, GPIO.HIGH)
        GPIO.output(4, GPIO.HIGH)
        time.sleep(0.7)
        GPIO.output(1, GPIO.LOW)
        GPIO.output(2, GPIO.LOW)
        GPIO.output(4, GPIO.LOW)
        time.sleep(0.7)
        right()
        time.sleep(0.2)

    # т 2345
    elif i == 'т':
        GPIO.output(1, GPIO.HIGH)
        GPIO.output(2, GPIO.HIGH)
        GPIO.output(3, GPIO.HIGH)
        GPIO.output(4, GPIO.HIGH)
        time.sleep(0.7)
        GPIO.output(1, GPIO.LOW)
        GPIO.output(2, GPIO.LOW)
        GPIO.output(3, GPIO.LOW)
        GPIO.output(4, GPIO.LOW)
        time.sleep(0.7)
        right()
        time.sleep(0.2)

    # у 156
    elif i == 'у':
        GPIO.output(0, GPIO.HIGH)
        GPIO.output(4, GPIO.HIGH)
        GPIO.output(5, GPIO.HIGH)
        time.sleep(0.7)
        GPIO.output(0, GPIO.LOW)
        GPIO.output(4, GPIO.LOW)
        GPIO.output(5, GPIO.LOW)
        time.sleep(0.7)
        right()
        time.sleep(0.2)

    # ф 123
    elif i == 'ф':
        GPIO.output(0, GPIO.HIGH)
        GPIO.output(1, GPIO.HIGH)
        GPIO.output(2, GPIO.HIGH)
        time.sleep(0.7)
        GPIO.output(0, GPIO.LOW)
        GPIO.output(1, GPIO.LOW)
        GPIO.output(2, GPIO.LOW)
        time.sleep(0.7)
        right()
        time.sleep(0.2)

    # х 134
    elif i == 'х':
        GPIO.output(0, GPIO.HIGH)
        GPIO.output(2, GPIO.HIGH)
        GPIO.output(3, GPIO.HIGH)
        time.sleep(0.7)
        GPIO.output(0, GPIO.LOW)
        GPIO.output(2, GPIO.LOW)
        GPIO.output(3, GPIO.LOW)
        time.sleep(0.7)
        right()
        time.sleep(0.2)

    # ц 12
    elif i == 'ц':
        GPIO.output(0, GPIO.HIGH)
        GPIO.output(1, GPIO.HIGH)
        time.sleep(0.7)
        GPIO.output(0, GPIO.LOW)
        GPIO.output(1, GPIO.LOW)
        time.sleep(0.7)
        right()
        time.sleep(0.2)

    # ч 12345
    elif i == 'ч':
        GPIO.output(0, GPIO.HIGH)
        GPIO.output(1, GPIO.HIGH)
        GPIO.output(2, GPIO.HIGH)
        GPIO.output(3, GPIO.HIGH)
        GPIO.output(4, GPIO.HIGH)
        time.sleep(0.7)
        GPIO.output(0, GPIO.LOW)
        GPIO.output(1, GPIO.LOW)
        GPIO.output(2, GPIO.LOW)
        GPIO.output(3, GPIO.LOW)
        GPIO.output(4, GPIO.LOW)
        time.sleep(0.7)
        right()
        time.sleep(0.2)

    # ш 146
    elif i == 'ш':
        GPIO.output(0, GPIO.HIGH)
        GPIO.output(3, GPIO.HIGH)
        GPIO.output(5, GPIO.HIGH)
        time.sleep(0.7)
        GPIO.output(0, GPIO.LOW)
        GPIO.output(3, GPIO.LOW)
        GPIO.output(5, GPIO.LOW)
        time.sleep(0.7)
        right()
        time.sleep(0.2)

    # щ 1256
    elif i == 'щ':
        GPIO.output(0, GPIO.HIGH)
        GPIO.output(1, GPIO.HIGH)
        GPIO.output(4, GPIO.HIGH)
        GPIO.output(5, GPIO.HIGH)
        time.sleep(0.7)
        GPIO.output(0, GPIO.LOW)
        GPIO.output(1, GPIO.LOW)
        GPIO.output(4, GPIO.LOW)
        GPIO.output(5, GPIO.LOW)
        time.sleep(0.7)
        right()
        time.sleep(0.2)

    # ъ 13456
    elif i == 'ъ':
        GPIO.output(0, GPIO.HIGH)
        GPIO.output(2, GPIO.HIGH)
        GPIO.output(3, GPIO.HIGH)
        GPIO.output(4, GPIO.HIGH)
        GPIO.output(5, GPIO.HIGH)
        time.sleep(0.7)
        GPIO.output(0, GPIO.LOW)
        GPIO.output(2, GPIO.LOW)
        GPIO.output(3, GPIO.LOW)
        GPIO.output(4, GPIO.LOW)
        GPIO.output(5, GPIO.LOW)
        time.sleep(0.7)
        right()
        time.sleep(0.2)

    # ы 2356
    elif i == 'ы':
        GPIO.output(2, GPIO.HIGH)
        GPIO.output(3, GPIO.HIGH)
        GPIO.output(4, GPIO.HIGH)
        GPIO.output(5, GPIO.HIGH)
        time.sleep(0.7)
        GPIO.output(2, GPIO.LOW)
        GPIO.output(3, GPIO.LOW)
        GPIO.output(4, GPIO.LOW)
        GPIO.output(5, GPIO.LOW)
        time.sleep(0.7)
        right()
        time.sleep(0.2)

    # ь 23456
    elif i == 'ь':
        GPIO.output(1, GPIO.HIGH)
        GPIO.output(2, GPIO.HIGH)
        GPIO.output(3, GPIO.HIGH)
        GPIO.output(4, GPIO.HIGH)
        GPIO.output(5, GPIO.HIGH)
        time.sleep(0.7)
        GPIO.output(1, GPIO.LOW)
        GPIO.output(2, GPIO.LOW)
        GPIO.output(3, GPIO.LOW)
        GPIO.output(4, GPIO.LOW)
        GPIO.output(5, GPIO.LOW)
        time.sleep(0.7)
        right()
        time.sleep(0.2)

    # э 236
    elif i == 'э':
        GPIO.output(1, GPIO.HIGH)
        GPIO.output(2, GPIO.HIGH)
        GPIO.output(5, GPIO.HIGH)
        time.sleep(0.7)
        GPIO.output(1, GPIO.LOW)
        GPIO.output(2, GPIO.LOW)
        GPIO.output(5, GPIO.LOW)
        time.sleep(0.7)
        right()
        time.sleep(0.2)

    # ю 1346
    elif i == 'ю':
        GPIO.output(0, GPIO.HIGH)
        GPIO.output(2, GPIO.HIGH)
        GPIO.output(3, GPIO.HIGH)
        GPIO.output(5, GPIO.HIGH)
        time.sleep(0.7)
        GPIO.output(0, GPIO.LOW)
        GPIO.output(2, GPIO.LOW)
        GPIO.output(3, GPIO.LOW)
        GPIO.output(5, GPIO.LOW)
        time.sleep(0.7)
        right()
        time.sleep(0.2)

    # я 1236
    elif i == 'я':
        GPIO.output(0, GPIO.HIGH)
        GPIO.output(1, GPIO.HIGH)
        GPIO.output(2, GPIO.HIGH)
        GPIO.output(5, GPIO.HIGH)
        time.sleep(0.7)
        GPIO.output(0, GPIO.LOW)
        GPIO.output(1, GPIO.LOW)
        GPIO.output(2, GPIO.LOW)
        GPIO.output(5, GPIO.LOW)
        time.sleep(0.7)
        right()
        time.sleep(0.2)
    elif i == ' ':
        right()
        time.sleep(0.7)
    else:
        x.clear()
