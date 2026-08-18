import textwrap

def wrap(string, max_width):
    a=textwrap.fill(string,max_width)
    return a

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
  #textwrap.wrap aaaa aaaa aaaa 
  #textwrap.fill 
  #aaaa
  #aaaa
  #aaaa
