Affichez par ordre décroissant d’ancienneté les employés masculins dont le salaire net (salaire + commission) est supérieur ou égal à 8000. Le tableau résultant doit inclure les colonnes suivantes : Numéro d’employé, Prénom et Nom, Âge et Ancienneté.
Affichez les produits qui répondent aux critères suivants : (C1) la quantité est conditionnée en bouteille(s), (C2) le troisième caractère du nom du produit est 't' ou 'T', (C3) fournis par les fournisseurs 1, 2 ou 3, (C4) le prix unitaire est compris entre 70 et 200, et (C5) les unités commandées sont spécifiées (non nulles). Le tableau résultant doit inclure les colonnes suivantes : numéro de produit, nom du produit, numéro du fournisseur, unités commandées et prix unitaire.
Affichez les clients qui résident dans la même région que le fournisseur 1, c’est-à-dire qui partagent le même pays, la même ville et les trois derniers chiffres du code postal. La requête doit utiliser une seule sous-requête. Le tableau résultant doit inclure toutes les colonnes de la table client.
Pour chaque numéro de commande entre 10998 et 11003, faites ce qui suit : 
- Affichez le nouveau taux de remise, qui doit être de 0% si le montant total de la commande avant remise (prix unitaire * quantité) est compris entre 0 et 2000, 5% s’il est entre 2001 et 10000, 10% s’il est entre 10001 et 40000, 15% s’il est entre 40001 et 80000, et 20% sinon.
- Affichez le message "appliquer l’ancien taux de remise" si le numéro de commande est compris entre 10000 et 10999, et "appliquer le nouveau taux de remise" sinon. Le tableau résultant doit afficher les colonnes : numéro de commande, nouveau taux de remise et note d’application du taux de remise.
Affichez les fournisseurs de produits de boissons. Le tableau résultant doit afficher les colonnes : numéro du fournisseur, société, adresse et numéro de téléphone.
Affichez les clients de Berlin ayant commandé au plus 1 (0 ou 1) produit dessert. Le tableau résultant doit afficher la colonne : code client.
Affichez les clients résidant en France et le montant total des commandes qu’ils ont passées chaque lundi d’avril 1998 (en tenant compte des clients n’ayant pas encore passé de commande). Le tableau résultant doit afficher les colonnes : numéro client, nom de la société, numéro de téléphone, montant total et pays.
Affichez les clients ayant commandé tous les produits. Le tableau résultant doit afficher les colonnes : code client, nom de la société et numéro de téléphone.
 Affichez pour chaque client de France le nombre de commandes qu’il a passées. Le tableau résultant doit afficher les colonnes : code client et nombre de commandes.
Affichez le nombre de commandes passées en 1996, le nombre de commandes passées en 1997, et la différence entre ces deux nombres. Le tableau résultant doit afficher les colonnes : commandes en 1996, commandes en 1997 et Différence.

-- 1. Employés masculins avec salaire net ≥ 8000 (par ancienneté décroissante)
SELECT 
    EMPLOYEE_int AS "Numéro d'employé",
    FIRST_NAME AS "Prénom",
    LAST_NAME AS "Nom",
    EXTRACT(YEAR FROM AGE(CURRENT_DATE, BIRTH_DATE)) AS "Âge",
    EXTRACT(YEAR FROM AGE(CURRENT_DATE, HIRE_DATE)) AS "Ancienneté"
FROM EMPLOYEES
WHERE 
    TITLE = 'M.'  
    AND (SALARY + COMMISSION) >= 8000
ORDER BY "Ancienneté" DESC;

-- 2. Produits répondant aux critères spécifiés
SELECT 
    PRODUCT_REF AS "Numéro de produit",
    PRODUCT_NAME AS "Nom du produit",
    SUPPLIER_int AS "Numéro du fournisseur",
    UNITS_ON_ORDER AS "Unités commandées",
    UNIT_PRICE AS "Prix unitaire"
FROM PRODUCTS
WHERE 
    -- C1: Quantité conditionnée en bouteille(s)
    (QUANTITY ILIKE '%bouteille%' OR QUANTITY ILIKE '%bottle%')
    -- C2: 3ème caractère du nom est 't' ou 'T'
    AND SUBSTRING(PRODUCT_NAME, 3, 1) ILIKE 't'
    -- C3: Fournisseurs 1, 2 ou 3
    AND SUPPLIER_int IN (1, 2, 3)
    -- C4: Prix unitaire entre 70 et 200
    AND UNIT_PRICE BETWEEN 70 AND 200
    -- C5: Unités commandées sont spécifiées (non nulles)
    AND UNITS_ON_ORDER IS NOT NULL;

-- 3. Clients résidant dans la même région que le fournisseur 1
SELECT c.*
FROM CUSTOMERS c
WHERE (c.COUNTRY, c.CITY, RIGHT(c.POSTAL_CODE, 3)) = (
    SELECT COUNTRY, CITY, RIGHT(POSTAL_CODE, 3)
    FROM SUPPLIERS
    WHERE SUPPLIER_int = 1
);

--- 4. Nouveau taux de remise pour les commandes entre 10998 et 11003
SELECT 
    o.ORDER_int AS "Numéro de commande",
    CASE
        WHEN SUM(od.UNIT_PRICE * od.QUANTITY) BETWEEN 0 AND 2000 THEN 0
        WHEN SUM(od.UNIT_PRICE * od.QUANTITY) BETWEEN 2001 AND 10000 THEN 5
        WHEN SUM(od.UNIT_PRICE * od.QUANTITY) BETWEEN 10001 AND 40000 THEN 10
        WHEN SUM(od.UNIT_PRICE * od.QUANTITY) BETWEEN 40001 AND 80000 THEN 15
        ELSE 20
    END AS "Nouveau taux de remise",
    CASE
        WHEN o.ORDER_int BETWEEN 10000 AND 10999 THEN 'appliquer l''ancien taux de remise'
        ELSE 'appliquer le nouveau taux de remise'
    END AS "Note d'application du taux de remise"
