# Array1D

Array1D es una clase en Python que representa un array unidimensional con operaciones básicas como suma, resta, diferencia absoluta, media, máximo y mínimo. Permite inicializarse con un rango de valores o con una lista predefinida, validando los límites y asegurando que las operaciones se realicen entre arrays de la misma longitud.

## Uso

```python
vector1 = Array1D(0, 10)
vector2 = Array1D(10, 20)

sum_result = vector1 + vector2
print(sum_result)  # Suma elemento a elemento

diff_result = vector1.difference(vector2)
print(diff_result)  # Diferencia absoluta elemento a elemento

print("Media del vector 1:", vector1.mean())
print("Máximo del vector 2:", vector2.max())
```
