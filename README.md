# Comparación entre la solución exacta y el método de Euler

Este proyecto compara la solución analítica de una ecuación diferencial con
su aproximación numérica mediante el método de Euler.

## Planteamiento del problema

Se modela el decaimiento de sesiones activas en una caché. La variable `y`
representa la cantidad de sesiones activas, medida en miles, y `t` representa
el tiempo transcurrido, medido en horas. El modelo supone que la tasa de cambio
es proporcional a la cantidad de sesiones y al tiempo:

$$
\frac{dy}{dt} = -2ty, \qquad y(0) = 5.
$$

La condición inicial indica que al comienzo hay 5 mil sesiones activas.

## Resolución analítica por separación de variables

Partimos de la ecuación diferencial:

$$
\frac{dy}{dt} = -2ty.
$$

Separamos las variables, colocando los términos con `y` a la izquierda y los
términos con `t` a la derecha:

$$
\frac{1}{y}\,dy = -2t\,dt.
$$

Integramos ambos lados:

$$
\int \frac{1}{y}\,dy = \int -2t\,dt.
$$

$$
\ln|y| = -t^2 + C.
$$

Al exponenciar, absorbemos el signo y la constante en una nueva constante `A`:

$$
y = A e^{-t^2}.
$$

Aplicamos la condición inicial `y(0) = 5`:

$$
5 = A e^0 \quad\Longrightarrow\quad A = 5.
$$

Por lo tanto, la solución exacta es:

$$
y(t) = 5e^{-t^2}.
$$

## Ejecución

Con Python 3 instalado, ejecuta desde la raíz del proyecto:

```bash
python comparacion_euler.py
```

El programa aplica Euler en el intervalo `[0, 1]` con paso `h = 0.2` e imprime
la solución analítica, la aproximación numérica y sus errores en cada paso.

## Resultados

| t | Solución Analítica | Aproximación Euler | Error Absoluto | Error Relativo (%) |
|---:|---:|---:|---:|---:|
| 0.0 | 5.0000000000 | 5.0000000000 | 0.0000000000 | 0.000000 |
| 0.2 | 4.8039471958 | 5.0000000000 | 0.1960528042 | 4.081077 |
| 0.4 | 4.2607189448 | 4.6000000000 | 0.3392810552 | 7.963000 |
| 0.6 | 3.4883816304 | 3.8640000000 | 0.3756183696 | 10.767697 |
| 0.8 | 2.6364621202 | 2.9366400000 | 0.3001778798 | 11.385632 |
| 1.0 | 1.8393972059 | 1.9969152000 | 0.1575179941 | 8.563566 |

## Conclusión técnica

Euler aproxima la solución usando la pendiente al inicio de cada paso. En
`t = 0`, la pendiente es `dy/dt = -2(0)y = 0`; por eso, en el primer paso hasta
`t = 0.2`, la aproximación de Euler mantiene el valor inicial `y = 5`. La
solución exacta, en cambio, ya disminuye a aproximadamente `4.8039471958`.

La diferencia entre ambas soluciones es el error de truncamiento local
acumulado a lo largo de los pasos. En esta comparación, Euler sobreestima la
cantidad de sesiones durante el intervalo y el error relativo alcanza cerca de
`11.39 %` en `t = 0.8`; el resultado depende del tamaño de paso, y reducir `h`
generalmente mejora la aproximación.
