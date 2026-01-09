from pyinfra.api import deploy
from pyinfra.operations import pacman

@deploy('utilities')
def install_utils():
    pacman.update(
        name='update package database on Arch-based systems',
    )
    pacman.packages(
        name='install useful utilities on Arch-based systems',
        packages=[
            'fastfetch',
            'git',
            'less',
            'htop',
            'nano',
            'neovim',
            'wget',
            'zsh',
        ],
        present=True
    )