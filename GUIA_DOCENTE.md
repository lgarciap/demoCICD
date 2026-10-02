# Guía docente: multas, pruebas e integración continua

## Propósito

Esta demostración dura entre 15 y 20 minutos y está dirigida a estudiantes de
tercer año de Computación en Ingeniería de Software 2.

El ejemplo enseña este ciclo:

```text
Regla de negocio -> código -> pruebas -> integración continua -> corrección
```

Una biblioteca cobra Q2 por cada día de atraso en la devolución de un libro.
Después se agrega un máximo de Q20. Finalmente, una usuaria reporta que `-2`
días produce una multa negativa. La solución debe rechazar los días negativos
con `ValueError`.

## Archivos del ejemplo

- `multas.py`: implementación de la regla de negocio.
- `test_multas.py`: pruebas automatizadas con `unittest`.
- `preparar_etapa.py`: activa cada versión didáctica.
- `verificar.py`: ejecuta las pruebas y conserva el código de salida.
- `.github/workflows/ci.yml`: ejecuta las pruebas en GitHub Actions.

## Preparación

Abra PowerShell en la carpeta del ejemplo. Si el equipo usa `py` en lugar de
`python`, sustituya el comando en todas las instrucciones.

Deje activa la etapa 1:

```powershell
python preparar_etapa.py 1
python verificar.py
```

Debe observar 3 pruebas exitosas.

## Recorrido de las etapas

### Etapa 1: comportamiento inicial

Active y verifique:

```powershell
python preparar_etapa.py 1
python verificar.py
```

Implementación:

```python
return dias * 2
```

Resultado esperado: pasan las 3 pruebas.

- 0 días produce Q0.
- 3 días produce Q6.
- 15 días produce Q30.

Explicación: se implementa la regla original sin límite.

Pregunta: ¿qué caso importante todavía no está cubierto?

### Etapa 2: cambio incorrecto

Active y verifique:

```powershell
python preparar_etapa.py 2
python verificar.py
```

Implementación incorrecta:

```python
return 20
```

Resultado esperado: falla la prueba de 0 días, falla la de 3 días y pasa la de
15 días. Hay 2 fallos y 1 prueba exitosa.

Explicación: se cambió el resultado esperado de 15 días a Q20, pero la
implementación devuelve Q20 para todos los casos. El error se conserva
intencionalmente para mostrar una regresión.

Pregunta: ¿por qué no basta con actualizar solamente la prueba de 15 días?

### Etapa 3: corrección del límite

Active y verifique:

```powershell
python preparar_etapa.py 3
python verificar.py
```

Implementación:

```python
return min(dias * 2, 20)
```

Resultado esperado: pasan las 3 pruebas.

Explicación: se conserva la tarifa de Q2 y se agrega el máximo de Q20.

Pregunta: ¿qué valores probaría alrededor del límite, como 10 y 11 días?

### Etapa 4: incidente reportado

Active y verifique:

```powershell
python preparar_etapa.py 4
python verificar.py
```

Resultado esperado: pasan las 3 pruebas anteriores y falla la nueva prueba de
días negativos.

Explicación: la implementación actual calcula `-Q4` cuando recibe `-2`. Las
pruebas anteriores pasaban porque no incluían este caso. El reporte de la
usuaria se convirtió en una prueba reproducible que ahora revela el fallo.

Pregunta: ¿qué ventaja tiene conservar este caso como una prueba automatizada?

### Etapa 5: corrección del incidente

Active y verifique:

```powershell
python preparar_etapa.py 5
python verificar.py
```

Resultado esperado: pasan las 4 pruebas.

Explicación: los días negativos producen `ValueError` con un mensaje claro, y
se conservan la tarifa de Q2 y el límite de Q20.

Pregunta: ¿qué garantía aporta la prueba que espera `ValueError`?

## Activar CI con GitHub

El selector de una interfaz, si existe, no cambia archivos ni activa CI. Para
que GitHub Actions detecte una etapa, deben cambiarse los archivos, crear un
commit y hacer `push`.

Si todavía no existe un repositorio local:

```powershell
git init
git add .
git commit -m "Etapa 1: comportamiento inicial"
```

Después de conectar el repositorio local con un repositorio de GitHub, use este
flujo para cada etapa:

```powershell
python preparar_etapa.py N
```

El archivo `.github/workflows/ci.yml` se activa en cada `push` y en cada pull
request. En GitHub:

1. Abra la pestaña **Actions**.
2. Seleccione **Integración continua**.
3. Abra la ejecución correspondiente al commit.
4. Revise el paso **Ejecutar pruebas**.

Una marca verde significa que las pruebas pasaron. Una marca roja significa que
`verificar.py` terminó con código de salida `1`.

La secuencia esperada en GitHub es:

```text
Etapa 1: CI pasa
Etapa 2: CI falla
Etapa 3: CI pasa
Etapa 4: CI falla
Etapa 5: CI pasa
```

## Qué ocurre cuando CI falla

CI no corrige el código automáticamente. Informa que el cambio no cumple las
pruebas. El equipo debe revisar el error, corregir el código y crear otro
commit:

```text
CI falla -> revisar el error -> corregir -> probar -> nuevo commit
```

Si el repositorio tiene reglas de protección, un pull request con CI fallido
no puede combinarse.

## CI, entrega continua y despliegue continuo

- **Pruebas locales:** una persona ejecuta `python verificar.py` en su equipo.
- **Integración continua:** GitHub Actions ejecuta esas mismas pruebas en cada
  `push` y pull request.
- **Entrega continua:** sería construir una versión validada y dejarla lista
  para publicar. Esta demostración no implementa ese paso.
- **Despliegue continuo:** sería publicar automáticamente una versión en un
  servidor. Esta demostración no implementa ese paso.
- **DevOps:** el reporte de la usuaria se convierte en una prueba, la prueba
  revela el fallo, el código se corrige y CI confirma el resultado.

## Cierre

Deje activa la etapa 1:

```powershell
python preparar_etapa.py 1
python verificar.py
```

El resultado final esperado es que pasen las 3 pruebas de la etapa inicial.
