import sys

class StdioPresenter:
    def go(text_agent): 
        while True: 
            sys.stdout.write('> ')
            inp = input()
            for word in text_agent.respond(inp):
                sys.stdout.write(word)
                sys.stdout.flush()
            sys.stdout.write('\n')
