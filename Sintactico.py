#!/usr/bin/env python

import re
import Lexico

def mal( scanner, token ): return "VAR" , 'v', 1, token

def read_file(name):
  mat = []
  i = 0;
  f = open(name, 'r')
  for line in f:
    #~ mat[ i ] = line
    print "->", line;
    i = i + 1
  f.close()

def sintactico( string ):
  #~ print string
  expresion = 0;
  scanner = re.Scanner([
    (r"[0-5]*6[0-6]*", mal),# simbolo fuera del alfabeto
    (r"[0-5]*(41|42)[0-5]*", mal),# ( +           ( =
    (r"[0-5]*(15|25)[0-5]*", mal),# +)            =)
    (r"[0-5]*(34|04|45|54|50|53)[0-5]*", mal),# V(        D(        ()            )(          )V          )D
    (r"[0-5]*(11|22)[0-5]*", mal),# ++          ==
    (r"[0-5]*(12|21)[0-5]*", mal),# +=          =+
    (r"[0-5]*(33|00|30|03)[0-5]*", mal),# DD        VV        DV          VD
    (r"[0-5]*(132|102|32)[0-5]*", mal),# +D=         +V=         D=
    (r"\s+", None),
    ])

  tokens, remainder = scanner.scan( string )
  for token in tokens:
    #~ print token[ 0 ]
    #~ print token[ 1 ]
    #~ print token[ 2 ]
    #~ print token[ 3 ]
    expresion = expresion + token[2]
  return expresion

def opera( string ):
  par = 0

  #~ print ""
  #~ string = raw_input( "Escribe una ecuacion:\n" )
  lex = Lexico.lexico( string )
  t = len(lex)
  for i in range(t):
    if lex[ i ] == '4':
      par = par + 1
    elif lex[ i ] == '5':
      par = par - 1
    if par < 0:
      break;

  lis = "".join(lex)
  print ""
  print "------------------------------------------------------------------------"
  print ""
  if( sintactico( lis ) == 0 and par == 0):
    print string, "es una operacion valida" 
  else:
    print string, "no es una operacion valida" 
  print ""
  print "------------------------------------------------------------------------"
  print ""


if __name__ == '__main__':
  print ""
  string = raw_input( "Escribe el nombre del archivo:\n" )
  opera( string )
  #~ name = raw_input( "Escribe el nombre del archivo:\n" )
  #~ read_file( name )
