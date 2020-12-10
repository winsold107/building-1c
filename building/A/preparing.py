import sys

if __name__ == '__main__':
  with open(sys.argv[1], 'w') as file:
    file.write('str string = "Hello World!";')
  sys.stdout.write(' '.join(sys.argv))