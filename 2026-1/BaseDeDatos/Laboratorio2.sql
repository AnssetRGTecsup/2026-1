-- 1. Mostrar los nombres, salarios, salarios diarios, salarios diarios redondeados (un decimal, 2 decimales) y salarios diarios truncados (un decimal, 2 decimales) de todo empleado.
SELECT 
    NOMBRE_EMP, 
    SALARIO, 
    SALARIO/30 as SALARIO_DIARIO,
    ROUND(SALARIO/30, 1) as SALARIO_DIARIO_Round1,
    ROUND(SALARIO/30, 2) as SALARIO_DIARIO_Round2,
    TRUNC(SALARIO/30, 1) as SALARIO_DIARIO_Trunc1,
    TRUNC(SALARIO/30, 2) as SALARIO_DIARIO_Trunc2
from 
    EMPLEADOS;

-- 2. Mostrar los nombres, fechas de contratación, fechas de inicio y final de las primeras vacaciones de todo empleado cuya permanencia actual en la empresa sea de entre 16000 y 16500 días.
-- Dichas vacaciones duran 30 días y empiezan a 400 días de sus contrataciones.
SELECT
    NOMBRE_EMP,
    FECHA_ING,
    FECHA_ING + 400 as VAC_INI,
    FECHA_ING + 400 + 30 as VAC_END
from
    EMPLEADOS
WHERE
    SYSDATE - FECHA_ING BETWEEN 16000 and 16500;

-- 3. Mostrar las siguientes fechas: actual, el último día del presente mes, el próximo viernes y la fecha de hace un mes. Así como también la cantidad de meses que faltan para fin de año.
SELECT 
    SYSDATE AS FECHA_ACTUAL,
    LAST_DAY(SYSDATE) AS FIN_DE_MES,
    NEXT_DAY(SYSDATE, 'VIERNES') AS PROXIMO_VIERNES,
    ADD_MONTHS(SYSDATE, -1) AS HACE_UN_MES,
    MONTHS_BETWEEN(
        TO_DATE('31/12/' || TO_CHAR(SYSDATE, 'YYYY'), 'DD/MM/YYYY'),
        SYSDATE
    ) AS MESES_FIN_ANIO
FROM DUAL; -- Tabla ficticia

-- ALTER SESSION SET NLS_LANGUAGE = SPANISH;
-- ALTER SESSION SET NLS_TERRITORY = SPAIN;

-- SELECT
    -- NEXT_DAY(SYSDATE, 'FRIDAY') AS PROXIMO_VIERNES
-- FROM DUAL;

-- 4. Mostrar las ubicaciones de todo departamento de las siguientes formas: literal, iniciales en mayúscula y en minúsculas. Además mostrar las longitudes de las cadenas así como la posición de la primera letra S de la cadena.
SELECT
    UBICACION,
    INITCAP(UBICACION),
    LOWER(UBICACION),
    LENGTH(UBICACION),
    INSTR(UBICACION, 'S') --IN String
FROM DEPART;

-- 5. Mostrar las naciones (en mayúscula), así como las 2 primeras letras y las 2 últimas.
SELECT
    UPPER(NATION),
    SUBSTR(NATION, 1, 2),
    SUBSTR(NATION, -2)
FROM
    NATION;

-- 6. Mostrar las naciones, sus áreas multiplicadas por 100 y sus poblaciones. Además comparar estas 2 últimas columnas (GREATEST y LEAST).
SELECT
    NATION,
    NATION.AREA * 100,
    POPULATION,
    GREATEST(AREA * 100, POPULATION) AS MAYOR,
    LEAST(AREA * 100, POPULATION) AS MENOR
FROM
    NATION;

-- 7. Mostrar los departamentos bajo el siguiente formato: NOMBRE_DEPT se ubica en UBICACION.
SELECT 
    NOMBRE_DEPT || ' se ubica en ' || UBICACION AS DESCRIPCION
FROM DEPART;