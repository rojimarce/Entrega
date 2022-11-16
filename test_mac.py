from mac import *
import pytest 


###################################### Machete ##########################################################
sucursal_boedo = SucursalFisica()
remera_talle_s = Prenda(100,"remera_s",1500,"remera")
jean_talle_40 = Prenda(200, "jean_talle_40", 3000, "jean")
zapatos_negros = Prenda(400, "zapatos_negros", 5000, "zapatos")
gorra_blanca = Prenda(300, "gorra_blanca", 4500, "gorra")

sucursal_lujan = SucursalVirtual()
remera_talle_s = Prenda(100,"remera_s",1500,"remera")
jean_talle_40 = Prenda(200, "jean_talle_40", 3000, "jean")
gorra_blanca = Prenda(300, "gorra_blanca", 4500, "gorra")
zapatos_negros = Prenda(400, "zapatos_negros", 5000, "zapatos")

def reiniciar_listas(sucursal):
    sucursal.productos.clear()
    sucursal.ventas.clear()

def reiniciar_stock(prenda):
    prenda.stock = 0

def reinicio_el_precio_de_las_prendas():
    remera_talle_s.precio = 1500
    jean_talle_40.precio = 3000
    gorra_blanca.precio = 4500
    zapatos_negros.precio = 5000

def productos_previamente_recargados_retiro():
    reiniciar_listas(sucursal_boedo)
    reiniciar_stock(Prenda)
    reinicio_el_precio_de_las_prendas()
    sucursal_boedo.registrar_producto(zapatos_negros)
    sucursal_boedo.registrar_producto(gorra_blanca)
    sucursal_boedo.registrar_producto(remera_talle_s)
    sucursal_boedo.registrar_producto(jean_talle_40)
    sucursal_boedo.recargar_stock(400, 100)
    sucursal_boedo.recargar_stock(100, 200)
    sucursal_boedo.recargar_stock(300, 600)
    sucursal_boedo.recargar_stock(200, 300)

def productos_previamente_recargados_air():
    reiniciar_listas(sucursal_lujan)
    reiniciar_stock(Prenda)
    reinicio_el_precio_de_las_prendas()
    sucursal_lujan.registrar_producto(zapatos_negros)
    sucursal_lujan.registrar_producto(gorra_blanca)
    sucursal_lujan.registrar_producto(remera_talle_s)
    sucursal_lujan.registrar_producto(jean_talle_40)
    sucursal_lujan.recargar_stock(400, 100)
    sucursal_lujan.recargar_stock(100, 200)
    sucursal_lujan.recargar_stock(300, 600)
    sucursal_lujan.recargar_stock(200, 300)




###################################### TESTS / Pruebas ###################################################
              