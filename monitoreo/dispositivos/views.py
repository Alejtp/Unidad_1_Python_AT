from django.shortcuts import render

def inicio(request):
    contexto = {"nombre": "Profe Javier"}
    return render(request, "dispositivos/inicio.html", contexto)

def panel_dispositivos(request):
    dispositivos = [
        {"nombre": "Sensor Temperatura", "consumo": 50},
        {"nombre": "Medidor Solar", "consumo": 120},
        {"nombre": "Sensor Movimiento", "consumo": 30},
        {"nombre": "Calefactor", "consumo": 200},
    ]
    consumo_maximo = 100
    
    # Añadir estado a cada dispositivo
    for dispositivo in dispositivos:
        if dispositivo["consumo"] <= consumo_maximo:
            dispositivo["estado"] = "Correcto"
        else:
            dispositivo["estado"] = "Exceso"
    
    return render(request, "dispositivos/panel.html", {
        "dispositivos": dispositivos,
        "consumo_maximo": consumo_maximo
    })