FROM ORDERS o
INNER JOIN ORDER_DETAILS od ON o.ORDER_int = od.ORDER_int
WHERE o.ORDER_int BETWEEN 10998 AND 11003
GROUP BY o.ORDER_int
ORDER BY o.ORDER_int;

--- 5. Fournisseurs de produits de boissons
SELECT DISTINCT
    s.SUPPLIER_int AS "Numéro du fournisseur",
    s.COMPANY AS "Société",
    s.ADDRESS AS "Adresse",
    s.PHONE AS "Numéro de téléphone"
FROM SUPPLIERS s
INNER JOIN PRODUCTS p ON s.SUPPLIER_int = p.SUPPLIER_int
INNER JOIN CATEGORIES c ON p.CATEGORY_CODE = c.CATEGORY_CODE
WHERE c.CATEGORY_NAME ILIKE '%boisson%' 
   OR c.CATEGORY_NAME ILIKE '%beverage%'
   OR c.CATEGORY_NAME ILIKE '%drink%';

   --- 6. Clients de Berlin ayant commandé au plus 1 produit dessert
   SELECT DISTINCT
    c.CUSTOMER_CODE AS "Code client"
FROM CUSTOMERS c
LEFT JOIN ORDERS o ON c.CUSTOMER_CODE = o.CUSTOMER_CODE
LEFT JOIN ORDER_DETAILS od ON o.ORDER_int = od.ORDER_int
LEFT JOIN PRODUCTS p ON od.PRODUCT_REF = p.PRODUCT_REF
LEFT JOIN CATEGORIES cat ON p.CATEGORY_CODE = cat.CATEGORY_CODE
WHERE 
    c.CITY = 'Berlin'
    AND (
        SELECT COUNT(DISTINCT od2.PRODUCT_REF)
        FROM ORDERS o2
        INNER JOIN ORDER_DETAILS od2 ON o2.ORDER_int = od2.ORDER_int
        INNER JOIN PRODUCTS p2 ON od2.PRODUCT_REF = p2.PRODUCT_REF
        INNER JOIN CATEGORIES cat2 ON p2.CATEGORY_CODE = cat2.CATEGORY_CODE
        WHERE 
            o2.CUSTOMER_CODE = c.CUSTOMER_CODE
            AND cat2.CATEGORY_NAME ILIKE '%dessert%'
    ) <= 1;

--- 7. Clients résidant en France et montant total des commandes chaque lundi d’avril 1998
SELECT 
    c.CUSTOMER_CODE AS "Numéro client",
    c.COMPANY AS "Nom de la société",
    c.PHONE AS "Numéro de téléphone",
    COALESCE(SUM(od.UNIT_PRICE * od.QUANTITY), 0) AS "Montant total",
    c.COUNTRY AS "Pays"
FROM CUSTOMERS c
LEFT JOIN ORDERS o ON c.CUSTOMER_CODE = o.CUSTOMER_CODE
LEFT JOIN ORDER_DETAILS od ON o.ORDER_int = od.ORDER_int
WHERE 
    c.COUNTRY = 'France'
    AND (
        (EXTRACT(DOW FROM o.ORDER_DATE) = 1  -- 1 = Lundi
        AND EXTRACT(YEAR FROM o.ORDER_DATE) = 1998
        AND EXTRACT(MONTH FROM o.ORDER_DATE) = 4)
        OR o.ORDER_int IS NULL  -- Pour les clients sans commande
    )
GROUP BY c.CUSTOMER_CODE, c.COMPANY, c.PHONE, c.COUNTRY
ORDER BY c.CUSTOMER_CODE;

-- 8. Clients ayant commandé tous les produits
    c.CUSTOMER_CODE AS "Code client",
    c.COMPANY AS "Nom de la société",
    c.PHONE AS "Numéro de téléphone"
FROM CUSTOMERS c
WHERE (
    SELECT COUNT(DISTINCT p.PRODUCT_REF)
    FROM PRODUCTS p
) = (
    SELECT COUNT(DISTINCT od.PRODUCT_REF)
    FROM ORDERS o
    INNER JOIN ORDER_DETAILS od ON o.ORDER_int = od.ORDER_int
    WHERE o.CUSTOMER_CODE = c.CUSTOMER_CODE
);

--- 9. Nombre de commandes par client français
SELECT 
    c.CUSTOMER_CODE AS "Code client",
    COUNT(o.ORDER_int) AS "Nombre de commandes"
FROM CUSTOMERS c
LEFT JOIN ORDERS o ON c.CUSTOMER_CODE = o.CUSTOMER_CODE
WHERE c.COUNTRY = 'France'
GROUP BY c.CUSTOMER_CODE
ORDER BY c.CUSTOMER_CODE;

--- 10. Nombre de commandes en 1996, 1997 et différence
SELECT 
    (SELECT COUNT(*) FROM ORDERS WHERE EXTRACT(YEAR FROM ORDER_DATE) = 1996) AS "Commandes en 1996",
    (SELECT COUNT(*) FROM ORDERS WHERE EXTRACT(YEAR FROM ORDER_DATE) = 1997) AS "Commandes en 1997",
    (SELECT COUNT(*) FROM ORDERS WHERE EXTRACT(YEAR FROM ORDER_DATE) = 1997) -
    (SELECT COUNT(*) FROM ORDERS WHERE EXTRACT(YEAR FROM ORDER_DATE) = 1996) AS "Différence";
