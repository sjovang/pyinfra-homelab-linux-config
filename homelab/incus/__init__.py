from pyinfra.api import deploy
from pyinfra.operations import pacman

@deploy('incus')
def setup_incus():
    pacman.packages(
        name='install incus on Arch-based systems',
        packages=['incus'],
        present=True,
    )