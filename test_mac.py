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




###################################### TESTS / Pruebas ##################################################
def test_registrar_un_producto():
    reiniciar_listas(sucursal_boedo)
    sucursal_boedo.registrar_producto(remera_talle_s)
    assert len(sucursal_boedo.productos) == 1
    
def test_registrando_multiples_productos_3():
    sucursal_boedo.registrar_producto(zapatos_negros)
    sucursal_boedo.registrar_producto(gorra_blanca)
    sucursal_boedo.registrar_producto(remera_talle_s)
    assert len(sucursal_boedo.productos) == 3
    
def test_verifico_si_tengo_stock():
    reiniciar_listas(sucursal_boedo)
    sucursal_boedo.registrar_producto(remera_talle_s)
    sucursal_boedo.recargar_stock(100, 500)
    assert sucursal_boedo.hay_stock(100) == True
    
def test_recargo_el_stock_de_remera():
    reiniciar_listas(sucursal_boedo)
    sucursal_boedo.registrar_producto(remera_talle_s)
    sucursal_boedo.recargar_stock(100, 320)
    assert sucursal_boedo.hay_stock(100)

def test_recargar_varios_productos_a_nuestro_stock_en_total_tres_y_valido_us_cantidades():
    reiniciar_listas(sucursal_boedo)
    reiniciar_stock(remera_talle_s)
    sucursal_boedo.registrar_producto(remera_talle_s)
    sucursal_boedo.registrar_producto(jean_talle_40)
    sucursal_boedo.registrar_producto(gorra_blanca)
    sucursal_boedo.recargar_stock(100, 1)
    sucursal_boedo.recargar_stock(200, 50)
    sucursal_boedo.recargar_stock(300, 10)
    assert gorra_blanca.stock == 10
    assert remera_talle_s.stock == 1
    assert jean_talle_40.stock == 50
    
def test_muestro_mi_stock_sin_productos_y_por_ende_estara_vacio():
    reiniciar_listas(sucursal_boedo)
    reiniciar_stock(jean_talle_40)
    reiniciar_stock(gorra_blanca)
    sucursal_boedo.registrar_producto(gorra_blanca)
    assert sucursal_boedo.hay_stock(300) == False
    
def test_calculo_el_precio_final_con_cliente_extranjero():
    reiniciar_listas(sucursal_boedo)
    sucursal_boedo.registrar_producto(remera_talle_s)
    sucursal_boedo.recargar_stock(100, 500)
    assert sucursal_boedo.calcular_precio_final(remera_talle_s, True) == 1500
    
def test_calculo_el_precio_final_con_comprador_local():
    reiniciar_listas(sucursal_boedo)
    sucursal_boedo.registrar_producto(remera_talle_s)
    sucursal_boedo.recargar_stock(100, 500)
    assert sucursal_boedo.calcular_precio_final(remera_talle_s, False) == 1815

def test_realizo_una_compra():
    reiniciar_listas(sucursal_boedo)
    sucursal_boedo.registrar_producto(remera_talle_s)
    sucursal_boedo.recargar_stock(100, 500)
    sucursal_boedo.realizar_compra(100,1, True)
    assert len(sucursal_boedo.ventas) == 1

def test_valido_cantidad_de_compras_que_seran_3():
    productos_previamente_recargados_retiro()
    sucursal_boedo.realizar_compra(100, 27, True)
    sucursal_boedo.realizar_compra(400, 21, True)
    sucursal_boedo.realizar_compra(300, 22, True)
    assert len(sucursal_boedo.ventas) == 3
    
def test_contar_por_categorias_con_dos_productos_de_distinta_categoria():
    reiniciar_listas(sucursal_boedo)
    sucursal_boedo.registrar_producto(remera_talle_s)
    sucursal_boedo.registrar_producto(jean_talle_40)
    assert sucursal_boedo.contar_categorias() == 2
    
def test_descontinuar_jean_talle_40_sin_stock():
    reiniciar_listas(sucursal_boedo)
    sucursal_boedo.descontinuar_productos()
    assert len(sucursal_boedo.productos) == 0
    
def test_vamos_a_buscar_productos_por_su_precio_como_referencia():
    reiniciar_listas(sucursal_boedo)
    sucursal_boedo.registrar_producto(remera_talle_s)
    sucursal_boedo.registrar_producto(jean_talle_40)
    assert remera_talle_s.precio == 1500
    assert jean_talle_40.precio == 3000


def test_ventas_del_dia_con_productos_y_35_und_del_mismo():
    reiniciar_listas(sucursal_boedo)
    sucursal_boedo.registrar_producto(remera_talle_s)
    sucursal_boedo.registrar_producto(jean_talle_40)
    sucursal_boedo.recargar_stock(100, 500)
    sucursal_boedo.recargar_stock(200, 500)
    sucursal_boedo.realizar_compra(100, 100, True)
    assert sucursal_boedo.valor_ventas_del_dia() == 150000