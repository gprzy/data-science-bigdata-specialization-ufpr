arithmetic_expression = '23 + 7 * 50'

print(f'Arithmetic expression = "{arithmetic_expression}"\n')

print(f'Using "eval" result = {eval(arithmetic_expression)}')
print(f'Operators default order result = {23 + 7 * 50}')
print(f'"(23 + (7 * 50))" result = {23 + (7 * 50)}')
print(f'"((23 + 7) * 50)" result = {(23 + 7) * 50}')

print(
    f'Turning expression to',
    f'= "{arithmetic_expression[1] + arithmetic_expression[-1]*3}"',
    f'using strings!'
)
