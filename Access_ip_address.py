""" TO GET IPV4 ADDRESS """
import socket
soc=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
soc.connect(("8.8.8.8",80))
ip_address=soc.getsockname()[0]
soc.close()
print("YOUR LAPTOP'S IPV4 ADDRESS IS:",ip_address)

""" TO GET IPV6 ADDRESS """
import socket
soc=socket.socket(socket.AF_INET6,socket.SOCK_DGRAM)
soc.connect(("2001:4860:4860::8888",80))
ip_address=soc.getsockname()[0]
soc.close()
print("YOUR LAPTOP'S IPV6 ADDRESS IS:",ip_address)