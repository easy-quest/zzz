#!/usr/bin/sudo python3
from os import system
import click
TEXT_RESET = '\e[0m'
TEXT_YELLOW = '\e[0;33m'
TEXT_RED_B = '\e[1;31m' 

system('get update -y')
click.echo(TEXT_YELLOW)
click.echo(click.style({yellow}'Обновление APT завершено...'))
click.echo(TEXT_RESET)

#apt-get dist-upgrade -y
#echo -e $TEXT_YELLOW
#echo 'Обновление дистрибутива APT завершено...'
#echo -e $TEXT_RESET             

#apt-get upgrade -y
#echo -e $TEXT_YELLOW
#echo 'Обновление APT завершено...'
#echo -e $TEXT_RESET

#apt-get autoremove -y
#echo -e $TEXT_YELLOW
#echo 'Автоматическое удаление APT завершено...'
#echo -e $TEXT_RESET

#if [ -f /var/run/reboot-required ]; then
#    echo -e $TEXT_RED_B
#    echo 'Требуется перезагрузка!'
#    echo -e $TEXT_RESET
#fi
