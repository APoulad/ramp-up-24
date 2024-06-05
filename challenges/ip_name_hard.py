from socket import getfqdn as fo
def get_domain(ip_address):
	return fo(ip_address)