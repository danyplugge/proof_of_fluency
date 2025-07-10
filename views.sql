CREATE VIEW vw_onet_closest_oews AS
SELECT 
    a.ONETSOC_Code,
    a.Element_Name,
    b.A_MEAN AS avg_a_mean,
    b.TOT_EMP AS total_employment,
    b.OCC_CODE
FROM 
    onet_skills a
JOIN 
    oews_raw b ON LEFT(a.ONETSOC_Code, 7) = b.OCC_CODE; 

CREATE VIEW vw_oews_avg_over_onet AS
SELECT 
    a.OCC_CODE,  
    AVG(a.A_MEAN) AS avg_a_mean,              
    SUM(a.TOT_EMP) AS total_employment,
    b.Title,
    b.ONETSOC_Code
FROM 
    oews_raw a
JOIN
    onet_skills b ON a.OCC_CODE = (b.ONETSOC_Code, 7)
GROUP BY 
    a.OCC_CODE, b.ONETSOC_Code; 