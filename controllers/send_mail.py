import smtplib

def sendemail(msg, to_addr_list,
              from_addr='manager.stachu@gmail.com',
              login='manager.stachu',
              password='ccms_manager',
              smtpserver='smtp.gmail.com:587'):

    header  = 'From: ', from_addr
    header += 'To:', to_addr_list

    message = 'Witaj Studencie!\n\n' + msg + '\n\nPozdrawiam,\nStachu Jones'

    server = smtplib.SMTP(smtpserver)
    server.starttls()
    server.login(login,password)
    problems = server.sendmail(from_addr, to_addr_list, message)
    server.quit()
