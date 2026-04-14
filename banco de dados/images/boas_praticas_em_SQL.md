## Segurança
- Evitar a concatenação de strings nas consultas e usar consultas parametrizadas;
- Previne ataques de injeção SQL.

![alt text](images/image.png)

 Exemplo do injecao_sql.py

![alt text](image-1.png)
- Exemplo do fetchone().
- Fazendo injeção SQL.
Cliente 1 nem existe mas retorna o registro de id = 2 quando passado um input malicioso.


![alt text](image-2.png)
- exemplo do fetchall().
- Fazendo uma injeção SQL, nesse caso poderia ter uma dado sensível que não deveriamos poder visualizar mas conseguiriamos fazendo isso.