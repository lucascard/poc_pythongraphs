import os
from dotenv import load_dotenv

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

# Agora você pode acessar as variáveis usando os.getenv

# Configurações do servidor SMTP
smtp_server = "smtp.gmail.com"
smtp_port = 587
from_address = os.getenv('EMAIL_USER')
password = os.getenv('EMAIL_PASSWORD')

# Endereço do destinatário
to_address = "lucascardoso@cartaodetodos.com"

# Criar o objeto de mensagem MIMEMultipart
msg = MIMEMultipart()
msg['From'] = from_address
msg['To'] = to_address
msg['Subject'] = "Assunto do E-mail"

# Corpo do E-mail
body = "Este é o corpo do e-mail."
msg.attach(MIMEText(body, 'plain'))

# Anexar um arquivo (opcional)
filename = "nome_do_arquivo.extensao"
attachment = open("caminho_para_o_arquivo", "rb")

part = MIMEBase('application', 'octet-stream')
part.set_payload((attachment).read())
encoders.encode_base64(part)
part.add_header('Content-Disposition', "attachment; filename= %s" % filename)

msg.attach(part)

# Conectar ao servidor SMTP e enviar o e-mail
try:
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()  # Iniciar conexão TLS
    server.login(from_address, password)
    text = msg.as_string()
    server.sendmail(from_address, to_address, text)
    server.quit()
    print("E-mail enviado com sucesso!")
except Exception as e:
    print(f"Erro ao enviar e-mail: {e}")
