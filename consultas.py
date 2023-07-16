inicio = """
SELECT nombre_prestamo, tipo, cedula, empresa, autoriza, hora_inicio, usuario, numero FROM prestamos
INNER JOIN usuarios ON (
        prestamos.usuario_id = usuarios.id_usuario)
INNER JOIN gafetes ON(
        prestamos.gafete_id = gafetes.id_gafete)
ORDER BY gafete_id;
"""