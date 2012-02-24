from util import hook
import re
import random

fortunes = ["Help! I'm stuck in the fortune cookie factory!",
        "He who laughs at himself never runs out of things to laugh at.",
        "The world is your oyster.",
        "Today will be a good day.",
        "Life's short, party naked.",
        "Haters gonna hate.",
        "You are amazing and let no one tell you otherwise.",
        "A starship ride has been promised to you by the galactic wizard.",
        "That wasn’t chicken.",
        "Don’t fry bacon in the nude.",
        "Take calculated risks. That is quite different from being rash.",
        "DO THE IMPOSSIBLE, SEE THE INVISIBLE.",
        "You cannot plough a field by turning it over in your mind. Unless you have telekinesis.",
        "No one can make you feel inferior without your consent.",
        "Never lose the ability to find beauty in ordinary things.",
        "Ignore previous fortune.",
        "Smile more.",
        "You are the dancing queen.",
        "YOU'RE THE BEST AROUND, NOTHIN'S GONNA EVER KEEP YA DOWN.",
        "The cake is a lie.",
        "Never take life seriously. Nobody gets out alive anyway.",
        "Friendship is like peeing on yourself: everyone can see it, but only you get the warm feeling that it brings.",
        "Never go to a doctor whose office plants have died.",
        "Always remember you're unique, just like everyone else.",
        "What if everything is an illusion and nothing exists? In that case, I definitely overpaid for my carpet.",
        "Even if you are on the right track, you will get run over if you just sit there.",
        "Think like a man of action, and act like a man of thought.",
        "When in doubt, lubricate.",
        "It is time for you to live up to your family name and face FULL LIFE CONSEQUENCES.",
        "It's a good day to do what has to be done.",
        "Move near the countryside and you will be friends of John Freeman.",
        "If you can't beat 'em, mock 'em.",
        "Use gun. And if that don't work, use more gun.",
        "LOOK OUT BEHIND YOU",
        "This message will self destruct in 10 seconds.",
        "You'll never know what you can do until you try.",
        "You are talented in many ways",
        "Be both a speaker of words and a doer of deeds.",
        "A visit to a strange place will bring you renewed perspective.",
        "A passionate new romance will appear in your life when you least expect it.",
        "If you care enough for a result, you will most certainly attain it.",
        "To be loved, be loveable.",
        "Step away from the power position for one day.",
        "If you want to get a sure crop with a big yield, sow wild oats.",
        "It doesn't take guts to quit.",
        "You can expect a change for the better in job or status in the future.",
        "As the wallet grows, so do the needs.",
        "You have a reputation for being straightforward and honest.",
        "Learn a new language and get a new soul.",
        "A tall dark stranger will soon enter our life.",
        "Keep staring. I'll do a trick."]

@hook.command(autohelp=False)
def fortune(inp, nick=None, say=None, input=None):
    ".fortune -- get your fortune"
 
    msg = "(" + nick + ") " + random.choice(fortunes)
    if re.match("^[A-Za-z0-9_|.-\]\[]*$", inp.lower()) and inp != "":
        msg = "(@" + inp + ") " + random.choice(fortunes)

    say(msg)

