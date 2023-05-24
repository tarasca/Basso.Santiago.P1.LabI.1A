from functions import *

path_csv = 'insumos.csv'
path_json = str
path_txt = 'marcas.txt'
local_data = []
path_act = str

while True:
    opt = menu()

    match(opt):
        case "1":
            local_data = carga_csv(path_csv)
            pass 
        case "2":
            print_marcas_cant(local_data)
            pass    
        case "3":
            print_marcas_cant_precio(local_data)
            pass
        case "4":
            search_insumo(local_data)
            pass     
        case "5":
            print_ordenados(local_data)
            pass    
        case "6":
            realizar_compras(local_data)
            pass     
        case "7":
            path_json = json_pass(local_data)
            pass
        case "8":
            print_json(path_json)
            pass     
        case "9":
            actualizar_precios(path_csv,local_data)
            pass
        case "10":   
            agregar_insumo(local_data,path_txt)
            pass
        case "11":
            path_act = save_newdata(local_data)
            pass
        case "12":
            break   





















