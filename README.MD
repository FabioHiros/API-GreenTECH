<img src="./mgt/bannerGT.jpg">

<br>
<p align=center>
<a href="#objetivo">Objetivo</a> | <a href="#visao">Visão</a> | <a href="#metodologia">Metodologia</a> | <a href="#tecnologias">Tecnologias</a> | <a href="#mvp">MVP</a> | <a href="#como_utilizar">Como utilizar</a> | <a href="#cronograma">Cronograma</a> | <a href="#equipe">Equipe</a>  | <a href="#backlog">Backlog</a>
</p>
<h2 align=center id="objetivo">🎯Objetivo do Projeto</h2>



<p>Implementar um sistema para a inserção de dados, bem como o desenvolvimento de uma solução para a visualização personalizada desses dados, visando aprimorar a eficiência da agricultura indoor.<p>

<h2 align=center id="visao">👨‍🎨
 Visão do Produto</h2>
 

 <p>
O produto visa criar uma plataforma online que funcione como um centro de dados para a agricultura indoor. Esta plataforma receberá dados de diferentes sensores e dispositivos utilizados no cultivo indoor, analisará esses dados de forma inteligente e os apresentará aos usuários por meio de gráficos e visualizações intuitivas. Nosso objetivo é capacitar os agricultores indoor a tomar decisões mais informadas e eficazes, permitindo-lhes monitorar o ambiente de cultivo, detectar tendências e anomalias, e otimizar os recursos para maximizar a produtividade e a qualidade dos cultivos.</p>

<h2 align=center id="metodologia">👩‍🏫Metodologia</h2>

No desenvolvimento do sistema, seguimos a abordagem ágil do Scrum, um método conhecido por sua flexibilidade e eficácia. Utilizando essa metodologia, dividimos o trabalho em ciclos chamados Sprints, nos quais entregamos incrementos do produto. Antes de cada Sprint, priorizamos as tarefas com base no valor que agregariam ao cliente, definindo assim nosso Produto Mínimo Viável (MVP). Com o MVP estabelecido, construímos o backlog do projeto, detalhando as tarefas necessárias para alcançar nossos objetivos.


<h2 align=center id="tecnologias">⌨️Tecnologias</h2>
<ul>
<li>Figma: Prototipagem</li>
<li>Html: Estruturação de páginas web</li>
<li>Css: Estilização</li>
<li>Bootstrap: Estilização</li>
<li>JavaScript: Funcionalidades</li>
<li>Python: Backend</li>
<li>Flask: Servidor local</li>

</ul>

<h2 align=center>  <img id="mvp" src="./mgt/mvp_icon.png" style="width:20%; "></h2>
    <p align="center">
      <img src="./mgt/MVP.png" alt="MVP do Projeto">
</p>

<!-- video sprint 1 -->
<h2>Sprint 1</h2>

https://github.com/FabioHiros/API-GreenTECH/assets/144804717/87000834-bb4b-43c3-adba-09a89bdb7615

<h2>Sprint 2</h2>

https://github.com/FabioHiros/API-GreenTECH/assets/144804717/86861f28-0e6a-4991-afc4-3cbac6da6cf8

<h2>Sprint 3 </h2>

https://github.com/FabioHiros/API-GreenTECH/assets/144804717/0cfe0470-d654-4129-be84-2d06721af45c

<h2>Sprint 4 </h2>

https://github.com/FabioHiros/API-GreenTECH/assets/144804717/25d7cbd7-f0f4-4e58-a2e2-2bdd4157761b


<h2 align=center id="como_utilizar">💻Como utilizar o projeto:</h2>
<h3>Rodando Localmente:</h3>
<ol>
<li>Instale o <a href="https://www.python.org/">Python</a> e <a href="https://dev.mysql.com/downloads/mysql/">MySQL Server</a> mais atualizado.</li>
<li>Baixe os arquivos do projeto.</li>
<li>Abra o CMD e digite:<br>
<code>mysql -u root -p</code></li>
<li>Digite a senha do seu usuário root, em seguida digite o comando:<br>
<code>source C:\Caminho\Do\Projeto<strong>\mgt\database\dadosensores_setup.sql</strong></code></li>
<li>Feche o prompt do mysql e navegue até C:\Caminho\Do\Projeto<strong>\src\</strong>, usando o CMD nessa pasta digite:<br>
<code>python -m venv venv </code><br>
<code>.\venv\Scripts\activate </code><br>
<code>pip install -r requirements.txt</code></li>
<li>Agora está pronto para rodar o projeto, apenas digite:
<code>flask run</code></li>
    (Copie o IP que aparecer e cole no navegador)
