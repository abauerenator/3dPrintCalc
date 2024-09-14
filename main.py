from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
from kivy.utils import platform
from kivy.lang.builder import Builder


import json
import requests  # Importar el módulo requests

if platform == "android":
    from android.permissions import request_permissions, Permission
    request_permissions([Permission.INTERNET, Permission.WRITE_EXTERNAL_STORAGE, 
Permission.READ_EXTERNAL_STORAGE])


class CalculadoraImpresionApp(App):
    #Window.size = (1200, 600)  # Ajusta estos valores según tus preferencias
    
    def build(self):
        return Builder.load_file('CalculadoraImpresion.kv')
        self.icon = '3dPrintCalc.ico'
        
        
    def on_start(self):
        # Ejecutar la función obtener_cotizacion_dolar al iniciar la app
        self.obtener_cotizacion_dolar()

        # Cargar los datos desde el archivo JSON
        try:
            with open('datos.json', 'r') as archivo:
                datos = json.load(archivo)

            # Actualizar los campos con los datos cargados
            self.root.ids.material_cost_input.text = datos.get('material_cost_kg', '')
            self.root.ids.material_input.text = datos.get('material', '')
            self.root.ids.extra_material_input.text = datos.get('extra_material', '')
            self.root.ids.tiempo_input.text = datos.get('tiempo', '')
            self.root.ids.consumo_w_input.text = datos.get('consumo_w', '')
            self.root.ids.costo_kw_input.text = datos.get('costo_kw', '')
            self.root.ids.mano_obra_input.text = datos.get('mano_obra', '')
            self.root.ids.costo_mano_obra_input.text = datos.get('costo_mano_obra', '')
            self.root.ids.costo_adquisicion_input.text = datos.get('costo_adquisicion', '')
            self.root.ids.vida_util_input.text = datos.get('vida_util', '')
            self.root.ids.valor_residual_input.text = datos.get('valor_residual', '')
            self.root.ids.costo_mantenimiento_input.text = datos.get('costo_mantenimiento', '')
            self.root.ids.porcentaje_ganacia_input.text = datos.get('porcentaje_ganacia', '')
            self.root.ids.porcentaje_iva_input.text = datos.get('IVA %', '')
            self.root.ids.costo_embalaje_input.text = datos.get('costo embalaje', '')
            self.root.ids.costo_envio_input.text = datos.get('costo envio', '')
            # Actualiza otros campos aquí

        except FileNotFoundError:
            pass  # El archivo aún no existe
        
        #return BoxLayout()
    pass



    def on_stop(self):
        # Obtener los valores de los campos y guardarlos en un diccionario
        datos = {
            'material_cost_kg': self.root.ids.material_cost_input.text,
            'material': self.root.ids.material_input.text,
            'extra_material': self.root.ids.extra_material_input.text,
            'tiempo': self.root.ids.tiempo_input.text,
            'consumo_w': self.root.ids.consumo_w_input.text,
            'costo_kw': self.root.ids.costo_kw_input.text,
            'mano_obra': self.root.ids.mano_obra_input.text,
            'costo_mano_obra': self.root.ids.costo_mano_obra_input.text,
            'costo_adquisicion': self.root.ids.costo_adquisicion_input.text,
            'vida_util': self.root.ids.vida_util_input.text,
            'valor_residual': self.root.ids.valor_residual_input.text,
            'costo_mantenimiento': self.root.ids.costo_mantenimiento_input.text,
            'porcentaje_ganacia': self.root.ids.porcentaje_ganacia_input.text,
            'IVA %': self.root.ids.porcentaje_iva_input.text,
            'costo embalaje': self.root.ids.costo_embalaje_input.text,
            'costo envio': self.root.ids.costo_envio_input.text,
            # Agrega otros campos aquí
        }

        # Guardar los datos en un archivo JSON
        with open('datos.json', 'w') as archivo:
            json.dump(datos, archivo)

    def calcular_costo(self):
        try:
            material_costo_kg = float(self.root.ids.material_cost_input.text)
        except ValueError:
            material_costo_kg = 0.0

        try:
            material = float(self.root.ids.material_input.text)
        except ValueError:
            material = 0.0

        try:
            extra_material = float(self.root.ids.extra_material_input.text)
        except ValueError:
            extra_material = 0.0

        try:
            tiempo = float(self.root.ids.tiempo_input.text)
        except ValueError:
            tiempo = 0.0

        try:
            consumo_w = float(self.root.ids.consumo_w_input.text)
        except ValueError:
            consumo_w = 0.0


        try:
            costo_kw = float(self.root.ids.costo_kw_input.text)
        except ValueError:
            costo_kw = 0.0

        try:
            mano_obra = float(self.root.ids.mano_obra_input.text)
        except ValueError:
            mano_obra = 0.0

        try:
            costo_mano_obra = float(self.root.ids.costo_mano_obra_input.text)
        except ValueError:
            costo_mano_obra = 0.0

        try:
            costo_adquisicion = float(self.root.ids.costo_adquisicion_input.text)
        except ValueError:
            costo_adquisicion = 0.0

        try:
            vida_util = float(self.root.ids.vida_util_input.text)
        except ValueError:
            vida_util = 1

        try:
            valor_residual = float(self.root.ids.valor_residual_input.text)
        except ValueError:
            valor_residual = 0.0

        try:
            costo_mantenimiento = float(self.root.ids.costo_mantenimiento_input.text)
        except ValueError:
            costo_mantenimiento = 0.0

        try:
            porcentaje_ganacia = float(self.root.ids.porcentaje_ganacia_input.text)
        except ValueError:
            porcentaje_ganacia = 0.0

        try:
            porcentaje_iva = float(self.root.ids.porcentaje_iva_input.text)
        except ValueError:
            porcentaje_iva = 0.0
        
        try:
            costo_embalaje = float(self.root.ids.costo_embalaje_input.text)
        except ValueError:
            costo_embalaje = 0.0

        try:
            costo_envio = float(self.root.ids.costo_envio_input.text)
        except ValueError:
            costo_envio = 0.0

        
        
        # Calcular el costo de amortización anual de la impresora
        costo_amortizacion_anual = (costo_adquisicion - valor_residual) / vida_util + costo_mantenimiento
        costo_amortizacion_hs = (costo_amortizacion_anual / 365 / 24) * tiempo
        self.root.ids.costo_amortizacion_total.text = f'Amortizacion Impresora $ {costo_amortizacion_hs:.2f} ' 
        costo_material_utilizado = material * (material_costo_kg/1000)
        # Calcular el costo del material extra
        costo_material_extra = costo_material_utilizado * (extra_material / 100)
        filamento_total = costo_material_utilizado + costo_material_extra
        self.root.ids.costo_material_total.text = f'Costo Filamento $ {filamento_total:.2f} ' 
        costo_electricidad = consumo_w * tiempo * (costo_kw  / 1000)
        self.root.ids.costo_electricidad_total.text = f'Costo electricidad total $ {costo_electricidad:.2f} ' 
        #costo_electricidad = costo_kw * tiempo
        costo_mano_de_obra = costo_mano_obra * mano_obra
        self.root.ids.costo_mano_de_obra_total.text = f'Costo Mano de Obra total $ {costo_mano_de_obra:.2f} ' 
        costos_de_envios = costo_envio + costo_embalaje
        self.root.ids.costo_envio_total.text = f'Costo envio total $ {costos_de_envios:.2f} '

        
        costo_impresion = (costo_material_utilizado + costo_material_extra + costo_electricidad +  costo_mano_de_obra + costo_amortizacion_hs)
             
        
        
        self.root.ids.resultado_label.text = f'Costo de Impresión: ${costo_impresion:.2f}'

        precio_final = (costo_impresion + (costo_impresion * (porcentaje_ganacia/ 100)) + costos_de_envios )  
        precio_final_con_iva = (precio_final + (precio_final * (porcentaje_iva / 100)))

        ganancia_total = (precio_final - costo_impresion - costo_envio - costo_embalaje)

        self.root.ids.precio_final_label.text = f'Precio final: ${precio_final:.2f} precio + Imp. {precio_final_con_iva:.2f}'
        self.root.ids.ganancia_label.text = f'Ganancia neta $ {ganancia_total:.2f} ' 
        impuestos_totales = precio_final_con_iva - precio_final
        self.root.ids.total_impuestos_input.text = f'total impuestos $ {impuestos_totales:.2f} '

        



    # Función para obtener la cotización del dólar desde la URL
    def obtener_cotizacion_dolar(self):
        try:
            # Realizar una solicitud GET a la URL de cotización del dólar
            url = "https://api.bluelytics.com.ar/v2/latest"
            response = requests.get(url)

            # Verificar si la solicitud fue exitosa (código de estado 200)
            if response.status_code == 200:
                data = response.json()  # Analizar la respuesta JSON                   
                # Acceder al valor de 'value_avg' del dolar blue
                valor_dolar_blue = data['blue']['value_avg']
                print(valor_dolar_blue)
                self.dolarhoy = valor_dolar_blue
                self.root.ids.dolar_hoy_label.text = f'Calculadora de Costo de Impresión 3D - cotización del dólar hoy {valor_dolar_blue}.' 
                return valor_dolar_blue
            else:
                self.root.ids.dolar_hoy_label.text = f'Calculadora de Costo de Impresión 3D - No se pudo obtener la cotización del dólar.'


        except Exception as e:
            self.root.ids.dolar_hoy_label.text = f'Calculadora de Costo de Impresión 3D - Error al obtener la cotización del dólar.'

    
if __name__ == '__main__':
    CalculadoraImpresionApp().run()