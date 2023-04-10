total_galletas = int(input("¿Cuántas galletas hay?: "))
invitados = int(input("¿Cuántos invitados vienen?: "))
total_personas = invitados + 1 # Se le suma 1 a la variable ya que la persona también cuenta.

galletas_recibidas = total_galletas // total_personas # Se calcula cuántas galletas recibirá cada persona mediante división de parte entera.
galletas_sobrantes = total_galletas % total_personas # Se calcula cuántas galletas sobrarán mediante el módulo.
print(f"En total son {total_personas} personas. Cada una recibe {galletas_recibidas} galletas y sobran {galletas_sobrantes}.")
print("Hola, modifiqué el archivo")
