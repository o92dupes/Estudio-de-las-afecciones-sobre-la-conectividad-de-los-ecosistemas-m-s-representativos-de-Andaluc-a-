import arcpy
from arcpy.sa import *

# Establecer entorno de trabajo
arcpy.env.workspace = r"C:\TFM\Modelados Maxent\P.halepensis\maps_reescalados\20m"

# Obtener lista de rasters en el directorio
raster_list = arcpy.ListRasters()

# Ruta de salida para los nuevos rasters
output_folder = r"C:\TFM\Modelados Maxent\P.halepensis\Inputs_Guidos\2values"

# Verificar si la carpeta de salida existe, si no, crearla
if not arcpy.Exists(output_folder):
    arcpy.CreateFolder_management(arcpy.env.workspace, "Inputs_Guidos")

# Recorrer la lista de rasters y generar los nuevos rasters
for raster_name in raster_list:
    raster_path = arcpy.env.workspace + "\\" + raster_name
    
    # Crear objeto Raster a partir del archivo
    raster = arcpy.Raster(raster_path)
    
    # Aplicar la condición para establecer los valores en el nuevo raster
    output_raster = Con(raster > 0.65, 2, 1)
    
    # Guardar el nuevo raster en la carpeta de salida
    output_path = output_folder + "\\" + raster_name
    output_raster.save(output_path)
    
    print("Nuevo raster generado: " + raster_name)

print("Proceso completado.")
