-- 1. Mostrar los nombres, salarios, comisiones y sueldos (salario + comisión) de todo empleado. Ordenar el resultado del menor al mayor salario. No usar función NVL.
SELECT
    NOMBRE_EMP,
    SALARIO,
    COMISION,
    SALARIO + COMISION AS SUELDO
FROM
    EMPLEADOS;

-- 2. Repetir la consulta anterior mostrando los sueldos reales que recibiría cada empleado.
SELECT
    NOMBRE_EMP,
    SALARIO,
    COMISION,
    SALARIO + NVL(COMISION, 0) AS SUELDO
FROM
    EMPLEADOS;

-- 3. Repetir el ejercicio anterior mostrando esta vez los sueldos anuales.
SELECT
    NOMBRE_EMP,
    SALARIO,
    COMISION,
    (SALARIO + NVL(COMISION, 0)) * 12 AS SUELDO
FROM
    EMPLEADOS;

-- 4. Mostrar los nombres y salarios en formatos monetarios de todo empleado.
SELECT 
    NOMBRE_EMP,
    TO_CHAR(SALARIO, '$999,999.99') AS SALARIO_FORMATO
FROM EMPLEADOS;

-- 5. Mostrar la fecha actual bajo el siguiente formato:
-- Martes, 10 de MAYO del 2013 - 10:10:00
SELECT
    TO_CHAR(
        SYSDATE,
        'DAY, DD "de" MONTH "del" YYYY - HH24:MI:SS'
    ) AS FECHA
FROM
    DUAL;

-- 6. Escribir una consulta que muestre el nombre del empleado(con la primera letra en mayúscula y las demás en minúsculas) y la longitud del nombre del empleado de aquellos que inician con la letra A o terminan en Z.
SELECT 
    INITCAP(LOWER(NOMBRE_EMP)) AS NOMBRE_FORMATO,
    LENGTH(NOMBRE_EMP) AS LONGITUD
FROM EMPLEADOS
WHERE NOMBRE_EMP LIKE 'A%'
   OR NOMBRE_EMP LIKE '%Z';

-- 7. Crear un reporte que muestre:
-- a. [Empleado] gana [SALARIO], pero su salario anual es [SALARIO_ANUAL]
SELECT 
    NOMBRE_EMP || ' gana ' || SALARIO || 
    ', pero su salario anual es ' || ((SALARIO + NVL(COMISION, 0)) * 12) || ' (' || (SALARIO  * 12) || ')' as Reporte
FROM EMPLEADOS;

-- 8. Mostrar un reporte con los siguientes campos:
-- a. [NOMBRE EMPLEADO] [HIRE_DATE] [DIA] [MES] [AÑO]
SELECT 
    NOMBRE_EMP,
    FECHA_ING,
    TO_CHAR(FECHA_ING, 'DD') AS DIA,
    TO_CHAR(FECHA_ING, 'MONTH') AS MES,
    TO_CHAR(FECHA_ING, 'YYYY') AS ANIO
FROM EMPLEADOS;

-- 9. Crear un reporte que muestre:
-- a. [NOMBRE EMPLEADO] [COMISION]
-- b. Si tiene comisión debe mostrarla en caso de que no tenga comisión mostrar el mensaje “SIN COMISION”
SELECT 
    NOMBRE_EMP,
    DECODE(COMISION, 
           NULL, 'SIN COMISION', 
           TO_CHAR(COMISION)) AS COMISION
FROM EMPLEADOS;

-- 10. Crear un reporte que muestre:
-- a. [NOMBRE EMPLEADO] [SALARIO] [RANGO DE SALARIO]
-- b. El rango se calcula de la siguiente manera:
-- i. Mayor a 4000 nivel 1
-- ii. [3000-4000] nivel 2
-- iii. [2000-3000] nivel 3
-- iv. Menor a 2000 nivel 4
SELECT 
    NOMBRE_EMP,
    SALARIO,
    CASE 
        WHEN SALARIO > 4000 THEN 'NIVEL 1'
        WHEN SALARIO BETWEEN 3000 AND 4000 THEN 'NIVEL 2'
        WHEN SALARIO BETWEEN 2000 AND 2999 THEN 'NIVEL 3'
        ELSE 'NIVEL 4'
    END AS RANGO_SALARIO
FROM EMPLEADOS;