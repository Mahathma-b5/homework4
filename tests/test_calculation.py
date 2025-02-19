'''my calculator test'''
from decimal import Decimal
import pytest
from calculator.calculation import Calculation
from calculator.operations import add, subtract, multiply, divide

# Use pytest.mark.parametrize to provide various sets of test data
@pytest.mark.parametrize(
    'operand1, operand2, operation, expected',
    [
        (Decimal('5'), Decimal('3'), add, Decimal('8')),
        (Decimal('10'), Decimal('5'), subtract, Decimal('5')),
        (Decimal('4'), Decimal('2'), multiply, Decimal('8')),
        (Decimal('10'), Decimal('2'), divide, Decimal('5')),
        (Decimal('10'), Decimal('0'), divide, None),  # We will handle division by zero separately
    ]
)
def test_calculation_operations(operand1, operand2, operation, expected):
    """
    Test calculation operations with various scenarios.
    
    This test ensures that the Calculation class correctly performs the arithmetic operation
    (specified by the 'operation' parameter) on two Decimal operands ('operand1' and 'operand2'),
    and that the result matches the expected outcome.
    """
    # If we're testing division, handle the potential division by zero case
    # pylint: disable=comparison-with-callable
    if operation == divide and operand2 == Decimal('0'):
        with pytest.raises(ValueError, match="Cannot divide by zero"):
            Calculation(operand1, operand2, operation).perform()
    else:
        # Explicit check to ensure that we're working with the operation function reference
        if callable(operation):
            calc = Calculation(operand1, operand2, operation)  # Create a Calculation instance with the provided operands and operation.
            assert calc.perform() == expected, f"Failed {operation.__name__} operation with {operand1} and {operand2}"  # Perform the operation and assert that the result matches the expected value.
        else:
            raise TypeError(f"Provided operation {operation} is not callable.")

def test_calculation_repr():
    """
    Test the string representation (__repr__) of the Calculation class.
    
    This test verifies that the repr method of a Calculation instance returns a string
    that accurately represents the state of the Calculation object, including its operands and operation.
    """
    calc = Calculation(Decimal('10'), Decimal('5'), add)  # Create a Calculation instance for testing.
    expected_repr = "Calculation(10, 5, add)"  # Define the expected string representation.
    assert repr(calc) == expected_repr, "The repr method output does not match the expected string."  # Assert that the actual string representation matches the expected string.

def test_divide_by_zero():
    """
    Test division by zero to ensure it raises a ValueError.
    
    This test checks that attempting to perform a division operation with a zero divisor
    correctly raises a ValueError, as dividing by zero is mathematically undefined and should be handled as an error.
    """
    calc = Calculation(Decimal('10'), Decimal('0'), divide)  # Create a Calculation instance with a zero divisor.
    with pytest.raises(ValueError, match="Cannot divide by zero"):  # Expect a ValueError to be raised.
        calc.perform()  # Attempt to perform the calculation, which should trigger the ValueError.
# pylint: enable=comparison-with-callable
