'''my calculator operations'''
from decimal import Decimal
import pytest
from calculator.calculation import Calculation
from calculator.operations import add, subtract, multiply, divide


# Use pytest.mark.parametrize to provide various sets of test data
@pytest.mark.parametrize(
    'first_operand, second_operand, operation, expected',
    [
        (Decimal('5'), Decimal('3'), add, Decimal('8')),
        (Decimal('10'), Decimal('5'), subtract, Decimal('5')),
        (Decimal('4'), Decimal('2'), multiply, Decimal('8')),
        (Decimal('10'), Decimal('2'), divide, Decimal('5')),
        (Decimal('10'), Decimal('0'), divide, None),  # We will handle division by zero separately
    ]
)
def test_operation(first_operand, second_operand, operation, expected):
    '''Testing various operations'''
    # Directly use the Calculation constructor
    calculation = Calculation(first_operand, second_operand, operation)
    # If we're testing division, handle the potential division by zero case
    # pylint: disable=comparison-with-callable
    if operation == divide and second_operand == Decimal('0'):
        with pytest.raises(ValueError, match="Cannot divide by zero"):
            calculation.perform()
    else:
        assert calculation.perform() == expected, f"{operation.__name__} operation failed"

# Keeping the divide by zero test as is since it tests a specific case
def test_divide_by_zero():
    '''Testing the divide by zero exception'''
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        calculation = Calculation(Decimal('10'), Decimal('0'), divide)
        calculation.perform()
        # pylint: enable=comparison-with-callable
