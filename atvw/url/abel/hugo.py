# import arrow
# hoje=arrow.now()

# #criar um  obj arrow p a data e hr atuais
# formatado= hoje.format("YYYY-MM-DD HH:mm:ss")
# print(f"data e hr atual: {formatado}")

# #add 7 dias a data atual
# futuro=hoje.shift(days=7)
# print(f"data apos 7 dias: {futuro.format("YYYY-MM-DD HH:mm:ss")}")

# #subtrai 2h da hr atual
# passado= hoje.shift(hours=-2)
# print(f"data duas h atras: {passado.format("YYYY-MM-DD HH:mm:ss")}")

# #converte a data p um fuso horario diferente
# nova_york = hoje.to('America/New_York')
# print(f"Data e hora em Nova York: {nova_york.format('YYYY-MM-DD HH:mm:ss')}")


#atv: tente colocar no fuso horário de Campo Grande 
import arrow
hoje=arrow.now()

Campo_Grande= hoje.to("America/Campo_Grande")
print(f"data e hr em cg: {Campo_Grande.format("YYYY-MM-DD HH:mm:ss")}")