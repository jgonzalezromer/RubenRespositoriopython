# Crear un programa que recoja por parámetro una ruta y una palabra clave y 
# termine con error ( sys.exit(n) ) en caso de que un archivo o más en el
# directorio contenga esa palabra clave
#
# Tip 1: Comando egrep de linux, método walk de la librería os, etc.
# Tip 2: Códigos de salida con error para github
# https://docs.github.com/en/actions/sharing-automations/creating-actions/setting-exit-codes-for-actions
def coincide_contraseña():
    import subprocess
    import sys
    ruta=sys.argv[1]
    palabra_clave=sys.argv[2]
    resultado=subprocess.run([`egrep`,`-R`,`palabra_clave`,`ruta`], capture_outpo=true)
    if resultado.return == 0
        Print("Se ha encontrado una coincidencia")
        ( sys.exit(150) )
    else
        ( sys.exit(0) )
def main():
    coincide_contraseña()
    print("Todavía no estoy listo!")

if __name__ == "__main__":
    main()
