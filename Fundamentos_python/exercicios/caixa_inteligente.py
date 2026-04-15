entrada = input().strip()
preco_str, codigo_promocao = entrada.split()

preco = float(preco_str)

if(codigo_promocao == "S"):
  preco_final = preco * 0.90
  print(f"{preco_final:.2f}")
else:
  preco_final = preco
  print(f"{preco_final:.2f}")