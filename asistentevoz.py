import webbrowser

print("Bienvenido, Andy")
dia = input("Ingrese un dia de la semana: ")

match (dia):
    case "Lunes":
        print("Hoy debes hacer ejercicio")
    case "Martes":
        print("Hoy debes,hacer las compras")
    case "Miercoles":
        print("Hoy debes,ver peliculas")
        print("Deseas que te recomiende un canal")
        tipoWeb=input("si o no: ")
        if tipoWeb == "si":
            webbrowser.open_new_tab("https://www.primevideo.com")
    case "Jueves":
        print("Hoy debes,hacer deberes")
    case "Viernes":
        print("Hoy debes,jugar futbol")
    case _:
        print("No existe actividad para ese dia")


print ("Instagram")

user = input ("Phone number,username or email")
password=input ("Password")

if user == "Andy" and password == "123":
    print(f"Welcome {user}")
    print("Loading your posts")
else:
    print("Sorry, your password was incorrect. Please double-check your password.")

print("Sign up to see phots and videos from your friends. ")
input("Log in with Facebook")
facebook=input("Yes or No")
if facebook == "si" :
    print ("Welcome")
else: 
    mobile=input("Mobile numbre or email")
    name=input("Full name")
    username=input("Username")
    password=input("password")