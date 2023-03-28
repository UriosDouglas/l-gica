import math

coeficiente_a = float(input('Digite o coeficiente de "a" '))
(coeficiente_b) = float(input('Digite o coeficiente de "b" '))
coeficiente_c = float(input('Digite o coeficiente de "c" '))

delta = coeficiente_b**2 - 4*coeficiente_a*coeficiente_c

if delta < 0:
    print('não há raízes reais.')
elif delta == 0:
    x = -coeficiente_b / (2*coeficiente_a)
    print(f'A raiz dupla é {x}')
else:
    x1 = (-coeficiente_b + math.sqrt(delta)) / (2*coeficiente_a)
    x2 = (-coeficiente_b - math.sqrt(delta)) / (2*coeficiente_a)
    print(f'As raízes são {x1} e {x2}')
