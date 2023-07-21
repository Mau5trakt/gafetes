inicio = """
SELECT * FROM prestamos 
    INNER JOIN 
        usuarios u on u.id_usuario = prestamos.usuario_id 
    INNER JOIN gafetes g on g.id_gafete = prestamos.gafete_id 
WHERE hora_fin IS NULL ;
"""