</ol>
<h3>Iniciando pelo AWS:</h3>
<ol>
<li>Selecione o botão 'Executar Instâncias'.</li>
<li>Dê um nome à instância e escolha o SO Ubuntu.</li>
<li>Depois de escolher suas configurações abra a aba 'Detalhes Avançados' e vá ao final da página.</li>
<li>Em 'Dados do usuário' clique em 'Escolher arquivo'.</li>
<li>Selecione o arquivo:<br>
C:\Caminho\Do\Projeto<strong>\mgt\api_dockerized\compose_config.sh</strong></li>
<li>Clique em 'Executar Instância' e espere um tempo para terminar o setup (pode demorar um pouco).</li>
<li>Finalmente copie o IP da instância criada no navegador usando a porta 5000.<br>
Exemplo: 100.90.80.70<strong>:5000</strong></li>
</ol>

<br><br>

<h2 id='cronograma'>Cronograma de entregas<h2>


| Item                                                     | Data de Entrega | Grau de Prioridade  | ID |
|----------------------------------------------------------|-----------------|---------------------|----|
| Documentação                                               |12/06           | 20                | 01 |
| Refinamento do sistema                                        | 07/06           | 15               | 02 |
| Botão de Download                                         | 10/06           | 10               | 03 |

<BR>
<br>

<h2 align=center id="backlog">🗄 Backlog</h2>

| Item | Prioridade | ID | Descrição | Sprint|
| ---- | ---------- | -- | --------- | ----- |
| Criação da Estrutura do Software | 100 |#1| "Como Cliente quero ter maior visualização da Estrutura do software" | **1** |
|Desenvolvimento do menu base  | 95 |#2| "Como cliente quero ter visualização de três cards de direcionamento intuitivos " | **1**|
| Desenvolvimento da landing page | 90 |#3| "Enquanto cliente quero uma interface pratica e de facil uso " | **1** |
| Desenvolvimento da página para os gráficos | 85 |#4| "Como cliente quero ter visualização dos gráficos gerados" | **1** |
| Graficos Ilustrativos | 80 |#5| "Eu como cliente quero, encontrar no site, exemplos práticos para que o método seja aplicado para meus funcionários de forma padronizada". | **1** |
| Flask | 75 |#6| "Criação do backend da pagina"| **1** |
| Tabela  de Variaveis | 70 |#7| "Enquanto cliente quero uma tabela de acordo com resultado dos dados"| **1** |
| Implementação de Dados  | 60 |#8| "Enquanto Cliente quero que os dados sejam implementados em tempo real" | **2**|
| Implementação para Upload | 50 |#9| "Enquanto cliente quero uma solução para realizar upload de dados" | **2** |
| Implementação de banco de dados relacional  | 45 |#10| "Enquanto cliente quero que meus dados sejam persistentes"| **3** |
| Melhorias de Desempenho Funcional | 40 |#11| "Enquanto cliente quero melhor desempenho funcional". | **3** |
| Leitura temporal de dados  | 35 |#12| "Enquanto cliente quero leitura por hora dos dados". | **3** |
| Responsividade  | 30 |#13| "Enquanto cliente quero que a pagina suporte, website e mobile" | **3** |
| Nuvem  | 25 |#14| "Enquanto cliente quero que o sistema esteja na nuvem" | **3** |
| README | 20 |#15| Documentação do projeto. | **4** |
| Refinamento do sistema | 15 |#16| Correções de bugs e melhorias de desempenho | **4** |
| Botão de download | 10 |#17| "Eu como cliente quero um botão de download para baixar um csv padrão" | **4** |


<!--  -->

<br><br>

