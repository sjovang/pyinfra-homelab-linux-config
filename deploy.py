from homelab.fail2ban import configure_fail2ban
from homelab.sshd import configure_sshd
from homelab.utils import install_utils

configure_fail2ban(_sudo=True)
configure_sshd(_sudo=True)
install_utils(_sudo=True)