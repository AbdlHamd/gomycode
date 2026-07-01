SET search_path TO exercise;

SELECT * FROM employe_projet;

--Employés affectés à plus d'un projet
SELECT e.nom, COUNT(ep.Projet_Num_P) AS NombreProjets
FROM employe e
INNER JOIN employe_projet ep ON ep.employe_num_e = e.num_e
GROUP BY e.num_e, e.nom
HAVING COUNT(ep.projet_num_p) > 1

--Projets gérés par chaque département
SELECT p.titre AS Projet, 
d.libelle AS Departement, 
d.responsable
FROM projet p
INNER JOIN departement d ON d.num_s = p.departement_num_s

--Employés travaillant sur le projet "Refonte du site web"
SELECT e.nom, ep.role, p.titre
FROM employe e
INNER JOIN employe_projet ep ON ep.employe_num_e = e.num_e
INNER JOIN projet p ON ep.projet_num_p = p.num_p
WHERE p.titre = 'Refonte du site web';

-- Département ayant le plus grand nombre d'employés
SELECT 
    d.Libelle,
    d.Responsable,
    COUNT(e.Num_E) AS NombreEmployes
FROM departement d
LEFT JOIN Employe e ON d.Num_S = e.Departement_Num_S
GROUP BY d.Num_S, d.Libelle, d.Responsable
ORDER BY NombreEmployes DESC
LIMIT 1;

--Employés avec salaire > 60000 et nom de leur département
SELECT 
    e.Nom,
    e.Poste,
    e.Salaire,
    d.Libelle AS Departement
FROM exercise.Employe e
INNER JOIN exercise.Departement d ON e.Departement_Num_S = d.Num_S
WHERE e.Salaire > 60000
ORDER BY e.Salaire DESC;


--Nombre d'employés affectés à chaque projet
SELECT 
    p.Titre,
    COUNT(ep.Employe_Num_E) AS NombreEmployes
FROM exercise.Projet p
LEFT JOIN exercise.Employe_Projet ep ON p.Num_P = ep.Projet_Num_P
GROUP BY p.Num_P, p.Titre
ORDER BY NombreEmployes DESC, p.Titre;


--Résumé des rôles des employés dans les projets
SELECT 
    e.Nom AS Employe,
    p.Titre AS Projet,
    ep.Role
FROM exercise.Employe e
INNER JOIN exercise.Employe_Projet ep ON e.Num_E = ep.Employe_Num_E
INNER JOIN exercise.Projet p ON ep.Projet_Num_P = p.Num_P
ORDER BY e.Nom, p.Titre;


--Dépense salariale totale par département
SELECT 
    d.Libelle,
    d.Responsable,
    SUM(e.Salaire) AS MasseSalariale
FROM exercise.Departement d
LEFT JOIN exercise.Employe e ON d.Num_S = e.Departement_Num_S
GROUP BY d.Num_S, d.Libelle, d.Responsable
ORDER BY MasseSalariale DESC;


 