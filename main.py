from tkinter import ttk
from tkinter import ttk
import logging
import tkinter as tk
from tkinter import messagebox
from clientes import Cliente, ErrorCliente
from servicios import ReservaSala, AlquilerEquipo, AsesoriaEspecializada, ErrorServicio
from reservas import Reserva, ErrorReserva

def crear_cliente():
    try:
        nombre = entry_nombre.get()
        email = entry_email.get()
        telefono = entry_telefono.get()
        cliente = Cliente(nombre, email, telefono)
        cliente.validar()
        messagebox.showinfo("Éxito", cliente.descripcion())
        return cliente
    except ErrorCliente as e:
        logging.error(f"Error Cliente: {e}")
        messagebox.showerror("Error Cliente", str(e))
        return None


def crear_servicio():
    try:
        costo = float(entry_costo.get())
        tipo = combo_servicio.get()  # obtiene el valor del desplegable

        if tipo == "Sala de reuniones":
            servicio = ReservaSala("Sala de reuniones", costo)
        elif tipo == "Alquiler de equipo":
            servicio = AlquilerEquipo("Proyector", costo)
        elif tipo == "Asesoría especializada":
            servicio = AsesoriaEspecializada("Consultoría TI", costo)
        else:
            raise ErrorServicio("Tipo de servicio no válido")

        servicio.validar()
        messagebox.showinfo("Éxito", servicio.descripcion())
        return servicio
    except ErrorServicio as e:
        logging.error(f"Error Servicio: {e}")
        messagebox.showerror("Error Servicio", str(e))
        return None



def crear_reserva():
    try:
        cliente = crear_cliente()
        servicio = crear_servicio()
        duracion = int(entry_duracion.get())

        if cliente is None or servicio is None:
            messagebox.showerror("Error", "No se pudo crear la reserva por datos inválidos.")
            return

        reserva = Reserva(cliente, servicio, duracion)
        resultado = reserva.confirmar()
        messagebox.showinfo("Reserva", resultado)

        # 👉 Insertar la reserva en la tabla de resumen
        tabla_resumen.insert("", "end", values=(
            cliente._nombre,
            cliente._email,
            cliente._telefono,
            servicio.nombre,
            duracion,
            reserva.estado
        ))

    except ErrorReserva as e:
        logging.error(f"Error Reserva: {e}")
        messagebox.showerror("Error Reserva", str(e))

def cancelar_reserva():
    try:
        # Obtener la fila seleccionada en la tabla
        seleccion = tabla_resumen.selection()
        if not seleccion:
            messagebox.showerror("Error", "Debe seleccionar una reserva en la tabla.")
            return

        # Tomar los valores de la fila seleccionada
        valores = tabla_resumen.item(seleccion[0], "values")
        nombre, email, telefono, servicio_nombre, duracion, estado = valores

        # Crear objetos temporales para cancelar
        cliente = Cliente(nombre, email, telefono)
        if servicio_nombre == "Sala de reuniones":
            servicio = ReservaSala(servicio_nombre, 0)
        elif servicio_nombre == "Proyector":
            servicio = AlquilerEquipo(servicio_nombre, 0)
        else:
            servicio = AsesoriaEspecializada(servicio_nombre, 0)

        reserva = Reserva(cliente, servicio, int(duracion))
        reserva.estado = estado  # mantener estado actual

        resultado = reserva.cancelar()
        messagebox.showinfo("Reserva", resultado)

        # Actualizar la fila en la tabla
        tabla_resumen.item(seleccion[0], values=(
            nombre, email, telefono, servicio_nombre, duracion, reserva.estado
        ))

    except ErrorReserva as e:
        logging.error(f"Error Reserva: {e}")
        messagebox.showerror("Error Reserva", str(e))


def procesar_reserva():
    try:
        seleccion = tabla_resumen.selection()
        if not seleccion:
            messagebox.showerror("Error", "Debe seleccionar una reserva en la tabla.")
            return

        valores = tabla_resumen.item(seleccion[0], "values")
        nombre, email, telefono, servicio_nombre, duracion, estado = valores

        cliente = Cliente(nombre, email, telefono)
        if servicio_nombre == "Sala de reuniones":
            servicio = ReservaSala(servicio_nombre, 200)
        elif servicio_nombre == "Proyector":
            servicio = AlquilerEquipo(servicio_nombre, 150)
        else:
            servicio = AsesoriaEspecializada(servicio_nombre, 300)

        reserva = Reserva(cliente, servicio, int(duracion))
        reserva.estado = estado

        resultado = reserva.procesar(impuesto=0.19, descuento=0.05)
        messagebox.showinfo("Procesamiento", resultado)

    except ErrorReserva as e:
        logging.error(f"Error Reserva: {e}")
        messagebox.showerror("Error Reserva", str(e))

 

# Interfaz Tkinter
root = tk.Tk()
root.title("Sistema Integral - Software FJ")

tk.Label(root, text="Nombre").grid(row=0, column=0)
entry_nombre = tk.Entry(root)
entry_nombre.grid(row=0, column=1)

tk.Label(root, text="Email").grid(row=1, column=0)
entry_email = tk.Entry(root)
entry_email.grid(row=1, column=1)

tk.Label(root, text="Teléfono").grid(row=2, column=0)
entry_telefono = tk.Entry(root)
entry_telefono.grid(row=2, column=1)

tk.Label(root, text="Tipo de Servicio").grid(row=5, column=0)
combo_servicio = ttk.Combobox(root, values=["Sala de reuniones", "Alquiler de equipo", "Asesoría especializada"])
combo_servicio.grid(row=5, column=1)
combo_servicio.current(0)  # valor por defecto: Sala de reuniones


tk.Label(root, text="Costo Servicio").grid(row=3, column=0)
entry_costo = tk.Entry(root)
entry_costo.grid(row=3, column=1)

tk.Label(root, text="Duración").grid(row=4, column=0)
entry_duracion = tk.Entry(root)
entry_duracion.grid(row=4, column=1)

tk.Button(root, text="Crear Reserva", command=crear_reserva, width=20, height=2).grid(row=5, column=2, padx=10)

# Tabla de resumen de reservas
columns = ("Nombre", "Email", "Teléfono", "Servicio", "Duración", "Estado")
tabla_resumen = ttk.Treeview(root, columns=columns, show="headings")

tk.Button(root, text="Cancelar Reserva", command=cancelar_reserva, width=20).grid(row=8, column=0, pady=10)
tk.Button(root, text="Procesar Reserva", command=procesar_reserva, width=20).grid(row=8, column=1, pady=10)


# Encabezados
for col in columns:
    tabla_resumen.heading(col, text=col)
    tabla_resumen.column(col, width=120)

tabla_resumen.grid(row=7, column=0, columnspan=3, pady=20)


root.mainloop()