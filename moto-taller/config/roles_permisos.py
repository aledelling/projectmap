# config/roles_permisos.py

# Diccionario de permisos por rol
PERMISOS = {
    'administrador': {
        'ver_usuarios': True,
        'editar_usuarios': True,
        'eliminar_usuarios': True,
        'gestionar_roles': True,
        'ver_logs': True,
        'respaldo_bd': True,
        'ver_facturas': True,
    },
    'tecnico': {
        'ver_ordenes_asignadas': True,
        'actualizar_estado_reparaciones': True,
        'subir_evidencia': True,
        'ver_historial_reparaciones': True,
    },
    'asesor': {
        'crear_orden': True,
        'asignar_tecnico': True,
        'crear_factura': True,
        'ver_inventario': True,
        'ver_historial_clientes': True,
        'aplicar_descuento': True,
        'ver_estado_pagos': True,
    },
    'cliente': {
        'consultar_estado_moto': True,
        'enviar_encuesta': True,
        'ver_historial_moto': True,
        'descargar_facturas': True,
        'solicitar_cita': True,
    },
}


def tiene_permiso(rol, permiso):
    """
    Verifica si el rol tiene el permiso solicitado.
    """
    return PERMISOS.get(rol, {}).get(permiso, False)
