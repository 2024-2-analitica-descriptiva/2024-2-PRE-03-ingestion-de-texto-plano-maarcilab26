"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""

# pylint: disable=import-outside-toplevel


def pregunta_01():
  import pandas as pd
  with open("files/input/clusters_report.txt", "r", encoding='utf-8') as file:
      lines = file.readlines()
  #lines

  # contenido = lines[4:]

  # contenido = [line.strip() for line in contenido]  # Aplicar .strip() a cada línea. Este no se aplica en listas
  # contenido

  # Procesar las líneas para eliminar encabezados y líneas separadoras
  data_lines = lines[4:]  # Ignorar las primeras 4 líneas (encabezado y separador)
  
  # Lista para almacenar los datos
  data = []
  current_cluster = None

  for line in data_lines:
      if line.strip():  # Ignorar líneas vacías
          parts = line.split()
          
          # Si la línea comienza con un número, es un nuevo clúster
          if parts[0].isdigit():
              if current_cluster:
                  data.append(current_cluster)  # Guardar el clúster anterior
              
              # Combinar el porcentaje (posiciones 2 y 3) y convertir a formato decimal
              porcentaje = float(f"{parts[2].replace(',', '.')}".replace('%', ''))
              
              # Inicializar un nuevo clúster
              current_cluster = {
                  'cluster': int(parts[0]),
                  'cantidad_de_palabras_clave': int(parts[1]),
                  'porcentaje_de_palabras_clave': porcentaje,  # Guardar como float
                  'principales_palabras_clave': ' '.join(parts[4:])  # Resto son palabras clave
              }
          else:
              # Continuar palabras clave del clúster actual
              current_cluster['principales_palabras_clave'] += ' ' + ' '.join(parts)

  # Agregar el último clúster
  if current_cluster:
      data.append(current_cluster)

  # Crear un DataFrame
  df = pd.DataFrame(data)

  # Limpiar nombres de las columnas
  df.columns = df.columns.str.lower().str.replace(' ', '_')

  # Ajustar formato de las palabras clave
  df['principales_palabras_clave'] = (
      df['principales_palabras_clave']
      .str.replace(r'\s+', ' ', regex=True)  # Espacios múltiples a un solo espacio
      .str.replace(', ', ', ').str.strip()  # Espaciado correcto en comas
      .str.replace("." , "")
  )

  # Mostrar el DataFrame
  return df

"""
    Construya y retorne un dataframe de Pandas a partir del archivo
    'files/input/clusters_report.txt'. Los requierimientos son los siguientes:

    - El dataframe tiene la misma estructura que el archivo original.
    - Los nombres de las columnas deben ser en minusculas, reemplazando los
      espacios por guiones bajos.
    - Las palabras clave deben estar separadas por coma y con un solo
      espacio entre palabra y palabra.


"""
