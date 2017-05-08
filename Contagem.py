segundos = input("Por favor, entre com o número de segundos que deseja converter: ")
segundos = int(segundos)

dias = segundos // 86400 #Segundos total dividido pelo segundos de um dia
segundosRestantes = segundos % 86400 #Para saber os segundos que sobraram, que virarao horas
horas = segundosRestantes // 3600 #Segundos que sobraram do dia, que viraram horas
segundosSobraHoras = segundosRestantes % 3600 #Segundos que sobraram das horas, que virarao minutos
minutos = segundosSobraHoras // 60 
segundos = segundosSobraHoras % 60 


print(dias, "dias,", horas, "horas,", minutos, "minutos e", segundos, "segundos")
