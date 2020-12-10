import sys

if __name__ == '__main__':
  with open(sys.argv[1], 'w') as file:
    file.write('int a = 10;')
  sys.stdout.write(' '.join(sys.argv))