from arithmetic_operations import perform_operation

def test_operations():
    assert perform_operation(10, 5, 'add') == 15
    assert perform_operation(10, 5, 'subtract') == 5
    assert perform_operation(10, 5, 'multiply') == 50
    assert perform_operation(10, 5, 'divide') == 2
    assert perform_operation(10, 0, 'divide') == "Error: Division by zero"
    assert perform_operation(10, 5, 'modulus') == "Error: Invalid operation"

    print("All tests passed!")

if __name__ == "__main__":
    test_operations()
