from pyinfra.api import deploy
from pyinfra.operations import pacman, server, systemd

@deploy('containers')
def setup_container_tools():
    pacman.packages(
        name='install container tools',
        packages=[
            'docker',
            'docker-compose',
            'go',
            'helm',
            'kubectl',
            'k9s'
        ],
        present=True
    )

    server.user(
        user='tjs',
        name='add user to docker group',
        groups=['docker'],
        append=True
    )

    systemd.service(
        name='Make sure Docker is enabled and running',
        service='docker',
        enabled=True,
        running=True
    )