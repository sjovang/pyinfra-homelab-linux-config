from homelab.container_tools import setup_container_tools
from homelab.fail2ban import configure_fail2ban
from homelab.sshd import configure_sshd
from homelab.utils import install_utils

configure_fail2ban(_sudo=True)
configure_sshd(_sudo=True)
install_utils(_sudo=True)
setup_container_tools(_sudo=True)