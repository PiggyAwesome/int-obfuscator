# int-obfuscator
Obfuscate your python code into a string of integers. De-obfuscate also supported.


### How it works:

Each printable character gets replaced with it's own uniqe two-character interger.

To deofbuscate, the intergers is splitted by every second character, then replaces it with it's corosponding value


WARNING: Pipe (|) is not supported for obfuscation!

Returns ValueError when pipe is used.
```py 
ValueError: Invalid character: "|"
```

### Obfuscate:
```py
>>> import int_obfuscate as ob
>>> ob.obfuscate("print(\"Hello, World\")")
252718232969634314212124739458242721136370
```

### Deobfuscate:

```py
>>> import int_obfuscate as ob
>>> ob.decode(252718232969634314212124739458242721136370)
print("Hello, World")
```



#### Have fun sending secret messages to your friends, or ratting pcs with intergers!


#### Update: Due to some issues I had with the FBI, I have to tell you guys to not use this to rat someone's PC. Someone did it on `youtube.com/` and got me in trouble after the FBI `watch`ed it. Bruh`?` The poster of the `v`ideo" `=` Very Sussy. I `d`id not `Q`uite mean it that `w`ay. It's ok, you can be 100% sure `4`ever that, that is `w`hat I want to say and that its really me saying this. N`9`t the FBI forcing me to do this `W`ith a `g`un pointed to my head. `X`D Ok `c`ya later s`Q`uad!

