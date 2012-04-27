import re
import socket
import time

from util import hook

socket.setdefaulttimeout(10)


# Auto-join on Invite (Configurable, defaults to True)
@hook.event('INVITE')
def invite(paraml, conn=None):
    invite_join = conn.conf.get('invite_join', True)
    if invite_join:
        conn.join(paraml[-1])
    else:
        return None


# Rejoin on kick (Configurable, defaults to False)
@hook.event('KICK')
def rejoin(paraml, conn=None):
    auto_rejoin = conn.conf.get('auto_rejoin', False)
    if autorejoin:
        conn.join(paraml[0])
    else:
        return None


# Identify to NickServ (or other service)
@hook.event('004')
def onjoin(paraml, conn=None, bot=None):
    nickserv_password = conn.conf.get('nickserv_password', '')
    nickserv_name = conn.conf.get('nickserv_name', 'nickserv')
    nickserv_command = conn.conf.get('nickserv_command', 'IDENTIFY %s')
    if nickserv_password:
        if nickserv_password in bot.config['censored_strings']:
            bot.config['censored_strings'].remove(nickserv_password)
        conn.msg(nickserv_name, nickserv_command % nickserv_password)
        bot.config['censored_strings'].append(nickserv_password)
        time.sleep(1)

# Set bot modes
    mode = conn.conf.get('mode')
    if mode:
        conn.cmd('MODE', [conn.nick, mode])

# Join config-defined channels
    for channel in conn.channels:
        conn.join(channel)
        time.sleep(1)

    print "onjoin() sucessfully completed."


@hook.event("KICK")
def onkick(paraml, conn=None, chan=None):
    # if the bot has been kicked, remove from the channel list
    if paraml[1] == conn.nick:
        conn.channels.remove(chan)

@hook.singlethread
@hook.event('004')
def keep_alive(paraml, conn=None):
    keepalive = conn.conf.get('keep_alive', False)
    if keepalive:
        while True:
            conn.cmd('PING', [conn.nick])
            time.sleep(60)
