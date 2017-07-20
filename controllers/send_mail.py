import smtplib

def send_email(msg, to_addr_list,
               from_addr='manager.stachu@gmail.com',
               login='manager.stachu',
               password='ccms_manager',
               smtpserver='smtp.gmail.com:587'):
    """
    Get user login and generated password
    and send it to the user's e-mail.

    Return:
            None
    """        

    header = 'From: ', from_addr
    header += 'To:', to_addr_list

    message = 'Witaj!\n\n' + msg + '\n\nPozdrawiam,\nStachu Jones'

    server = smtplib.SMTP(smtpserver)
    server.starttls()
    server.login(login, password)
    problems = server.sendmail(from_addr, to_addr_list, message)
    server.quit()
