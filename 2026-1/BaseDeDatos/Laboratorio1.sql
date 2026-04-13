-- 1. Mostrar el nombre, salario y cod_dept con el alias departamento de los empleados del departamento 10 y 30 ordenados por el máximo salario
Select NOMBRE_EMP, SALARIO, COD_DEPT from EMPLEADOS WHERE COD_DEPT in (10, 30) ORDER BY SALARIO DESC;

--2. Mostrar a los empleados que tienen el tercer carácter del nombre la letra “R” y terminan con “Z” o con “S”
SELECT * from EMPLEADOS WHERE NOMBRE_EMP LIKE '__R%Z' or NOMBRE_EMP LIKE '__R%S';

--3. Mostrar los empleados que ingresaron el año 81 u 82 en los meses de enero o diciembre. No deben ser gerentes y deben tener un salario entre 1000 y 3500
SELECT * from EMPLEADOS WHERE EXTRACT(YEAR from FECHA_ING) in (1981, 1982) and EXTRACT(MONTH from FECHA_ING) in (1, 12) and SALARIO BETWEEN 1000 and 3500 AND PUESTO != 'GERENTE';

-- 4. Mostrar los empleados de los departamentos 10 y 30 que tengan derecho a comisión y que su puesto sea ANALISTA, VENDEDOR o ADMINISTRATIVO
Select * from EMPLEADOS WHERE COD_DEPT in (10, 30) AND PUESTO in ('ANALISTA', 'VENDEDOR', 'ADMINISTRATIVO') and COMISION IS not NULL;

-- 5. Mostrar los inventos de EDISON, LAND, LOUD y PASCAL que hayan realizado en la década de los 40, 70 y 80; ordenados por año y por inventor.
SELECT INVENTION, INVENTOR, YEAR
FROM INVENTION
WHERE UPPER(INVENTOR) IN ('EDISON', 'LAND', 'LOUD', 'PASCAL')
  AND (
        YEAR BETWEEN 1940 AND 1949 OR
        YEAR BETWEEN 1970 AND 1979 OR
        YEAR BETWEEN 1980 AND 1989
      )
ORDER BY YEAR, INVENTOR;

-- 6. Mostrar el código de nación, nombre de nación, capital, área y población (usar estos alias) de las naciones de que inicien con I ó G y que tengan un área mayor a 100,000
SELECT 
    CODE AS CODIGO,
    NATION AS NOMBRE,
    CAPITAL,
    AREA,
    POPULATION
FROM NATION
WHERE (NATION LIKE 'I%' OR NATION LIKE 'G%')
  AND AREA > 100000;

-- 7. Escribir la siguiente consulta y analizar el resultado:
-- SELECT NOMBRE_EMP, PUESTO, SALARIO FROM EMPLEADOS
-- WHERE SALARIO >= 1500
-- AND PUESTO = 'GERENTE' OR PUESTO = 'VENDEDOR';

-- 8. Escribir la siguiente consulta y compararla con la anterior.
-- SELECT NOMBRE_EMP, PUESTO, SALARIO FROM EMPLEADOS
-- WHERE SALARIO >= 1500
-- AND (PUESTO = 'GERENTE' OR PUESTO = 'VENDEDOR');

-- 9. Mostrar los nombres, puestos y salarios de aquellos empleados que laboren en el departamento 30. Ordenarlos en función al puesto que ocupen, al salario (de mayor a menor) y finalmente por nombre alfabéticamente.
SELECT NOMBRE_EMP, PUESTO, SALARIO
FROM EMPLEADOS
WHERE COD_DEPT = 30
ORDER BY PUESTO ASC, SALARIO DESC, NOMBRE_EMP ASC;

-- 10. Mostrar a todo los departamentos almacenados en la tabla DEPART ordenados en forma descendente por ubicación y por código. Emplear posiciones para el ordenamiento
SELECT COD_DEPT, NOMBRE_DEPT, UBICACION
FROM DEPART
ORDER BY 3 DESC, 1 DESC;