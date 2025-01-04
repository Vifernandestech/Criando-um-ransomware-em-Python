# **Criando um Ransomware Troll com Python**  

## **Descrição**  
Este projeto é uma demonstração prática de como um ransomware funciona. Ele foi desenvolvido com o objetivo de **aprendizado** e **pesquisa em cibersegurança**, utilizando a linguagem Python para criptografia e descriptografia de arquivos com o algoritmo **AES (Advanced Encryption Standard)**.  

⚠️ **Aviso**: Este projeto é **exclusivamente para fins educativos** e foi desenvolvido como parte do **Bootcamp Santander Cibersegurança #2** na plataforma **DIO**. **Não utilize este código para atividades maliciosas!**  

---

## **Estrutura do Projeto**  

```
ransomware-troll/
├── src/
│   ├── encrypter.py   # Script para criptografia
│   ├── decrypter.py   # Script para descriptografia
│   └── README.md      # Documentação técnica para os scripts
├── assets/
│   ├── screenshot1.png # Mostrando os arquivos criados com o comando `touch`
│   ├── screenshot2.png # Arquivo TESTE.TXT original descriptografado
│   ├── screenshot3.png # Script Encrypter.py
│   ├── screenshot4.png # Script Decrypter.py
│   ├── screenshot5.png # Comando Python Encrypter.py
│   ├── screenshot6.png # Resultado arquivo TESTE.TXT criptografado
│   ├── screenshot7.png # Comando Python Decrypter.py
│   ├── screenshot8.png #Arquivo TESTE.TXT descriptografado
├── README.md           # Documentação principal do projeto
└── LICENSE             # Licença do projeto
```  

---

## **Como Usar o Projeto**  

### **Pré-requisitos**  
1. Python 3 instalado no seu computador.  
2. Biblioteca `pyaes` instalada. Para instalar, execute o comando:  
   ```bash
   pip install pyaes
   ```  
### **Após pré-requisitos serem cumpridos**
1. Clone este repositório para o seu computador.
2. Instale as dependências (caso não tenha instalado) - (biblioteca `pyaes`).
3. Execute o `encrypter.py` para criptografar arquivos.
4. Use o `decrypter.py` para reverter a criptografia. 

---

## **Capturas de Tela**  
Veja abaixo exemplos do projeto em execução:  

### **Criptografia com o `encrypter.py`**  
![Criptografia](./assets/screenshots/06-Resultado-Arquivo-TESTE-TXT-criptografado.png)  

### **Descriptografia com o `decrypter.py`**  
![Descriptografia](./assets/screenshots/08-Arquivo-TESTE-TXT-descriptografado.png)  

---

## **Licença**  
Este projeto está licenciado sob a **MIT License**. Consulte o arquivo [LICENSE](./LICENSE) para mais informações.  

---

**Desenvolvedor:**  
[Vitor Fernandes da Silva](https://github.com/Vifernandestech)  
Aluno de Cibersegurança - Senac São Paulo  
Bootcamp Santander Cibersegurança #2 - DIO  

