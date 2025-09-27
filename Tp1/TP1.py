import sys
from datetime import datetime
from typing import Dict, List, Tuple, Optional

def parse_line(line: str) -> Optional[Tuple[str, Optional[float], Optional[float], str]]:
    line = line.rstrip("\n")
    
    if not line.strip():
        return None
    # Omitir encabezado
    if line.startswith("FECHA") or line.startswith("--------"):
        return None
    
    #FECHA (ddmmyyyy) | TMAX | TMIN | NOMBRE
    try:
        fecha = line[0:8]
        tmax_str = line[8:14].strip()
        tmin_str = line[14:20].strip()
        nombre = line[20:].strip()
        tmax = float(tmax_str) if tmax_str not in ("") else None
        tmin = float(tmin_str) if tmin_str not in ("") else None
        # Validar fecha con datetime
        datetime.strptime(fecha, "%d%m%Y")
        return fecha, tmax, tmin, nombre
    
    except Exception:
        # si algo falla, descarta la línea
        return None

def leer_dataset(ruta: str):
    fecha_ordenada: List[str] = [] #fecha_ordenada: lista de fechas (str ddmmyyyy) en orden de aparición
    por_fecha: Dict[str, Dict[str, Tuple[Optional[float], Optional[float]]]] = {} #por_fecha: dict fecha -> dict(estacion -> (tmax, tmin))
    estaciones = set() #estaciones: set con nombres de estaciones

    with open(ruta, "r", encoding="latin-1", errors="replace") as f:
        for raw in f:
            
            parsed = parse_line(raw)
            
            if not parsed:
                continue
            fecha, tmax, tmin, nombre = parsed
            
            if fecha not in por_fecha:
                
                por_fecha[fecha] = {}
                fecha_ordenada.append(fecha)
                
            por_fecha[fecha][nombre] = (tmax, tmin)
            estaciones.add(nombre)

    return fecha_ordenada, por_fecha, estaciones

def construir_datos(fecha_ordenada, por_fecha, estaciones):
    
    datos: Dict[str, Dict[str, List[Optional[float]]]] = {}
    for est in estaciones:
        datos[est] = {"tmax": [], "tmin": []}

    for fecha in fecha_ordenada:
        diario = por_fecha.get(fecha, {})
        for est in estaciones:
            tmax, tmin = diario.get(est, (None, None))
            datos[est]["tmax"].append(tmax)
            datos[est]["tmin"].append(tmin)
    return datos

def max_min_por_estacion(datos):
    #Devuelve dict con (max, min) por estación (ignorando None).
    result = {}
    for est, series in datos.items():
        tmax_vals = [v for v in series["tmax"] if v is not None]
        tmin_vals = [v for v in series["tmin"] if v is not None]
        result[est] = {
            "max_anual": max(tmax_vals) if tmax_vals else None,
            "min_anual": min(tmin_vals) if tmin_vals else None,
        }
    return result

def amplitudes_extremas(datos, fecha_ordenada):

    mayor = (None, None, None, None)  # amp, est, fecha, doy
    menor = (None, None, None, None)
    for est, series in datos.items():
        for idx, (tx, tn) in enumerate(zip(series["tmax"], series["tmin"])):
            if tx is None or tn is None:
                continue
            amp = tx - tn
            fecha = fecha_ordenada[idx]
            doy = datetime.strptime(fecha, "%d%m%Y").timetuple().tm_yday
            if (mayor[0] is None) or (amp > mayor[0]):
                mayor = (amp, est, fecha, doy)
            if (menor[0] is None) or (amp < menor[0]):
                menor = (amp, est, fecha, doy)
    return mayor, menor

def dif_max_min_entre_estaciones(por_fecha, fecha_ordenada):
    max_global = (None, None, None, None, None, None, None)
    min_global = (None, None, None, None, None, None, None)
    for fecha in fecha_ordenada:
        
        diario = por_fecha.get(fecha, {})
        # Listas de (estacion, valor)
        tmax_list = [(e, v[0]) for e, v in diario.items() if v[0] is not None]
        tmin_list = [(e, v[1]) for e, v in diario.items() if v[1] is not None]
        if not tmax_list or not tmin_list:
            continue
        for est1, tx in tmax_list:
            
            for est2, tn in tmin_list:
                
                diff = tx - tn
                doy = datetime.strptime(fecha, "%d%m%Y").timetuple().tm_yday
                if (max_global[0] is None) or (diff > max_global[0]):
                    max_global = (diff, fecha, doy, est1, tx, est2, tn)
                if (min_global[0] is None) or (diff < min_global[0]):
                    min_global = (diff, fecha, doy, est1, tx, est2, tn)
    return max_global, min_global

def formatear_fecha(fecha_ddmmyyyy: str) -> str:
    
    dt = datetime.strptime(fecha_ddmmyyyy, "%d%m%Y")
    return dt.strftime("%d/%m/%Y")

