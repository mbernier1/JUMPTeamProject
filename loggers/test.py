from loggers import log

@log
def test_one(a, b):
    return a + b



@log
def test_exeption(a, b):
    raise Exception("Test exception")

test_one(1, 2)


test_exeption(1, 2)