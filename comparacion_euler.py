"""Compara la solución exacta con el método de Euler para una EDO separable."""

import math


def solucion_exacta(t: float) -> float:
    """Devuelve la solución analítica y(t) = 5 * exp(-t²)."""
    return 5.0 * math.exp(-(t**2))


def comparar_metodos(t0: float, y0: float, t_final: float, h: float) -> None:
    """Imprime una comparación paso a paso entre Euler y la solución exacta.

    El último paso se acorta si el intervalo no es un múltiplo exacto de h.
    Los tiempos se calculan desde el índice entero del paso para evitar
    acumular errores de punto flotante.
    """
    if h <= 0:
        raise ValueError("El paso h debe ser mayor que cero.")
    if t_final < t0:
        raise ValueError("El tiempo final debe ser mayor o igual que t0.")

    duracion = t_final - t0
    cociente = duracion / h
    pasos_cercanos = round(cociente)
    if pasos_cercanos >= 1 and math.isclose(
        cociente, pasos_cercanos, rel_tol=1e-12, abs_tol=1e-12
    ):
        numero_pasos = pasos_cercanos
    else:
        numero_pasos = math.ceil(cociente)

    def imprimir_fila(t: float, y_euler: float) -> None:
        """Imprime los valores y errores correspondientes a un tiempo."""
        y_exacta = solucion_exacta(t)
        error_absoluto = abs(y_exacta - y_euler)
        error_relativo = (
            error_absoluto / abs(y_exacta) * 100.0 if y_exacta != 0 else 0.0
        )
        print(
            f"{t:8.4f} | {y_exacta:20.10f} | {y_euler:20.10f} | "
            f"{error_absoluto:16.10f} | {error_relativo:20.6f}"
        )

    print(
        f"{'t':>8} | {'Solución Analítica':>20} | "
        f"{'Aproximación Euler':>20} | {'Error Absoluto':>16} | "
        f"{'Error Relativo (%)':>20}"
    )
    print("-" * 100)

    t = t0
    y = y0
    imprimir_fila(t, y)

    for indice in range(1, numero_pasos + 1):
        t_siguiente = min(t0 + indice * h, t_final)
        paso_actual = t_siguiente - t
        y += paso_actual * (-2.0 * t * y)
        t = t_siguiente
        imprimir_fila(t, y)


if __name__ == "__main__":
    comparar_metodos(t0=0.0, y0=5.0, t_final=1.0, h=0.2)
