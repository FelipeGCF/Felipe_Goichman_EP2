import turtle        # Usa a biblioteca de turtle graphics
window = turtle.Screen()    # cria uma janela
window.bgcolor("lightblue")
window.title("Poligonos")

forca   = turtle.Turtle()  
forca.speed(5)             
forca.penup()      
forca.setpos(150,-150)
forca.pendown()
forca.backward(250)
forca.left(90)
forca.forward(300)
forca.right(90)
forca.forward(100)
forca.right(90)
forca.forward(50)
forca.color("blue")

palavra=input("Digite a palavra secreta").lower().strip()
for x in range(100):
    print()
digitadas=[]
acertos=[]
erros=0



