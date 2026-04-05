## Tipos de API

### API Restful 
    Uso dos métodos HTTP
    Curva de aprendizado menor

### API Soap
    Protocolo baseado em XML para troca de informações.
    Independente de linguagem e plataforma de transporte.
    Suporte para operações complexas e segurança avançada.
    Mais descritivo, mais padrões, mais verboso.

### API GraphQL
    Permite que os clientes especifiquem exatamente quais dados querem
    Eficiente na redução de solicitações e no tamanho dos dados transferidos.
    Flexível e fortemente tipada, facilitando a evolução das APIs.

## FastAPI

### Pontos positivos:
   **Alto desempenho** Comparável ai NodeJS e superior ao Flask.
   **Geração de documentação automática:** Suporta OpenAPI para documentação.
   **Validação de dados e serialização:** Usa Pydantic para validação de dados e serialização automática.
   **Facilidade de uso:** Aprenser e começar a usar o FastAPI é geralmente considerado simples.
   **Suporte a async/await:** Suporte nativo para operações assíncronas, o que é ótimo para lidar com operações de IO.

## Pontos negativos:

 **Comunidade menor**;
 **Maturidade**: Por ser relatviamento novo, pode faltar alguma maturidade e ter menos plugins quando comparado a outros frameworks mais antigos.
 **Complexidade em projetos grandes:** Em projetos muito grandes e complexos, a gestão pode se tornar um desafio, especialmente para quem não está acostumado com a tipagem estrita e programação assícrona
 **Convenções diferentes:** Por ser relativamente novo, não há convenções absolutas para alguns casos, isso faz com que projetos diferentes tenham regras/nomenclaturas de négocios diferentes.
 