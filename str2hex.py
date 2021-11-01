#!/usr/bin/python3

import sys
import re

usage = """
+---------+
|[+]usage:|
+---------+----------------+
| -> str_hex \"some_text\" |
| -> str_hex \"/bin\"      |
+--------------------------+
"""

def init():
    if len(sys.argv) != 2:
        print("[!]Need More Arguments, show the usage...")
        print(usage)

        sys.exit()

def step1():

    text = sys.argv[1]
    textd = text.encode("utf-8")
    hex_decoded = textd.hex()
    input_array = re.split(r"(..)",hex_decoded)
    
    while True:
        input_array.remove("")
        
        if "" not in input_array:
            break
    print(f"[*]Inputed : {text}")
    print(f"[-]HexEncoded: {hex_decoded}")

    fixed_array = input_array.sort()
    
    return fixed_array
   
    del input_array
    del fixed_array

def step2(fixed_array):
    
    form1 = "0x"
    form2 = "\\x"
    outter = "".join(p for p in fixed_array)
     
    def finalize(form,outter):
        
        if "\\x" in form:
            
            part_offs = re.split(r"(..)",outter)
            
            while True:
            
                part_offs.remove("")
                
                if "" not in part_offs:
                    break
            
            text =""

            for i in part_offs:
                
                text += form + i
            
            print(f"[+]Generated: {text}")
       
        else:

            print(f"[+]Generated: {form + outter}")

    finalize(form1,outter)
    finalize(form2,outter)


def shellcode_crafting(shellcode):

    array = re.split(r"(..)",shellcode)

    while True:
        array.remove("")

        if "" not in array:
            break

    forms = "\\x"
    outter = ""

    for i in array:
        outter += forms + i

    print(f"[+]Generated: {outter}")


def main():
    
    if sys.argv[1] == "--shellcode":

        x86_shellcode    = "31c050682f2f7368682f62696e89e3505389e199b00bcd80"
        x86_64_shellcode = "31c048bbd19d9691d08c97ff48f7db53545f995257545eb03b0f05"

        shellcode_crafting(x86_shellcode)
        shellcode_crafting(x86_64_shellcode)
    
    else:

        fixed_array = step1()
        step2(fixed_array)

if __name__ == "__main__":
    
    init()
    main()
    
    
