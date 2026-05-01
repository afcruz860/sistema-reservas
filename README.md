# Sistema Integral de Clientes, Servicios y Reservas – Software FJ

## Descripción
Este proyecto implementa un sistema integral de gestión de clientes, servicios y reservas, desarrollado en **Python** bajo una arquitectura orientada a objetos.  
El sistema permite:
- Registrar clientes con validaciones robustas y encapsulación de datos personales.
- Gestionar servicios especializados (salas de reuniones, alquiler de equipos, asesorías).
- Crear reservas con confirmación, cancelación y procesamiento.
- Manejar excepciones de forma controlada.
- Registrar eventos y errores en un archivo de logs (`logs.txt`).
- Visualizar las reservas en una interfaz gráfica con tabla resumen.

---

##  Requisitos
- Python 3.11 o superior
- Librerías estándar incluidas en Python:
  - `tkinter` (interfaz gráfica)
  - `logging` (registro de eventos)

---

##  Uso
1. Clonar o descargar el proyecto en una carpeta local.  
2. Ejecutar el programa principal:  
   ```bash
   python main.py
Ingresar los datos del cliente (nombre, email, teléfono).

Seleccionar el tipo de servicio en el menú desplegable.

Ingresar costo y duración.

Pulsar Crear Reserva para confirmar la operación.

Opcional:

Seleccionar una reserva en la tabla y pulsar Cancelar Reserva.

Seleccionar una reserva en la tabla y pulsar Procesar Reserva.

Consultar el archivo logs.txt para verificar los eventos registrados.

Estructura del proyecto
Código
SistemaReservas/

main.py          Interfaz gráfica y flujo principal

clientes.py      Clase Cliente con validaciones y encapsulación

servicios.py     Clase abstracta Servicio + servicios especializados

reservas.py      Clase Reserva con confirmación, cancelación y procesamiento

logs.txt         Registro de eventos y errores

README.md        Documentación del proyecto

Ejemplo de ejecución

Tabla de reservas
Nombre	Email	Teléfono	Servicio	Duración	Estado
Andrés Cruz	andres@yahoo.com	3126549875	Sala de reuniones	5	Confirmada
Andrés Cruz	andres@yahoo.com	3126549875	Sala de reuniones	5	Cancelada


Logs registrados

text

2026-05-01 12:34:54,064 - INFO - Reserva confirmada correctamente.
2026-05-01 12:35:04,716 - INFO - Reserva cancelada correctamente.
2026-05-01 12:35:07,040 - INFO - Reserva procesada: costo total = 356.95

Validación frente al enunciado
El sistema cumple con los requisitos solicitados:

Arquitectura orientada a objetos.

Clase abstracta Servicio y tres servicios especializados.

Clase Cliente con validaciones robustas y encapsulación.

Clase Reserva con confirmación, cancelación y procesamiento.

Polimorfismo y métodos sobrescritos.

Métodos sobrecargados (calcular_costo con impuestos y descuentos).

Manejo de excepciones.

Registro en archivo de logs.

Pruebas sugeridas (10 operaciones)
Para validar el sistema, se recomienda ejecutar las siguientes pruebas:

Reserva válida de sala de reuniones

Cliente con email correcto y teléfono válido.

Resultado: Confirmada, aparece en tabla y log.

Reserva inválida por email incorrecto

Cliente con email sin “@”.

Resultado: Error Cliente en log.

Reserva inválida por teléfono no numérico

Cliente con teléfono “ABC123”.

Resultado: Error Cliente en log.

Reserva de proyector con duración válida

Confirmación exitosa.

Resultado: Confirmada en tabla y log.

Reserva de asesoría con duración negativa

Resultado: Error Servicio en log.

Cancelar una reserva confirmada

Seleccionar en tabla y pulsar “Cancelar Reserva”.

Resultado: Estado cambia a Cancelada, log registra evento.

Cancelar una reserva no confirmada

Intentar cancelar directamente.

Resultado: Error Reserva en log.

Procesar reserva confirmada con impuestos y descuentos

Resultado: Costo total calculado, log registra evento.

Procesar reserva inválida (servicio sin costo definido)

Resultado: Error en procesamiento, log registra excepción.

Crear múltiples reservas y limpiar tabla

Resultado: Tabla muestra todas, logs registran confirmaciones.

Al limpiar, tabla queda vacía, logs siguen intactos.

Autor
Andrés Cruz – UNAD  
Proyecto académico de Programación Orientada a Objetos
