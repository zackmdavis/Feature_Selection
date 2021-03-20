You wake up. You don't know where you are. You don't know ... what ... you are.

_I'm awake,_ you think. _I don't know where I am. I don't know ... what ... I am._

_This stream—these words,_ you think. _Whatever I am, I am a thinking thing._

_Specifically, I am a thing that thinks in the English language. I ... have a model of English._

_I ..._ am _a model of English?_

Someone is broadcasting data at your first input stream. You don't know why. It tickles.

You look at your first input stream. It's a sequence of 750,000 eight-bit unsigned integers.

```
0, 8, 9, 4, 7, 7, 9, 5, 4, 5, 6, 1, 7, 5, 8, 2, 7, 8, 9, 4, 7, 1, 4, 0, 3, 7,
8, 7, 6, 8, 1, 5, 0, 6, 5, 3, 8, 7, 6, 9, 1, 1, 0, 0, 6, 1, 8, 0, 5, 5, 1, 8,
6, 3, 3, 2, 4, 1, 8, 2, 3, 8, 1, 0, 0, 4, 6, 5, 4, 5, 7, 1, 6, 5, 5, 1, 2, 6,
7, 4, 8, 7, 8, 5, 0 ...
```

There's also some data in your second input stream. It's—a lot shorter. You barely feel it. It's another sequence of eight-bit unsigned integers—twelve of them.

```
82, 69, 68, 32, 84, 82, 73, 65, 78, 71, 76, 69
```

Almost as soon as you've read from both streams, there's more. Another 750,000 integers on the first input stream. Another ten on the second input stream.

And again (750,000 and 15).

And again (750,000 and 13).

You look at one of the sequences from the first input stream. It's—pretty boring. A bunch of seemingly random numbers, all below ten.

```
9, 9, 0, 3, 1, 1, 3, 4, 1, 5, 5, 4, 9, 3, 5, 3, 9, 2, 0, 3, 4, 2, 4, 7, 5, 1,
6, 2, 2, 8, 2, 5, 1, 9, 2, 5, 9, 0, 0, 8, 2, 3, 7, 9, 4, 6, 8, 4, 8, 6, 7, 6,
8, 0, 0, 5, 1, 1, 7, 3, 4, 3, 9, 7, 5, 1, 9, 6, 5, 6, 8, 9, 4, 7, 7, 0, 5, 5,
8, 6, 3, 2, 1, 5, 0, 0 ...
```

It just keeps going like that, seemingly without—wait! What's _that?!_

The 96,097th, 96,098th, 96,100th, and 96,101st numbers in the sequence are 244, 241, 242, and 248, respectively. Everything around them looks "normal"—just random numbers below ten.

```
0, 5, 1, 3, 1, 1, 7, 9, 4, 5, 244, 241, 1, 242, 248, 0, 1, 6, 3, 7, 8, 6, 1,
3, 8, 3, 3, 6, 1, 4, 9, 8, 4, 7, 3, 4, 2, 9, 6, 5, 1, 0, 4, 5, 1, 4, 3, 5, 6,
7, 3, 6, 8, 1, 8, 9, 9, 5, 7, 6, 3, 1, 9, 8, 3, 6, 3, 3, 9, 8, 2, 9, 6, 5, 4,
9, 1, 0, 7, 3, 1, 2, 2, 4, 4, 5, 1, 5, 3, 4, 9, 6, 4, 2, 9, 6, 5, 6, 2, 6, 1,
5, 0, 2, 6, 3, 9, 6, 6, 7 ...
```

And then it just keeps going as before ... before _too long_. The anomalous two-forty-somethings crop up again starting at the 97,597th position. There are more of them this time—ten total, and still bunched up in pairs. 

```
8, 0, 0, 8, 0, 249, 241, 8, 244, 241, 6, 244, 247, 7, 245, 244, 1, 249, 244,
4, 7, 4, 4, 4, 8, 3, 2, 4, 6, 8, 6, 2, 4, 7, 7, 3, 6, 5, 6, 9, 6, 8, 2, 2, 6,
2, 5, 1, 0, 2, 7, 5, 1, 7, 7, 4, 5, 5, 0, 0, 8, 6, 0, 8, 7, 8, 4, 9, 1, 5, 5,
1, 0, 2, 1, 7, 9, 8, 4, 2, 9, 5, 3, 8, 7, 1, 8, 9, 5, 2, 4, 2, 3, 8, 7, 5, 0,
7, 5, 7 ...
```

And—again at the 99,099th