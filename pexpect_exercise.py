import pexpect
import re


username = 'admin'
password = 'cisco'

    
child = pexpect.spawn("telnet 172.31.114.3")
child.expect("Username")
child.sendline(username)
child.expect("Password")
child.sendline(password)
child.expect("\r\n\S+#")

print(child.after.decode("UTF-8") + " connected!")
child.sendline("conf t")
child.expect("#")
child.sendline("int loopback 0")
child.expect("#")
child.sendline("ip add 172.16.1.1 255.255.255.255")
child.expect("#")
child.sendline("do wr")
child.expect("#")

child = pexpect.spawn("telnet 172.31.114.4")
child.expect("Username")
child.sendline(username)
child.expect("Password")
child.sendline(password)
child.expect("\r\n\S+#")

print(child.after.decode("UTF-8") + " connected!")
child.sendline("conf t")
child.expect("#")
child.sendline("int loopback 0")
child.expect("#")
child.sendline("ip add 172.16.2.2 255.255.255.255")
child.expect("#")
child.sendline("do wr")
child.expect("#")


child.close()