<h2 id="equipe"> Equipe: </h2>
<table>
    <tr>
        <th> Foto </th>
        <th> Função </th>
        <th> Nome </th>
        <th> Linkedin </th>
        <th> Git Hub </th>
    </tr>
    <tr>
        <td><img src="./mgt/pfp/fabio.png" alt="ft de perfil" height="40px" width="40px"> </td>
        <td> Scrum Master </td>
        <td> Fábio Hiroshi </td>
        <td> <a href="https://www.linkedin.com/in/f%C3%A1bio-hiroshi-5393a51a0"> <img src='https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white&color=1AB85C'/> </a> </td>
        <td> <a href="https://github.com/FabioHiros"> <img src='https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white&color=1AB85C'/> </a> </td>
    </tr>
    <tr>
        <td> <img src="./mgt/pfp/alexandre.jpeg" alt="ft de perfil" height="40px" width="40px"> </td>
        <td> Product Owner </td>
        <td> Alexandre Ribeiro </td>
        <td> <a href="https://www.linkedin.com/in/alexandre-ribeiro-b3b931111/"> <img src='https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white&color=1AB85C'/> </a> </td>
        <td> <a href="https://github.com/AlexandreFatec"> <img src='https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white&color=1AB85C'/> </a> </td>
    </tr>
    <tr>
        <td> <img src="./mgt/pfp/kat.jpg" alt="ft de perfil" height="40px" width="40px"> </td>
        <td> Scrum Team </td>
        <td> kathellyn Santos </td>
        <td> <a href="https://www.linkedin.com/in/kathellyn-caroline-a562101b9/"> <img src='https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white&color=1AB85C'/> </a> </td>
        <td> <a href="https://github.com/CarolineKathellyn"> <img src='https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white&color=1AB85C'/> </a> </td>
    </tr>
    <tr>
            <td> <img src="./mgt/pfp/eric.jpeg" alt="ft de perfil" height="40px" width="40px"> </td>
        <td> Scrum Team </td>
        <td> Eric Kawata </td>
        <td> <a href="http://www.linkedin.com/in/eric-kawata-99678b302
        "> <img src='https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white&color=1AB85C'/> </a> </td>
        <td> <a href="https://github.com/ericFatec"> <img src='https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white&color=1AB85C'/> </a> </td>
    </tr>
    <tr>
        <td> <img src="./mgt/pfp/bianca.jpeg" alt="ft de perfil" height="40px" width="40px"> </td>
        <td> Scrum Team </td>
        <td> Bianca Isabela </td>
        <td> <a href="https://www.linkedin.com/in/bianca-isabela-souza-vasques-31a8b1284/"> <img src='https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white&color=1AB85C'/> </a> </td>
        <td> <a href="https://github.com/IzyBellah"> <img src='https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white&color=1AB85C'/> </a> </td>
    </tr>
    <tr>
        <td> <img src="./mgt/pfp/gabriel.jpeg" alt="ft de perfil" height="40px" width="40px"> </td>
        <td> Scrum Team </td>
        <td> Gabriel Lourenço </td>
        <td> <a href="https://www.linkedin.com/in/gabriel-lourenço-676688117/"> <img src='https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white&color=1AB85C'/> </a> </td>
        <td> <a href="https://github.com/GabrielMulp"> <img src='https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white&color=1AB85C'/> </a> </td>
    </tr>
    <tr>
        <td> <img src="./mgt/pfp/tiago.jpeg" alt="ft de perfil" height="40px" width="40px"> </td>
        <td> Scrum Team </td>
        <td> Thiago Silva </td>
        <td> <a href="https://www.linkedin.com/in/thiago-monteiro-b559162a7/"> <img src='https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white&color=1AB85C'/> </a> </td>
        <td> <a href="https://github.com/thiagoms14"> <img src='https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white&color=1AB85C'/> </a> </td>
    </tr>
    <tr>
        <td> <img src="./mgt/pfp/fjr.jpeg" alt="ft de perfil" height="40px" width="40px"> </td>
        <td> Scrum Team </td>
        <td> Fabio Fonseca </td>
        <td> <a href="https://www.linkedin.com/in/fabiofonsecajodi/
        "> <img src='https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white&color=1AB85C'/> </a> </td>
        <td> <a href="https://github.com/fabiojotar"> <img src='https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white&color=1AB85C'/> </a> </td>
    </tr>
</table>

