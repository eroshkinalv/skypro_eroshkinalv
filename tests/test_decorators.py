from src.decorators import log


def test_log_1(capsys):
    @log(filename="mylog.txt")
    def my_function(x, y):
        return x + y

    result = my_function(1, 2)
    assert result == 3


def test_log_2(capsys):
    @log()
    def my_function(x, y):
        return x + y

    result = my_function(1, 2)
    assert result == 3


def test_log_3(capsys):
    @log()
    def my_function(x, y):
        return x + y

    result = my_function("1", "2")
    assert result == "my_function error: <TypeError>. Inputs: ('1', '2'), {}\n"


def test_log_to_file():
    @log(filename="test_log.txt")
    def my_function(x, y):
        return x + y

    my_function(1, 2)

    with open("test_log.txt", "r", encoding="utf-8") as file:
        log_content = file.read()

    assert "my_function ok" in log_content
