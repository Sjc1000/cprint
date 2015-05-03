#!/urs/bin/env python3
"""
cprint. An easy way to colorize your terminal!
"""

generated = ['\033[{}m'.format(str(i)) for i in range(0,99)]
colors = {
    'end': generated[0],
    '/': generated[0],
    'endall': generated[0],
    'error': generated[1],
    'bold': generated[1],
    'italic': generated[3],
    'underline': generated[4],
    'strike': generated[9],
    'dblack': generated[30],
    'dred': generated[31],
    'dgreen': generated[32],
    'dyellow': generated[33],
    'dblue': generated[34],
    'dpurple': generated[35],
    'dteal': generated[36],
    'dwhite': generated[37],
    '_black': generated[40],
    '_red': generated[41],
    '_green': generated[42],
    '_yellow': generated[43],
    '_blue': generated[44],
    '_purple': generated[45],
    '_teal': generated[46],
    '_white': generated[47],
    'black': generated[90],
    'red': generated[91],
    'green': generated[92],
    'yellow': generated[93],
    'blue': generated[94],
    'purple': generated[95],
    'teal': generated[96],
    'white': generated[97]
}

def cprint(data, prefix='', suffix='[.endall]\n'):
    """cprint
    Converts simple color names to terminal color values.
    params:
        - data - The data to print
        - prefix - something to add to the start of data.
        - suffix - something to add to the end. Defaults to [end]\n
            Which ends the color and creates a newline.
    """
    data = prefix + '[.endall]' + data + '[.endall]' + suffix
    c = []
    output = ''
    for i in data.split('[.'):
        color = i[:i.find(']')]
        text = i[i.find(']')+1:]
        if color in ['/', 'end']:
            c.pop()
            output += '[.end]' + ''.join(['[.' + x + ']' for x in c])
        else:
            if color == '':
                continue
            if color not in colors:
                output += color
                pass
            else:
                output += '[.' + color + ']'
                c.append(color)
        output += text
    for color in colors:
        output = output.replace('[.' + color + ']', colors[color])
    print( output, end='')
    return None

if __name__ == '__main__':
    cprint('[.red]This is an [.underline]example[.end] of what this'
           ' [.italic]simple[.end] [.green]program can[.bold] do!')
    cprint('This is another [.underline]line. You can still use '
           '[these normally] [] [:D]')
