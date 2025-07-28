from utils import check_environment_variable
def main():
    test_check_environment_variable1()
    test_check_environment_variable2()
    test_check_environment_variable3()

def test_check_environment_variable1():
    assert check_environment_variable("USERNAME") == "hardboy001"
def test_check_environment_variable2():
    assert check_environment_variable("EMAIL") == "yepiengesso@gmail.com"

def test_check_environment_variable3():
    assert check_environment_variable("PWD") == "Hardboynedy1"

if __name__ == "__main__":
    main()