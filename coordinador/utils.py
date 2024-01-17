import pickle
import pandas as pd

def store_data_frame_in_session(request, data_frame):
    try:
        # Asegúrate de que data_frame sea un DataFrame de pandas
        if not isinstance(data_frame, pd.DataFrame):
            raise ValueError("El objeto no es un DataFrame de pandas válido.")
        
        pickled_data_frame = pickle.dumps(data_frame)
        request.session['data_frame'] = pickled_data_frame
    except Exception as e:
        # Manejo de errores, imprime o registra el error según sea necesario
        print(f"Error al almacenar el DataFrame en la sesión: {e}")

def retrieve_data_frame_from_session(request):
    pickled_data_frame = request.session.get('data_frame')
    if pickled_data_frame is not None:
        try:
            data_frame = pickle.loads(pickled_data_frame)
            # Asegúrate de que data_frame sea un DataFrame de pandas
            if not isinstance(data_frame, pd.DataFrame):
                raise ValueError("El objeto almacenado en la sesión no es un DataFrame de pandas válido.")
            
            return data_frame
        except Exception as e:
            # Manejo de errores, imprime o registra el error según sea necesario
            print(f"Error al recuperar el DataFrame de la sesión: {e}")
            return None
    else:
        return None

def clear_data_frame_from_session(request):
    try:
        request.session.pop('data_frame', None)
    except Exception as e:
        # Manejo de errores, imprime o registra el error según sea necesario
        print(f"Error al limpiar el DataFrame de la sesión: {e}")
