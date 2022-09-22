print('22.5.1 Übung Strings:')
import os
output = "Das soll in der Mitte stehen"
centeredOutput = output.center(os.get_terminal_size()[0], '!')
print(centeredOutput)