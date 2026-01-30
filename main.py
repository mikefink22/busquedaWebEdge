import time
import random
import requests
import subprocess
import uuid

def obtener_temas_reales():
    url = f"https://es.wikipedia.org/w/api.php?action=query&list=random&rnnamespace=0&rnlimit=30&format=json&cb={random.random()}"
    
    # Agregamos esto para que la API crea que somos un navegador real
    cabecera = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
    }

    try:
        # Añadimos 'headers=cabecera' y un 'timeout' por si la red de la clinica es lenta
        response = requests.get(url, headers=cabecera, timeout=10)
        response.raise_for_status() # Esto nos avisará si hay un error de permisos
        datos = response.json()
        temas = [articulo['title'] for articulo in datos['query']['random']]
        random.shuffle(temas)
        return temas
    except Exception as e:
        print(f"La API falló por: {e}")
        # Mantenemos el respaldo pero lo hacemos más variado
        return [f"Tendencia {random.randint(1,100)}", "Clima hoy", "Noticias"]

def iniciar_busquedas():
    # Ruta absoluta de Edge (Verificá que sea esta en tu PC)
    ruta_edge = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
    
    temas = obtener_temas_reales()
    print(f"Iniciando {len(temas)} búsquedas únicas en Edge...")

    for i, tema in enumerate(temas):
        # Generamos un ID de sesión único para cada búsqueda
        session_id = uuid.uuid4().hex
        query = tema.replace(' ', '+')
        
        # URL optimizada con parámetros de búsqueda real
        url_bing = f"https://www.bing.com/search?q={query}&form=QBLH&sp=-1&ghc=1&cvid={session_id}"
        
        print(f"[{i+1}] Buscando: {tema}")
        subprocess.Popen([ruta_edge, url_bing])

        # Pausa entre búsquedas
        espera = random.randint(8, 17)
        
        # Cada 10 búsquedas, hacemos una pausa extra larga de 2 a 5 minutos
        if (i + 1) % 10 == 0:
            pausa_larga = random.randint(25, 60) # Pausa de seguridad entre 25 y 60 segundos
            print(f"   Pausa de seguridad: {pausa_larga} segundos...")
            time.sleep(pausa_larga)
        else:
            print(f"   Esperando {espera} segundos...")
            time.sleep(espera)

if __name__ == "__main__":
    iniciar_busquedas()