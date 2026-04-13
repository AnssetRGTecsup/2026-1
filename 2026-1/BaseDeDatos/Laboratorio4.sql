-- 1. ¿Las funciones de grupo incluyen los NULOS en sus cálculos?.- Respondan sí o no y la razón.
-- 2. Encontrar el salario más alto, el más bajo, la suma y el promedio de todos los empleados
SELECT 
    MAX(SALARIO) AS SALARIO_MAX,
    MIN(SALARIO) AS SALARIO_MIN,
    SUM(SALARIO) AS SUMA_SALARIOS,
    AVG(SALARIO) AS PROMEDIO_SALARIO
FROM EMPLEADOS;

-- 3. Modificar la consulta anterior y mostrar los resultados por cada puesto.
SELECT 
    PUESTO,
    MAX(SALARIO) AS SALARIO_MAX,
    MIN(SALARIO) AS SALARIO_MIN,
    SUM(SALARIO) AS SUMA_SALARIOS,
    AVG(SALARIO) AS PROMEDIO_SALARIO
FROM EMPLEADOS
GROUP BY PUESTO;

-- 4. Mostrar el número de empleados que tienen el mismo puesto.
SELECT 
    PUESTO,
    COUNT(*) AS NUM_EMPLEADOS
FROM EMPLEADOS
GROUP BY PUESTO;

-- 5. Mostrar la diferencia entre el máximo salario y el mínimo salario
SELECT 
    MAX(SALARIO) - MIN(SALARIO) AS DIFERENCIA_SALARIAL
FROM EMPLEADOS;

-- 6. Mostrar los puestos que tienen más de 3 empleados
SELECT 
    PUESTO,
    COUNT(*) AS TOTAL
FROM EMPLEADOS
GROUP BY PUESTO
HAVING COUNT(*) > 3;

-- 7. Mostrar los departamentos que tengan menos de 3 empleados y que su salario sea menos 3000.
SELECT 
    COD_DEPT,
    COUNT(*) AS TOTAL_EMPLEADOS
FROM EMPLEADOS
WHERE SALARIO < 3000
GROUP BY COD_DEPT
HAVING COUNT(*) < 3;