def generar_reporte(ruta_datos: str, ruta_salida: str):
    
    fecha_ordenada, por_fecha, estaciones = leer_dataset(ruta_datos)
    datos = construir_datos(fecha_ordenada, por_fecha, estaciones)

    # 1) Máx y mín anual por estación
    extremos = max_min_por_estacion(datos)

    """ 2) Amplitud térmica extrema por estación/día
    Considera solo días donde existan ambos valores (no None)"""
    mayor_amp, menor_amp = amplitudes_extremas(datos, fecha_ordenada) 

    # 3) Dif máx y mín entre Tmax(est1) y Tmin(est2) el mismo día
    dif_max, dif_min = dif_max_min_entre_estaciones(por_fecha, fecha_ordenada)

    # Construcción del texto del reporte
    line = "-" * 92
    with open(ruta_salida, "w", encoding="utf-8") as out:    #no usar latin-1

        out.write("1) Máxima y mínima registradas en el período por estación\n")
        out.write(line + "\n")
        out.write(f"{'ESTACIÓN':60s}  {'TMAX MAX(°C)':>14s}  {'TMIN MIN(°C)':>14s}\n")
        out.write(f"{'-'*60}  {'-'*14}  {'-'*14}\n")
        for est in sorted(extremos.keys()):
            mx = extremos[est]["max_anual"]
            mn = extremos[est]["min_anual"]
            mx_s = f"{mx:.1f}" if mx is not None else "(nada)"
            mn_s = f"{mn:.1f}" if mn is not None else "(nada)"
            out.write(f"{est:60s}  {mx_s:>14s}  {mn_s:>14s}\n")
        out.write("\n" + line + "\n\n")

        # 2) Amplitudes
        if mayor_amp[0] is not None:
            amp, est, fecha, doy = mayor_amp
            out.write("2.a) Mayor amplitud térmica en un mismo día\n")
            out.write(f"Estación: {est}\n")
            out.write(f"Amplitud: {amp:.1f} °C\n")
            out.write(f"Fecha: {formatear_fecha(fecha)} (día {doy} del año)\n\n")
        else:
            out.write("2.a) Mayor amplitud térmica: No encontrada\n\n")

        if menor_amp[0] is not None:
            amp, est, fecha, doy = menor_amp
            out.write("2.b) Menor amplitud térmica en un mismo día\n")
            out.write(f"Estación: {est}\n")
            out.write(f"Amplitud: {amp:.1f} °C\n")
            out.write(f"Fecha: {formatear_fecha(fecha)} (día {doy} del año)\n\n")
        else:
            out.write("2.b) Menor amplitud térmica: No encontrada\n\n")

        out.write(line + "\n\n")

        # 3) Diferencias entre Tmax(est1) y Tmin(est2)
        if dif_max[0] is not None:
            diff, fecha, doy, est_tx, tx, est_tn, tn = dif_max
            out.write("3.a) Máxima diferencia entre Tmax(estación A) y Tmin(estación B) en un día\n")
            out.write(f"Fecha: {formatear_fecha(fecha)} (día {doy} del año)\n")
            out.write(f"Estación A (Tmax): {est_tx} = {tx:.1f} °C\n")
            out.write(f"Estación B (Tmin): {est_tn} = {tn:.1f} °C\n")
            out.write(f"Diferencia: {diff:.1f} °C\n\n")
        else:
            out.write("3.a) Máxima diferencia: No encontrada\n\n")

        if dif_min[0] is not None:
            diff, fecha, doy, est_tx, tx, est_tn, tn = dif_min
            out.write("3.b) Mínima diferencia entre Tmax(estación A) y Tmin(estación B) en un día\n")
            out.write(f"Fecha: {formatear_fecha(fecha)} (día {doy} del año)\n")
            out.write(f"Estación A (Tmax): {est_tx} = {tx:.1f} °C\n")
            out.write(f"Estación B (Tmin): {est_tn} = {tn:.1f} °C\n")
            out.write(f"Diferencia: {diff:.1f} °C\n\n")
        else:
            out.write("3.b) Mínima diferencia: No encontrada\n\n")

        out.write(line + "\n")

def main():
    try:
        if len(sys.argv) >= 3:
            in_path = sys.argv[1]
            out_path = sys.argv[2]
        else:
            in_path = "registro_temperatura365d_smn.txt" #verificar que se llamen iguales
            out_path = "reporte.txt"
        print("archivo creado, revise la carpeta donde se ejecuto el codigo (puede tardar un poco)")
        generar_reporte(in_path, out_path)
    except Exception:
        print("Error:verifique que el txt *registro_temperatura365d_smn* este en la misma carpeta que el codigo que se esta compilando")
        return None
        return None
if __name__ == "__main__":
    main()
