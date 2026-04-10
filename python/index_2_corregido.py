from colorama import init, Fore, Back, Style
import os
import sys
import subprocess

init(autoreset=True)  

while True:
    print(Fore.BLUE + "==========================================")
    print(Fore.BLUE + "Taller 1 - algoritmos basicos en python")
    print(Fore.BLUE + "jostin sneyder bedoya")
    print(Fore.BLUE + "==========================================\n")

    for i in range(1, 26):
        print(f"  {i}. Ejecutar algoritmo {i}")
    print("  0. Salir\n")
    

    opcion = input("Seleccione una opcion: ").strip()  

    if opcion == "0":
        print("Saliendo del programa...")
        break

   
    try:
        num = int(opcion)
        if 1 <= num <= 25:
            archivo = f"a{num}.py"  

            if os.path.exists(archivo):
                print(Fore.GREEN + f"\n--- Ejecutando {archivo} ---\n")
                resultado = subprocess.run([sys.executable, archivo])  

                if resultado.returncode != 0:  
                    print(Fore.RED + f"\nEl algoritmo {archivo} termino con un error.")
            else:
                print(Fore.YELLOW + f"El archivo '{archivo}' no existe en este directorio.")
        else:
            print(Fore.RED + "Opcion invalida. Ingrese un numero entre 0 y 25.")
    except ValueError:
        print(Fore.RED + "Opcion invalida. Debe ingresar un numero.")

    input("\nPresiona Enter para continuar...")
