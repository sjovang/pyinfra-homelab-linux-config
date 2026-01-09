from pyinfra.api import deploy
from pyinfra.operations import files, pacman, systemd

@deploy('fail2ban')
def configure_fail2ban():

    package_op = pacman.packages(
        name='install fail2ban on Arch-based systems',
        packages=['fail2ban'],
        present=True,
    )

    if package_op.changed:
        systemd.service(
            name='Ensure fail2ban service is enabled and running',
            service='fail2ban',
            running=True,
            enabled=True,
        )

    jail_local_op = files.template(
        name='Deploy jail.local template',
        src='./homelab/fail2ban/jail.local.j2',
        dest='/etc/fail2ban/jail.local',
        user='root',
        group='root',
        mode='644',
    )

    sshd_jail_op = files.template(
        name='Deploy sshd jail configuration',
        src='./homelab/fail2ban/sshd.local.j2',
        dest='/etc/fail2ban/jail.d/sshd.local',
        user='root',
        group='root',
        mode='644',
    )

    service_override_op = files.template(
        name='Deploy fail2ban service override configuration',
        src='./homelab/fail2ban/service.override.conf.j2',
        dest='/etc/systemd/system/fail2ban.service.d/override.conf',
        user='root',
        group='root',
        mode='644',
    )

    if any([jail_local_op.changed, sshd_jail_op.changed, service_override_op.changed]):
        systemd.service(
            name='Restart fail2ban service',
            service='fail2ban',
            restarted=True,
        )