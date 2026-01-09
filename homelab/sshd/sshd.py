from pyinfra.api import deploy
from pyinfra.operations import files, pacman, systemd

@deploy('sshd')
def configure_sshd():

    package_op = pacman.packages(
        name='install openssh on Arch-based systems',
        packages=['openssh'],
        present=True,
    )

    if package_op.changed:
        systemd.service(
            name='Ensure sshd service is enabled and running',
            service='sshd',
            running=True,
            enabled=True,
        )

    template_op = files.template(
        name='Deploy sshd_config template',
        src='./homelab/sshd/sshd_config.j2',
        dest='/etc/ssh/sshd_config.d/30-pyinfra-hardening.conf',
        user='root',
        group='root',
        mode='644',
    )

    if template_op.changed:
        systemd.service(
            name='Restart sshd service',
            service='sshd',
            restarted=True,
        )