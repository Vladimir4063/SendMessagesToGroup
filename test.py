try:
    archivo = open('bereshit.txt')
    print(archivo.read())
    archivo.close()

except Exception as error:
    print("Error:" , error)
