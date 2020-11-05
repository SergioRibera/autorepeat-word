#!/bin/python3
import pyautogui, time, sys, argparse
from rich import print as pri

def end():
    print("")
    print("")
    pri("[bold white]Please report all bugs and problems[/bold white]")
    print("")
    pri("Made with the [bold red]❤️[/bold red] by [bold blue]SergioRibera[/bold blue] [cyan]https://sergioribera.com[/cyan]")

parse = argparse.ArgumentParser(description="Esta herramienta automatiza publicar comentarios repetitivos en facebook")
parse.add_argument('-t', '--timesleep', default=5, help="Este parametro indica el tiempo de espera antes de comzar la automatización")
parse.add_argument('-p', '--timepause', default=0.5, help="Este parametro indica la pausa entre accion y accion")
parse.add_argument('-w', '--word', default='.', help="Este parametro indica el texto o palabra que se va a repetir")
parse.add_argument('-a', '--action', default='enter', help="Este parametro indica la accion a realizar luego de escribir el texto")
parse.add_argument('-r', '--repeats', default=20, help="Este parametro indica la cantidad de veces que se repetirá el texto y la accion")
args = parse.parse_args()

time.sleep(float(args.timesleep))
if __name__ == "__main__":
    try:
        actions = []
        if str(args.action).find('+'):
            actions = str(args.action).split('+')
        else:
            actions.append(args.action)
        for repeat in range(int(args.repeats)):
            print(str(repeat + 1) + " veces ejecutado la accion")
            pyautogui.typewrite(args.word)
            for act in actions:
                pyautogui.press(act.strip())
            time.sleep(float(args.timepause))
    except:
        parse.print_help()
    end()
